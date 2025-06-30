from shutil import which
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
game_data = [
    {"name": "Cristiano Ronaldo", "followers": 630_000_000, "description": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 520_000_000, "description": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 430_000_000, "description": "Singer & Actress", "country": "USA"},
    {"name": "Kylie Jenner", "followers": 410_000_000, "description": "Model & Entrepreneur", "country": "USA"},
    {"name": "Dwayne Johnson", "followers": 390_000_000, "description": "Actor & Wrestler", "country": "USA"},
    {"name": "Ariana Grande", "followers": 380_000_000, "description": "Singer", "country": "USA"},
    {"name": "Kim Kardashian", "followers": 360_000_000, "description": "Entrepreneur & TV Star", "country": "USA"},
    {"name": "Beyoncé", "followers": 320_000_000, "description": "Singer", "country": "USA"},
    {"name": "Khloé Kardashian", "followers": 310_000_000, "description": "TV Star", "country": "USA"},
    {"name": "Justin Bieber", "followers": 290_000_000, "description": "Singer", "country": "Canada"},
    {"name": "Nike", "followers": 290_000_000, "description": "Sports Brand", "country": "USA"},
    {"name": "Taylor Swift", "followers": 280_000_000, "description": "Singer", "country": "USA"},
    {"name": "Kendall Jenner", "followers": 280_000_000, "description": "Model", "country": "USA"},
    {"name": "Virat Kohli", "followers": 270_000_000, "description": "Cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "followers": 250_000_000, "description": "Singer & Actress", "country": "USA"},
    {"name": "Miley Cyrus", "followers": 210_000_000, "description": "Singer & Actress", "country": "USA"},
    {"name": "Zendaya", "followers": 190_000_000, "description": "Actress & Model", "country": "USA"},
    {"name": "Shakira", "followers": 170_000_000, "description": "Singer", "country": "Colombia"},
    {"name": "Billie Eilish", "followers": 110_000_000, "description": "Singer", "country": "USA"},
    {"name": "Drake", "followers": 140_000_000, "description": "Rapper", "country": "Canada"},
    {"name": "Cardi B", "followers": 160_000_000, "description": "Rapper", "country": "USA"},
    {"name": "Chris Hemsworth", "followers": 100_000_000, "description": "Actor", "country": "Australia"},
    {"name": "Emma Watson", "followers": 75_000_000, "description": "Actress", "country": "UK"},
    {"name": "Rihanna", "followers": 160_000_000, "description": "Singer & Entrepreneur", "country": "Barbados"},
    {"name": "LeBron James", "followers": 160_000_000, "description": "Basketball Player", "country": "USA"},
    {"name": "Gigi Hadid", "followers": 80_000_000, "description": "Model", "country": "USA"},
    {"name": "Zlatan Ibrahimović", "followers": 60_000_000, "description": "Footballer", "country": "Sweden"},
    {"name": "Camila Cabello", "followers": 65_000_000, "description": "Singer", "country": "USA/Cuba"},
    {"name": "Will Smith", "followers": 75_000_000, "description": "Actor", "country": "USA"},
    {"name": "David Beckham", "followers": 85_000_000, "description": "Footballer", "country": "UK"},
    {"name": "Lisa (BLACKPINK)", "followers": 100_000_000, "description": "K-pop Artist", "country": "Thailand"},
    {"name": "Jisoo (BLACKPINK)", "followers": 90_000_000, "description": "K-pop Artist", "country": "South Korea"},
    {"name": "Suga (BTS)", "followers": 65_000_000, "description": "K-pop Artist", "country": "South Korea"},
    {"name": "Tom Holland", "followers": 85_000_000, "description": "Actor", "country": "UK"},
    {"name": "Post Malone", "followers": 30_000_000, "description": "Singer", "country": "USA"},
    {"name": "Millie Bobby Brown", "followers": 65_000_000, "description": "Actress", "country": "UK"},
    {"name": "Kourtney Kardashian", "followers": 220_000_000, "description": "TV Star", "country": "USA"},
    {"name": "Blake Lively", "followers": 45_000_000, "description": "Actress", "country": "USA"},
    {"name": "Doja Cat", "followers": 35_000_000, "description": "Singer", "country": "USA"},
] #lista dei personaggi famosi dal quale il programma andrà a prendere casualmente le scelte
import random

def continuare():
    # definisco la funzione "continuare" per gestire l'utente che vuole fare un'altra partita
    cont = input("\nDo you want to do another game? (type 'y' or 'n'): ")
    if cont == "y":
        return True
    else:
        return False

while continuare():
    print(logo)
    print("Welcome to Higher or Lower game! ") #do il benvenuto/a all'interno del programma
    print("\nType A or B for choosing, let's go\n") #do indicazioni su cosa scrivere per andare avanti
    utente_perde = False # Inizializzo la variabile utente_perde. Mi servirà per determinare se l'utente perde
    score = 0 # inizializzo lo score dell'utente
    firs_person = random.choice(game_data)  # scelta random della prima celebrità
    print("A:", firs_person["name"] + ":", firs_person["description"]) #stampo il nome della prima persona e la sua descrizione
    second_person = random.choice(game_data)  # scelta random della seconda celebrità

    while firs_person == second_person:  # gestisco il fatto che la prima persona sia uguale alla seconda
        second_person = random.choice(game_data)  # in questo modo saranno sempre diverse
    right_answer = [] #Inizializzo la variabile right_answer. La rendo lista per gestire un eventuale pareggio

    #scelta della seconda persona da comparare
    while not utente_perde: # condizione ciclica finché l'utente non perde, riprendo la variabile utente_perde.
        second_person = random.choice(game_data)
        # gestisco la risposta corretta in termini di follower
        if firs_person["followers"] > second_person["followers"]: #se la prima è maggiore della seconda
            right_answer = ["a"]
        elif second_person["followers"] > firs_person["followers"]: #se la seconda è maggiore della prima
            right_answer = ["b"]
        elif second_person["followers"] == firs_person["followers"]: #se sono uguali
            right_answer = ["a","b"]

        print(vs)
        print("B:",second_person["name"]+":",second_person["description"])

        scelta = input("\nWho has more followers? Type 'A' or 'B': ").lower() #Gestione della scelta dell'utente. Da qui torna utile la variabile right_answer come lista
        if scelta in right_answer: #dico che se la scelta fatta dall'utente è contenuta nella lista delle risposte corrette
            score += 1 #aggiungo uno allo score
            print("\n"*30) #lascio uno spazio di 30 righe in modo che sembri resettare tutto il programma e cambiasse pagina
            print(logo)
            print(f"You're right! Current score: {score}.\n") #stampo l'informazione di vittoria con relativo punteggio "score"
            print("A:", second_person["name"] + ":", second_person["description"])
            second_person = firs_person # questa è la parte fondamentale del ciclo in quanto ho bisogno che la seconda persona diventi la prima per farla restare all'interno delle variabili
            # senza questo passaggio sarebbe impensabile fare un paragone tra una persona nuova e la vincitrice delle precedenti.


        else: # se la risposta non è contenuta all'interno della lista right_answer --> risposta sbagliata
            print(f"\nSorry, that's wrong. Final score: {score}") # stampo l'informazione di sconfitta con relativo punteggio "score"
            utente_perde = True # cambio la variabile utente_perde per farlo uscire dal ciclo while di richiesta risposte per confronto e farlo entrare in "continuare()"



