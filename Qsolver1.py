

def equation_ab(a,b):

	# n = (a + b)**2
	n = a**2+b**2+ 2*a*b

	if  n >= 0:

		return n 

	else:

		return -n

result = equation_ab(25,30)

print("Your answer sir: ",result)