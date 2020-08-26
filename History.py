# To visualize the data set, we can draw a histogram with the data
# we collected. we will use the python module Matplotlib to draw a histogram

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x,5)
plt.show()

# Big data Distribution
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0,5.0,1000)
plt.hist(x,100)
plt.show()

# Normal Data Distribution 

import numpy
import matplotlib.pyplot as plt 

x = numpy.random.normal(5.0, 1.0, 1000)
plt.hist(x,100)
plt.show()

# NOTE: a normal distibution graph is also know as the bell curve because 
# of it characteristics shape of a bell

# Scatter Plot 
# A scatter plot is a diagram where each value in the data set is represented by a dot

x = [5,7,8,7,2,9,17,2,4,11,12,9,6]
y = [99,86,87,88,111,86,103,89,94,78,77,85,86]

plt.scatter(x,y)
plt.show()


# Random Data Distribution 

import numpy
import matplotlib.pyplot as plt 
 
x = numpy.random.normal(5.0,1.0,1000)
y = numpy.random.normal(10.0,2.0,1000)

plt.scatter(x,y)
plt.show()