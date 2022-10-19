def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")  

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
#output
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.

#Move the last line of this program to the top, so the function call appears before the definitions.


repeat_lyrics()
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")  

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#output
# Traceback (most recent call last):
#   File "<string>", line 35, in <module>
# NameError: name 'repeat_lyrics' is not defined

