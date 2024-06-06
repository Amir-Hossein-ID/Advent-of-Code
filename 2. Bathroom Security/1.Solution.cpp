#include <bits/stdc++.h>

using namespace std;

int main() {
    string moves;
    int arr[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
    int curx = 1, cury = 1;
    int code = 0;

    for (int i = 0; i < 5; i++) { // no of lines of input
        getline(cin, moves);
        for (auto j : moves) {
            if (j == 'U' and cury > 0) cury--;
            else if (j == 'D' and cury < 2) cury++;
            else if (j == 'R' and curx < 2) curx++;
            else if (j == 'L' and curx > 0) curx--; 
        }
        code = code * 10 + arr[cury][curx];
    }

    cout << code;
}
