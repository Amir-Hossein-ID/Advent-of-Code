#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream input("input.txt");
    char ch;
    int ans = 0;
    while (input.get(ch)) {
        if (ch == '(') {
            string num1;
            string num2;
            while (input.get(ch) && ch != 'x') num1.push_back(ch);
            while (input.get(ch) && ch != ')') num2.push_back(ch);
            int togo = stoi(num1);
            ans += togo * stoi(num2);
            while (togo--) input.get(ch);
        } else ans++;
    }
    cout << ans;
}
