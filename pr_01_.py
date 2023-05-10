

n = int(input("Enter the number:"))

for i in range(n):

	print("*",end=" *")

	print("*","","*")
	print("")

	print(""*(n-i-1),end="")

	print("*"*(1*i+1))

	print()