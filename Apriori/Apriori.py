def creatcandidate(data):
    cand = []
    for raw in data:
        for item in raw:
            if item not in cand:
                cand.append(item)
    cand.sort()
    return list(map(frozenset, cand))


def sub_count(data, candidate, minsupp):
    sub_count = {}
    for i in data:
        for j in candidate:
            if j.issubset(i):
                if j not in sub_count:
                    sub_count[j] = 1
                else:
                    sub_count[j] += 1
    l = []
    for i in sub_count:
        if sub_count[i] >= minsupp:
            l.append(i)
    return l, sub_count


def union(l, k):
    c = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            l1 = list(l[i])[:k-2] # = []
            l2 = list(l[j])[:k-2] # = []
            # mục đích để nối l1 với l2
            if l1 == l2:
                c.append(l[i] | l[j]) #union
    return c


def apriori(data, minsup):
    cand = creatcandidate(data)
    l, count = sub_count(data, cand, minsup)
    l = [l] #chuyển l sang dạng [[l]]
    k = 2
    while len(l[k - 2]) > 0: #l[k-2] = list[0] = l tránh trường hợp sử dụng luôn l sẽ bị lỗi list to list do l đang chứa bộ các frozenset
        c = union(l[k-2], k)
        t1, count1 = sub_count(data, c, minsup)
        count.update(count1)
        l.append(c)
        k += 1
    return l, count


if __name__ == '__main__':
    data = []
    dataSetFilename = 'Apriori.txt'
    with open(dataSetFilename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))

    print("?Minsupport")
    minSupp = input()
    minSupp = int(minSupp)
    sets, counts = apriori(data, minSupp)

    print("\nANS:\n")
    for k, v in counts.items():
        if (v >= minSupp): print(list(k), v)
