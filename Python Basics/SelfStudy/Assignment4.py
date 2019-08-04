maths,physics,chemistry =[int(x) for x in (input("Enter the marks of maths, physics & chemistry out of 100 (comma separated): ").split(","))]
print("Marks are as follow: \n Maths:",maths,", Physics:",physics," & Chemistry:",chemistry)

isFailes = False
avg = ""

if((maths>34) & (physics>34) & (chemistry>34)):
    avg = (maths + chemistry + physics)/3
    print("Average is: ",avg)
    if(avg>69):
        print("Grade is: A")
    elif(avg>59):
        print("Grade is: B")
    else:
        print("Grade is: C")
else:
    print("You have failed in exams !")