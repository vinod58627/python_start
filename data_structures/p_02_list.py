# List declare with []
# List is one of data structure
# List is mutable
# list accepts index and slicingepts duplicate values

x = [10,20,30,40,50,60]
print(x)
print(type(x))

# List is mutable means we can change the values
print(x[2]) #30

x[2] = 25
print(x) #<class 'list'>
print(x[2]) #25

# list accepts duplicate values
x = [10,20,30,40,50,60,30,30,-23]
print("Achek duplicate values", x) # Achek duplicate values [10, 20, 30, 40, 50, 60, 30, 30, -23]

#List methods
#=======================
#=========================

#1. Append: to add values in end of list
#-----------------------------------------
# add value at the end of list

x.append(25)
x.append(30)
x.append(-23)
print("After Append", x) # After Append [10, 20, 30, 40, 50, 60, 25, 30, -23]


y = [10, 20, 30, 40, 50, 60, 10,20]

y.append(25)

print(y) #[10, 20, 30, 40, 50, 60, 10, 20, 25]

#Replace the value

y[2] = 22

print(y) #[10, 20, 22, 40, 50, 60, 10, 20, 25] Replacing the value

#2. Pop: to remove values from the end of list
#========================================


print(y.pop()) # 25 pop remove the last element in list and return that value

print(y) #[10, 20, 22, 40, 50, 60, 10, 20] pop remove the last element in list

#3. Copy: to create a copy of the list
#========================================

z = y.copy()
print(z) #[10, 20, 22, 40, 50, 60, 10, 20] copy the values form y

z[-2] = 99
print(z)  #[10, 20, 22, 40, 50, 60, 99, 20] the 10 replace with 99 
print(y) # [10, 20, 22, 40, 50, 60, 10, 20] No change in y

#4. Count: to count the occurrences of a value in the list
#=========================================================

print(y) # [10, 20, 22, 40, 50, 60, 10, 20]
print(y.count(10)) # 2
print(y.count(20)) # 2
print(y.count(22)) # 1
print(y.count(100)) # 0

#5. Extend: to add multiple values at the end of the list
#=========================================================
y.extend(z) # [10, 20, 22, 40, 50, 60, 10, 20, 10, 20, 22, 40, 50, 60, 99, 20]

y.extend([100,200,300]) #[10, 20, 22, 40, 50, 60, 10, 20, 10, 20, 22, 40, 50, 60, 99, 20, 100, 200, 300]

print(y)

#6. Index: to find the index of a value in the list
#====================================================
a = [10,20, 30, 44, 50, 66, 70, 25, 10]
print(a.index(10)) # 0, returns the index of the first occurrence of 10
print(a.index(66)) # 5, returns the index of the first occurrence of 66
print(a.index(10, 2)) # 8, returns the index of the first occurrence of 10 starting from index 2
print(a.index(10, 4)) # 8, returns the index of the first occurrence of 10 starting from index 4

# print(a.index(16)) 
#  File "E:\Django_Python\python_start\data_structures\p_02_list.py", line 90, in <module>
#     print(a.index(16))
#           ~~~~~~~^^^^
# ValueError: list.index(x): x not in list

#7. Insert: to insert a value at a specific index in the list
#=========================================================
b = [10, 20, 30, 44, 50, 66, 70, 25, 10]

print(b) # [10, 20, 30, 44, 50, 66, 70, 25, 10]

b.insert(2, 109)
print(b) # [10, 20, 109, 30, 44, 50, 66, 70, 25, 10]
b.insert(92, 1000)
print(b) # [10, 20, 109, 30, 44, 50, 66, 70, 25, 10, 1000]

print(b.__len__())# 11
print(len(b)) # 11

print(type(b)) # <class 'list'>

# print(b[92])

# if i add at 92 position it will add at last position because the index is out of range
# <class 'list'>
# Traceback (most recent call last):
#   File "E:\Django_Python\python_start\data_structures\p_02_list.py", line 112, in <module>
#     print(b[92])
#           ~^^^^
# IndexError: list index out of range

#7. Remove: to remove the first occurrence of a value in the list
#==================================================================
c = [10, 20, 30, 44, 50, 66, 70, 25, 10]
print(c) # [20, 30, 44, 50, 66, 70, 25, 10]

c.remove(10) # removes the first occurrence of 10
print(c) # [20, 30, 44, 50, 66, 70, 25]

c.remove(10) # None, because remove() does not return a value
print(c) # [20, 30, 44, 50, 66, 70, 25]

# print(c.remove(99))
# Traceback (most recent call last):
#   File "E:\Django_Python\python_start\data_structures\p_02_list.py", line 133, in <module>
#     print(c.remove(99))
#           ~~~~~~~~^^^^
# ValueError: list.remove(x): x not in list

#8. Sort: to sort the list in ascending order
#==============================================
# sorts the list in ascending order
# print(c) # [20, 25, 30, 44, 50, 66, 70]

d = [10, 20, 30, 44, 50, 66, 70, 25, 10]
d.sort()
print(d) #[10, 10, 20, 25, 30, 44, 50, 66, 70]

# 9. Reverse: to reverse the order of the list
#==============================================
e = [10, 20, 30, 44, 50, 66, 70, 25, 10]
e.sort()
e.reverse()
print(e) # [70, 66, 50, 44, 30, 25, 20, 10, 10]
e.reverse()
print(e) # [10, 10, 20, 25, 30, 44, 50, 66, 70]

# 9. Clear: 
#==============================================
f = [10, 20, 30, 44, 50, 66, 70, 25, 10]
# f.clear()
# print(f) #[] clear the values  not the list still its a empty list
# print(type(f)) # <class 'list'>
