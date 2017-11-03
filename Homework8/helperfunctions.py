def add(x,y):
	return (x+y)

def product(x,y):
	return (x*y)

def greatest(x,y):
	if x>y :
		return x
	else:
		return y
def diff(x,y):
	return x-y


def addAll(inList):
	x=reduce(add,inList)
    	return x

def subAll(inList):
   	x=reduce(diff,inList)
    	return x

def multiplyAll(inList):
    	x=reduce(product,inList)
    	return x

def greatAll(inList):
	x= reduce(greatest,inList)
    	return x

