
while(True):

	age = int(input("Enter the age:"))
	if (age >= 11):
		print ("WELCOME TO THE MATCH")
		if (age <= 20  or age >= 60):
			print("Ticket : Rs 120 ")
		else:
			print("Ticket : Rs 200")
	else:
		print ("SORRY YOU ARE NOT ALLOWED...........................")
 