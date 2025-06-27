def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')
#main
do_twice(print_spam)