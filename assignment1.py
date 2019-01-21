import sys #to import from command line
import matplotlib.pyplot as plt #to plot

#Usage message
try:
    n = sys.argv[1] #read command line input
except:
    print("Usage: give one of the following command line arguments:")
    print("1: f(x) = x")
    sys.exit()
    
#initialize list
xval = [i*0.1 for i in range(-30,31)]
print(xval)

#implement function
if n == "1":
    yval = [x for x in xval]
else:
    print("Invalid argument")
    sys.exit()
    
#plot
plt.figure()
plt.plot(xval,yval)
plt.show()

