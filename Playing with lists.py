L=[10,1,13,7,3,14]
print("this is the original list",L)
count=0
for i in L:
    count+=i
average=count/len(L)
print("The average is",average)

L.sort()
print("The smallest number is",L[0])
print("The largest number is",L[-1])
print("The sum of the listed numbers is",count)


