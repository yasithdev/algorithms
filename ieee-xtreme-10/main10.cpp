#include <cmath>
#include <vector>
#include <iostream>
#include <map>
#include <sstream>

using namespace std;

// Create map in chronological order
map<int, int> createmap(vector<int> x) {

    int next = 0;
    map<int, int> map;

    // Insert into map ordered by thread time. value contains #of posts
    for (int i = 0; i < x.size(); ++i) {
        switch (x[i]) {

            // New thread
            case 0:
                map[next++]++;
                break;

                // Existing thread
            default:
                int iter = 0;
                for (int j = 0; j < map.size(); ++j) {
                    if (iter + map[j] >= x[i]) {
                        map[j]++;
                        break;
                    } else {
                        iter += map[j];
                        continue;
                    }
                }
        }
    }

    return map;
}

// Calculate the result
map<int, int> calculate(map<int, int> &postmap, int a) {
    // Initialize map with one slot
    map<int, int> result;

    // Initialize one page
    result[0] = 0;

    int iter = 0;
    int p = 0;

    while (iter < postmap.size()) {
        while (p < result.size()) {

            if (postmap[iter] > 0) {
                if ((a - result[p]) >= postmap[iter]) {
                    result[p] += postmap[iter];
                    postmap[iter] = 0;
                    iter++;
                    break;

                } else {
                    // try immediate next page. adds a page if none exist
                    result[p + 1] += postmap[iter];
                    postmap[iter] = 0;
                    iter++;
                    p++;
                    break;
                }
            }
        }
    }
    return result;
}

int findmin(int iter, int p, map<int,int> postmap, map<int, int> result, int size){
    map<int, int> &inter = postmap;
        if ((size - result[p]) >= inter[iter]) {
            result[p] += inter[iter];
            inter[iter] = 0;
            iter++;
            return size - result[p];

        } else {
            return findmin(iter, ++p, inter, result, size);
        }
}

// Inputs
int main() {
    int a, p;
    while (cin >> a >> p) {

        vector<int> x(p);

        for (int i = 0; i < p; ++i) {
            cin >> x[i];
        }

        map<int, int> m = createmap(x);
        map<int, int> r = calculate(m, a);

        int max = 0;

        for (int j = 0; j < r.size(); ++j) {
            if ((a - r[j]) > max) max = (a - r[j]);
        }

        cout << max << endl;
    }
    return 0;
}