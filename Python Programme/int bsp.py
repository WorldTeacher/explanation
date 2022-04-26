#here are some examples on how to use int

from re import M


string='This is a string' #auch Leerzeichen werden als Zeichen gewertet
def main(*argv):
    for x in string:
        print(x)
def main2(*argv):
    for x in string:
        print('Value: ' + x)
__name__=input('Name of the program: ')
if __name__ == 'main':
    main()
elif __name__ == 'main2':
    main2()
else:
    print('Nothing')

    