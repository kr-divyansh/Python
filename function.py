#functions---block of code that can be called from other parts of the program
#paramters---input to the function
#arguments---values passed to the function
#def is_even(num):
   # """
# Function to check if a number is even.
  #  input --any valid integer
   ###     raise ValueError("Input must be an integer")
 #   if num%2==0:
  #      return True
  #  else:
       # return False
# to call a function
#function_name(arguments)

#for i in range(1,11):
   # x= is_even(i)
   # print(f"{i} is even: {x}")

#types of argument 

#1 default argument 

#def power(base=1, exponent=1):
  #  return base ** exponent 

#power()#---no argument is given from the user but the function will still work because of the default values of the base and exponent parameters


#2 positional argument---pyhton will assign the values to the parameters based on their position in the function call


#3 keyword argument---power(base=2, exponent=3)---here the values are assigned to the parameters based on their names

# *args and **kwargs----are special python keywords that are used to pass the variable length of arguments to a function

#*args---used to pass a variable number of non-keyword arguments to a function

#def multiply(*args):
 #   product = 1
   # for num in args:
       # product *= num
  #  return product

#multiply(2, 3, 4,5,6,7,8) 


#**kwargs---used to pass a variable number of keyword arguments to a function
#keyword arguments are passed as a dictionary to the function
##def print_info(**kwargs):
    #for key, value in kwargs.items():
      #  print(f"{key}: {value}")

#print_info(name="Alice", age=30, city="New York")


#how functions are  executed in python--->
#whenever python sees a def it will create a function object and assign it to the function name. The function is not executed until it is called. When the function is called, the code inside the function is executed and the return value is returned to the caller.functin lifespan is upto only when the function is called. Once the function is executed, the function object is destroyed and the memory is freed up. If the function is called again, a new function object is created and assigned to the function name. This process continues until the program ends or the function is no longer needed.


#without return statement----->  the function will return None by default. The return statement is used to exit a function and return a value to the caller. If a function does not have a return statement, it will return None by default. The return statement can also be used to exit a function early, before the end of the function is reached. When a return statement is executed, the function terminates and control is returned to the caller.


#VARIABLE SCOPE IN PYTHON
#def g(y):
     #print(x)
     #print(x+1)
     #x = 5
    # g(x)
    # print(x)

#nested function---> function within function
#def f():
   #def g():
      #print("i am function g")
     # g()
#print("inside function f")
#f()
#firstly the function g value will be printed after that function f will be called and the value of function f will be printed
#if we called the nested function first there will be an error because the function g is not defined yet. The function g is defined inside the function f and can only be called after the function f is called. The function g is not accessible outside the function f. The function g is a local function and can only be accessed within the function f. The function f is a global function and can be accessed from anywhere in the program.


#functions are first class citizens in python--> functions here act as a dataype which means we can perform every operation on function that we can perform on other datatypes

#type and id
#def square(x):
    #return x**2
#type(square) #<class 'function'>
#id(square) #<unique id of the function object>

#reassign
#x = square
#x(5) #25
 

#benefit of using a function
#1--code reusability
#2--code readability
#3--code maintainability
#4--modularity



#lambda function
#a = lambda x :x**2
#a(5) #25

#b = lambda x,y : x+y
#b(2,3) #5

#difference between normal function and lambda function
#lambda function have no name 
#lambda has no return statement
#lambda is return in one line
#not reusable

#lambda functions are use with higher order functions like map, filter and reduce



#higher order functions are functions that take other functions as arguments or return a function as a result. In python, functions are first class citizens which means we can pass functions as arguments to other functions and return functions from other functions. Higher order functions are used to abstract away common patterns of computation and make code more readable and maintainable.

#def square(x):
#    return x**2

#   return [func(x) for x in data]

# Example usage:
##result = transform(square, data)
#print(result)  # Output: [1, 4, 9, 16, 25]


#map
#map(lambda x:x**2, [1,2,3,4,5]) #<map object at 0x7f8c8c8c8c8c>
#list(map(lambda x:x**2, [1,2,3,4,5]))---> will give a list of the squared values of the input list [1, 4, 9, 16, 25]

#filter --> filter is a higher order function that takes a function and an iterable as arguments and returns an iterator that contains only the elements of the iterable for which the function returns True. The function passed to filter should take a single argument and return a boolean value.
#reduce --> reduce is a higher order function that takes a function and an iterable as arguments and returns a single value that is the result of applying the function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value. The function passed to reduce should take two arguments and return a single value. The reduce function is not built-in in python 3, but it can be imported from the functools module.