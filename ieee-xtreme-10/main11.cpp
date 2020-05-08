#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

#define MODULO 1000000007

using namespace std;

bool isPrime(unsigned long long n) {
    if (n == 2) return true;
    if (n % 2 == 0 || n < 2) return false;
    for (unsigned long long i = 3; i <= pow(n, 0.5); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

vector<unsigned long long> factors(unsigned long long n) {

    vector<unsigned long long> factors;

    if (n != 1) {
        for (unsigned long long i = 2; i <= (pow(n, 0.5)); ++i) {
            if (n % i == 0) {
                if (isPrime(i)) factors.push_back(i);
                if (isPrime(n / i)) factors.push_back(n / i);
            }
        }
    } else {
        factors.insert(factors.begin(), 1);
    }

    sort(factors.begin(), factors.end());
    factors.erase(unique(factors.begin(), factors.end()), factors.end());

    return factors;
}


int crosssum(vector<unsigned long long> x) {
    unsigned long long sum = 0;
    for (int i = 0; i < x.size(); ++i) {
        for (int j = 0; j < x.size(); ++j) {
            if (i == j) continue;
            sum += x[i] * x[j];
        }
    }
    return sum / 2;
}


int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        unsigned long long n, a, b, factorint_sum, allint_sum, cross_sum;
        cin >> n >> a >> b;

        vector<unsigned long long> f = factors(n);
        factorint_sum = 0;
        cross_sum = crosssum(f);
        allint_sum = ((b * (b + 1) / 2) - (a * (a - 1) / 2));

        for (int j = 0; j < f.size(); ++j) {
            int factor = f[j];
            unsigned long long sum;
            int low, high;
            low = ceil((double) a / (double) factor) - 1;
            high = floor((double) b / (double) factor);
            sum = factor * (high * (high + 1) - low * (low + 1)) / 2;
            factorint_sum += sum;
        }

        unsigned long long result = allint_sum + cross_sum - factorint_sum;
        cout << result % MODULO << endl;
    }
}