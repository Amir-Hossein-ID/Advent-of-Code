#include <bits/stdc++.h>

using namespace std;

int main() {
    string oldrow;
    getline(cin, oldrow);
    string newrow(oldrow.size(), '1');
    long long ans = 0;
    int j = 400000;
    while (j--) {
        for (int i = 0; i < oldrow.size(); i++) {
            if (oldrow[i] == '.') ans++;
            if ((i > 0 && oldrow[i-1] == '^') ^ (i < oldrow.size()-1 && oldrow[i+1] == '^')) {
                newrow[i] = '^';
            } else {
                newrow[i] = '.';
            }
        }
        copy(newrow.begin(), newrow.end(), oldrow.begin());
    }
    cout << ans;
}
