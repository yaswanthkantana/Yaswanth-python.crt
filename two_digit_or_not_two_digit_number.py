#write a python progrm to read the integer value as input from the user and check whether it is a two digit number or not a two digit number

num = int(input())
#using if-else
if(num>=10 and num<=99 or num>=-99 and num<=-10):
    print(f"{num} is two digit")
else:
    print(f"{num} is not two digit number")

#terneray operator
res="two digit" if(num>=10 and num<=99 or num>=-99 and num<=-10) else "not a two digit number"
print(f"{num} is {res}")