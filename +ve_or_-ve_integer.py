#write a pyhton progrm to read the integer value as input from the user and check whether it is a positive number or negative number
#sample test case :

#enter the integer value : 15
#15 is a +ve number

a=int (input())
#using if-else 
if(a>0):
    print(f"{a} is +ve number")
elif(a<0):
    print(f"{a} is -ve number")
else:
    print(f"{a} is a zero")

#using ternary operator

res="+ve number" if(a>0) else "-ve number"
print(f"{a} is {res}")