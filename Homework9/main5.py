import sorthelper
import sys
(sys.argv).remove(sys.argv[0])

myList= []
for i in sys.argv:
    myList.append(int(i))
    
sorthelper.sortNumbers(myList)
print myList