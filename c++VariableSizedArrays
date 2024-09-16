#include <iostream>
#include <vector>

using namespace std;

int main() {
    int nArrays, nQueries;
    cin >> nArrays >> nQueries;

    vector<vector<int>> arrays(nArrays);

    for (int i = 0; i < nArrays; ++i) {
        int k;
        cin >> k;
        vector<int> arr(k);
        for (int j = 0; j < k; ++j) {
            cin >> arr[j];
        }
        arrays[i] = arr;
    }

    for (int i = 0; i < nQueries; ++i) {
        int x, y;
        cin >> x >> y;
        cout << arrays[x][y] << endl;
    }

    return 0;
}
