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

#1. Append: to add values in end of list
x.append(25)
x.append(30)
x.append(-23)
print("After Append", x) # After Append [10, 20, 30, 40, 50, 60, 25, 30, -23]