#Lesson: functions
#print(3,4) is function where "print" is function name and "3,4" are arguments.
print("print(3,4) is")
print(3,4)
#print(3,4, sep='- -') here sep is keyword argument with value - -.
print(3,4,sep='- -')
#following is the way to define functions
def function1(varN):
	varL = []
	varA = 0
	varB = 1
	while len(varL) < varN:
		varA, varB = varB, varA + varB
		varL.append(varA)
	return varL
#here function end. line spacing rule.
#lets call function inside print
print(" varN is 6 and fibonacci is", function1(6))
#Lets try another example where no return
varM = []
print("Value of varM is", varM)
def function2(varIP):
	varM.append(varIP)
function2(2)
function2(9)
function2('pop')
function2(2.888)
print("Value of varM is now", varM)
#multiple return values
def function3(varComplx):
	return varComplx.real, varComplx.imag, varComplx.conjugate()
print("Imaginary 3+4j is",function3(3+4j))

#default argument values: user can either take default parameter values or can specify parameter values.
def function11(varN1= 5, varA1=0, varB1=1):
	varL = []
	while len(varL) < varN1:
		varA1, varB1 = varB1, varA1 + varB1
		varL.append(varA1)
	return varL
print("The default values are 5, 0 & 1 so fibonacci series is ", function11())
print("New values are 10, 0 & 1 so fibonacci series is ", function11(10))
print("The new values are 4, 2 & 3 so fibonacci series is ", function11(4,2,3))
print("The new values are 6, 11 & 3 so fibonacci series is ", function11(varB1=3, varN1=6, varA1=11))
