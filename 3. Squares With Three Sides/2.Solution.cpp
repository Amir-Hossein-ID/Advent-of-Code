#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans = 0;
    int x[3], y[3], z[3];
    auto check = [&](int x[]) {
        return x[0] + x[1] > x[2] and x[0] + x[2] > x[1] and x[2] + x[1] > x[0];
    };

    for (int i = 0; i < 1734 / 3; i++) { // no of lines of input
        cin >> x[0] >> y[0] >> z[0];
        cin >> x[1] >> y[1] >> z[1];
        cin >> x[2] >> y[2] >> z[2];
        if (check(x)) ans++;
        if (check(y)) ans++;
        if (check(z)) ans++;
    }

    cout << ans;
}
