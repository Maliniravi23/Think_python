def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    print(count)

result = count("Snugglebunnies", "u")
print(result)
