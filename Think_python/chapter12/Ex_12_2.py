from random import random 
def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random(), word))

    t.sort(reverse=True)
    res = []
    for length, dupsort, word in t:

        res.append(word)
    return res

    
sortSequence = ('cat','rat','matt','fence','hair','chair')
print(sort_by_length(sortSequence))