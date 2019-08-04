#Ask a user to enter a number
n = int(input("Enter a number:"))
print("You have entered ", str(n))
i = 1
while(i<=n):
    if(i%10==0):
        i += 1
        continue
    if(i>100):
        break
    print(str(i))
    i += 1
