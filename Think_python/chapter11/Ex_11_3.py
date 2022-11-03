def histogram(word):
    dictionary = dict()
    for l in word:
        dictionary[l] = 1 + dictionary.get(l, 0)
    return dictionary

def print_hist(histogram):
    histo_list = sorted(histogram.keys())
    for l in histo_list:
        print(l, histogram[l])

h = histogram('parrot')
print_hist(h)