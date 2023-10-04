#include <iostream>
#include <vector>
#include <tuple>
#include <climits>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<tuple<int, int, int>> graph;

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        graph.emplace_back(u - 1, v - 1, w);
    }

    vector<int> dist(n, INT_MAX);
    dist[0] = 0;

    for (int i = 0; i < n - 1; ++i) {
        for (const auto& [u, v, w] : graph) {
            if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        if (dist[i] == INT_MAX) {
            dist[i] = 30000;
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << dist[i] << " ";
    }

    return 0;
}