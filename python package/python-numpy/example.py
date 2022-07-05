import numpy as np


myPythonList = [1,9,8,3]

#! Creating a NumPy Array
numpy_array_from_list = np.array(myPythonList)
print("Creating a NumPy Array",numpy_array_from_list)

#! Mathematical Operations on an Array
math_operation_on_array=numpy_array_from_list + 10
print("Mathematical Operations on an Array",math_operation_on_array)

#! Shape of Array
#### One type
shape_one  = np.array([1,2,3])
print("Shape One",shape_one.shape)
print("Shape One Type",shape_one.dtype)

#### Two type
shape_two  = np.array([1.1,2.0,3.2])
print("Shape Two",shape_two.dtype)

#! Two Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6)])
print("Two Dimension Array",two_dimension_array.shape)

#! Three Dimension Array
three_dimension_array = np.array([[[1, 2,3],[4, 5, 6]],[[7, 8,9],[10, 11, 12]]])
print("Three Dimension Array",three_dimension_array.shape)

#! Python numpy.zeros()
numpy_zeros=np.zeros((3,3))
print("Numpy Zeros",numpy_zeros)

#! Python numpy.ones() 2D Array with Datatype
numpy_ones=np.ones((1,2,3), dtype=np.int16)
print("Numpy Ones",numpy_ones)

#! Python numpy.reshape()
numpy_array  = np.array([(1,2,3), (4,5,6)])
print("Before Numpy Reshape",numpy_array)
numpy_reshape=numpy_array.reshape(3,2)
print("After Numpy Reshape",numpy_reshape)

#! Python numpy.flatten()
numpy_array  = np.array([(1,2,3), (4,5,6)])
numpy_flatten=numpy_array.flatten()
print("Numpy Flatten",numpy_flatten)

#! Python numpy.hstack()
## Horizontal Stack
f = np.array([1,2,3])
g = np.array([4,5,6])
print('Horizontal Append:', np.hstack((f, g)))

#! Python numpy.vstack()
## Vertical Stack
f = np.array([1,2,3])
g = np.array([4,5,6])
print('Vertical Append:', np.vstack((f, g)))

#! Generate Random Numbers using NumPy
# syntax :- numpy.random.normal(loc, scale, size)
# param :- 
    # loc: the mean. The center of distribution
    # scale: standard deviation.
    # size: number of returns

## Generate random number from normal distribution
normal_array = np.random.normal(5, 0.5, 10)
print("generate_random_number ",normal_array)		

#! Python numpy.asarray()
A = np.matrix(np.ones((4,4)))
np.array(A)[2]=2
print("Matrix ",A)
"""
    Matrix is immutable. You can use asarray if you want to add modification in the original array.

    Let’s see if any change occurs when you want to change the value of the third rows with the value 2
"""
np.asarray(A)[2]=2
print("AsArray ",A)

"""
    Code Explanation:

    np.asarray(A): converts the matrix A to an array

    [2]: select the third rows
"""

#! Python numpy.arange()
numpy_arrange=np.arange(1, 11)
print("Numpy Arrange",numpy_arrange)

#! Python numpy.linspace()
numpy_linspace=np.linspace(1.0, 5.0, num=10)
print("Numpy Linspace",numpy_linspace)
# If you do not want to include the last digit in the interval, you can set endpoint to false
numpy_linspace=np.linspace(1.0, 5.0, num=5, endpoint=False)
print("Numpy Linspace with endpoint=false",numpy_linspace)

#! Indexing and Slicing in Python
numpy_array  = np.array([(1,2,3), (4,5,6)])
print("Array",numpy_array)
## First row
print('First row:',numpy_array[0])
## Second row
print('Second row:',numpy_array[1])
## Second column
print('Second column:', numpy_array[:,1])

""" To return the first two values of the second row. You use : to select all columns up to the second """
## Second Row, two values
print("Second row , two values",numpy_array[1, :2])			

#! NumPy Statistical function 
## Normal Array
normal_array = np.random.normal(5, 0.5, 10)
print("Normal Array",normal_array)

### Min 
print("Min",np.min(normal_array))

### Max 
print("Max",np.max(normal_array))

### Mean 
print("Mean",np.mean(normal_array))

### Median
print("Median",np.median(normal_array))

### Standard deviation (sd)
print("Standard deviation",np.std(normal_array))