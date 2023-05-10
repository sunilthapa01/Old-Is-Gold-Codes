 


user1 = int(input("Enter the Num1\t:"))

user2 = int(input("Enter the Num2\t:"))

user3 = int(input("Enter the Num3\t:"))

user4 = int(input("Enter the Num4\t:"))


if user1 > user2:
	num1 = user1
else:
	num1 = user2

if user3 > user4:
	num2 = user3
else:
	num2 = user4


if (num1 > num2):
	print("it is greatest",num1)
else:
	print("it is greatest",num2)