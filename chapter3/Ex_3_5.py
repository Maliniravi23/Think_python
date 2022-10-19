def func1():
    print("+", 4*'-', '+', 4*'-', '+', 4*'-', '+')


def func2():
    for x in range(4):
        print('|', 4*' ', '|', 4*' ', '|', 4*' ', '|')


def total():
    func1()
    func2()
    func1()
    func2()
    func1()
    func2()
    func1()


total()