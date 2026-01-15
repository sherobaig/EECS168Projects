'''
Author: Shero Baig
KUID: 3093709
Date: 9/21/2022
Lab: lab02
Last modified: Date file was most recently modified
Purpose: The purpose of this program is to obtain a wind speed from the user and they will get to know what category storm that wind speed is. 
'''
try:

	wind_speed=int(input("Input a wind speed (m/s): "))

	if wind_speed>=0 and wind_speed<18:
		print("A wind speed of ",wind_speed," m/s is a Tropical Depression.")
	elif wind_speed>=18 and wind_speed<33:
		print("A wind speed of ",wind_speed," m/s is a Tropical storm.")
	elif wind_speed>=33 and wind_speed<43:
		print("A wind speed of ",wind_speed," m/s is a Category 1 hurricane.")
	elif wind_speed>=43 and wind_speed<50:
		print("A wind speed of ",wind_speed," m/s is a Category 2 hurricane.")
	elif wind_speed>=50 and wind_speed<58:
		print("A wind speed of ",wind_speed," m/s is a Category 3 hurricane.")\
	elif wind_speed>=58 and wind_speed<70:
		print("A wind speed of ",wind_speed," m/s is a Category 4 hurricane.")
	elif wind_speed>=70:
		print("A wind speed of ",wind_speed," m/s is a Category 5 hurricane.")
	else:
		print("Negative wind? Sorry, that's invalid.")
except:
	print("Invalid windspeed.")

