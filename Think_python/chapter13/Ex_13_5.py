import random
#chapter 11

def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)

    return d

def choose_from_hist(h):
    t = []
    for k, v in h.items():
        for i in range(v):
            t.append(k)

    return random.choice(t)

h = histogram(['a', 'a', 'b'])
for i in range(10):
    print(choose_from_hist(h))