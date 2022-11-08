from random import randint
def sort_letters(string):
    return ''.join(sorted(list(string.lower())))

def find_anagrams(text):
    sorted_dict = {}

    for line in text:
        orig_word = line.strip()
        print("orig_word",orig_word)
        sorted_word = sort_letters(orig_word)
        print("sorted word",sorted_word)
        sorted_dict.setdefault(sorted_word, []).append(orig_word)
        print("dorted dict",sorted_dict)
        
    anagrams = []

    for k, v in sorted_dict.items():
        l = len(v)
        if l > 1:
            anagrams.append((l, k, v))
            
    return anagrams

fin = "conserve"
print(find_anagrams(fin))