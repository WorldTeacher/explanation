#einfacher for-loop
__name__ = input('Name of the program: ')
#define functions
#int
def integers():
    for i in range(5): #für jeden Wert von 0 bis 4, wird i durchgezählt und gedruckt
        print(i)

#str
def strings():
    for i in 'Hello World': #für jedes Zeichen in der Zeichenkette, wird i durchgezählt und gedruckt
        print(i)
#array
def arrays():
    arr=[{'name':'John', 'age':23}, {'name':'Jane', 'age':24}, {'name':'Jack', 'age':25}] #ein Array mit 3 Objekten
    for i in arr: #für jeden Wert in der Liste, wird i durchgezählt und gedruckt
        print(i)
#start of program
if __name__ == "integers":
    integers()
elif __name__ == "strings":
    strings()
elif __name__ == "arrays":
    arrays()
else:
    print("Nothing")
        