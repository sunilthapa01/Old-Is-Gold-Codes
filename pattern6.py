

n = int(input("Enter the number of row:"))

m = int(input("Enter the number of cloumn:"))
for i in  range(n):
	for j in range(m):
		if (i == 0 and j%3 != 0) or (i == 1 and j%3 ==0) or (i-j == 2) or (i + j == 8):

			print("*",end="")
		else:
			print(" ",end="")

	print()