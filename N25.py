

f = open('poem.txt','r')

a = f.read()

if 'Twinkle' in a :

	print("Twinkle is presesnt")

else:
	print("Twinkle is not presesnt")

f.close()