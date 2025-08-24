#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Seguendo le lezioni precedenti e la logica dietro la scrittura e la lettura in Python
# nonché la creazione di nuovi file sono riuscito a scrivere in automatico le nuove lettere

new_list = [] #creo una nuova lista, conterrà i nomi degli invitati

with open("./Input/Names/invited_names.txt", mode="r") as f: #apro il file "invited_names_txt" in modalità lettura
    list = f.readlines() #associo la lista dei nomi nella variabile "list"

#questo ciclo mi serve per sostituire "\n" (evito che ad ogni nome succeda l'andare a capo)
for name in list:
    new_name = name.replace("\n", "")
    new_list.append(new_name)

letter =  open("./Input/Letters/starting_letter.txt", mode="r") #apro il file "startin_letter_txt" in modalità lettura
content = letter.read() #associo il contenuto di "letter" nella variabile "content"
letter.close()

# con questo ciclo sostituisco la parte [name] con ogni nome della nuova lista
for name in new_list:
    new_content = content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/Letter to {name}.txt", mode="w") as file: # creo un file per ogni nuova lettera creata associandola al nome dell'invitato
        file.write(new_content)

