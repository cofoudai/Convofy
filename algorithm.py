import random

topics= ["Sports","Academics","Food"]

firstselection = random.choices(topics, k=2)

#Placeholder

def algorithm:
  likes = input("What topics do you like")
  if likes in topics:
    print("We will show you more of" + likes + " .")
