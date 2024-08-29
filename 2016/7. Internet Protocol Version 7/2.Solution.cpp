#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans = 0;
    ifstream input("input.txt");
    string ip;
    while (getline(input, ip)) {
        bool right = false;
        map<char, set<char>> fcond;
        map<char, set<char>> scond;
        int j = 0;
        while (j < ip.size() - 2) {
            for (; j < ip.size() - 2; j++) {
                if (ip[j] == ip[j+2] and ip[j] != ip[j+1]) {
                    if (scond[ip[j+1]].find(ip[j]) != scond[ip[j+1]].end()) {
                        right = true;
                        break;
                    }
                    fcond[ip[j]].insert(ip[j+1]);
                } else if (ip[j] == '[') {
                    j++;
                    break;
                }
            }
            for (; j < ip.size() - 2; j++) {
                if (ip[j] == ip[j+2] and ip[j] != ip[j+1]) {
                    if (fcond[ip[j+1]].find(ip[j]) != fcond[ip[j+1]].end()) {
                        right = true;
                        break;
                    }
                    scond[ip[j]].insert(ip[j+1]);
                } else if (ip[j] == ']') {
                    j++;
                    break;
                }
            }
            if (right) break;
        }
        if (right) ans++;
    }
    
    cout << ans;
}
