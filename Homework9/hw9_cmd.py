import sys
(sys.argv).remove(sys.argv[0])
print "sum:",reduce(lambda x,y:int (x)+int (y),sys.argv)



#l=len(sys.argv)
#sum=0
#for i in range(1,l):
#	sum=sum+int(sys.argv[i])
#def fsum(x,y)
#	return x+y









