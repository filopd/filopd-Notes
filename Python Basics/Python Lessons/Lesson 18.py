#Lesson 18:
#Let's Raise own exception.
#1. raise RuntimError
print("------------------------------------------------------------------------")
#Uncomment Below Line for 1.
#raise RuntimeError("1. This is RuntimeError")
#This appears as "RuntimeError: This is RuntimeError"
print("------------------------------------------------------------------------")
#Uncomment Below Line for 2.
#raise RuntimeError("2. This is ValueError")
#This appears as "RuntimeError: This is ValueError"
#Let's write an exception and use except for it.
def fun1(varA = 1):
    try:
        if(varA == 2):
            raise ValueError("ValueError for Input: 2.")
        return 1 / varA
    except ZeroDivisionError:
        return "This is Zero Division Error"
    except ValueError:
        return "This is Value Error"
    except:
        return "This is Unknown Error"

print("No Error :",fun1(5))
print("ZeroDivisionError :",fun1(0))
print("ValueError :",fun1(2))
print("UnknownError :",fun1('Hello'))
print("------------------------------------------------------------------------")
#Accessing the Error Message
def fun2(varB = 1):
    try:
        print("Program started !",varB)
        return 1 / varB
    except ZeroDivisionError as myErr:
        print("Error Message type is", type(myErr))
        print("Error Message is", myErr)
print("Here is the type and error message:")
fun2()
fun2(3)
fun2(0)
print("------------------------------------------------------------------------")
#Define Custom Exception
class mySpclErr(ValueError):
    pass
#Uncomment Below Line.
#raise mySpclErr("This is my Error !")
print("------------------------------------------------------------------------")
#Try Except Else Finally
def fun3(varC = 1):
    try:
        varD = 0
        print("TRY: Program Started")
        varD = 1 / varC
    except:
        print("EXCEPT: Error is occured. So varD is", varD)
    else:
        print("ELSE: There is no error and varD is", varD)
    finally:
        print("FINALLY: This block will always print and program stopped here.")
print("Here is the result of Try/Except/Else/Finally:")
fun3()
print("---------")
fun3(0)



