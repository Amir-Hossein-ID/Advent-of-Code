#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans = 0;
    ifstream input("input.txt");
    string ip;
    while (getline(input, ip)) {
        bool fcond = false, scond = true;
        int j = 0;
        while (j < ip.size() - 3) {
            for (; j < ip.size() - 3; j++) {
                if (ip[j] == ip[j+3] and ip[j+1] == ip[j+2] and ip[j] != ip[j+1]) {
                    fcond = true;
                } else if (ip[j] == '[') {
                    j++;
                    break;
                }
            }
            for (; j < ip.size() - 3; j++) {
                if (ip[j] == ip[j+3] and ip[j+1] == ip[j+2] and ip[j] != ip[j+1]) {
                    scond = false;
                } else if (ip[j] == ']') {
                    j++;
                    break;
                }
            }
        }
        if (fcond && scond) ans++;
    }
    
    cout << ans;
}
