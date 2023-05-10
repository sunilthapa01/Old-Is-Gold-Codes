



intro = "Dear <|name|>,\n\t You are selected! for tournament enjoy your day \n\t which is on  <|Date|>"

name = input("Enter your name\t :")
date = input("Enter  date\t:")

intro = intro.replace("<|name|>",name)
intro = intro.replace("<|Date|>",date)
print(intro)