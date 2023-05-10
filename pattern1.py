

star_no = int(input("Enter the number:"))

h = 8
for i in range(0,star_no):
	for j in (0,h):

		print(end=" ")

		h  = h - 2 
		for j in range(0,i+1):
			print("*",end="")

			print()