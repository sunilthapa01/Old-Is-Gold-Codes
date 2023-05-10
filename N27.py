


num = int(input("Enter the number\n:"))

num2 = print("Fixed order(1) or Reverse order(0)")
new = bool(num2)
if new == True:
	for i in range(1,num+1):
		for k in range(1,i+1):
			print("*",end="")

elif new == False:
	for l in range(num,0,num-1):
		for m in range(1,i+1):
			print("*",end="")


