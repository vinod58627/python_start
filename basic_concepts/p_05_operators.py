#Operators
#===================

# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Bitwise Operators
# Special Operators

# Operator	Operation	    Example
#   +	    Addition	    5 + 2 = 7
#   -	    Subtraction	    4 - 2 = 2
#   *	    Multiplication	2 * 3 = 6
#   /     	Division	    4 / 2 = 2
#   //	    Floor Division	10 // 3 = 3
#   %	    Modulo	        5 % 2 = 1
#   **	    Power	        4 ** 2 = 16 

# 1: Arithmetic Operators in Python
#====================================

a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   
print(2**32) #4294967296

# Sum: 9
# Subtraction: 5
# Multiplication: 14
# Division: 3.5
# Floor Division: 3
# Modulo: 1
# Power: 49
# 4294967296

# 2. Python Assignment Operators
#================================

# Operator	Name	                    Example
#   =	    Assignment Operator	        a = 7
#   +=	    Addition Assignment	        a += 1 # a = a + 1
#   -=	    Subtraction Assignment	    a -= 3 # a = a - 3
#   *=	    Multiplication Assignment	a *= 4 # a = a * 4
#   /=	    Division Assignment	        a /= 3 # a = a / 3
#   %=	    Remainder Assignment	    a %= 10 # a = a % 10
#   **=	    Exponent Assignment	        a **= 10 # a = a ** 10

# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

# Output: 15

# 3. Python Comparison Operators
#====================================

# Operator	Meaning	                Example
#   ==	    Is Equal To	                3 == 5 gives us False
#   !=	    Not Equal To	            3 != 5 gives us True
#   >	    Greater Than	            3 > 5 gives us False
#   <	    Less Than	                3 < 5 gives us True
#   >=	    Greater Than or Equal To	3 >= 5 give us False
#   <=	    Less Than or Equal To	    3 <= 5 gives us True

a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

# a == b = False
# a != b = True
# a > b = True
# a < b = False
# a >= b = True
# a <= b = False


# 4. Python Logical Operators
#===================================

# Operator	    Example	    Meaning
#   and	        a and b	    Logical AND:True only if both the operands are True
#   or	        a or b	    Logical OR:True if at least one of the operands is True
#   not	        not a	    Logical NOT:True if the operand is False and vice-versa.

x = True
y = False

print(x and y) #False
print(x or y)  #True
print(x and x) #True
print(y and y) #False
print(not x)   #False
print(not y)   #True

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

# 5. Python Bitwise operators
# ===========================

# Operator	Meaning	            Example
#   &	    Bitwise AND	        x & y = 0 (0000 0000)
#   |	    Bitwise OR	        x | y = 14 (0000 1110)
#   ~	    Bitwise NOT	        ~x = -11 (1111 0101)
#   ^	    Bitwise XOR	        x ^ y = 14 (0000 1110)
#   >>	    Bitwise right shift	x >> 2 = 2 (0000 0010)
#   <<	    Bitwise left shift	x 0010 1000)

x = True
y = False
print(x & y) #False
print(x | y) #True

# 6. Python Special operators
# ============================

# a. Identity operators
# ------------------------
# Operator	    Meaning	Example
#   is	        True if the operands are identical (refer to the same object)	x is True
#   is not	    True if the operands are not identical (do not refer to the same object)	x is not True


x1 =5
x2 =5

y1 = "vinod"
y2 = "vinod"

z1 = [1,2,3]
z2 = [1,2,3]

print("Check1", x1 is x2)
print("Check1 Not", x1 is not x2)
print("Check2", y1 is y2)
print("Check2 Not", y1 is not y2)
print("check3", z1 is z2)
print("check3 Not", z1 is not z2)
# Check1 True
# Check1 Not False
# Check2 True
# Check2 Not False
# check3 False
# check3 Not True

# But z1 and z2 are lists. They are equal but not identical. It is because the interpreter locates them separately in memory, although they are equal.

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False

# b. Membership operators
# ----------------------------

# In Python, in and not in are the membership operators. 
# They are used to test whether a value or variable is found in a sequence 
# (string, list, tuple, set and dictionary).

# In a dictionary, we can only test for the presence of a key, not the value.

# Operator	Meaning	Example
# in	True if value/variable is found in the sequence	5 in x
# not in	True if value/variable is not found in the sequence	5 not in x

message = 'Hello world'
dict1 = {1:'a', 2:'b'}
arr = [2,5,9,6, True]

#String

print("o :", "o" in message)
print("H:",  "H" in message)
print("Z:", "Z" in message)
# o : True
# H: True
# Z: False

#Object
print ("Dict", 1 in dict1)
print ("Dict", 2 in dict1)
print ("Dict", "A" in dict1)
print ("Dict", "A" not in dict1)

# Dict True
# Dict True
# Dict False
# Dict True

#Array
print("Arr", 2 in arr)
print("Arr", 5 in arr)
print("Arr", 9 in arr)
print("Arr", 6 in arr)
print("Arr", 8 in arr)
print("Arr", 26 in arr)
print("Arr", 26 not in arr)
print("Arr", "A" not in arr)
print("Arr", True in arr)
print("Arr", True not in arr)

# Arr True
# Arr True
# Arr True
# Arr True
# Arr False
# Arr False
# Arr True
# Arr True
# Arr True
# Arr False

message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False