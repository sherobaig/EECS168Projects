'''
Author: Shero Baig
KUID: 3093709
Date: 9/21/2022
Last modified: Data file was most recently modified
Purpose: Making a soda program that will take the number of sodas and distribute them into different types of packs.
'''

soda = int(input("How many sodas do you have? "))

fridge_cube = int(soda/24)

soda = soda%24

six_pack = int(soda/6)

soda = soda%6


print("Fridge Cubes:",fridge_cube)
print("Six packs:",six_pack)
print("Singles:",soda)
