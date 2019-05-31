#include <iostream>
#include <vector>

using namespace std;

int main() {
    int _len, _check_amount;
    cin >> _len >> _check_amount;
    const int len = _len+1-1, check_amount=_check_amount+1-1;
    int cucheck, max_gap=-1, cugap=0;
    char data[len];
    cin >> data;
    for (int i=0; i<len; i++) {
        if (data[i] == '1') {
            cugap++;
            if (max_gap < cugap) {
                max_gap = cugap;
            }
        } else {
            cugap = 0;
        }
    }
    vector <bool> answers(check_amount);
    for (int i=0; i<check_amount; i++) {
        cin >> cucheck;
        if (cucheck <= max_gap) {
            answers[i] = 0;
        } else {
            answers[i] = 1;
        }
    }
    for (bool ans : answers) {
        if (ans) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
