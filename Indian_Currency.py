#wirte a python program to read amount as input from the user and print the number of notes requried in Indian Currency Dimesion?

#sample test case
#Enter the amount : 
#2000---->1
#500---->3
#200---->1
#100---->1
#50---->1
#20---->0

amount = int(input("enter the amount"))
print("2000---->1",amount//2000)
amount=amount%2000
print("500---->1",amount//500)
amount=amount%500
print("200---->1",amount//200)
amount=amount%200
print("100---->1",amount//100)
amount=amount%100
print("50---->1",amount//50)
amount=amount%50
print("20---->1",amount//20)
amount=amount%20
print("10---->1",amount//10)
amount=amount%10
print("5---->1",amount//5)
amount=amount%5
print("2---->1",amount//2)
amount=amount%2
print("1---->1",amount//1)
