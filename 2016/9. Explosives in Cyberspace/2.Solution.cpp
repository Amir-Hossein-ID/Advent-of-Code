#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream input("input.txt");
    char ch;
    long long ans = 0;
    stack<pair<int, long long>> rewards;
    int where = 0;
    while (input.get(ch)) {
        if (ch == '(') {
            where++;
            string num1;
            string num2;
            while (where++ && input.get(ch) && ch != 'x') {
                num1.push_back(ch);
            }
            while (where++ && input.get(ch) && ch != ')') {
                num2.push_back(ch);
            }
            // store how much character does it count until "where"
            // for example (3x2) means 3 characters from now (3 + where) will have 2 duplicates each
            long long rew = stoi(num2);
            int togo = stoi(num1) + where;
            if (!rewards.empty() && rewards.top().first >= togo) {
                rewards.push({togo, rew * rewards.top().second});
            } else {
                rewards.push({togo, rew});
            }
            
        } else {
            while (!rewards.empty() && rewards.top().first < where) rewards.pop();
            if (rewards.empty()) ans++;
            else {
                ans += rewards.top().second;
            }
            where++;
            while (!rewards.empty() && rewards.top().first <= where) rewards.pop();
        }
    }
    cout << ans;
}
