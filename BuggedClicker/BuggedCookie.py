import os
from colorama import Fore, Back, Style
score = -1
result = "ja"
while(result):    
    os.system("cls")    
    print(Fore.BLUE+"           _/o\/ \_         ")
    print("  .-.   .-` \_/\o/ '-.      ")
    print(" /:::\ / ,_________,  \     ")
    print("/\:::/ \  '. (:::/  `'-;    ")
    print("\ `-'`\ '._ `''''\__    \   ")
    print(" `'-.  \   `)-=-=(  `,   |  ")
    print("     \  `-'`      `'-'   /  ")
    print("                            ")
    score += 1
    print(Fore.GREEN +"je score is "+ str(score))
    result = str(input(Fore.BLUE + "wil je klikken?") or "ja")    
os.system("cls")
print(Fore.RED + "GAME OVER")
print(Fore.BLUE+"           _/o\/ \_         ")
print("  .-.   .-` \_/\o/ '-.      ")
print(" /:::\ / ,_________,  \     ")
print("/\:::/ \  '. (:::/  `'-;    ")
print("\ `-'`\ '._ `''''\__    \   ")
print(" `'-.  \   `)-=-=(  `,   |  ")
print("     \  `-'`      `'-'   /  ")
print("                            ")
print(Fore.GREEN + "je eindscore is " + str(score))