
kontostand = [150]

def menu():
    print("\n--Bank System V.1.0--\n")
    print(f"AKTUELLRE KONTOSTAND: {kontostand}")
    
    options = """
    Aktuellere Kontosta
    1 = Geld einzahlen
    2 = Geld abheben
    """

    print(f"Wähle deine Option: {options}")
    user_input = input(">> ")
    
    if user_input == "1":
        option_1()


def option_1():
    print("Wieviel Geld möcchtest du Einzahlen? ")
    user_input = input("Betrag: ")

    kontostand.append(user_input)
    
    print(f"aaaa: ", *kontostand)
    
menu()

#--notes--
#list: var speichern + wert ändern mit user input
#mit index arbeiten? 0-10+?