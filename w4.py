

numbers = (11,22,33,45,34,56,78,87,67)
odd = 0
even = 0
for x in numbers:
	if x % 2:
		odd += 1
	else:
		even += 1
print("the numberof even is",even)
print("the number of odd is",odd)  



data = [566,78.90,False,"My name is Sunil",{'nam':'Sunil'}]
for items in data:
	print("The type is ",items,type(items))


color = {"c1":"Red", "c2": "Green", "c3": "Orange"}
for key in color.keys():
   print(key)
 

a = "Sunny"
print("todayis weather is",a)