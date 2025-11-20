'''
betting.py: Ett betting system där du börjar med 1000 kr och du har 7 chanser att gissa fram ett tal mellan 1-100.

__author__  = "Philip Urhammar"
__version__ = "1.0.0"
__email__   = "philip.urhammar@elev.ga.dbgy.se"
'''

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# 1. Spelet ska själv slumpa ett tal (mellan 1-100) som är hemligt: random.randint(1, 100), man ska ha sju försök. Du får själv bestämma hur spelet ska se ut
import os
import random
import time
money = 1000 


while True:
    os.system('cls')
    print(bcolors.GREEN + f"__________        __    __  .__                                      .__               ")
    print(bcolors.GREEN + f"\______   \ _____/  |__/  |_|__| ____    ____     ____ _____    _____|__| ____   ____  ")
    print(bcolors.GREEN + f" |    |  _// __ \   __\   __\  |/    \  / ___\  _/ ___\\__  \  /  ___/  |/    \ /  _ \ ")
    print(bcolors.GREEN + f" |    |   \  ___/|  |  |  | |  |   |  \/ /_/  > \  \___ / __ \_\___ \|  |   |  (  <_> )")
    print(bcolors.GREEN + f" |______  /\___  >__|  |__| |__|___|  /\___  /   \___  >____  /____  >__|___|  /\____/ ")
    print(bcolors.GREEN + f"        \/     \/                   \//_____/        \/     \/     \/        \/        ")
    
    randomized = random.randint(1, 100)
    print(bcolors.BOLD + f"Du har {money} kr i saldot, du ska gissa rätt på ett tal mellan 1-100, du har sju försök")

    while True:
        try:
            bet = int(input(bcolors.GREEN + f"Hur mycket vill du betta?: "))      
            if bet > money:
                print(bcolors.RED + f"Du kan inte betta mer än vad du har på saldot, du har", money ,"på kontot")
            elif bet <= 0:
                print(bcolors.RED + f"Bet måste vara ett positivt tal, försök igen.")
            else:
                break
        except ValueError:
            print(bcolors.RED + f"Felaktig inmatning, skriv en siffra.")
            
    won = False
    attempt = 1
    while attempt < 8:
        try:
            print("-------------------------------")
            guess = int(input(f"Gissning {attempt}: "))
        except ValueError:
            print(bcolors.RED + f"-------------------------------")
            print(bcolors.RED + f"Felaktig inmatning, försök igen.")
            continue
        
        if not 1 <= guess <= 100:
            print(bcolors.RED + f"-------------------------------")
            print(bcolors.RED + f"Din gissning får inte vara mindre än 1 eller större än 100")
            continue
            
        if guess > randomized:
            print(bcolors.RED + f"För stort")
            attempt += 1
        elif guess < randomized:
            print(bcolors.BLUE + f"För litet")
            attempt += 1
        else:
            print(bcolors.GREEN + f"-------------------------------")
            print(bcolors.GREEN + f"Grattis! Du gissade rätt!")
            money += bet*2
            print("Du har nu ", money ,"kr på kontot")
            won = True
            break
            
    if not won:
        money -= bet
        print(bcolors.RED + f"--------------------------------------------------------------------------")
        print(bcolors.RED + f"Tyvärr, du gissade fel. Talet var {randomized}. Du har nu {money} kr")

    if money <= 0:
        print(bcolors.RED + f"Du kan inte spela igen då du har 0 kr på saldot. Tack för att du spelade!")
        time.sleep(2)
        os.system('cls')
        break 
    
    while True:
        restart = input(bcolors.GREEN + f"Spela igen? (J = Ja, N = Nej): ").upper()
        if restart == "N":
            print(bcolors.GREEN + f"Tack för att du spelade!")
            time.sleep(2)
            os.system('cls')
            break
        elif restart == "J":
            break
        else:
            print(bcolors.RED + f"Ogiltigt val. Svara med J eller N.")
            
    if restart == "N":
        break

# 8. Dokumentera hur det gick och vad du kunde göra bättre