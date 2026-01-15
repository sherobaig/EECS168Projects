'''
Author: Shero Baig
KUID: 3093709
Date: October 27th 2022
Lab: lab06
Last modified: Date file was most recently modified
Purpose: Allows user to
1) Count digits
2) Sum digits
3) Is Palindrome
4) Reverse 
5) Exit 

'''


def last_digit(num):
    return num % 10


def remove_last_digit(num):
    return int(num / 10)


def add_digit(current_num, new_digit):
    current_num = str(current_num) + str(new_digit)
    return int(current_num)


def reverse(num):
    r_num = 0
    while num != 0:
        digit = last_digit(num)
        r_num = r_num * 10 + digit
        num = remove_last_digit(num)
    return r_num



def is_palindrome(num):
    t = num
    r_num = 0
    while num != 0:
        digit = last_digit(num)
        r_num = r_num * 10 + digit
        num = remove_last_digit(num)
    return r_num == t



def count_digits(num):
    if num == 0:
        return 1
    count = 0
    num = abs(num)
    while num != 0:
        num = remove_last_digit(num)
        count += 1
    return count



def sum_digits(num):
    digit_sum = 0
    num = abs(num)
    while num != 0:
        digit = last_digit(num)
        digit_sum = digit_sum + digit
        num = remove_last_digit(num)
    return digit_sum



def print_menu():
    print("1) Count digits")
    print("2) Sum digits")
    print("3) Is Palindrome")
    print("4) Reverse")
    print("5) Exit")


def main():
    while True:
        print_menu()
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue
        if choice == 1:
            number = int(input("Enter a whole number: "))
            print("Digits Count = " + str(count_digits(number)))
        elif choice == 2:
            number = int(input("Enter a whole number: "))
            print("Digits Sum = " + str(sum_digits(number)))
        elif choice == 3:
            number = int(input("Enter a whole number: "))
            print("Is Palindrome = " + str(is_palindrome(abs(number))))
        elif choice == 4:
            number = int(input("Enter a whole number: "))
            print("Reverse Number = " + str(reverse(abs(number))))
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Please enter a number from 1 to 5.")


main()

