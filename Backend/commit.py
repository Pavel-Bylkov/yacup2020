import sys

maxN = N = int(sys.stdin.readline().strip())
n = 0
list1 = []
list0 = []
while N > 0:
    if (n + N) % 2 == 0:
        k = (n + N) // 2
    else:
        k = (n + N) // 2 + 1
    if k in list1 and k + 1 <= maxN:
        k = k + 1
    elif k in list0 and k - 1 > 0:
        k = k - 1
    print(k)
    sys.stdout.flush()
    m = sys.stdin.readline().strip()
    if N - n > 1 and m == '1':
        list1.append(k)
        n = k
        if n == maxN:
            break
    elif N - n > 2 and m == '0':
        list0.append(k)
        N = k - 1
    elif m == '0':
        print("!", k)
        break
    elif k + 1 in list0:
        print("!", k + 1)
        break
    elif k + 1 <= maxN:
        print(k + 1)
        sys.stdout.flush()
        m = sys.stdin.readline().strip()
        if m == '0':
            print("!", k + 1)
            break
        elif k + 2 <= maxN:
            print("!", k + 2)
            break
    else:
        break