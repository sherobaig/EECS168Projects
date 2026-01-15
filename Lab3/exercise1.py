'''
Author: Shero Baig
KUID: 3093709
Date: 9/29/22
Lab: lab03
Last modified: Date file was most recently modified
Purpose: This is a sequence search, the program will obatain a string from the user then the user will look for a specific sequence in the string and will wonder how much of that sequence is in the string. The program will tell the user that.
'''


user_string = input("Enter a string: ")

decision = input("Do you want case-sensitive match?: ")

sequence = input("Enter a sequence to count: ")


if decision.lower() == 'y':

    count = user_string.count(sequence)


else:
 
    count = user_string.lower().count(sequence.lower())


print(f"In the string {user_string} the sequence '{sequence}' occurs {count} time(s)")
