#Tuple 
# =====================================

# Tuple is one of the data structures in Python
# Tuple is immutable
# Tuple accepts index and slicing
# Tuple can contain duplicate values
# Tuple is faster than list
# It is used when you want to store a collection of items that should not be changed

# How to create a tuple:
# ========================

# tuple has 2 methods only 
# 1. index 
# 2. count
    
#With No value:
# --------------------

x = ()
print(x) #()
print(type(x)) #<class 'tuple'>

#With single value
# ---------------------
y =("vinod") # if we try to create like this single value should be just a value if you want to make this tuple then you have a=to add comma
print(y)#vinod
print(type(y)) #<class 'str'>

z = ("vinod",) 
print(z) #('vinod',)
print(type(z)) #<class 'tuple'>

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1)) #<class 'tuple'>

x = (10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10)
print(x)
print(type(x)) #<class 'tuple'>

#Update values: its not updatable . 
# still if you wan to update first you can convert tuple into list then update then convert in to tuple
# ===================================
# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# ex:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# x[2] = 66
# print(x)
# <class 'tuple'>
# Traceback (most recent call last):
#   File "E:\Django_Python\python_start\data_structures\ds_03_tuple.py", line 15, in <module>
#     x[2] = 66
#     ~^^^
# TypeError: 'tuple' object does not support item assignment

#How to access:
# ==========================


x = (10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10)

print(x[0]) #10
print(x[-3]) #90
print(x[5])#50
print(x[-2])#100

# Check if Item Exists
# ========================

print(50 in x) #True
print(100 in x) #True
print(200 in x) #False
if 50 in x: #True
    print(True)
else:
    print(False)
    
if 66 in x: #False
    print(True)
else:
    print(False)
    
    
# 1. Index: t.index(value, start, end)
#    - value: The value to search for.
#    - start (optional): The starting index to search from.
#    - end (optional): The ending index to search to.
# ========================

x = (10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10, 10)

print(x.index(20)) #1
print(x.index(100)) #10
print(x.index(50)) #5
# print(x.index(99)) # ValueError: tuple.index(x): x not in tuple
print(x.index(10, 1)) #11
print(x.index(10, 11)) #11
print(x.index(10, 12)) #12

# Your tuple is:

# x = (10, 20, 30, 40, 96, 50, 60, 70, 80, 90, 100, 10, 10)

# Indexes are:

# Index:   0   1   2   3   4   5   6   7   8   9   10  11  12
# Value:  10  20  30  40  96  50  60  70  80  90  100 10  10

#2. Count
# =========================
print(x.count(10))#2
print(x.count(90))#1
print(x.count(101))#0 if not presentit wont throw any error it will gives 0


#Slicing
# =========================

x = (10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10)
print(x.index(10)) #0
print(x.index(50)) #5
print(x.index(100)) #10

print(x.index(10, 1)) #11z

# If you want any methods from list you can convert tuple into list then use that method then convert it back into tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)



# unpacking:
# =========================

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)#apple
print(yellow)#banana
print(red)#cherry

# Using Asterisk*
# =========================

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(app, man, pap, pin, cher) = fruits #Here we have to add eval number of item to the tuple length
print(app) #apple
print(man) #mango
print(pap) # papaya

# but if you want to pericularly some values then we can use * for unwanted
(app, man, *paa) = fruits
print(app) #apple
print(man) # mango

print(paa) #[papaya, pineapple, cherry]
print(*paa) #papaya pineapple cherry

(*app, man, paa) = fruits
print(app) #['apple', 'mango', 'papaya']
print(man) # pineapple
print(paa) #cherry

(app, *man, paa) = fruits
print(app) #apple
print(man) #['mango', 'papaya', 'pineapple']
print(paa) #cherry


# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


#Slicing
# =========================
x = (10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10)

print(x[:]) #(10, 20, 30, 40, 96, 50, 60, 70, 80, 90, 100, 10)
print(x[::]) # (10, 20, 30, 40, 96, 50, 60, 70, 80, 90, 100, 10)
print(x[::-1]) # (10, 100, 90, 80, 70, 60, 50, 96, 40, 30, 20, 10)


print(x[2:])#(30, 40, 96, 50, 60, 70, 80, 90, 100, 10)
print(x[:5]) #(10, 20, 30, 40, 96)
print(x[1:10:2]) #(20, 40, 50, 70, 90)

print(x[2::2])#(30, 96, 60, 80, 100)
print(x[::3])#(10, 40, 60, 90)

print(x[2:])#(30, 40, 96, 50, 60, 70, 80, 90, 100, 10)
print(x[:5]) #(10, 20, 30, 40, 96)
print(x[1:10:2]) #(20, 40, 50, 70, 90)

print(x[2::2])#(30, 96, 60, 80, 100)

print(x[-10: -1: 3]) #(30, 50, 80)

