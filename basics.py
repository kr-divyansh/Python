print("Hello, World!")

#variables and data types
a= 10
b= 20.45
print(type(b))
print(type(a))

#strings
str="this is a string  245959606095985  $%^^^^$#%$"
print(type(str))
#UNICODE AND CONVERSION
a ="A" 
print(ord(a))
a =65
print(chr(a))
a= "divyansh code"
print(a[0])
print(a[1])
#string slicing
print(a[0:8:1])


#type conversion
a=12349
print(type(a))# yaha pei a is an integer
#a= str(a)
print(type(a))# yaha pei a is a string


#input and output 
age= 12
name= "sonu"
print(name,age)

print("my name is",name,"and my age is",age)
#formatting
print(f"my name is {name} and my age is {age}")

#input#

#operators
a = 12
b = 6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#assignment operators

a = 123
print(a)
#compound assignment operators
a= 24
a+= 24
a+=56
print(a)
#comparison operators
a = 10
b = 20 
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a != b)
print(a == b)
#logical operators
  #&&  if both the conditons are true
  #OR if any of the conditon is true
  #not reverse the result


  #conditional statements 
a =25 
if a>15:
    print("i will do the work")
else:
    print("i will not do the work")
    
money =int(input("enter the money you have"))
if money>500:
    print("i will eat pizza ")
elif money ==400:
    print("i will eat ice cream")
else:
    print("i will not eat pizza")
    a= 233
    sher ="rakhi is chillar"
    print(sher)


#loops 
a= range(1,15,1)
for i in a :
    print(i)

    # 20 to 50
    for i in range(20,51,1):
        print(i)


    # -3 to -15
    for i in range(-3,-16,-1):
        print(i)


    # 16 to 1
    for i in range(16,0,-1):
        print(i)
   # print table of 7
for i in range (7,71,7):
     print(i)


     #loops for string
     name ="sheryians is the best python teachers"
     print(len(name)) #idexing 1 se shuru hoti hai
     for i in range(len(name)):
         print(name[i])
# iterating directly over a string
b = "sheryians is the best python teachers"
for i in b:
    print(i)


    #print natural number upto n
    n = int(input("pls enter ur number: "))
    for i in range(1,n+1):
        print(i)
    # reverse n to 1
    n = int(input("pls enter ur number: "))
    for i in range(n,0,-1):
        print(i)
   # take a number and print its table
    n = int(input("pls enter ur number:"))
    for i in range(n,n*11,n):
         print(i)

   #sum upto n
    n = int(input("pls enter ur number: "))
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(sum)
    # factorial of a number
    n = int(input("pls enter ur number: "))
    fact = 1    
    for i in range(1,n+1):
        fact *= i
    print(fact)


    #while loop
    a= 1
    while a<=30:
        print(a)
        a= a+1
    