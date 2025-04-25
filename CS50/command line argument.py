import sys

if len(sys.argv)<2:
    sys.exit("Too few arguments")
# elif len(sys.argv)>2:
#     sys.exit("Too many arguments")

for arg in sys.argv[1:]:    #Thie list of sys.argv has the file name in 0 index so to avoid printing the file name we slice the list
    print("Hello, My name is",arg)  
