from importtest import hello
import sys

if len(sys.argv)<2:
    sys.exit("Too few aruments")
elif(len(sys.argv)>2):
    sys.exit("Too many arguments")

hello(sys.argv[1])


