#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<unsigned long long> pf(unsigned long long n) {
    vector<unsigned long long> factors;
    for (unsigned long long i = 2; i * i <= n; ++i) //no sqrt, please
    {
        while (n % i == 0) //while, not if
        {
            factors.push_back(i);
            n /= i;
        }
    }
    if (n != 1) {
        factors.push_back(n);
    }
    return factors;
}

bool nogcd(unsigned long long x, vector<unsigned long long> cmp) {
    for (unsigned long long y : cmp){
        if (x % y == 0) return false;
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    unsigned long long a, b, c;
    cin >> t;

    for (unsigned long long i = 0; i < t; i++) {
        cin >> a >> b >> c;
        vector<unsigned long long> factors = pf(a);

        unsigned long long sum = 0;

        for (unsigned long long j = b; j <= c; j++) {
            if (nogcd(j, factors)) sum += j;
        }

        cout << sum % 1000000007 << endl;
    }
    return 0;
}

