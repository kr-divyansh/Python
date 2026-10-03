#list is a data type whee we can store multiple item under 1 name .More technically ,list act like dyanmic array which means we can add more item on the fly
#arry vs list
#1.list act like dynamic array,it can store multiple data type inside it 
#2. list is slow and occupy more space due to its referential array properties
#3.array is fixed in size ,where as list can be updated whenever we want
 

#characteristic of list
#1.list are ordered 
#l =[1,2,3]
#l2 = [3,2,1]
#l2 == l false because order matters in list

#2.list are mutable
#3  hetergenous--can store multiple data type inside it
#4 items can be duplicates
#5 are dynamic in nature
#6 can be nested inside another list
#7 items can be accessed using index and slicing
#8 can contain any kind of object in python



#creating a list

#empty list
#l = []
#print(l)

#1D  and homogeneouslist

#l = [1,2,3,4,5]
#print(l)

#2D
#l2 = [[1,2,3],[4,5,6]]
#print(l2)

#heterogeneous list
#l = [1,2,3,"hello",True,3.4]
#print(l)


#using type conversion'
#print(list("divyansh"))

#accessing list items
#l = [1,2,3,4,5]
#print(l[0]) it is ALSO known as positive indexing ----left to right
#print(l[-1]) it is also known as negative indexing ----- right to left


#l = [1,2,3,[4,5]]
#print(l[3][1]) #accessing nested list



#slicing 
#l = [1,2,3,4,5]
#print(l[0:4]) #it will print 1,2,3,4

#print(l[0::2]) # it will print number in gap of 2


#append---- add element to the last of list 
#l = [1,2,3,4,5]
#l.append(45)
#print(l)

#extend----- add multiple element to the last of list
#l = [1,2,3,4,5]
#l.extend([6,7,8,6])
#print(l)

#insert --when we want to add number to the desired position
#l = [1,2,3,4,5]
#l.insert(1,100)
#print(l)

#editing item in a list
#l = [2,34,545,323]
#l[-1] = 0
#print(l) 

#del----use to delete the entire list but this not happen on the memory level

#l =[1,2,3,4,5]
#print(l)
#del l[1:3]----deletion with slicing
#del l
#print(l)

#remove-----no need to tell the index,remove function directly delete on the value base

#l = [1,23,4,5,6,3,2]
#l.remove(2)
#print(l)


#pop 
#l=[1,23,45,565,44,233]
#l.pop(0)#---it also works on index basis
#l.pop()#--- default or without index value it remove the last element
#print(l)


#clear --do not delete the list but clear all the element from the list
#l=[1,23,4,5,45,3,222,34]
#l.clear()
#print(l)


#operation on list
#1.arithmetic
#2.membership
#3.loop


#arithmetic(+,*)---- + helps in merging of 2 list,,,* repeats the element number of times it was asked to do so
#l1=[1,2,3,4,5]
#l2 =[23,45,12,56,78]
#print(l1+l2)
#print(l1*3)
#print(l2*2)

#membership----check the availaibilty of element
#l1 =[1,2,3,4,5]
#l2 =[1,2,3,4,[5,6]]
#print(5 in l1)
#print([5,6] in l2)

#loops in list
#l1=[1,2,3,4,5,6]
#l2=[23,45,[2,4]]
#for i in l2:
    #print(i)
#for i in l1:
    #print(i)


#more list functions

#len/min/max/sorted

#l =[2,1,5,7,0]
#print(len(l))
#print(min(l))
#print(max(l))
#print(sorted(l))


#count----return the count of any element in a list
#l=[1,2,1,3,4,1,5]
#l.count(1)

#index--tell the index of any particular element
#l =[1,2,4,5,6,6,7]
#print(l.index(5))

#reverse---it permanently reverse the list
#l =[2,34,77,1,54,23]
#l.reverse()
#print(l)

#list comprehension


#add 1 to 10 numbers to a list

#l=[]
#for i in range(1,11):
   # l.append(i)
#print(l)

#l=[i for i in range(1,11) ]
#print(l)

#scalar multiplication on a vector
#v = [2,3,4]
#s = -3

#[s*i for i in v]
#print(v)


#add squares

#l=[1,2,3,4,5,6]
#l=[i**2 for i in l]
#print(l)

#print all the number divisble by 5
#l=[i for i in range(1,51) if i%5 == 0]
#print(l)

#find languages which start with letter p

#languages =['java','python','php','c','javascript']
#language=[language for language in languages if language.startswith('p')]


#print a (3x3) matrix using list comprehension --> nested list comprehension

#[[i*j for i in range(1,4)] for j in range(1,4)]


#cartesian product --->list comprehension on 2 lists together

#l1 = [1,2,4,45]
#l2 =[3,2,56,32]
#l3=[i*j for i in l1 for j in l2]
#print(l3)

#ways to traverse a list
#1 itemwise
l=[34,2,3,12,4,5]

for i in l:
    print(i)

#2 indexwise

for i in range(0,len(l)):
    print(i)




