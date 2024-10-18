#include <iostream>
#include <string>
using namespace std;

int main() {
	string a,b;
    string ab;
    int la,lb;
    
    cin >> a >> b;
    la = a.size();
    lb = b.size();
    ab = a+b;
    printf("%i %i\n",la,lb);
    cout << ab << endl;
    cout << b[0] + a.substr(1) + " " +a[0] +b.substr(1)<< endl;

    return 0;
}
