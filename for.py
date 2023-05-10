
i = int(input("Enter the number :")) 


if i < 0:
   print("this is negative number")
else:
   s = 0
   while(i > 0):
       s += i
       i -= 1
   print(s)


