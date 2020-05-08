#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int r_lru, r_fifo, p, s, n;

void lru(int pg, vector<int> &mem) {

    for (int i = 0; i < mem.size(); i++) {
        if (pg == mem[i]) {
            mem.erase(mem.begin() + i);
            mem.push_back(pg);
            return;
        }
    }

    if (mem.size() == p) {
        mem.erase(mem.begin());
        mem.push_back(pg);
        r_lru++;

    } else {
        mem.push_back(pg);
    }
}

void fifo(int pg, vector<int> &mem) {

    for (int i = 0; i < mem.size(); i++) {
        if (pg == mem[i]) return;
    }

    if (mem.size() == p) {
        mem.erase(mem.begin());
        mem.push_back(pg);
        r_fifo++;

    } else {
        mem.push_back(pg);
    }
}

int main() {
    int t;
    cin >> t;

    // for each test case
    for (int i = 0; i < t; i++) {
        cin >> p >> s >> n;
        r_fifo = 0, r_lru = 0;

        vector<int> mem_fifo(0), mem_lru(0);

        for (int j = 0; j < n; j++) {
            int loc;
            cin >> loc;
            int pg = floor(loc / s);

            fifo(pg, mem_fifo);
            lru(pg, mem_lru);
        }

        cout << ((r_fifo > r_lru) ? "yes " : "no ") << r_fifo << " " << r_lru << endl;
    }
    return 0;
}

