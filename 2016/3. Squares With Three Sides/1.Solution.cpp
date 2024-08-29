#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans = 0;
    int x, y, z;
    for (int i = 0; i < 1734; i++) { // no of lines of input
        cin >> x >> y >> z;
        if (x + y > z and x + z > y and z + y > x) ans++;
    }
    cout << ans;
}
