'''
Author: Shero Baig
KUID: 3093709
Date: 9/29/22
Lab: lab03
Last modified: Date file was most recently modified
Purpose: A program that tells the user how many sick people there are with the flu on a day the user types. 
'''


def sick_count(day):
    if day<1:
        return 0
    elif day==1:
        return 1
    elif day==2:
        return 4
    elif day==3:
        return 64
    else:

        return sick_count(day-1)+sick_count(day-2)+sick_count(day-3)


day=int(input("What day do you want a sick count for?: "))
print(day)
if day<1:
    print("Invalid day")
else:
    print("Total people with flu: ",sick_count(day))
