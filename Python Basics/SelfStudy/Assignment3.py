#Prime Number
"""
varN = int(input("Enter the n:"))
intI = 2
isPrime = True
while(intI < varN):
    if((varN % intI)==0):
        isPrime = False
        pass
    intI += 1
if(isPrime == True):
    print("%i is a Prime Number"%intI)
else:
    print("%i is not a Prime Number" %intI)
"""
primeFlag=True

n=int(input("Enter a number::"))

if n>1:

    for x in range(2,n-1):

        if n%x==0:

            primeFlag=False

    if(primeFlag):

        print("Is a prime number.")

    else:

        print("Is not a prime number.")

else:

    print("Is not a prime number.")