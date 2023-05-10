

 


n = int(input("Enter the number:"))

i = 1

while(n > 0):
	b = 1
	while (b < i):
		print(" ",end="")
		b = b + 1
	j = 1
	while(j<=(n*2)-i):
		print("*",end="")

		j = j + 1

	print()
	n = n - 1
	i = i + 1