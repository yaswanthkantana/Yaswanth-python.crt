num = int(input())
#using if-else
if(num>=100 and num<=999 or num>=-999 and num<=-100):
    print(f"{num} is a three digit")
else:
    print(f"{num} is not three digit number")

#terneray operator
res="three digit" if(num>=100 and num<=999 or num>=-999 and num<=-100) else "not a three digit number"
print(f"{num} is {res}")