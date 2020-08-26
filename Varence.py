# Varience is another number that indicates how spread out the values are.
# If you take the square root of the varience, you get the standard deviation
# or the other way round. if you multiply the 

# Using the numpy var() method to find a varience

import numpy

speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)

# percentiles 
# percentiles are used in statistics to give you a number that describes
#  the value that a given percent of the values arelower than.

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82]
x = numpy.percentile(ages, 50)
print(x)

# Data distribution 
# Create an array containg 250 random floats between 0 and 5 

import numpy
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)