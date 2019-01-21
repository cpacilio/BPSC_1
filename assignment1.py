import sys #to import from command line
import matplotlib.pyplot as plt #to plot
import math as mt

#Usage message
try:
    n = sys.argv[1] #read command line input
except:
    print("Usage: give one of the following command line arguments:")
    print("1: f(x) = x")
    print("5: f(x) = exp(x)")
    print("6: f(x) = sqrt(abs(x))")
    sys.exit()
    
#initialize list
xval = [i*0.1 for i in range(-50,51)]

#implement function
if n == "1":
    yval = [x for x in xval]
elif n == "5":
    yval = [mt.exp(x) for x in xval]
elif n == "6":
    yval = [mt.sqrt(mt.fabs(x)) for x in xval]
else:
    print("Invalid argument")
    sys.exit()
    
#plot
plt.figure()
plt.plot(xval,yval)
plt.show()

