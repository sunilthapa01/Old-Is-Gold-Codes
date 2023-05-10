



i = int(input("Enter the number\n:"))

if i < 0:
	print("")
else:
	sum = 0
	while i > 0:
		sum = sum +i
		i -= 1
print(sum)