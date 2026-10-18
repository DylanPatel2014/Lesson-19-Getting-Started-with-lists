num=1
even_list=[]
odd_list=[]
range=int(input("Please enter a number to show the maximum range:"))
while num**2<=range:
    square=num**2
    num=num+1
    if square%2==0:
        even_list.append(square)
    else:
        odd_list.append(square)
print("These are the square numbers between your range which is 0 and",range,"that is even",even_list)
print("These are the square numbers between your range which is 0 and",range,"that is odd",odd_list)

