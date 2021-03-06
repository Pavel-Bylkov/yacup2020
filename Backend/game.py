import sys

K, N = map(int, sys.stdin.readline().strip().split())
karts = tuple(map(int, sys.stdin.readline().strip().split()))
i = 0
kp = 0
kv = 0
while kp < K and kv < K and i < N:
    if karts[i] % 15 == 0:
        i += 1
        continue
    if karts[i] % 5 == 0:
        kp += 1
    elif karts[i] % 3 == 0:
        kv += 1
    i += 1
if kp == kv:
    print("Draw")
elif K - kp > K - kv:
    print("Petya")
else:
    print("Vasya")