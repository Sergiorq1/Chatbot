
from random import choice
def get_box_response(user_response):
  bot_response_music = ["omg! great!", "Keep smiling!", "I love to see you happy!"]
  bot_response_space = ["im here for you", "sending good vibes"]
  bot_response_food = ["My favorite food is sushi, what's yours?"]

  if user_response == "Music" or "music":
    return choice(bot_response_music)
  elif user_response == "Space" or "space":
    return choice(bot_response_space)
  elif user_response == "Food" or "food":
    return choice(bot_response_food)
  else:
    return "Wow, I do not know what that is. Tell me more!"




print("Welcome to Chat Bot")
print("What do you want to talk about? (Ex: Music,Space,Food)")

user_response = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
  user_response = input("How are you feeling today?: ")
  
  # Quits program when user responds with 'done'
  if user_response == 'done':
    break

  
  print(get_bot_response(user_response))
