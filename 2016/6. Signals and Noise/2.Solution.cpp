#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans = 0;
    map<int, map<char, int>> chars;
    for (int i = 0; i < 572; i++) { // no of lines of input
        string word;
        getline(cin, word);
        for (int j = 0; j < word.size(); j++) {
            chars[j][word[j]]++;
        }
    }
    string answer;
    for (auto i = chars.begin(); i != chars.end(); i++) {
        answer.push_back(min_element(i->second.begin(), i->second.end(), [](const pair<char, int> &a, const pair<char, int> &b) {
            return  a.second < b.second;
        })->first);
    }
    
    cout << answer;
}
