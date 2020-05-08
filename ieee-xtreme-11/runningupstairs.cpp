#include <iostream>
#include <map>
#include <tclDecls.h>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b;
    return 0;
}
std::map<int, int> prunes;

int calc_steps(int n, int i, std::map<int,int>* p){
    if((n-i)>1){
        if (prunes.find(i)){

        }
    }
}

def calc_steps(n, i):
global prunes
if n - i > 1:
if i in prunes.keys():
return prunes[i]
else:
prunes[i+2] = calc_steps(n, i + 2)
prunes[i+1] = calc_steps(n, i + 1)
return prunes[i+1] + prunes[i+2]
else:
return 1


for _ in range(get_number()):
n = get_number()
if n == 1:
print(1)
else:
print(calc_steps(n, 0))
