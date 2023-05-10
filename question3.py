
print("// TICKETS COUNTER //")


while(1):
	customer = int(input("Enter your age :"))
	if customer <= 3 :
		print(" // It's free for  you little kid // ")

	elif customer == 3 or customer <= 12 :
		print("// U have to pay $10 //")

	elif customer > 12:
		print("// U have to pay $15 //")

	else:
		print("//W/E/L/C/O/M/E//")


	customer = customer + 1


if(customer >= 9):

	print("\\You buy your all tickekts\\")

