'''
Author: Shero Baig
KUID: 3093709
Date: 9/29/22
Lab: lab03
Last modified: Date file was most recently modified
Purpose: User has to guess the secret word. The user will be told if they have guesses too many or too few letters.They will be told if they have typed the same amount of letters as the secret word. If they guess it right, they will be told that it is correct. They will also be told how many times it took them to guess the secret word. 
'''


word = "bringcoffee"

print("Guess the secret phrase!")

count = 0
while True:
  user_guess = input("Guess: ")
  user_guess = user_guess.lower()
  count += 1
  if len(user_guess) < 11:
    print("Too few characters")
  elif len(user_guess) > 11:
    print("Too many characters")
  else:
    if user_guess == word:
      print("Correct!")
      break
    incount = 0
    for i in range(11):
      if user_guess[i] == word[i]:
        incount += 1
      else:
        break
    print(f"Correct letters: {incount}")

print(f"Number of guesses: {count}")
