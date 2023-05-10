


print("Weclome to sunil's intigration dictionary")

int_dict_for = {"sinx":"-cosx","cosx":"sinx","sec**2x":"tan**2x","cosec**2x":"-cotx","secxtanx":"secx","cosecxcotx":"-cosecx"}


user = input("Enter the trignometric identity :")

# print(int_dict_for.keys())
i = 1

while(i < 7):
	print(int_dict_for[user])

	i = i + 1

if i <=  7:

	print("//we have only 7 intigrations.Sorry we will add soon//")
