import time #for sleep
import random #for random number
#ask for input of __name__
def small_game():
    #declare variables that the program is based on
    min_profit= 50
    max_profit= 100
    min_expenses= 10
    max_expenses= 75
    min_sales= 10
    max_sales= 75
    salary= 200
    bank=500
    ownbank= 0
    day=0

    while bank>=0: #As long as bank is greater than or equal to 0, the loop will continue
        #if the bank is less than 0, the loop will break
        #variables declared here will be used in the loop
        profit= random.randint(min_profit, max_profit)
        expenses= random.randint(min_expenses, max_expenses)
        sales= random.randint(min_sales, max_sales)
        bank= bank + profit - expenses - salary
        if bank>200: #if the bank has more than 200, you will get paid
            ownbank= ownbank + salary
        print("The company made " + str(profit) + " in profit and " + str(expenses) + " in expenses. You made " + str(sales) + " sales. The bank balance is " + str(bank) + ".")
        time.sleep(1)

        if bank<salary:
            day= day + 1
            print('Day: ' + str(day))
            print("The company couldn't afford to pay you!")
            print("Your bank balance is " + str(ownbank) + ".")
            
            break
        time.sleep(1)
        if bank>salary:
            day= day + 1
            print('Day: ' + str(day))
            print("You've been paid " + str(salary) + ".")
            print("Safe for another day!")
            print("Your bank balance is " + str(ownbank) + ".")
        time.sleep(1)
def count():
    a=0
    while a!=100:
        a=a+1
        print(a)
        time.sleep(0.25)
def danger():
    b = 1
    while b >0 :
        print(b)
        b = b+1
def whiletrue():
    while True:
        print('Hello')
        time.sleep(1)



#start of program       
__name__ = input('Name of the program: ')
if __name__ == 'sim':
    small_game()
elif __name__ == 'count':
    count()
elif __name__ == 'danger':
    danger()
elif __name__ == 'whiletrue':
    whiletrue()
    
else:
    print('Nothing')


