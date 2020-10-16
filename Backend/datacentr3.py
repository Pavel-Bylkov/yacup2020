#coding: utf-8
def add_in_union(group, union_klasters):
    if len(union_klasters):
        for klaster in union_klasters:
            if len(klaster.intersection(group)):
                klaster.update(group)
                return
    union_klasters.append(group)
def main():
    from sys import stdin
    N = int(stdin.readline().strip())
    klasters = []
    for _ in range(N):
        klasters.append(stdin.readline().strip().split())
    flag = True
    while flag and len(klasters) > 1:
        flag = False
        klaster_index = []
        for i, klasteri in enumerate(klasters):
            klaster_index.append(set([i]))
            for j, klasterj in enumerate(klasters):
                for server in klasteri:
                    if i != j and (server in klasterj):
                        klaster_index[i].add(j)
                        flag = True
        if flag:
            union_klasters = []
            result = []
            for group in klaster_index:
                add_in_union(group, union_klasters)
            for kl_ind in union_klasters:
                tmp = set()
                for ind in kl_ind:
                    tmp.update(klasters[ind])
                result.append(tmp)
            klasters = result
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

