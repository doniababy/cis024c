import sys
from helper import *

n1=0
n2=0
if len(sys.argv)==3:
    n1= int(sys.argv[1])
    n2= int(sys.argv[2])
    print "Sum:",add(n1,n2)