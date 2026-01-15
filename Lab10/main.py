'''
Author: Shero Baig
KUID: 3093709
Date: 12/08/22
Lab: lab010
Last modified: Date file was most recently modified
Purpose: Creating the main that runs the program
'''
from DMV import DMV
def main():
   file_name = input("Put in a file name: ")
   my_dmv = DMV(file_name)
   my_dmv.run()

if __name__ == "__main__":
   main()

