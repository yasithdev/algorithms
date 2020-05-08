#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    float a, b, c, d, l, m, n, k, p, q, r, s, D, x, y, z;

    cin >> a >> b >> c >> d >> l >> m >> n >> k >> p >> q >> r >> s;
    cout << a << b << c << d << l << m << n << k << p << q << r << s << endl;

    D = (a * m * r + b * p * n + c * l * q) - (a * n * q + b * l * r + c * m * p);
    x = ((b * r * k + c * m * s + d * n * q) - (b * n * s + c * q * k + d * m * r)) / D;
    y = ((a * n * s + c * p * k + d * l * r) - (a * r * k + c * l * s + d * n * p)) / D;
    z = ((a * q * k + b * l * s + d * m * p) - (a * m * s + b * p * k + d * l * q)) / D;

    cout << x << " " << y << " " << z << endl;
    return 0;
}