#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long n;
    cin >> n;
    vector<long long> arr(n, 1);
    for (long long i = 2; i < (n + 1) / 2; i++) {
        for (int j = i; j < n; j+=i) {
            arr[j] += i;
        }
    }

    for (int i = 0; i < n; i++) {
        if (arr[i] * 10 >= n) {
            cout << i;
            break;
        }
    }
}
