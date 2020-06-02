import numpy as np

# Array Function : Create Array from list or tuples.
# array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

# array = np.array([1, 2, 8, 4])  # Create array from single list
# arrayTow = np.array([[1, 2,5], [4, 5, 7], [4, 9, 10]], dtype=int)  # Create array from nested list
# print(array)

# -------------------------------------------------------
# Arange function : Create array from evenly spaced values
# It is takes four arguments (start, stop, steps, data type) or tow arguments  (stop, data type)

array = np.arange(1, 20, 5)
arrayTow = np.arange(1, 20, 5, dtype=complex)
print(array)
print(arrayTow)

# ----------------------------------------------------------

# Zeros function : Create array filled with zeros
# zeros(shape, dataType= float, order) shape can be int or tuples to specific shape of array

# zerosArray = np.zeros(2)
# zerosArrayTow = np.zeros(5, dtype=int)
# arrayThree = np.zeros((3, 2), dtype=float, order="C")
#
# print(array)
# print(arrayTow)
# print(arrayThree)

# ---------------------------------------------------------------

# Ones Function : Create array filled with ones
# ones(shape, dtype=None, order='C')

# onesArray = np.ones(5)
# oneArrayTow = np.ones((3, 5), dtype=int)  # Create 5 dimensional
# print(array)
# print(arrayTow)

# -------------------------------------------------------------------

# Empty function return uninitialized array
# It similar to ones array
# empty(shape, dtype=float, order='C')


# emptyArray = np.empty((2, 3), dtype=int, order="C")
# print(emptyArray)
#
# ----------------------------------------------------

# linspace function : Create array from evenly spaced values
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)


# linSpaceArray = np.linspace(10, 100, num=10)
# linSpaceArrayTow = np.linspace(2.0, 3.0, num=5, endpoint=False)
#
# linSpaceArrayThree = np.linspace(2.0, 3.0, num=5, retstep=True)
# linSpaceArrayFour = np.linspace(1, 10, num=5, endpoint=True, retstep=True, dtype=int)
# linSpaceArrayFive = np.linspace(1, 10, num=5, endpoint=True, retstep=True, dtype=float)
#
# print(linSpaceArray)
# print(linSpaceArrayTow)
# print(linSpaceArrayThree)
# print(linSpaceArrayFour)
# print(linSpaceArrayFive)

# ----------------------------------------------------------------

# Eye function
# eye(N, M=None, k=0, dtype=<class 'float'>, order='C') N Number of rows in the output.
# M : int, optional
#       Number of columns in the output. If None, defaults to `N`.

# print(help(np.eye))
# Retrun array that is filled with zeros except in the k diagonal, whose values are equal to 1
# eyeArray = np.eye(5)
# print(eyeArray)
# eyeArrayTow = np.eye(3, 3, k=-1) # start form the index zero and for rows - and for column is +

# == == == == == == == == == == == ==
# Random
# Number
# Generation
# == == == == == == == == == == == ==
# 1- Rand : Create array of specified shape and fills it with random values as per uniform distribution
# Values will be in [1, 0) interval
# random.rand(row, column)
#
# rand = np.random.rand(2, 5)
# print(rand)

# 2- Randn Create array of specified shape and fills it with random values as per standard distribution

# randn = np.random.randn(2, 2)
# print(randn)

# 3- Randf Create array of specified shape and fills it with random float values as per standard distribution
# [0.0, 1.0]
#
# ranf = np.random.ranf(10)
# print(ranf)

# 4- Randint Create array of specified shape and fills it with random values as per standard distribution
#  randint(low, high=None, size=None, dtype=int)
#     Return random integers from `low` (inclusive) to `high` (exclusive).
# If high not mentioned then interval will be [0, low]

# randint = np.random.randint(1, 5, size=10, dtype=int)
# randintTow = np.random.randint(1, 10, size=(3, 3)) # the shape of array will be 3 dimensional
#
# print(randint)
# print(randintTow)

# *********************************************************************************
# Array attributes in numpy library
# 1- Dimension  2- Shape  3- Size  4- dtype  5- itemsize


# 1- Number of dimensional array named as ndim can be obtained as an integer value int with attribute ndim.

# dimArray = np.array([1, 2, 3, 4, 5, 6])
# dimen = dimArray.ndim  # Get the number of array dimension
#
# a_2d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# print(dimen)
# print(a_2d_array)
# -----------------------------------------------------------------------------------
# The shape (= size of each dimension) of numpy.ndarray can be obtained as a tuple with attribute shape.

# a_1d_array = np.array([1, 2, 3, 4])
#
# print(a_1d_array.shape)
#
# a_2d_array = np.array([[1, 2, 3], [1, 2, 3]])
#
# print(a_2d_array.shape)
#
# a_3d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# print(a_3d_array)
# --------------------------------------------------------------------------------

# The size (= total number of elements) of numpy.ndarray can be obtained with the attributesize.

# a_1d_array = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(a_1d_array.size)  # 9

# ------------------------------------------------------------------------------

# Itemsize if we are using zeros array the float64 / 8 = 8byte and array int32 / 8 = 4byte

# a_1d_array = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(a_1d_array.itemsize)  # 4
#
# a_2d_array = np.zeros((3, 2))
#
# print(a_2d_array.itemsize)

#  **************************************************************************************
#  **************************************************************************************

# Numerical data type in numpy
# 1- Integer,  2- Float,  3- Boolean,  5- unsigned integer,  6- Complex
#  To change the data type we can use var.astype( data type) or np."data type"(var)


# a_2d_array = np.zeros((3, 2))
#
# print(a_2d_array.astype(int))

# ****************************************************************************************

# Basic Indexing and slicing in numpy
# Indexing : we can access the element of array using index
# 1 d array indexing

# a_1d_array = np.array([1, 2, 3, 4, 5, 6, 100, 9, 10])
# a_2d_array = np.random.randint(1, 11, size=(2, 3, 4))
#
# print(a_2d_array)
# print("="*20)
# print(a_2d_array[:, 1:, ::2])

# -------------------------------------------

# Advance indexing in numpy (Integer and Boolean)
# in basic indexing we use integer or slice object to access an element of array
# but using advance indexing we create a array of index then we use it as index

# Integer indexing
# array = np.arange(1, 10)
# index = np.array([1, 2, 5])  # For one dimensional array
# print(array)
# print(array[index])
# print("*"*10)
#
# a_2d_array = np.array([[1, 2, -3], [4, 5, 6], [-7, 8, 9]])
#
# print(a_2d_array)
# print(a_2d_array[[0, 2], [2, 0]])  # For 2 dimensional array 2 element [3 7]
# print(a_2d_array[[1, 1, 2], [0, 2, 1]])  # Get 3 element [4 6 8]
#
# # Boolean indexing help to filter the array for specific elements
#
# print(a_2d_array[a_2d_array < 0])  # Get the negative numbers [-3 -7]
# print(a_2d_array[a_2d_array > 5])  # Get the  numbers that bigger than 5 [6 8 9]

# ********************************************************************************
# ********************************************************************************

# Arithmetic operation on array

# arrayOne = np.arange(1, 10)
# arrayTow = np.arange(10, 19)
# print(arrayOne)
# print(arrayTow)
# print(arrayOne / 2)
# print(arrayOne*2)
# print(arrayOne+10)
# print(arrayOne-5)
# print(arrayOne**2)
# print(arrayOne/arrayTow)
# # Or using arithmetic operation function in numpy
# print("--"*10)
# print(np.add(arrayOne, arrayTow))
# print(np.subtract(arrayOne, arrayTow))
# print(np.multiply(arrayOne, arrayTow))
# print(np.power(arrayOne, arrayTow))

# -------------- Broadcasting rules -------------
# a = np.array([[4, 8], [4, 5], [4, 8]])
# b = np.array([[4], [4], [4]])
#
# print(a.shape)
# print(b.shape)
# print(a+b)
#

# *************************************************************
# **************************************************************

# Array Manipulation

# 1- Reshape(): Changes the shape of array  numpy.reshape(array, shape, order) or array_name.reshape(new shape)

# array = np.array([[1, 2, 3], [4, 5, 6]])
# reshaped_array = np.reshape(array, (3, 2))
#
# print(reshaped_array)
# print(array)

# 2- Resize() : Changes the shape of array  numpy.resize(array, shape, order) or array_name.resize(new shape)
# Resize the original array

# a = np.array([1, 2, 3, 4, 5, 6])
# print(a)
# print(np.resize(a, (2, 3)))

# Flatten() taking a multidimensional array and turning it into a regular "single" dimensional array

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# print(a.flatten(order="F"))
# print(a.flatten(order="A"))
# print(a.flatten(order="C"))

# Ravel() The ravel() function is used to create a contiguous flattened array

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# ravel_array = a.ravel()
# print(ravel_array)

#  ******************************************************************
# *******************************************************************
# Transpose Array transpose(a, axes=None)
# Default value of axes = (1, 0) and (0, 1) will reverse it again

# array = np.arange(1, 11).reshape(2, 5)
# print(array)
#
# transposed_array = np.transpose(array)
# print(transposed_array)
# print(np.transpose(array, axes=(0, 1)))
# for 3d array

# arrayTow = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  # Shape (2, 2, 3)
# print(arrayTow.shape)                                                     # axes=(0, 1, 2)
# print(np.transpose(arrayTow, axes=(1, 2, 0)).shape)  # Change using transpose the shape of array shape (2, 3, 2)

# **********************************************************************
# **********************************************************************

# Splitting and Joining arrays

# Joining array using concatenate  concatenate((a1, a2, ...), axis=0, out=None)
#
# Join a sequence of arrays along an existing axis.

# a = np.arange(11)
# b = np.arange(10, 15)
# print(np.concatenate((a, b)))

# axes=0 concatenate the arrays vertically
# c = np.arange(1, 11).reshape(2, 5)
#
# d = np.arange(10, 25).reshape(3, 5)
#
# print(c)
# print(d)
#
# print(np.concatenate((c, d), axis=0))  # When axes=0 the size dimension of column must be the same
#
# # axes=1 will concatenate the arrays horizontally
# c = np.arange(1, 10).reshape(3, 3)
#
# d = np.arange(10, 25).reshape(3, 5)
#
# print(c)
# print(d)
#
# print(np.concatenate((c, d), axis=1))  # When axes=0 the size dimension of column must be the same


# ------ vstack and hstack : Stack arrays in sequence vertically and horizontally .

# c = np.arange(1, 10).reshape(3, 3)
#
# d = np.arange(10, 22).reshape(3, 4)
#
#
# print(np.hstack((c, d)))

# ---------- Split function hsplit and vsplit

# c = np.arange(1, 10).reshape(3, 3)
#
# print(c)
# print(np.split(c, 3, axis=1))


# ********************************************************************************
# ********************************************************************************

# Insert()  insert(arr, obj, values, axis=None)
#  arr : array_like
#         Input array.
#     obj : int, slice or sequence of ints
#         Object that defines the index or indices before which `values` is
#         inserted.

# a = np.arange(1, 10)
# print(np.insert(a, 3, 50))
# print(np.insert(a, (1, 3, 5), 10))

# b = np.arange(1, 10).reshape(3, 3)
# print(np.insert(b, 1, 23))  # Without using axis the array will be flattened
# print(np.insert(b, 2, 23, axis=0))  # Will insert value vertically
# print(np.insert(b, 0, [1, 3, 5], axis=1))

# ---------------- Append() append(arr, values, axis=None)
# Append values to the end of an array.

# array = np.arange(1, 10)
#
# print(np.append(array, 100))
#
# a_2d_array = np.arange(1,10).reshape(3, 3)
#
# print(np.append(a_2d_array, [[10, 20, 30]], axis=0))
# # print(np.append(a_2d_array, [[10, 20, 30]], axis=1))  # Error
# print(np.append(a_2d_array, [[10], [20], [30]], axis=1))

# ---------------- Delete() delete(arr, obj, axis=None)

# array = np.arange(1, 10)
# print(array)
# print(np.delete(array, 2))
#
# array_tow = np.arange(1, 10).reshape(3, 3)
# print(array_tow)
# print(np.delete(array_tow, 2, axis=0))

# *******************************************************************************
# *******************************************************************************

# Create matrix in numpy using nested list or numpy array or matrix class
# 1- Addation matrix with simple addation operation +
# array = np.arange(1, 10).reshape(3, 3)
# array_tow = np.arange(10, 19).reshape(3, 3)
# print(array)
# print(array_tow)
# print("-"*20)
# print(array + array_tow)
# matrix(data, dtype=None, copy=True)

# 2- Multiplication we need to use the Dot() method in array
# array_one = np.arange(1, 10).reshape(3, 3)
# array_tow = np.arange(10, 19).reshape(3, 3)
# print(array_one)
# print(array_tow)
# print("-"*20)
# print(array_one * array_tow)  # Element by element multiplication
# print(np.dot(array_one, array_tow))  # Multiplication row by column
#
# print(help(np.matrix))


