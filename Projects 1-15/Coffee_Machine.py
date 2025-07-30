from re import search

#Inzializzo la variabile MENU: contiene tutte le voci che l'utente può scegliere
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Inizializzo la variabile resources per indicare quante risorse sono presenti all'interno della macchinetta
resources = {
    "water": 2000,
    "milk": 1000,
    "coffee": 100,
}

def utente_scelta():
    """
    ritorna la scelta dell'utente tra le quattro possibili variabili (espresso, latte, cappuccino, report)
    La funziona finché l'intput dell'utente è diverso da una delle 4 opzioni non procede oltre
    """
    scelta = ""
    while scelta != "espresso" and scelta != "latte" and scelta != "cappuccino" and scelta != "report" and scelta != "price" and scelta != "recharge":
        scelta = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    return scelta

def inserisci_monete():

    """
    Chiede quante monete ha inserito e restituisce il totale del denaro inserito
    """
    totale_soldi = 0
    print("Please insert coin")
    totale_soldi += 0.1 * int(input("How many €0.10? "))
    totale_soldi += 0.2 * int(input("How many €0.20? "))
    totale_soldi += 0.5 * int(input("How many €0.50? "))
    totale_soldi += 1.0 * int(input("How many €1? "))
    totale_soldi += 2.0 * int(input("How many €2? "))
    return totale_soldi

def recharge_machine():
    a = ""
    print("\nInsert the amount of resources do you want to add into coffee machine")
    while a != "coffee" and a != "milk" and a != "water":
        a = input("Please type the risource (latte, water, coffee): ").lower()
    return a


# Inizializzo le variabili (water, coffee, milk) saranno poi utili per stampare il report e verificare che tutti gli ingredienti ci siano
acqua_rimanente = resources["water"]
caffe_rimanente = resources["coffee"]
latte_rimanente = resources["milk"]

costo_espresso = MENU["espresso"]["cost"]
costo_latte = MENU["latte"]["cost"]
costo_capuccino = MENU["cappuccino"]["cost"]
ingredienti = False #inizializzo la variabile che mi permetterò di continuare a chiedere opzioni all'utente finché ci saranno tutti gli ingredienti
soldi = 0 #  inizializzo la variabile soldi
print("\nPlease insert the right input below:\n'Espresso'\n'Latte'\n'Cappuccino'\n'Report' - check the resources"
      "\n'Price' - check the menu prices\n'Recharge' - add resources into the machine\n")
while not ingredienti:
    scelta_utente = utente_scelta()

    # Scelta dell'espresso dall'utente
    if scelta_utente == "espresso":
        acqua_da_usare = MENU["espresso"]["ingredients"]["water"] #verifico quanti ingredienti sono da usare
        caffe_da_usare = MENU["espresso"]["ingredients"]["coffee"]

        if acqua_rimanente < acqua_da_usare:
            print("Sorry, there isn't enough water ")
            ingredienti = True
        elif caffe_rimanente < caffe_da_usare:
            print("Sorry, there isn't enough coffee ")
            ingredienti = True
        else:
            soldi_inseriti = inserisci_monete()
            if soldi_inseriti >= costo_espresso:
                resto = soldi_inseriti - costo_espresso
                soldi += costo_espresso
                print(f"Here is €{resto:.2f} in change.")
                print("Here is your espresso ☕️. Enjoy!")
                acqua_rimanente -= acqua_da_usare
                caffe_rimanente -= caffe_da_usare

    # Scelta del latte dall'utente
    elif scelta_utente == "latte": # se l'utente sceglie il latte
        acqua_da_usare = MENU["latte"]["ingredients"]["water"]
        caffe_da_usare = MENU["latte"]["ingredients"]["coffee"]
        latte_da_usare = MENU["latte"]["ingredients"]["milk"]
        if acqua_rimanente < acqua_da_usare:
            print("Sorry, there isn't enough water ")
            ingredienti = True
        elif caffe_rimanente < caffe_da_usare:
            print("Sorry, there isn't enough coffee ")
            ingredienti = True
        elif latte_rimanente < latte_da_usare:
            print("Sorry, there isn't enough milk")
            ingredienti = True
        else:
            soldi_inseriti = inserisci_monete()
            if soldi_inseriti >= costo_latte:
                resto = soldi_inseriti - costo_latte
                soldi += costo_latte
                print(f"Here is €{resto:.2f} in change.")
                print("Here is your latte ☕️. Enjoy!")
                acqua_rimanente -= acqua_da_usare
                caffe_rimanente -= caffe_da_usare
                latte_rimanente -= latte_da_usare

    # Scelta del cappuccino dall' utente
    elif scelta_utente == "cappuccino":
        acqua_da_usare = MENU["cappuccino"]["ingredients"]["water"]
        caffe_da_usare = MENU["cappuccino"]["ingredients"]["coffee"]
        latte_da_usare = MENU["cappuccino"]["ingredients"]["milk"]
        if acqua_rimanente < acqua_da_usare:
            print("Sorry, there isn't enough water ")
            ingredienti = True
        elif caffe_rimanente < caffe_da_usare:
            print("Sorry, there isn't enough coffee ")
            ingredienti = True
        elif latte_rimanente < latte_da_usare:
            print("Sorry, there isn't enough milk")
            ingredienti = True
        else:
            soldi_inseriti = inserisci_monete()
            if soldi_inseriti >= costo_capuccino:
                resto = soldi_inseriti - costo_capuccino
                soldi += costo_capuccino
                print(f"Here is €{resto:.2f} in change.")
                print("Here is your cappuccino ☕. Enjoy!")
                acqua_rimanente -= acqua_da_usare
                caffe_rimanente -= caffe_da_usare
                latte_rimanente -= latte_da_usare

     # Se l'utente inserisce "price"
    elif scelta_utente == "price":
        print(f"\nespresso: €{costo_espresso}\nlatte: €{costo_latte}\ncappuccino: €{costo_capuccino}\n")

    # L'utente scrive report
    elif scelta_utente == "report":
        print(f"\nWater: {acqua_rimanente}ml\nCoffee: {caffe_rimanente}g\nMilk: {latte_rimanente}ml\nMoney: €{soldi:.2f}\n")

    elif scelta_utente == "recharge":
        resource = recharge_machine()
        if resource == "coffee":
            caffe_rimanente += int(input("\nHow much coffee: g "))
        elif resource == "milk":
            latte_rimanente += int(input("\nHow much milk: ml "))
        else:
            acqua_rimanente += int(input("\nHow much water: ml "))


