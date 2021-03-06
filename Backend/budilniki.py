import sys

N, X, K = map(int, sys.stdin.readline().strip().split())
time = set(map(int, sys.stdin.readline().strip().split()))
min_t = min(time)
max_t = min_t + X * K
time = {x for x in time if min_t < x < max_t}
time.add(min_t + X)
for _ in range(2, K):
    min_t = min(time)
    time.remove(min_t)
    time.add(min_t + X)
print(min(time))