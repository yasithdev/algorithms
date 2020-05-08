#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

// list, brush 1 color, brush 2 color
int mincount(vector<int> x, int a, int b, int ptr) {

    if (ptr == x.size()) return 0;

    int clr = x[ptr];
    if (a == 0 && b != clr) return 1 + mincount(x, clr, b, ptr + 1);
    if (b == 0 && a != clr) return 1 + mincount(x, a, clr, ptr + 1);

    if (clr != a && clr != b) {
        int a_, b_;
        for (int i = ptr + 1; i < x.size(); i++){
            if (x[i] == a) a_++;
            if(x[i] == b) b_++;
        }
        if(a_ == 0) return 1 + mincount(x, clr, b, ptr + 1);
        if(b_ == 0) return 1 + mincount(x, a, clr, ptr + 1);
        return 1 + min(mincount(x, clr, b, ptr + 1), mincount(x, a, clr, ptr + 1));
    } else {
        return mincount(x, a, b, ptr + 1);
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;

        vector<int> x(n);

        for (int j = 0; j < n; j++) {
            cin >> x[j];
        }

        cout << mincount(x, 0, 0, 0) << endl;
    }
    return 0;
}