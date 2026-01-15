'''
Author: Shero Baig
KUID: 3093709
Date: 11/17/22
Lab: lab08
Last modified: Date file was most recently modified
Purpose: Creating a program where you can load in a pokedex and interact with it in many ways.
'''






import random


def build_pokedex(filename):
   pokedex_dict = {}
   with open(filename) as i:
       for pokemon in i:
           names = pokemon.strip().split()
           us_name = names[0]
           jpn_name = names[1]
           pokedex_dict[us_name] = jpn_name
   return pokedex_dict


def build_team(pokedex, size=6, is_unique=False):
   team_list = []
   if is_unique == False:
       for i in range(size):
           team_list.append(random.choice(list(pokedex)))

   else:
       help_dict = {}
       while size > 0:
           pokemon = random.choice(list(pokedex))

           if help_dict.get(pokemon):
               continue
           else:
               team_list.append(pokemon)
               help_dict[pokemon] = 1

               size -= 1
   return team_list



def battle(team1, team2):
   fighter1 = 0
   fighter2 = 0
   print("+++Team 1+++")
   for pokemon_fighter in team1:
       print(pokemon_fighter)

   print("\n+++Team 2+++")
   for pokemon_fighter in team2:
       print(pokemon_fighter)



   round = 1
   print()
   while fighter1 < 6 and fighter2 < 6:
       print(f"+++Round {round}+++")
       print(f"{team1[fighter1]} VS {team2[fighter2]}")
       victory = random.randint(0, 1)

       if victory == 1:
           fighter2 += 1
           print(f"{team1[fighter1]} wins!")
       else:
           fighter1 += 1
           print(f"{team2[fighter2]} wins!")
       round += 1
       print()


   if fighter2 == 6:
       print("Team1 won the battle.")
       print("Remaining Pokemon:")
       for i in range(fighter1, 6):
           print(team1[i])


   else:
       print("Team2 won the battle.")
       print("Remaining Pokemon:")
       for i in range(fighter2, 6):
           print(team2[i])


def main():
   pokedex_build = build_pokedex("pokedex.txt")
   while True:
       print("1) Print Pokedex")
       print("2) Translate")
       print("3) Build a team")
       print("4) Pokemon battle")
       print("5) Exit")


       try:
           decision = int(input("Enter the number you want to do: "))
       except:
           print("Please enter a valid number choice.\n")
           continue


       if decision < 1 or decision > 5:
           print("Please enter a valid choice.\n")
           continue

       if decision == 1:
           print()
           print("US_Name | JPN_Name")
           for us, jpn in pokedex_build.items():
               print(f"{us} | {jpn}")
           print()

       elif decision == 2:
           print()
           us_name = input("Enter the US Name: ")
           if pokedex_build.get(us_name) is None:
               print("The name you entered was not found in the pokedex.")
           else:
               print("The JPN name is :", pokedex_build.get(us_name))
           print()

       elif decision == 3:
           print()
           team = build_team(pokedex_build)
           print("+++TEAM+++")
           for pokemon_fighter in team:
               print(pokemon_fighter)
           print()

       elif decision == 4:
           print()
           team1 = build_team(pokedex_build, is_unique=True)
           team2 = build_team(pokedex_build, is_unique=True)
           battle(team1, team2)
           print()

       else:
           break


main()
