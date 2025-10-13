import random
name = input("Hello, what is your name?")
question = input(f'Do you have a question for me {name}, my child? ')
answer = " "
random_int = random.randint(1,9)

if(random_int == 1):
  answer = "Yes - Definitely"
elif(random_int == 2):
  answer = "It is decidedly so"
elif(random_int == 3):
  answer = "Without a doubt"
elif(random_int == 4):
  answer = "Reply hazy, Try again"
elif(random_int == 5):
  answer = "Ask again later"
elif(random_int == 6):
  answer = "Better not tell you now"
elif(random_int == 7):
  answer = "My sources say so"
elif(random_int == 8):
  answer = "Outlook not so good"
elif(random_int == 9):
  answer = "Very Doubtful"
else: 
  print("Error")

print(answer)