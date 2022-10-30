def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


result = find("Snugglebunnies", "u", 0)
print(result)

