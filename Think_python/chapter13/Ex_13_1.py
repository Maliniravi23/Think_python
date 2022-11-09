import string

def get_words_from_file(text, encode = "utf8"):
    punct = string.punctuation
    punct += '‘’“”—'
    punct += string.digits
    out = " " * len(punct)
    print(out)
    opened_text = open(text, 'r', encoding = encode)
    t = []
    for line in opened_text:
        translation = line.maketrans(punct, out)
        for word in line.translate(translation).split():
            t.append(word.strip().lower()) 
    print(t)      
    return t

new = get_words_from_file('/Users/malini/Desktop/Think_python/chapter13/words.txt')
