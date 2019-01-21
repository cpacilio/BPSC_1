import sys #to import from command line
import matplotlib.pyplot as plt #to plot

#Usage message
try:
    n = sys.argv[1] #read command line input
except:
    print("Usage: give one of the following command line arguments:")
    print("1: f(x) = x")
    print("2: f(x) = x**2")
    print("3: f(x) = x**3")
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
else:
    print("Invalid argument")
    sys.exit()
    
#plot
plt.figure()
plt.plot(xval,yval)
plt.show()

