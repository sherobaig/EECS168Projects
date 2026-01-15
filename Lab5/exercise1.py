'''
Author: Shero Baig
KUID: 3093709
Date: 10/19/2022
Lab: lab05
Last modified: Date file was most recently modified
Purpose: This program is a Web history simulator and the purpose of it is so the user can keep track of their web history and which is older and newer. 
'''
history = []


index = -1
while(True):
    user_input = input("Command: ")
    instruction = user_input.split(" ")
    if(instruction[0] == "NAVIGATE"):
        index += 1
        history = history[0:index]
        history.append(instruction[1])
    elif(instruction[0] == "BACK"):
        if(index > 0):
            index -= 1
    elif(instruction[0] == "FORWARD"):
        if (index < len(history) - 1):
            index += 1
    elif(instruction[0] == "HISTORY"):
        print("Oldest")
        print("============")
        for elem, val in enumerate(history):
            if(elem == index):
                print(val + " <==")
            else:
                print(val)
        print("============")
        print("Newest")
    elif(instruction[0] == "EXIT"):
        break
