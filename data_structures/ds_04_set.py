#Set: {}, union , intesection, difference, 
# =================
#Set is unorderes so we get based on index
#Unchangeable elements can be added to the set
#Duplicate values will be removed automatically
#Sets are mutable, meaning we can add or remove elements after creation
#However, the elements themselves must be immutable (e.g., numbers, strings, tuples)

s = {10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10}
print(s)#{96, 100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
print(type(s))#<class 'set'>

# print(s[1]) #TypeError: 'set' object is not subscriptable
# print(s[:]) #TypeError: 'set' object is not subscriptable

# or

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
print(type(thisset))#<class 'set'>

# How to check existance:
# =====================================
s = {10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10} 
if 40 in s:# True
  print(True)
else:
  print(False)

if 39 in s: #False
  print(True)
else:
  print(False)
  
#Methods:
# ===================

# 1. add() :will add in random
# =====================

s = {10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10} 
s.add("vinod")
print(s) #{96, 100, 70, 'vinod', 40, 10, 80, 50, 20, 90, 60, 30}

s.add("kumar")
s.add("v1")
s.add("v2")
s.add("v3")
print(s) #{96, 'v1', 100, 70, 40, 'vinod', 10, 'kumar', 'v2', 80, 50, 20, 'v3', 90, 60, 30}

# 2. remove() :will remove the specified element
# ================================================

s = {10, 20, 30, 40, 96,50, 60, 70, 80, 90, 100, 10} 
print(s) #{96, 100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
print(type(s))#<class 'set'>
s.remove(40)
print(s) #{96, 100, 70, 10, 80, 50, 20, 90, 60, 30}

s = {10, 20, 30, "vinod", "kumar"} 
s.remove("kumar")
print(s) #{10, 20, 30, 'vinod'}
s.remove(20)
print(s) #{10, 30, 'vinod'}

#Set Methods:
# ====================================

a = {10, 20, 30, 40, 50, 60}
b = {50, 60, 70, 80, 90, 100, 110}
c = { 100, 110, 120, 130, 10, 20}

# 1. union() : will return a set containing all items from both sets, duplicates removed
# =====================================================
print(a.union(b))# {100, 70, 40, 10, 110, 80, 50, 20, 90, 60, 30}
print(a.union(b, c))#{130, 100, 70, 40, 10, 110, 80, 50, 20, 120, 90, 60, 30}
a = {10, 20, 30, 40, 50, 60}
b = {50, 60, 70, 80, 90, 100, 110}
c = { 100, 110, 120, 130, 10, 20}

print(a.union(b))#{100, 70, 40, 10, 110, 80, 50, 20, 90, 60, 30}
print(a.union(c)) #{130, 100, 40, 10, 110, 50, 20, 120, 60, 30}
print(a.union(b, c)) #{130, 100, 70, 40, 10, 110, 80, 50, 20, 120, 90, 60, 30}
print(b.union(c)) #{130, 100, 70, 10, 110, 80, 50, 20, 120, 90, 60}

# 2. intersection() : will return a set containing only items that are present in both sets
# =====================================================

print(a.intersection(b))#{50, 60}
print(a.intersection(c)) #{10, 20}
# print(a.intersection(b,c)) #Wont work set()
print(b.intersection(c)) #{100, 110}

# 3. difference() : will return a set containing items that are present in the first set but not in the second set
# =====================================================

print(a.difference(b)) #{40, 10, 20, 30} in a and not in b
print(a.difference(c)) #{40, 50, 60, 30}
print(b.difference(c)) #{70, 80, 50, 90, 60}

# 4. issubset() and issuperset() : will check subset and superset relationships
# =====================================================
d = {100}

print(d.issubset(a)) #False
print(d.issubset(b)) #True
print(d.issubset(c)) #True

#5. isSuperset() : will check subset and superset relationships
# =====================================================

print(a.issuperset(d)) #False
print(b.issuperset(d)) #True
print(c.issuperset(d)) #True

# 6. isdisjoint() : will check if two sets have no elements in common
# =====================================================

print(a.isdisjoint(b)) #False
print(a.isdisjoint(c)) #False
print(b.isdisjoint(c)) #False
print(a.isdisjoint(d)) #True
print(b.isdisjoint(d)) #False
print(c.isdisjoint(d)) #False