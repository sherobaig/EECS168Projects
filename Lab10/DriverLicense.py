'''
Author: Shero Baig
KUID: 3093709
Date: 12/08/22
Lab: lab010
Last modified: Date file was most recently modified
Purpose: Creating a Driverlicense class
'''





class DriverLicense:
   def __init__(self, first_name, last_name, age, voter_status, license_number):
       self._first_name = first_name
       self._last_name = last_name
       self._age = age
       self._voter_status = voter_status
       self._license_number = license_number

   def __lt__(self, other):
       return self._license_number < other._license_number

   def __gt__(self, other):
       return self._license_number > other._license_number

   def __le__(self, other):
       return self._license_number <= other._license_number

   def __ge__(self, other):
       return self._license_number >= other._license_number

   def __eq__(self, other):
       return self._license_number == other._license_number

   def __ne__(self, other):
       return self._license_number != other._license_number

   def __str__(self):
       return f"{self._first_name} {self._last_name} is {self._age} years old and has a {self._voter_status} voter status. Their license number is {self._license_number}."

   def __repr__(self):
       return f"DriverLicense('{self._first_name}', '{self._last_name}', {self._age}, '{self._voter_status}', {self._license_number})"

