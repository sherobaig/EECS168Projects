'''
Author: Shero Baig
KUID: 3093709
Date: 10/06/22
Lab: lab04
Last modified: Date file was most recently modified
Purpose: Have user open two files and compare the lists in the files in different ways
''' 
try:

	file_one = input("Enter name of first data file: ")
	file_two = input("Enter name of second data file: ")

	nums_one = open(file_one, "r")
	nums_two = open(file_two, "r")
	list_one  = []
	list_two = []
	for line in nums_one :
		list_one.append(int(line.strip()))
	for line in nums_two:
		list_two.append(int(line.strip()))

	nums_one.close()
	nums_two.close()

	print("\n\nList Statistics:")

	if sum(list_one) > sum(list_two):
		print("The first list has the larger sum of", sum(list_one))
	else:
		print("The second list has the larger sum of", sum(list_two))

	if (sum(list_one)/len(list_one)) > (sum(list_two)/len(list_two)):
		print("The first list has the larger average of %.1f"%(sum(list_one)/len(list_one)))
	else:
		print("The second list has the larger average of %.1f"%(sum(list_two)/len(list_two)))

	count = 0
	for value in list_one:
		if value in list_two:
			count = count + 1
	print("Count of values that appear in both lists:", count)

	isPalindrome = True

	if len(list_one) == len(list_two):

		for i in range(len(list_one)):
			if value != list_two[len(list_two)-i-1]:
				isPalindrome = False
		if isPalindrome:
			print("The lists are palindromes")
		else:
			print("The lists are not palindromes")
	else:
		print("The lists are not palindromes")
except Exception as ex:
	print(ex)

