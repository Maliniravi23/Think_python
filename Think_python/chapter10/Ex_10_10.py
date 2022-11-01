def make_word_list_with_append():
    new = open('/Users/malini/Desktop/Think_python/chapter10/words.txt')
    t = []

    for i in new:   
        t.append(i.strip())
    return t

print(make_word_list_with_append())

def make_word_list_with_add():   
    f = open('/Users/malini/Desktop/Think_python/chapter10/words.txt')
    t_1 = []

    for j in f:   
        t_1 = t_1 + [j.strip()]
    return t_1

print(make_word_list_with_add())
