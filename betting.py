'''
app.py: Ett betting system där du börjar med 1000 kr och du har 7 chanser att gissa fram ett tal mellan 1-100.

__author__  = "Philip Urhammar"
__version__ = "1.0.0"
__email__   = "philip.urhammar@elev.ga.dbgy.se"
'''
# 1. Spelet ska själv slumpa ett tal (mellan 1-100) som är hemligt: random.randint(1, 100), man ska ha sju försök. Du får själv bestämma hur spelet ska se ut
import os
import random

money = 1000 


while True:
    os.system('cls')
    print("__________        __    __  .__                                      .__               ")
    print("\______   \ _____/  |__/  |_|__| ____    ____     ____ _____    _____|__| ____   ____  ")
    print(" |    |  _// __ \   __\   __\  |/    \  / ___\  _/ ___\\__  \  /  ___/  |/    \ /  _ \ ")
    print(" |    |   \  ___/|  |  |  | |  |   |  \/ /_/  > \  \___ / __ \_\___ \|  |   |  (  <_> )")
    print(" |______  /\___  >__|  |__| |__|___|  /\___  /   \___  >____  /____  >__|___|  /\____/ ")
    print("        \/     \/                   \//_____/        \/     \/     \/        \/        ")
    
    randomized = random.randint(1, 100)
    print(f"Du har {money} kr i saldot, du ska gissa rätt på ett tal mellan 1-100, du har sju försök")

    while True:
        try:
            bet = int(input("Hur mycket vill du betta?: "))      
            if bet > money:
                print("Du kan inte betta mer än vad du har på saldot, du har", money ,"på kontot")
            elif bet <= 0:
                print("Bet måste vara ett positivt tal, försök igen.")
            else:
                break
        except ValueError:
            print("Felaktig inmatning, skriv en siffra.")

    won = False
    for attempt in range(1, 8):
        try:
            guess = int(input(f"Gissning {attempt}: "))
        except ValueError:
            print("Felaktig inmatning, försök igen.")
            continue
        if guess > randomized:
            print("Din gissning är större än talet")
        elif guess < randomized:
            print("Din gissning är mindre än talet")
        else:
            print("Grattis! Du gissade rätt!")
            money += bet
            print("Grattis, du har nu ", money ,"kr")
            won = True
            break
    if not won:
        money -= bet
        print(f"Tyvärr, du gissade fel. Du har nu {money} kr")

    restart = input("Spela igen? (Enter = Ja, N = Nej)")
    if restart == "n":
        print("Tack för att du spelade!")
        break
    else:
        continue

# 8. Dokumentera hur det gick och vad du kunde göra bättre