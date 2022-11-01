def cumulative_sum(t):
    j = 0
    m =[]
    for i in t:
        j +=i
        m.append(j)
    return m

t = [1,3,4,6,7]
print(cumulative_sum(t))
