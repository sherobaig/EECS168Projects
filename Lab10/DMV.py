'''
Author: Shero Baig
KUID: 3093709
Date: 12/08/22
Lab: lab010
Last modified: Date file was most recently modified
Purpose: Creating a DMV class
'''
from DriverLicense import DriverLicense
class DMV:
   def __init__(self, file):
       self._file = file
       self._driver_licenses_together = []
       self._read_store_file()

   def _read_store_file(self):
       with open(self._file, 'r') as i:
           for line in i:
               line_split = line.split('\t')
               license_num = line_split[0]
               first = line_split[1]
               last = line_split[2]
               age = line_split[3]
               voter = line_split[4].strip()
               self._driver_licenses_together.append(
                   DriverLicense(first, last, age, voter, license_num))

   def mix_licenses(self):
       self._driver_licenses_together.sort()

   def print_all_drivers_info(self):
       for license in self._driver_licenses_together:
           print(f"{license._last_name}, {license._first_name} ({license._age}): {license._license_number} {license._voter_status}")

   def voting_age(self):
       for license in self._driver_licenses_together:
           if int(license._age) >= 18 and int(license._age) <= 24 and license._voter_status == "N":
               print(f"{license._last_name}, {license._first_name} ({license._age}): {license._license_number} {license._voter_status}")

   def by_letter(self):
       letter = (input("Please enter a single character: "))
       exist = False
       for license in self._driver_licenses_together:
           if license._last_name[0].lower() == letter.lower():
               exist = True
               print(f"{license._last_name}, {license._first_name} ({license._age}): {license._license_number} {license._voter_status}")
       if not exist:
           print("No record has been found.")

   def print_age(self):
       age = int(input("Enter an age you want to search: "))
       exist = False
       for license in self._driver_licenses_together:
           if int(license._age) == age:
               print(f"{license._last_name}, {license._first_name} ({license._age}): {license._license_number} {license._voter_status}")
               exist = True
       if not exist:
           print("No record has been found.")

   def register_to_vote(self):
       license_num = input("Enter license number to register: ")
       found = False
       for license in self._driver_licenses_together:
           if license._license_number == license_num:
               if int(license._age) >= 18:
                   if license._voter_status == "N":
                       license._voter_status = "Y"
                       print(f"{license._last_name}, {license._first_name} has been registered to vote.")
                   else:
                       print(f"{license._last_name}, {license._first_name} is already registered to vote.")
                   found = True
               else:
                   print(f"{license._last_name}, {license._first_name} is not old enough to vote (must be 18 or older).")
                   found = True
       if not found:
           print("No record has been found with that license number.")

   def menu(self):
       print("Select an option:")
       print("1) Print all Drivers Info, sorted by drivers license numbers")
       print("2) Print all young, unregistered voters")
       print("3) Print drivers by last initial")
       print("4) Print drivers of a specific age")
       print("5) Quit")
       print("6) Register to vote")
       decision = input("Enter your choice: ")

       if decision == "1":
           self.mix_licenses()
           self.print_all_drivers_info()
       elif decision == "2":
           self.voting_age()
       elif decision == "3":
           self.by_letter()
       elif decision == "4":
           self.print_age()
       elif decision == "5":
           return False
       elif decision == "6":
           self.register_to_vote()
       else:
           print("Invalid Input")
       return True

   def run(self):
       while self.menu():
           pass
