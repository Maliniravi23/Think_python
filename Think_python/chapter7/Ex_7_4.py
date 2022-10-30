import math

def eval_loop():
    while True:
        line = input("What should I evaluate?")
        if line == "done":
            break
        last = eval(line)
        print(last)
    
    return last
    
result = eval_loop()
print(result)