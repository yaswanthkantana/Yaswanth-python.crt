num = int(input())
#using if-else
if(num>=-9 and num<=9):
    print(f"{num} is digit")
else:
    print(f"{num} is number")

#terneray operator
res="digit" if(num>=-9 and num<=9) else "number"
print(f"{num} is {res}")