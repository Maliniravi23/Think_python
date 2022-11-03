def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        inv.setdefault(val, [])
        inv[val].append(key)
    return inv

hist = histogram('parrot')
inv = invert_dict(hist)
print(inv)