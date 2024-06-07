#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans = 0;
    string room;
    for (int i = 0; i < 974; i++) { // no of lines of input
        getline(cin, room);
        bool brack = false;
        map<char, int> counter;
        vector<char> chars;
        string room_name;
        int num = 0;
        for (auto j : room) {
            if (brack and j != ']') {
                chars.push_back(j);
            } else if (j >= 'a' and j <= 'z') {
                counter[j]++;
                room_name.push_back(j);
            } else if (j >= '0' and j <= '9') {
                num = num * 10 + (j - '0');
            } else if (j == '[') {
                brack = true;
            } else {
                room_name.push_back(' ');
            }
        }
        vector<pair<char, int>> vec;
        for (auto j : counter) {
            vec.push_back(j);
        }

        sort(vec.begin(), vec.end(), [&](pair<char, int> a, pair<char, int> b) {
            if (a.second != b.second) {
                return a.second > b.second;
            }
            return a.first < b.first;
        });

        bool ok = true;
        for (int j = 0; j < 5; j++) {
            if (vec[j].first != chars[j]) ok = false;
        }
        if (ok) {
            for (int j = 0; j < room_name.size(); j++) {
                if (room_name[j] != ' ') {
                    room_name[j] = (room_name[j] - 'a' + num % 26) % 26 + 'a';
                }
            }
            if (room_name.find("north") != string::npos) {
                ans = num;
                cout << room_name << " " << num << '\n';
            }
            
        }
    }
    
    cout << ans;
}
