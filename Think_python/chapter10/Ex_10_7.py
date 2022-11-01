import re


def is_anagram(word1, word2):
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    return False

word1 = "peT"
word2 = "tep"
print(is_anagram(word1, word2))