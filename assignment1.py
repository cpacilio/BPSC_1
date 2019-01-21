import sys #to import from command line
import matplotlib.pyplot as plt #to plot
import math as mt

n = sys.argv[1] #read command line input

#initialize list
xval = [i*0.1 for i in range(-50,51)]

#implement function
if n == "1":
    yval = [x for x in xval]
if n == "2":
    yval = [mt.sin(x) for x in xval]
if n == "3":
    yval = [mt.cos(x) for x in xval]
if n == "4":
    yval = [mt.tan(x) for x in xval]
    
#plot
plt.figure()
plt.plot(xval,yval)
plt.show()

