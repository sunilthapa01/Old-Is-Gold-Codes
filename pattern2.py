

i = 1

while i <= 6:
	j = 1

	while j <= i:
		print("*",end="")
		j = j + 1
		if i == 0 or i == 1 and j == 0 or j == 1:
			print(" ",end="")

		print(" ",end="")
	print()

	i = i+1