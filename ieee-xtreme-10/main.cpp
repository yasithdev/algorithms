#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int diff(vector<int> x, int start, int length){

    return x[start + length - 1] - x[start];
}

int minsum(vector<int> x, int start, int end, int partitions){

    for (int i=0;i<partitions;i++){
        return minsum(x, 1, x.size(), partitions - 1);
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t, k, n;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> k >> n;
        vector<int> x;

        for (int j = 0; j < k; j++) {
            int xx;
            cin >> xx;
            x.push_back(xx);
        }

        sort(x.begin(), x.end());

        // algorithm
        cout << diff(x, 0, x.size()) << endl;
    }
    return 0;
}

