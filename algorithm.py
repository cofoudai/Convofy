import random

topics= ["Sports","Academics","Food","Life"]

#Placeholder

def algorithm():
  likes = input("What topics do you like")
  if likes in topics:
    print("We will show you more of " + likes + " .")
  else:
    print("That is not a topic, sorry.")

firstselection = random.choices(topics, k=2)
print(firstselection)
algorithm()
