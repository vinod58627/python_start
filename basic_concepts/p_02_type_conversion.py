#Type conversion mean to change the value form one data type to another data type 
#ex: int to float

a = False
w = 10+2J
v ="Vinod"
x = 20.5
y = True
z ="10"

print(x,y,z,w, a) #20.5 True 10 (10+2j)
print(type(x), type(y), type(z), type(w), type(a)) #<class 'float'> <class 'bool'> <class 'str'> <class 'complex'>  <class 'bool'>

# Convert Into Int : can convert except complex and string having non numeric value
#======================
print(int(x),int(y),int(z), int(a)) #20 1 10 0

# print(int(w)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

# print(int(v)) #ValueError: invalid literal for int()

#Convert to String : Can convert all types
#=======================

print(str(x),str(y),str(z),str(w),str(v), str(a)) #20.5 True 10 (10+2j) Vinod False
print(type(str(x)),type(str(y)),type(str(z)),type(str(w)),type(str(v)), type(str(a))) #<class 'str'> <class 'str'> <class 'str'> <class 'str'> <class 'str'>

#Convert into Float : Can convert except complex and string having non numeric value
#======================================================================================
# w = 10+2J
# v ="Vinod"


print(float(x),float(y),float(z), float(a))  #20.5 1.0 10.0 0.0
# print(float(w)) #float() argument must be a string or a real number, not 'complex'
# print(float(v)) #could not convert string to float: 'Vinod'
print(type(float(x)),type(float(y)),type(float(z)), type(float(a)))  #<class 'float'> <class 'float'> <class 'float'> <class 'float'>

# print(type(float(w)))
# print(type(float(v)))


#Convert into Bool : Can convert All  types but if string is empty then its return false else true
#====================

print(bool(x),bool(y),bool(z), bool(a), bool(w), bool(v)) #True True True False True True

print(type(bool(a)),type(bool(v)),type(bool(w)),type(bool(x)),type(bool(y)),type(bool(z)) ) #<class 'bool'> <class 'bool'> <class 'bool'> <class 'bool'> <class 'bool'> <class 'bool'>


#Convert to Complex:  Can convert except string having non numeric value
#=======================
print(complex(x), complex(y), complex(z), complex(a), complex(w)) #(20.5+0j) (1+0j) (10+0j) 0j (10+2j)
# v ="Vinod"
# print(complex(v)) #ValueError: complex() arg is a malformed string

print(type(complex(a)),type(complex(w)),type(complex(x)),type(complex(y)),type(complex(z)) ) #<class 'complex'> <class 'complex'> <class 'complex'> <class 'complex'> <class 'complex'>

# print(type(complex(v))) 
