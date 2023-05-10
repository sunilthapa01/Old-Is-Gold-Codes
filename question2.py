

print("Printing current and previous number sum in a range(10)")

pre_num = 0

for i in range(1,11):

	pr_num = pre_num + i

	print("Current Number",i,"Previous Number",pre_num,"Sum:",pre_num + i)

	pre_num = i


