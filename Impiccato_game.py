import random
import sys

# Questi sono tutti gli step della grafica dell'impiccato
# Si tratta di una lista che va dall'indice 0 all'indice 6
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# Mi sono fatto generare dalla AI delle parole casuali in italiano e l'ho inserite dentro la lista 'word_list'
word_list = [
    "CANE", "GATTO", "SCUOLA", "PIZZA", "FIUME",
    "LUNA", "MARE", "SOLE", "PENNA", "LIBRO",
    "MONTAGNA", "ALBERO", "GIARDINO", "TELEFONO", "BICICLETTA",
    "TAVOLO", "SEDIA", "PORTA", "SCARPA", "NUVOLA",
    "CIELO", "VULCANO", "STELLA", "CUORE", "CARTA",
    "CALCIO", "FESTA", "VETRO", "SAPONE", "FIORE",
    "CITTÀ", "STRADA", "CAMPANA", "FANTASMA", "ANELLO",
    "ZAINO", "QUADERNO", "MATITA", "GOMMA", "RIGA",
    "COLLA", "FORBICI", "BOTTIGLIA", "TAPPETO", "DIVANO",
    "CUCINA", "FRIGORIFERO", "FORNO", "LAVATRICE", "SPECCHIO",
    "FINESTRA", "MURO", "PAVIMENTO", "LAMPADA", "OMBRELLO",
    "OROLOGIO", "CAVALLO", "MUCCA", "PECORA", "GALLINA",
    "UCCELLO", "PESCE", "RANA", "TARTARUGA", "LEONE",
    "TIGRE", "ELEFANTE", "SCIMMIA", "CANGURO", "ORSO",
    "FOCA", "BALENA", "DELFINO", "AEREO", "TRENO",
    "NAVE", "MACCHINA", "MOTO", "AUTOBUS", "TRATTORE",
    "SEMAFORO", "PIETRA", "SABBIA", "TERRA", "FOGLIA",
    "RAGNO", "FARFALLA", "APE", "FORMICA", "LUCCIOLA",
    "FRUTTO", "MELA", "PERA", "BANANA", "ARANCIA",
    "LIMONE", "ANGURIA", "CILIEGIA", "FRAGOLA", "PESCA",
    "PRUGNA", "UVA", "ZUCCHERO", "SALE", "PEPE",
    "PASTA", "RISO", "PANE", "LATTE", "FORMAGGIO",
    "BURRO", "OLIO", "CARNE", "PESCE", "UOVO",
    "INSALATA", "CIPOLLA", "PATATA", "POMODORO", "CAROTA",
    "CAVOLFIORE", "ZUCCHINA", "MELANZANA", "PEPERONE", "ZUCCA",
    "GIACCA", "MAGLIA", "PANTALONE", "CALZA", "CAPPELLO",
    "GUANTO", "SCIARPA", "CINTURA", "OCCHIALI", "ZAPPA"
]

# Definisco una variabile che mi servirà successivamente per stampare lo status dell'impiccato
stage_status = 6

# faccio scegliere una parola random dal programma
chosen_word = random.choice(word_list)

#definisco la variabile placeholder e all'interno della variabile aggiungo tanti "_" quante sono le lettere dalla parola random
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += " _"

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')
print("\nWelcome to hangman game!\n")
print("This is the word to guess:\n ")
# stampo placeholder
print(placeholder)

# inizializzo la veriabile display che utilizzerò dopo la scelta della lettera da parte dell'utente
display = ["_"] * len(chosen_word)

# Inizializzo la lista delle lettere sbagliate per farla stampare
wrong_letter = []

# Il ciclo continua finché "_" è presente nella variabile "display" (cioè la grafica che verrà mostrata all'utente e.g. A____O)
# Logicamente finché "_" è presente significa che la parola non è stata indovinata
life = 7
print(f"\nYou have {life} lives... good luck!\n")
while "_" in display:

    #chiedo all'utente la lettera e inizializzo la variabile "guess"
    print("\n----------------------------------------------------------------------------------------------------------")
    print(f"You have {life}/7 lives left")
    guess = input("\nChoose a letter: ").upper()
    print("\n")

    # inserisco la condizione che se l'utente digita l'intera parola corretta allora vince e la partita termina
    if guess == chosen_word:
        print(f"RIGHT! The word was {chosen_word}... YOU WIN!!\n")
        display = chosen_word
        exit()
    else:
        # il ciclo mette a confronto le lettera della parola con quella digitata dall'utente
        # se la lettera è uguale sostituisce al simbolo "_" la lettera scelta altrimenti lascia "_"
        # e.g. parola random = mela --> _ _ _ _
        # digito "a" --> _ _ _ a
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

    # se la lettera non è contenuta ci sono possibilità
    if guess not in chosen_word:

        # 1) l'utente ha terminato le vite perché lo status dell'impiccato è arrivato a 0 ( lo stato finale, corrispondente al primo indice della lista "stages" )
        if stage_status == 0:

            #in questo caso stampa l'ultimo stadio della grafica e il gioco termina
            print(stages[0])
            print(f"\nThe word was {chosen_word}\nYOU LOSE...\n")
            exit()

        # 2) l'utente ha ancora altre vite quindi il gioco continua
        # la lettera errato viene inserita dentro la lista wrong_letter e verrà stampa e lo stadio dell'impiccato avanzerà di uno
        else:
            if guess in wrong_letter:
                print(stages[stage_status])
                print("Wrong letters you chose", wrong_letter,"\n")
                life -= 1
            else:
                wrong_letter.append(guess)
                print(stages[stage_status])
                print("Wrong letters you chose", wrong_letter,"\n")
                stage_status -= 1
                life -= 1

    # stampa della varibile display
    print(" ".join(display))

# se "_" non è presente all'interno di display significa che l'utente ha vinto e il gioco termina
print(f"\nThe word was {chosen_word}\nYOU WIN!!!\n")
input("\nPremi INVIO per chiudere...")
