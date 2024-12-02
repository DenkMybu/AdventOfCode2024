with open('list.txt') as f:
        a, b = zip(*(map(int, line.split()) for line in f))
        a,b = sorted(a), sorted(b)
        print(a[:3])
        print(b[:3])
        result = sum(x * b.count(x) for x in a)
        print(result)
