'''
Author: Shero Baig
KUID: 3093709
Date: 10/06/22
Lab: lab04
Last modified: Date file was most recently modified
Purpose: Helping user make a grocery list
'''



grocery = []

while True:
    print("\nWelcome to your shopping List!")
    print("1) Add item")
    print("2) Check off item")
    print("3) Print list")
    print("4) Exit")
    choice = int(input("Enter a choice: "))

    if choice == 1:
        item = input("What will you add to the list?: ")
        grocery.append(item)

    elif choice == 2:
        index = int(input("Enter the index of the item: "))
        if 1 <= index <= len(grocery):
            index = index - 1
            temp = ""
            for i in range(len(grocery[index])):
                if i == 0 or i == len(grocery[index]) - 1:
                    temp += grocery[index][i]
                else:
                    temp += "-"
            grocery[index] = temp
            print("Check off is successful !")

    elif choice == 3:
        print("Items in the grocery list are : ", end="")
        print(grocery)

    elif choice == 4:
        print("Exiting...")
        break
