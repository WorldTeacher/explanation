#declare variables
name = "John"
age = 23
age2= "23"
dob= "10/12/1992"
pob= "London"
surname= "Smith"
list= [name, age, dob, pob, surname] #list of variables, useful for when you want to iterate over a list
def main():
    print(list)

    print(name + " " + surname + " is " + age + " years old." " He was born in " + dob + " and lives in " + pob + ".")

