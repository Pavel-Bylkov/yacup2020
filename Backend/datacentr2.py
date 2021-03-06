def main(): 
    from sys import stdin
    N = int(stdin.readline().strip())
    klasters = []
    for _ in range(N):
        klasters.append(set(stdin.readline().strip().split()))
    flag = True
    while flag and len(klasters) > 1:
        flag = False
        k = len(klasters) - 1
        for i in range(k):
            for j in range(i + 1, len(klasters)):
                if not klasters[i].isdisjoint(klasters[j]):
                    klasters[i].update(klasters[j])
                    if j + 1 == len(klasters):
                        klasters.pop()
                    else:
                        klasters = klasters[:j] + klasters[j + 1:]
                    flag = True
                    break
            if flag:
                break
    Q = int(stdin.readline().strip())
    requests = []
    for _ in range(Q):
        X, K = stdin.readline().strip().split()
        requests.append((X, K, stdin.readline().strip().split()))
    for request in requests:
        R = 0
        result = []
        klaster = [x for x in klasters if request[0] in x]
        for k in request[2]:
            if k in klaster[0]:
                R += 1
                result.append(k)
        if R > 0:
            print(R, " ".join(result))
        else:
            print(0)

main()
