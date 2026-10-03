 #python oops
#class is a blueprint for creating objects ,,,object is an instance of a class 
#object name = classname()--> object syntax
import os


class Atm:
    # Constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
Hi, how can I help you?

1. Press 1 to create PIN
2. Press 2 to change PIN
3. Press 3 to check balance
4. Press 4 to exit
5. Press 5 to withdraw money

Enter your choice: 
""")

        if user_input == "1":
            # Create PIN logic
            self.create_pin()

        elif user_input == "2":
            # Change PIN logic
            self.change_pin()

        elif user_input == "3":
            # Check balance logic
            self.check_balance()

        elif user_input == "4":
            # Exit logic
            print("Thank you!")

        elif user_input == "5":
            # Withdraw money logic
            self.withdraw_money()

        else:
            print("Invalid option!")

    def create_pin(self):
        input_pin = input("Enter your PIN: ")
        self.pin = input_pin


        input_balance = input("Enter your initial balance: ")
        self.balance = float(input_balance)
        print("PIN created successfully!")
        self.menu()

    def change_pin(self):
        input_pin = input("Enter your current PIN: ")
        if input_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully!")
            self.menu()
        else:
            print("Incorrect PIN!")
            self.menu()
    
    def check_balance(self):
        input_pin = input("Enter your PIN: ")
        if input_pin == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Incorrect PIN!")
            self.menu()

    def withdraw_money(self):
        input_pin = input("Enter your PIN: ")
        if input_pin == self.pin:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful! Your new balance is:", self.balance)
            else:
                print("ye jo gareeb hoye nn ,apne adat se gareeb hoye")
        else:
            print("Incorrect PIN!")
        self.menu()


# Creating object
obj = Atm()

print(type(obj))

class fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self,other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return fraction(new_num,new_den)
    def __sub__(self,other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return fraction(new_num,new_den)
    def __mul__(self,other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return fraction(new_num,new_den) 
    def __truediv__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return fraction(new_num,new_den)     

class point:
    def __init__(self,x,y):
        self.x_co = x
        self.y_co = y
    def __str__(self):
        return f"({self.x_co},{self.y_co})"
    def euclidian_distance(self,other):
        return ((self.x_co - other.x_co) ** 2 + (self.y_co - other.y_co) ** 2) ** 0.5
    def distance_from_origin(self):
        return (self.x_co ** 2 + self.y_co ** 2) ** 0.5 
class person:
    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input
    def greet(self):
        if self.country== "india":
            print(f"namaste {self.name}")
        else:
            print(f"hello {self.name}")
p = person("divyansh","india")
p.greet()



#object without a refernce 

class person:
   def __init__(self):
     self.name ="divynash"
     self.gender ="male"

person()


#pass by reference
class person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
def greet(person):# this is a function because it is outside the class 
    print(f"hello {person.name} you are {person.gender}")


p = person("divyansh","male")
greet(p)

#class relationships
 #1 .aggregation --(has a relationship)---when one class contains the other class
class customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address  
class address:
    def __init__(self,city,state,pin):
        self.city = city
        self.state = state
        self.pin= pin

add = address("delhi","delhi",110001)
cust = customer("divyansh","male",add)


#inheritance --(is a relationship)---when one class inherits the other class
class User:
    def __init__(self):
        self.name ="divyansh"
    def login(self):
        print("login successful")


#child class
class student(User): 
    def enroll(self):
        print("enroll into the course")
u = User()
s = student()
print(s.name)


#agr child class ke pass khud ka constructor nahe hai tb parent class ka constructor use hoga

class Phone:
    def __init__(self,name,price,camera):
        print("phone constructor called")
        self.name = name
        self.price = price 
        self.camera = camera
    def buy(self):
        print(f"buying {self.name} for {self.price} with camera {self.camera}")
class Smartphone(Phone):
    pass
p = Phone("iphone",1000,"12MP")


#method overriding --when child class has same method as parent class
class Phone:
    def __init__(self,name,price,camera):
        print("phone constructor called")
        self.name = name
        self.price = price 
        self.camera = camera
    def buy(self):
        print(f"buying {self.name} for {self.price} with camera {self.camera}")

class Smartphone(Phone):
    def buy(self):
        print(f"buying {self.name} for {self.price} with camera {self.camera} and extra features")
#super keyword --to call parent class method in child class
class Phone:
    def __init__(self,name,price,camera):
        print("phone constructor called")
        self.name = name
        self.price = price 
        self.camera = camera
    def buy(self):
        print(f"buying {self.name} for {self.price} with camera {self.camera}")

class Smartphone(Phone):
    def buy(self):
        super().buy()  # Calls the parent class's buy method
        print(f"buying {self.name} for {self.price} with camera {self.camera} and extra features")

#super---> constructor
class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price = price
        self.brand=brand
        self.cmaera = camera

class Smartphone(Phone):
    def __init__(self,price,brand,camera,ram):
        
        print("inside smartphone constructor")
        super().__init__(price,brand,camera)
        self.ram = ram
        self.os = os
        print("inside smartphone constructor")
s = Smartphone(1000,"iphone","12MP","4GB")
