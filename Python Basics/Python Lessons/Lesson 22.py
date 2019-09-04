#Lesson 22
#List Comprehension: good feature of python.
varA = [varJ for varJ in range(5)]
print("varA is:", varA)
#this looks more simple than below code
varB = []
for varK in range(5):
	varB.append(varK)
print("varB is:", varB)
#syntax: [expr for var in interator]     this expr can be anything.
varC = [varL**2 for varL in range(5)]
print("varC is:", varC)
#append if condition at the end as well
varD = [varM for varM in range(10) if varM % 2 == 0]
print("varD:", varD)
#Multiple iteration is possible for list
varE = [(varN, varO) for varN in range(3) for varO in range(5)]
print("varE:", varE)
#lets test the conditions
varF = [varP for varP in range(10) if varP % 2 == 0]
print("Condition with == 0:", varF)
varG = [varP for varP in range(10) if varP % 2 == 1]
print("Condition with == 1:", varG)
varH = [varP for varP in range(10) if varP % 2]
print("Condition without == 0:", varH)
bool1 = 0
bool2 = 1
print("bool1 & bool2:", bool1, bool2)
if (bool1):
	print("bool1", bool1)
if (bool2):
	print("bool2", bool2)
#this is how condition without == 0 work well with varH, 0 false 1 true.


