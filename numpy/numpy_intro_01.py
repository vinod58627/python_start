import numpy as np
#python -m pip install numpy to install the numpy library
# python -m pip show numpy
# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy stands for Numerical Python.
# The array object in NumPy is called ndarray,
# An ndarray is a multidimensional array with a fixed size, and all elements must be of the same type.

# Why Use NumPy?
# =========================
# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

print(np.__version__)

# Why numpy Fast?
# =========================
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.
# NumPy is fast because it uses optimized C code under the hood, and it allows for vectorized operations that avoid the overhead of Python loops.


# Array types in NumPy:
# =========================
# NumPy supports different types of arrays such as 0-D, 1-D, 2-D, and n-D arrays.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) # 0
print(b.ndim) # 1
print(c.ndim) # 2
print(d.ndim) # 3

print("0 d", a) #0 d 42
print("1 d", b) #1 d [1 2 3 4 5]
print("2 d", c) #2 d
# [[1 2 3]
# [4 5 6]]
print("3 d", d) #3 d 
# [[[1 2 3]
#   [4 5 6]],
#  [[1 2 3]
#   [4 5 6]]]


#How to create numpy arrays
# ================================

import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)#[1 2 3 4 5]
print(type(arr)) #<class 'numpy.ndarray'>

arr1 = np.array([0,2,3,4,5])
print(arr1)#[0 2 3 4 5]
print(type(arr1)) #<class 'numpy.ndarray'>


# Use a tuple to create a NumPy array
# =============================================

arr_tpl = np.array((5,6,7,8,9,10))
print(arr_tpl)#[5 6 7 8 9 10]
print(type(arr_tpl)) #<class 'numpy.ndarray'>


# # Creating a 1-dimensional numpy array
# arr1 = np.array([1, 2, 3, 4, 5])
# print("1D array:", arr1)

# # Creating a 2-dimensional numpy array
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print("2D array:\n", arr2)

# arr3 = np.ndarray((2, 3))


# How to create arrays with list and type:
# =================================================

lsarray = np.array([1,2,3,4,5,6,7,8,9,0])
tparray = np.array((1,2,3,4,5,6,7,8,9,0))
print(lsarray) # [1 2 3 4 5 6 7 8 9 0]
print(type(lsarray)) # <class 'numpy.ndarray'>
print(tparray) # [1 2 3 4 5 6 7 8 9 0]
print(type(tparray)) # <class 'numpy.ndarray'>

# Dimensional Array
# =========================

zerodarr = np.array(10)
print(zerodarr)#10
print(type(zerodarr)) #<class 'numpy.ndarray'>
print(zerodarr.ndim)

#1- Dimensional Array
# ========================

oneDArrayList = np.array([1,2,3,4,5,6,7,8,9])
print(oneDArrayList) #[1 2 3 4 5 6 7 8 9]
print(type(oneDArrayList)) #<class 'numpy.ndarray'>
print(oneDArrayList.ndim) # 1

oneDArrayTuple = np.array((1,2,3,4,5,6,7,8,9))
print(oneDArrayTuple) #[1 2 3 4 5 6 7 8 9]
print(type(oneDArrayTuple)) #<class 'numpy.ndarray'>

# Slicing
# =====================================

print("5th index",oneDArrayTuple[5])#5th index 6
print("From 5th index to next all", oneDArrayTuple[5:])#5th index 6
print("upto 4th index 5th index exclude", oneDArrayTuple[:5])#upto 4th index 5th index exclude [1 2 3 4 5]
print("from 0 to 6th index",oneDArrayTuple[0:6] )#from 0 to 6th index [1 2 3 4 5 6]
print("from 0 to 6th index with step 2",oneDArrayTuple[0:6:2] ) #from 0 to 6th index with step 2 [1 3 5]
print("Print reverse", oneDArrayTuple[::-1])#Print reverse [9 8 7 6 5 4 3 2 1]

#2- Dimensional Array:
# ========================

# In every 2-dimensional array, the elements are arranged in rows and columns.
# In every 2 or 3 or more array the rows length should be the same.
# ex: twoDarray = np.array([[1,2,3], [4,5,6], [7,8,9]]) // accepted 
# what if twoDarray = np.array([[1,2,3], [4,5,6], [7,8,9, 0]]) 
#  You will get ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (3,) + inhomogeneous part.

#you will get an error or a warning depending on the version of NumPy.

twoDArrayList = np.array([[1,2,3],[4,5,6]])
print(twoDArrayList) 
print(type(twoDArrayList)) #<class 'numpy.ndarray'>

twoDArrayTuple = np.array(((1,2,3),(4,5,6)))
print(twoDArrayTuple) 
print(type(twoDArrayTuple)) #<class 'numpy.ndarray'>

twoDarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12], [77,88,99,100] ])
print("2-D array", twoDarr)
#2-D array 
# [[  1   2   3   4]
#  [  5   6   7   8]
#  [  9  10  11  12]
#  [ 77  88  99 100]]
print("2-D array Type", type(twoDarr)) #2-D array Type <class 'numpy.ndarray'>

# How to get Rows: 

print("get first row", twoDarr[0]) # get first row [1 2 3 4]
print("get second row", twoDarr[1]) # get second row [5 6 7 8]
print("get third row", twoDarr[2]) # get third row [9 10 11 12]
print("get fourth row", twoDarr[3]) # get fourth row [77 88 99 100]

# how to get Rows
# ============================================================

twoDarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12], [77,88,99,100] ])
print("2-D array", twoDarr)
print("Print first row", twoDarr[0]) #Print first row [1 2 3 4]
print("Print 2nd row", twoDarr[1]) #Print 2nd row [5 6 7 8]
print("Print 3rb row", twoDarr[2]) #Print 3rb row [ 9 10 11 12]
print("Print 4th row", twoDarr[3]) #Print 4th row [ 77  88  99 100]

# How to get Columns:
# ====================================
twoDarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12], [77,88,99,100] ])


#How to get values
print("get value 6 value 1 row 2 value",twoDarr[1][1] ) # get value 6 value 1 row 2 value 6
print("get value 12 value 4 row 3 value",twoDarr[2][3] ) # get value 12 value 4 row 3 value 12



#3- Dimensional Array:
# ======================================


twoDarray = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(twoDarray)
print(type(twoDarray))
