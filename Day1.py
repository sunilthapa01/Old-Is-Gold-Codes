

def func_num(num):

	if len(num) == len(set(num)):
		return True
	else:
		return False

print(func_num([1,5,7,9]))

print(func_num([2,4,5,5,7,9]))

