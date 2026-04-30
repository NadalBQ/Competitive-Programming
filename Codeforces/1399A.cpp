#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        cin >> n;
        vector<int> l(n);
        for (int j = 0; j < n; ++j) {
            cin >> l[j];
        }
        bool yes = true;
        sort(l.begin(), l.end());

        for (int j = 1; j < n; ++j) {
            if ((l[j] - l[j-1]) > 1) {
                yes = false;
                break;
            }
        }
        if (yes) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
}