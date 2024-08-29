#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    long long n;
    cin >> n;
    
    long long i = 1;
    vector<long long> firsts;
    long long ans = 1;

    while (ans * 10 < n) {
        i++;
        ans = 1;
        long long sq = sqrt(i) + 1;
        
        for (long long j : firsts) {
            if (j > sq) {
                break;
            }
            long long cur = 1;
            long long newj = j;
            while (i % newj == 0) {
                cur += newj;
                newj *= j;
            }
            ans *= cur;
        }
        
        if (ans == 1) {
            firsts.push_back(i);
            ans += i;
        }
    }
    
    cout << i;

    return 0;
}
