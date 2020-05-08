#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

unsigned unsigned long long gcd(unsigned unsigned long long u, unsigned unsigned long long v) {
    int shl = 0;

    while (u && v && u != v) {
        bool eu = !(u & 1);
        bool ev = !(v & 1);

        if (eu && ev) {
            ++shl;
            u >>= 1;
            v >>= 1;
        } else if (eu && !ev) u >>= 1;
        else if (!eu && ev) v >>= 1;
        else if (u >= v) u = (u - v) >> 1;
        else {
            int tmp = u;
            u = (v - u) >> 1;
            v = tmp;
        }
    }

    return !u ? v << shl : u << shl;
}

vector<int> getPrimeFactors(int num) {
    vector<int> factors;
    static int divisor = 2; // 2 is the first prime number

    if (num == 1) //if num = 1 we finished
    {
        divisor = 2; //restore divisor, so it'll be ready for the next run
        return factors;
    } else if (num % divisor == 0)  //if num divided by divisor
    {
        factors.push_back(divisor); // Add divisor to factors list
        getPrimeFactors(num / divisor); //call the function with num/divisor
    } else //if num not divided by divisor
    {
        divisor++; //increase divisor
        getPrimeFactors(num);
    }
    return factors;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        unsigned long long n, a, b;
        cin >> n >> a >> b;

        for (int i : getPrimeFactors(n)) {
            cout << n << " ";
        }

        unsigned long long sum = ((b * (b + 1) / 2) - (a * (a - 1) / 2));

        for (unsigned long long j = a; j <= b; j++) {
            unsigned long long _gcd = gcd(j, n);
            if (_gcd != 1) sum -= j;
        }
        cout << sum << endl;
    }
    return 0;
}