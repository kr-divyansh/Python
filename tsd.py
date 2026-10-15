#tuple ()-----> it is similar to list ,,we cannot change element in a tuple once they are assigned
#characteristic
#1.ordered
#2.unchangeable
#3.allows duplicate


#creating tuple
# t1 = ()
# print(t1)----> empty tuple
# t2 =(2)
# print(type(t2))-----> we face difficulty in making a single element tuple
# t2 =(2,)--->now it is a tuple

#hetro tuple
# t = (1,2,True,[1,2,3])
#homo tuple
# t = (1,2,3,4,5)

#tuple within a tuple
# t = (1,2,4,(5,3))

#using type conversion
 
# t6 = tuple("divyansh")
#print(t6)


#indexing and slicing

#t3 = (1,2,3,5,4)
#print(t3[0])
#print(t3[2])
#print(t3[3])

#print(t3[0:4])___> slicing


#editing tuple----tuples are immutable
# t3 = (1,2,3,4,5)
# t3[0] = 10  # This will raise an error because tuples are immutable

# we also can not add or remove elements from a tuple once it is created
# we can delete the entire tuple using the del keyword but not a single element 


#operations on tuple
# t1 = (1,2,3,4)
# t2 = (5,6,7,8)
# print(t1 + t2)  Concatenation
# print(t1 * 3)  Repetition


#membership operator
# t1 = (1,2,3,4)
# print(2 in t1)  # True
# print(5 in t1)  # False


#function in tuple
# t1 = (1,2,3,4,5)
# print(len(t1))  # Length
# print(max(t1))  # Maximum
# print(min(t1))  # Minimum
#print(sum(t1))  # Sum
#print(sorted(t1))  # Sorted list of elements


#count and index
# t1 = (1,2,3,4,5,2,3)
# print(t1.count(2))  # Count of 2 in the tuple
# print(t1.index(2))  # Index of first occurrence of 2 in the tuple

#tuples are faster than lists because they are immutable and have a smaller memory footprint

#why use tuple instead of list

#1 special syntax for creating tuples
# tuple unpacking
# a,b,c = (1,2,3)
#print(a)  # 1
#print(b)  # 2


#swaping values using tuple unpacking
# a= 1
# b= 2
# a,b = b,a
#print(a,b)  # 2, 1

#a,b,*others =(1,2,3,4)
#print(a,b)
#print(others)  # [3, 4]

#zipping tuples
#a=(1,2,3)
#b=('a','b','c')
#zipped = zip(a,b)



#sets{}--->it is an unoredered collection of items.Every set element is unique (no duplicates) and must be immutable (which cannot be changed). However, a set itself is mutable. We can add or remove items from it. Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
#characteristics of set
# unordered
# mutable
# no duplicates
# cant contain mutable data types like list, dict, set

#creating set
#empty set
# s ={}
#print(type(s))  # <class 'dict'> because {} creates a dictionary, not a set
# s = set()  # correct way to create an empty set

#1d and 2D
#s1 ={23,46,2,232,2,3,4,5}
#2D set is not possible because sets are unordered and cannot contain mutable elements like lists or other sets.

#homo set
#s1 = {1,2,3,4,5}
#hetro set
#s2 = {1,2,3,4,5,"divyansh",True}

#using type conversion
# s3 = set("divyansh")
#print(s3)  # {'d', 'i', 'v', 'y', 'a', 'n', 's', 'h'}

#accessing set elements

# acccessing set elements is not possible using indexing or slicing because sets are unordered collections. However, you can iterate through the set using a loop.

#adding and removing elements from a set
#s1 = {1,2,3,4,5}
#s1.add(6)  # Adding an element
#s1.remove(3)  # Removing an element
#udpdating a set
#s1.update([7,8,9])  # Adding multiple elements


#deleting in set
#s1.clear()  # Removes all elements from the set
#del s1  # Deletes the entire set
#s1.discard(4)  # Removes an element if it exists, does nothing if it doesn't
#s1.pop()  # Removes and returns an arbitrary element from the set




















#dictionary
d={1:"kriti",2:459,3:"lovable",10:2000}
d[10]=300 #updating 
d.update({50:210}) # adding new key value pair
del d[2]
print(d[3])
print(d)
k={1:"kriti",2:459,3:"lovable",10:2000}
for i in k:
    print(k[i])


