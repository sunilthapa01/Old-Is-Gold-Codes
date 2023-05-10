

#Program to print Left Half Pyramid
num_rows = int(input("Enter the number of rows"));
k = 1
for i in range(0, num_rows):
	for j in range(0, k):
		print("* ", end="")

		k = k + 1

		print()
