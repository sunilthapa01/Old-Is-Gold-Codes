

text = input("Enter the text\n:")

if ("Make a lot of money" in text):
	spam = True
elif ("Buy now" in text):
	spam =  True 
elif ("subscribe this" in text):
	spam = True
elif ("click this " in text):
	spam = True 
else:
	spam = False


if spam:
	print("\t\\This is spam\\")
else:
	print("\t\\This is not spam\\")