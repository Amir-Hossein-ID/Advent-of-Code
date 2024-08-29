#include <bits/stdc++.h>

using namespace std;

int main() {
    string oldrow;
    getline(cin, oldrow);
    string newrow;
    int ans = 0;
    int j = 40;
    while (j--) {
        for (int i = 0; i < oldrow.size(); i++) {
            if (oldrow[i] == '.') ans++;
            if ((i > 0 && oldrow[i-1] == '^') ^ (i < oldrow.size()-1 && oldrow[i+1] == '^')) {
                newrow.push_back('^');
            } else {
                newrow.push_back('.');
            }
        }
        copy(newrow.begin(), newrow.end(), oldrow.begin());
        newrow.clear();
    }
    cout << ans;
}
