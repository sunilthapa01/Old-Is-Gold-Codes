

print("     //CALUCLATOR//   ")

dic_nam = {"a":"+","b":"-","c":"*","d":"/"}

print(dic_nam.keys())

W1 = input("Enter the operator")
# 45*3 == 555,56+9 = 77, 56/6 = 4 
if W1 == "a":
	num1 = int(input("Enter  the first number:"))

	num2 = int(input("Enter the second number:"))


	if num1 == 56:

		if num2 == 9:
			print("",77)
		else:
			print(":",num1 + num2)
elif W1 == "b":
	num3 = int(input("Enter the first number:"))

	num4 = int(input("Enter the second number:"))

	if num3 == 0:
		if num4 == 1:
			print("your answer is // 1 //")
		else:
			print(num3 - num4)

elif  W1== "c":
	num5 = int(input("Enter the first number :"))

	num6 = int(input("Enter the second number :"))

	if num5 == 45:
		if num6 == 3:
			print("",555)
		else:
			print(num5*num6)
elif W1 == "d":

	num7 = int(input("Enter the first number: "))

	num8 = int(input("Enter the  second number:"))
	

	if num7 == 56:
		if num8 == 6:
			print("",4)

		else:
			print(num7/num8)
