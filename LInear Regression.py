# The term linear regresion is used twhen you try to find the relationship 
# between variables .in machine learning, that relationship is used to predict
# the outcome of thr=e future events.
# Start by drawing a statter plot:

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope,intercept,r,p,std_err = stats.linregress(x,y)

def call(x):
    return slope* x + intercept

mymodel = list(map(call,x))


plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()


# Pridict future values 
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope,intercept,r,p,std_err = stats.linregress(x,y)

def lock(x):
    return slope * 10 + intercept

car_speed = lock(10)

print(car_speed) 
plt.scatter(10,10)
plt.plot(10,car_speed)
plt.show()


# Bad fit

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def card(x):
  return slope * x + intercept

land = list(map(card, x))

print(r)
plt.scatter(x, y)
plt.plot(x, land)
plt.show()

x = [3,12,3,6,17,19,20,10,13,16,20]
y = [44,55,66,73,43,65,83,21,44,42,51]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def cali(x):
  return slope * x + intercept

mymodel = list(map(cali, x))

print(r)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
