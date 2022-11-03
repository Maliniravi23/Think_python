f = open('/Users/malini/Desktop/Think_python/chapter11/words.txt')

def create_word_dict():
    word_dict = dict()
    for line in f:
        word = line.strip()
        word_dict[word] = word
        print(word_dict)
    return word_dict

