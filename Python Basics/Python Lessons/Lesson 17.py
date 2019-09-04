#Lesson 17: try and except
#to give meaningful errors, use this.
print("an error for for = 3/0 is as follow:")
print("-------------_-------------_-----------------_-------")
#varA = 3 / 0
print("ZeroDivisionError: division by zero")
print("-------------_-------------_-----------------_-------")
#let's catch this error
def fun1(varA = 2, varB = 1):
	try:
		varC = varA/varB
		print("No Error")
		return varC
	except:
		print("Error appeared")
		return "Error !"
		
print("fun1 with 2 / 1 gives:")
fun1()
print("-------------_-------------_-----------------_-------")
print("fun1 with 2 / 0 gives:")
fun1(2,0)
print("-------------_-------------_-----------------_-------")
#let's catch this error with error type
def fun2(varA = 2, varB = 1):
	try:
		varC = varA/varB
		print("No Error")
		return varC
	except ZeroDivisionError:
		print("Zero Division Error appeared")
		return "Specific Error !"
	except:
		print("Unknown Error appeared")
		return "Unknown Error !"

print("fun2 with 2 / 1 gives:")
fun2(2,1)
print("-------------_-------------_-----------------_-------")
print("fun2 with 2 / 0 gives:")
fun2(2,0)
print("-------------_-------------_-----------------_-------")
print("fun2 with 2 / 'abc' gives:")
fun2(2,"abc")
print("-------------_-------------_-----------------_-------")

#let's catch this error with error type
if (1==1):
	print("Now Print Runtime Error Hey")
	print("-------------_-------------_-----------------_-------")
	raise RuntimeError("Runtime Error Hey")

print("-------------_-------------_-----------------_-------")



