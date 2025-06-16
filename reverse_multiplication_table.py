num=int(input())
for i in range(num,0,-1):
    print(f"multiplication table of {i}:")
    for j in range(10,0,-1):
        print(f"{i} x {j} = {i*j}")

#multiplication tables
num=int(input())
for i in range(1,num+1):
    print(f"multiplication table of {i}:")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")