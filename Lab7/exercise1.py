'''
Author: Shero Baig
KUID: 3093709
Date: 11/03/22
Lab: lab07
Last modified: Date file was most recently modified
Purpose: Do some processing of a file on the entire constitution
'''
def build_count(text):
   counts_build = {}
   for word in text:
       clean = clean_word(word).lower()
       if clean.lower() in counts_build:
           counts_build[clean] += 1
       else:
           counts_build[clean] = 1

   return counts_build



def clean_word(word):
 
    cleaned_word = ""
    clean_list = ['!', '?', ':', ';', ',', '|', '.', '[', ']', '(', ')', '--', '\n']

    for i in word: 
        if i not in clean_list :
            cleaned_word += i 

    
    cleaned_word = cleaned_word.lower()

    
    return cleaned_word



def unique_words(word_counts):
   unique_list = []
   for key in word_counts:
       if word_counts[key] == 1:
           unique_list.append(key)

   return unique_list


def main():
   print("========Welcome to the word counter!========")
   file_name = input("Enter a file name: ")
   print(f"The file {file_name} has been processed.")
   file = open(file_name, 'r')
   word_list = file.read().split()

   word_data = open('word_data.txt', 'w')
   word_data.write("\n".join(f"{s}: {t}" for s, t in build_count(word_list).items()))
   word_data.close()

   unique_word = open('unique_words.txt', 'w')
   unique_word.write("\n".join(s for s, t in build_count(word_list).items() if t == 1))
   unique_word.close()

   print("Output stored in word_data.txt and unique_words.txt")
   input("Exiting...")


main()

