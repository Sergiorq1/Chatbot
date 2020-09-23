
from random import choice
print("Welcome to Chat Bot")

def get_box_response(user_response):
  bot_response_music = ["Ya like jazz?", "Keep smiling!", "I love to see you happy!"]
  bot_response_space = ["im here for you", "sending good vibes"]
  bot_response_food = ["My favorite food is sushi, what's yours?", "Pinapple belongs on pizza, sorry to break the news", "Lettuce is just crunchy water"]

  if "Music" in user_response or "music" in user_response:
    return choice(bot_response_music)
  elif "Space" in user_response or "space" in user_response:
    return choice(bot_response_space)
  elif "Food" in user_response or "food" in user_response:
    return choice(bot_response_food)
  else:
    return "Wow, I do not know what that is. Tell me more!"


while True:
  user_response = input("What do you want to talk about? (Ex: Music,Space,Food)")
  if user_response == 'done':
    break

  
  print(get_box_response(user_response))
