#include <bits/stdc++.h>
using namespace std;

struct Star {
    long long x, y, dx, dy;
};

struct Point {
    long long x, y;
    bool operator<(const Point &p) const {
        if (x != p.x) return x < p.x;
        return y < p.y;
    }
};

// 벡터 외적
long long cross(const Point &a, const Point &b, const Point &c) {
    long long x1 = b.x - a.x, y1 = b.y - a.y;
    long long x2 = c.x - a.x, y2 = c.y - a.y;
    return x1 * y2 - y1 * x2;
}

// 볼록껍질 - Andrew's monotone chain
vector<Point> convexHull(vector<Point> &pts) {
    int n = (int)pts.size();
    if (n <= 1) return pts;
    sort(pts.begin(), pts.end());

    vector<Point> lower, upper;

    for (int i = 0; i < n; i++) {
        while ((int)lower.size() >= 2 && cross(lower[lower.size()-2], lower.back(), pts[i]) <= 0)
            lower.pop_back();
        lower.push_back(pts[i]);
    }
    for (int i = n - 1; i >= 0; i--) {
        while ((int)upper.size() >= 2 && cross(upper[upper.size()-2], upper.back(), pts[i]) <= 0)
            upper.pop_back();
        upper.push_back(pts[i]);
    }
    lower.pop_back();
    upper.pop_back();

    lower.insert(lower.end(), upper.begin(), upper.end());
    return lower;
}

// 두 점 사이 거리 제곱
long long distSq(const Point &a, const Point &b) {
    long long dx = a.x - b.x;
    long long dy = a.y - b.y;
    return dx*dx + dy*dy;
}

// 로테이팅 칼립스 - 볼록껍질에서 최대 거리 제곱 찾기
long long rotatingCalipers(const vector<Point> &hull) {
    int n = (int)hull.size();
    if (n == 1) return 0;
    if (n == 2) return distSq(hull[0], hull[1]);

    long long maxDist = 0;
    int j = 1;
    for (int i = 0; i < n; i++) {
        while (abs(cross(hull[i], hull[(i+1)%n], hull[(j+1)%n])) > abs(cross(hull[i], hull[(i+1)%n], hull[j])))
            j = (j + 1) % n;
        maxDist = max(maxDist, distSq(hull[i], hull[j]));
        maxDist = max(maxDist, distSq(hull[(i+1)%n], hull[j]));
    }
    return maxDist;
}

// t시점 별 위치 계산
vector<Point> getPositions(const vector<Star> &stars, long long t) {
    vector<Point> pts;
    pts.reserve(stars.size());
    for (auto &s : stars) {
        pts.push_back({s.x + s.dx * t, s.y + s.dy * t});
    }
    return pts;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long T;
    cin >> N >> T;

    vector<Star> stars(N);
    for (int i = 0; i < N; i++) {
        cin >> stars[i].x >> stars[i].y >> stars[i].dx >> stars[i].dy;
    }

    long long left = 0, right = T;

    // 삼분탐색으로 최소 최대 거리 찾기
    while (right - left > 3) {
        long long mid1 = left + (right - left) / 3;
        long long mid2 = right - (right - left) / 3;

        auto pts1 = getPositions(stars, mid1);
        auto hull1 = convexHull(pts1);
        long long dist1 = rotatingCalipers(hull1);

        auto pts2 = getPositions(stars, mid2);
        auto hull2 = convexHull(pts2);
        long long dist2 = rotatingCalipers(hull2);

        if (dist1 > dist2) left = mid1;
        else right = mid2;
    }

    long long ans_t = left;
    auto pts = getPositions(stars, left);
    auto hull = convexHull(pts);
    long long ans_dist = rotatingCalipers(hull);

    for (long long t = left + 1; t <= right; t++) {
        auto pts_t = getPositions(stars, t);
        auto hull_t = convexHull(pts_t);
        long long dist_t = rotatingCalipers(hull_t);
        if (dist_t < ans_dist) {
            ans_dist = dist_t;
            ans_t = t;
        }
    }

    cout << ans_t << "\n" << ans_dist << "\n";

    return 0;
}
