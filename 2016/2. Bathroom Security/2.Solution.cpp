#include <bits/stdc++.h>

using namespace std;

int main() {
    string moves;
    char arr[5][5] = {
        {0,0,'1',0,0},
        {0,'2','3','4',0},
        {'5','6','7','8','9'},
        {0,'A','B','C',0},
        {0,0,'D',0,0}
    };

    int curx = 0, cury = 2;
    string code = "";

    for (int i = 0; i < 5; i++) { // no of lines of input
        getline(cin, moves);
        for (auto j : moves) {
            if (j == 'U' and cury > 0 and arr[cury - 1][curx] != 0) cury--;
            else if (j == 'D' and cury < 4 and arr[cury + 1][curx] != 0) cury++;
            else if (j == 'R' and curx < 4 and arr[cury][curx + 1] != 0) curx++;
            else if (j == 'L' and curx > 0 and arr[cury][curx - 1] != 0) curx--;
        }
        code += arr[cury][curx];
    }

    cout << code;
}
