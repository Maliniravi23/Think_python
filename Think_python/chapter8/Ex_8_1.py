def backwards(string):
    backwards_length = -len(string)
    index = -1
    while index >= backwards_length:
        print(string[index])
        index -= 1

result = backwards("Snugglebunnies!")
print(result)
