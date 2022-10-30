def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True

result1 = any_lowercase1("kkjdEq")
result2 = any_lowercase2("kWWeq")
result3 = any_lowercase3("BNWE")
result4 = any_lowercase4("oeioQ")
result5 = any_lowercase5("vmnQQQ")

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)