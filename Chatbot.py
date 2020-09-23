
from random import choice
print("Welcome to Chat Bot")

def get_box_response(user_response):
  bot_response_music = ["Ya like jazz?", "Music nowadays is great! people need to stop hating", "I personally prefer Stevie Wonder over The Beatles, but it's a close one", "My favorite album is To Pimp a Butterfly by Kendrick Lamar, what's yours?", "I know how to sing in autotune!"]
  bot_response_space = ["We are made of stardust :O", "The temperature in the void of space is about -270.45 degrees celsius, that's cold!!", "Space is void of sound because molecules are too far apart to transmit sound", "Space between galaxies has an average of one atom per cubic meter, so it's basically nothingness..."]
  bot_response_food = ["My favorite food is sushi, what's yours?", "Pinapple belongs on pizza, sorry to break the news", "Lettuce is just crunchy water", "My specialty meal are eggs, what's yours?", "How do you like your celreal? personally I go cereal, milk, then bowl"]
  

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
