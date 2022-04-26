#einfacher for-loop
__name__ = input('Name of the program: ')
#int
def integers():
    for i in range(5): #für jeden Wert von 0 bis 4, wird i durchgezählt und gedruckt
        print(i)

#str
def strings():
    for i in 'Hello World': #für jedes Zeichen in der Zeichenkette, wird i durchgezählt und gedruckt
        print(i)

if __name__ == "integers":
    integers()
elif __name__ == "strings":
    strings()