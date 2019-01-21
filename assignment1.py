import sys #to import from command line

n = sys.argv[1] #read command line input

#initialize list
xval = [i*0.1 for i in range(-50,51)]

#implement function
if n == "1":
    yval = [x for x in xval]

print(yval)

