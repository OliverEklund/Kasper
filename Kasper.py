
print("räkna upp från 1 och när man kommer till ett tal som är delbart/innehåller 7 eller 11 då skriver man 0, man får inte säga siffran. ")

Number_before = 0

print("/")

round_status = True
while round_status == True:
    print("Skriv Nummret")
    player_number = input()

    P = int(player_number)
    
    if P == Number_before + 1:
        print(f" Du sa {P}. Och nummret är nu {P}")

    if P%7 == 0 or P%11 == 0:
        if P == 0:
            print(f"Du skippade det olagliga nummret. Du sa {P}")
            
        else:
            print(f"Du skrev ett olagligt nummer, du sa {P}.")
            Number_before = 0

    if P != Number_before + 1:
        if P%7 == 0 or P%11 == 0:
            if P == 0:
                print("Fortsätt")
        else:
            print("Du skrev fel, börja om")
            Number_before = 0
    
    Number_before = Number_before + 1
