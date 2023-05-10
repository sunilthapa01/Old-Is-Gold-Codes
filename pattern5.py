 




n = int(input("Enter the number of rows and coloumn:"))
m = int(input("Enter the number of coloumn:"))
for i in range(n):
	for j in range(m):
		if i == 0 or i == n-1 or j == 0 or j == n-1:
			print("*",end="")
		else:
			print(" ",end="")

	print()

