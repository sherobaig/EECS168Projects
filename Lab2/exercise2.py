'''
Author: Shero Baig
KUID: 3093709
Date: 9/21/2022
Lab: lab02
Last modified: Date file was most recently modified 
Purpose: Make a program for long division
'''

while True:

	numerator = int(input("Enter a numerator: "))
	denominator = int(input("Enter a denominator: "))

	if(denominator == 0):
		print("You can not divide by a zero.")
	else:
		answer = int(numerator / denominator)
		remainder = int(numerator % denominator)
		print(numerator, "/",denominator, " = ",answer, "Remainder",remainder)
	leave = input("Do you want to leave the program now? (Y/y) or (N/n): ")
	if(leave == "y" or leave == "Y"):
			print("Exiting...")
			break
