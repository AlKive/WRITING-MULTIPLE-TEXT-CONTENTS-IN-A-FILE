# BABIERA,ALEXA | CMPE-103-MODULE-2-FILE-HANDLING-IN PYTHON | PROGRAMMING EXERCISE 2
# A method in python to write multiple line of text contents into a text file

#import necessary modules
from pyfiglet import figlet_format
import pygame
from termcolor import colored
import pyfiglet
from colorama import Back, Fore, Style, init
import time

# formatting the header
art = figlet_format(" Writing Multipe Lines into a File", font='digital', width=250)
c_art = colored(art, 'yellow')

print(Fore.MAGENTA + "━༻❁༺━༻❁༺━༻❁༺━" * 7)
for line in c_art.split("\n"):
    print(line.center(80))
print(Fore.MAGENTA + "━༻❁༺━༻❁༺━༻❁༺━" *7 )

with open("mylife.txt", "w") as user_line:
   while True:
        enter_again = input(Fore.LIGHTCYAN_EX + "Do you want to add lines (YES or NO) ? : " + Fore.LIGHTYELLOW_EX)
        user_line.write("Do you want to add lines (YES or NO) ? : " + str(enter_again) + "\n")

        if enter_again.upper() == "YES": 
            user_input = input(Fore.LIGHTGREEN_EX + "Type in a phrase or sentence: " + Fore.YELLOW)
            user_line.write("Type in a phrase or sentence: " + str(user_input) + "\n")
            continue

        elif enter_again.upper() == "NO" :
            print (Fore.RED + "The program has ended~")
            exit()
      
        elif enter_again.lower() == "y" or enter_again.lower() == "n":
            print(Fore.RED + "Please enter only YES or NO")
               
        else:
            print(Fore.RED + "ERROR! Invalid input.") 
            break