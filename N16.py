

num = int(input("Enter the number\n:"))

prime = True
for i in range(2,num):

	if (num%i == 0):
		prime = False
if prime:

	print("// It is Prime number //")

else:
	print("// It is not Prime number //")