#include <iostream>
#include <vector>

using namespace std;

bool check(std::vector<std::vector<int>> arr, int x, int y, int n){
    int sum = 0;
    for (int i = x; i < x + n; ++i) {
        for (int j = y; j < y+n; ++j) {
            if(arr[i][j] != 0){
                sum += 1;
            }
        }
    }
    return sum < n;
}

bool array_check(std::vector<std::vector<int>> a, int n, int h, int w){
    if(n<3){
        return true;
    }
    for (int i = 0; i < h - n + 1; ++i) {
        for (int j = 0; j < w - n + 1; ++j) {
            if (!check(a, i, j, n)){
                return false;
            }
        }
    }
    return true;
}

int main() {
    int c;
    std::cin >> c;
    for (int i = 0; i < c; ++i) {
        int h,w;
        std::cin >> h >> w;
        if(h<3 or w<3){
            std::cout << "YES" << std::endl;
        } else {
            std::vector<std::vector<int>> board = new std::vector();
            for (int j = 0; j < h; ++j) {
                std::vector<int> row = new std::vector();
                for (int k = 0; k < w; ++k) {
                    int temp;
                    std::cin >> temp;
                    row.push_back(temp);
                }
                board.push_back(row);
            }
            int n;
            if(h<w){
                n = h;
            } else{
                n = w;
            }
            bool ans = true;
            for (int l = n; l > 2; --l) {
                if(!array_check(board,l,h,w)){
                    ans = false;
                    break;
                }
            }
            std::cout << (ans ? "YES" : "NO");
        }
    }
    return 0;
}