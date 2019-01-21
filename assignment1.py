import sys #to import from command line
import matplotlib.pyplot as plt #to plot
import math as mt

#Usage message
try:
    n = sys.argv[1] #read command line input
except:
    print("Usage: give one of the following command line arguments:")
    print("1: f(x) = x")
    print("2: f(x) = x**2")
    print("3: f(x) = x**3")
    print("4: f(x) = sin(x)")
    print("5: f(x) = cos(x)")
    print("6: f(x) = tan(x)")
    print("7: f(x) = exp(x)")
    print("8: f(x) = sqrt(abs(x))")
    sys.exit()
    
#initialize list
xval = [i*0.1 for i in range(-30,31)]
print(xval)

#implement function
if n == "1":
    yval = [x for x in xval]
elif n == "2":
    yval = [x**2 for x in xval]
elif n == "3":
    yval = [x**3 for x in xval]
elif n == "4"
    yval = [mt.sin(x) for x in xval]
elif n == "5":
    yval = [mt.cos(x) for x in xval]
elif n == "6":
    yval = [mt.tan(x) for x in xval]
elif n == "7":
    yval = [mt.exp(x) for x in xval]
elif n == "8":
    yval = [mt.sqrt(mt.fabs(x)) for x in xval]
else:
    print("Invalid argument")
    sys.exit()
    
#plot
plt.figure()
plt.plot(xval,yval)
plt.show()

