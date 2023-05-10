

num = int(input("Enter any digit number: "))

sum = 0

for num  in range(0):

	sum = sum + num%10

	num = num + num//10



print("result is ",sum)