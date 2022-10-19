#2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
word = "spam"
def do_twice(f, word):
   f(word)
   f(word)

def print_spam(word):
   print(word)

do_twice(print_spam, word)
#spam
#spam

#3. Write a more general version of print_spam, called print_twice, that takes a string as a parameter and prints it twice

string = "spam"

def print_twice(string):
   print(string)
   print(string)

print_twice(string)
#spam
#spam

#4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument
Word1 = "spam"
do_twice(print_twice, Word1)
#spam
#spam

#5. Define a new function called do_four that takes a function object and a value and calls the
#function four times, passing the value as a parameter.
#There should be only two statements in the body of this function, not four.
arg = 'spam'
def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print(arg)
    print(arg)

do_twice(print_twice, arg)
print()

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, arg)

# spam
# spam
# spam
# spam

# spam
# spam
# spam
# spam
# spam
# spam
# spam
# spam
