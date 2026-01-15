'''
Author: Shero Baig
KUID: 3093709
Date: 9/22/2022
Lab: lab02
Last modified: Date file was most recently modified
Purpose: Make a program of restaurant where the user can pick foods from the menu and will be given the cost of the order after.
'''



print("=================================")
print("WELCOME TO THE RESTAURANT")
print("=================================")

price={"cold pasta":50, "grilled cheese":70, "pie":20}

cost=0

discount=0

pie_count=0

cold_pasta=0

grilled_cheese=0

pie_cost=0

print("Do you want Cold Pasta (Y/N)")
x=input()
if x=='y' or x=='Y':
	print("Enter Quantity: ")
	y=int(input())
	if y<0:
		y=0
	cost+=y*price["cold pasta"]
	cold_pasta=y*price["cold pasta"]
print("Do you want Grilled Cheese (Y/N)")
x=input()
if x=='y' or x=='Y':
	print("Enter Quantity: ")
	y=int(input())
	if y<0:
		y=0
	cost+=y*price['grilled cheese']
	grilled_cheese=y*price['grilled cheese']
print("Do you want pie (Y/N)")
x=input()
if x=='y' or x=='Y':
	print("Enter Quantity: ")
	y=int(input())
	if y<0:
		y=0
	pie_count=y
	cost+=y*price['pie']
	pie_cost=y*price['pie']
print("Enter Age: ")
age = int(input())
if age >= 55:
	cost=cost+(cost*0.08)
	discount=(cost*0.08)
elif age <= 5:
	discount=pie_cost * price['pie']
	cost=cost+(cost*0.08)
else:
	cost=cost+(cost*0.08)
print("Cost of Cold Pasta")
print("$",cold_pasta)
print("Cost of Grilled Cheese")
print("$",grilled_cheese)
print("Cost of Pie")
print("$",pie_cost)
print("Cost is")
print("$",cost)
print("Discount is")
print("$",discount")
print(f"total: $(cost-discount:0.2f")

