
"""This is a character creator program
   for three different games: Fallout,
   D&D, and Sims 4. To start your character
   creation, please run the program."""

#Fallout character creation
def fallout():
  #SPECIAL stats dictionary
  stats_dict = {
      "Strength":0,
      "Perception":0,
      "Endurance": 0,
      "Charisma": 0,
      "Intelligence": 0,
      "Agility": 0,
      "Luck": 0
      }
  #SPECIAL stats total values
  special_total_older = 40
  special_total_4 = 28

  #Fallout trees
  if game_choice.lower() == "fallout":
    print("Are you playing Fallout 4? Yes or No: ")
    while True:
      try:
        user_fallout_game = str(input())
        if user_fallout_game.lower() == "yes" or user_fallout_game.lower() == "no":
          print(user_fallout_game)
          break
        else:
          print("Please type yes or no. ")
      except Exception:
        print("That is not a valid response.")

    print("Please choose your character's name: ")
    character_name = str(input())
    print(f"Your character's name is: {character_name}")

    #updating SPECIAL stats per user input
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

    #User's sum after their choices
    user_total_sum = sum(stats_dict.values())
    #checking total amount for Fallout 4
    if user_fallout_game.lower() == "yes":
      if user_total_sum == special_total_4:
        print(f"Your current stats are: {stats_dict}")
      else:
        difference_new = special_total_4 - user_total_sum
        print(f"You have {difference_new} points to allocate.")
        print(f"Please add/subtract values until you have a total of {special_total_4}.")
    #checking total amount for other games
    if user_fallout_game.lower() == "no":
      if user_total_sum == special_total_older:
        print(f"Your current stats are: {stats_dict}")
      else:
        difference_old = (special_total_older - user_total_sum)
        print(f"You have {difference_old} points to allocate.")
        print(f"Please add/subtract values until you have a total of {special_total_older}.")


#function for Sims 4 character creation
def sims_4():
  print("""Notice:
    This character creator includes
    base game traits that are available
    in CAS. None of the bonus traits
    or pack specific traits are 
    included in this creator.\n""")
  print("""Please choose three traits
  from the list below: \n""")
  print("""Emotional:           Hobby:            Lifestyle:            Social:
  - Active            - Bookworm         - Ambitious           - Good
  - Cheerful          - Music Lover      - Art Lover           - Jealous 
  - Creative          - Perfectionist    - Foodie              - Loner
  - Genius            - Loves Outdoors   - Neat                - Evil 
  - Gloomy            - Geek             - Lazy                - Bro 
  - Goofball                             - Slob 
  - Hot-Headed                           - Materialistic 
  - Romantic                             - Outgoing
                                         - Noncommittal
                                         - Self-Assured
                                         - Hates Children
                                         - Family-Oriented
                                         - Clumsy\n""")
  #dictionary to hold traits
  traits_dict = {}
  traits_dict["Emotional"] = ("Active", "Cheerful", "Creative", "Genius", "Gloomy", "Goofball", "Hot-Headed", "Romantic")
  traits_dict["Hobby"] = ("Bookworm", "Music Lover", "Perfectionist", "Loves Outdoors", "Geek")
  traits_dict["Lifestyle"] = ("Ambitious", "Art Lover", "Foodie", "Neat", "Lazy", "Slob", "Materialistic", "Outgoing", "Noncommittal", "Self-Assured", "Hates Children", "Family-Oriented", "Clumsy")
  traits_dict["Social"] = ("Good", "Jealous", "Loner", "Evil", "Bro")

  #user chosen traits
  while True:
    try:
      trait_1 = str(input())
      if trait_1.capitalize() in traits_dict.values():
        break
      else:
        print("That is not a valid trait. Please try again.")
    except Exception:
      print("That is not a valid response.")
  trait_2 = str(input())
  trait_3 = str(input())

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
      fallout()
      break
    if game_choice.lower() == "d&d":
      print("You've chosen D&D.")
      break
    if game_choice.lower() == "sims":
      print("You've chosen Sims.")
      sims_4()
      break
    else:
      print("That is not a valid game.\nPlease try again.")
      continue
  except Exception:
    print("That is not a valid response.")


