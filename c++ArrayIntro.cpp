#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int nline;
    cin >> nline;
    std::vector<int> arr(nline);
    for (int i =0 ;i < nline;i++){
        std::cin >> arr[i];
    }
    std::reverse(arr.begin(), arr.end());
        for (int i = 0; i < nline; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
