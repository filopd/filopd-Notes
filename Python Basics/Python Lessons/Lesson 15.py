#Lesson: Functions Cont...
#any number of input parameters to the function: *kargs (arguments) and **kwargs (keyword} arguments 
def function1(*args, **kwargs):
	print("arguments are", args)
	print("keyword arguments are", kwargs)
#function1 ends here.

print("lets call function1(4,5,6,varA=99, varB=44)")
function1(4,5,6,varA=99, varB=44)
#here args and kwargs are not important but * and **.
#* means expand this as sequence
#** means expand this as dictionary
def function2(*x, **xy):
	print("*x are:",x)
	print("*xy are:",xy)
#lets call this
function2(1,7,5,666, varM='gdgdgd', varN=34445)



