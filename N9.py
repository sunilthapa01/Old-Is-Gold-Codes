


M1  = int(input("Enter the marks\t:"))

M2 = int(input("Enter the marks\t:"))

M3 = int(input("Enter the marks\t:"))

total = M1 + M2 +M3

aver = total/3

if aver > 33:
	print("Congratulation !! You passed the exam")
elif aver < 33:
	print("You are failed")
else:
	print("Sorry you still failed")

print(aver)