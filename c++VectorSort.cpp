#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;


int main() {
    int ln;
    vector<int> vec;
    cin >> ln;
    vec.resize(ln);
    for (int i = 0; i <ln ; i++) {
        cin >> vec[i];
    }
    sort(vec.begin(), vec.end());
    stringstream ss;
    for (int i = 0; i <ln ; i++) {
        ss << vec[i];
        ss << " ";
    }
    string res = ss.str();
    std::cout << res <<std::endl;
    return 0;
}
