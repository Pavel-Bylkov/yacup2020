#coding = utf-8
def add_in_union(group, union_klasters):
    """docstring"""
    if len(union_klasters) != 0:
        for klaster in union_klasters:
            if len(klaster.intersection(group)):
                klaster.update(group)
                return
    union_klasters.append(group)


def main():
    """docstring"""
    from sys import stdin

    n_lines = int(stdin.readline().strip())
    klasters = []
    for _ in range(n_lines):
        klasters.append(stdin.readline().strip().split())
    klaster_index = []
    for klasteri in klasters:
        klaster_index.append(set(klasteri))
        for klasterj in klasters:
            for server in klasteri:
                if server in klasterj:
                    klaster_index[-1].update(klasterj)
    union_klasters = []
    for group in klaster_index:
        add_in_union(group, union_klasters)
    q_requests = int(stdin.readline().strip())
    requests = []
    for _ in range(q_requests):
        x_ind, k_servers = stdin.readline().strip().split()
        requests.append((x_ind, k_servers, stdin.readline().strip().split()))
    for request in requests:
        r_result = 0
        result = []
        klaster = [x for x in union_klasters if request[0] in x]
        for k in request[2]:
            if k in klaster[0]:
                r_result += 1
                result.append(k)
        if r_result > 0:
            print(r_result, " ".join(result))
        else:
            print(0)


main()
