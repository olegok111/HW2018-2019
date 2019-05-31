#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int sek, com;
    cin >> sek >> com;
    string sectors="", command="";
    char c1, c2;
    cin >> sectors;
    vector <pair <char, char>> commands;
    for (int i=0; i<com; i++) {
        cin >> command;
        if (command == "Forward") {
            c1 = 'f';
            cin >> c2;
            // TODO: commands and arguments to vector
            // TODO: locate the last element before GOTO command; it appears again => inf
        }
    }
    return 0;
}
