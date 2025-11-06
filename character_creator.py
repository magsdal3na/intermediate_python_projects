print("""Welcome to the Character Creator!
This program will help you customize
a character for a few different games.
To start, please choose the game you
want to make a character for: \n""")

while True:
  game_choice = input()
  try:
    if game_choice.lower() == "fallout":
      print("You've chosen Fallout.")
      break
    if game_choice.lower() == "d&d":
      print("You've chosen D&D.")
      break
    if game_choice.lower() == "sims":
      print("You've chosen Sims.")
      break
    else:
      print("That is not a valid game.\nPlease try again.")
      continue
  except Exception:
    print("That is not a valid response.")

#Fallout character creation
stats_dict = {
    "Strength":0,
    "Perception":0,
    "Endurance": 0,
    "Charisma": 0,
    "Intelligence": 0,
    "Agility": 0,
    "Luck": 0
    }
if game_choice.lower() == "fallout":
  print("Please choose your character's name: ")
  character_name = str(input())
  print(f"Your character's name is: {character_name}")
  #print("Please choose your level of Strength\nfrom 1-10: ")
  #stats_dict["strength"] = int(input())

  for key in list(stats_dict.keys()):
    current_value = stats_dict[key]
    print(f"Please choose your amount of {key}: ")
    while True:
      try:
        updated_stat = int(input())
        if 1 <= updated_stat <= 10:
          stats_dict[key] = updated_stat
          print(f"Your {key} level is: {updated_stat}")
          break
        else:
          print("Please make your selection between 1 and 10: ")
      except Exception:
        print("Please select a number value.")
        updated_stat = int(input())
  
  print(f"Your final stats are: {stats_dict}")
  
  
  
  
  
  
  """print("Please choose your level of Perception: ")
  perception = int(input())
  while True:
    try:
      if 1 <= perception <= 10:
        print(f"Your perception level is: {perception}")
        break
      else:
        print("Please make your selection between 1 and 10: ")
        perception = int(input())
    except Exception:
      print("Please select a number value.")
      perception = int(input())"""

