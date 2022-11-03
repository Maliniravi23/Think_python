def reverse_lookup(d, v):
    list_of_matches = []
    for k in d:
        if d[k] == v:
            list_of_matches.append(k)
    return list_of_matches

def histogram(word):
    dictionary = dict()
    for l in word:
        dictionary[l] = 1 + dictionary.get(l, 0)
    return dictionary

h = histogram('parrot')
k = reverse_lookup(h, 2)
print(k)