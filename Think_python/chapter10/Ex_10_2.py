def capitalize_nested(t):
    res = []
    for s in t:
        res.append(s)
    return res

t = [["thank","you"],["for","everything"]]
print(capitalize_nested(t))
