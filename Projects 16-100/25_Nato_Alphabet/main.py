student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

in_app = True

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

with open("nato_phonetic_alphabet.csv", mode="r") as f: #apro il file in lettura
    content = f.readlines() #leggo ogni riga del file
    content = [line.replace("\n", "") for line in content[1:]] #tolgo "\n" da ogni elemento della lista
    content = [element.split(",") for element in content] # Separo ogni elemento in due sotto elementi usando come separatore la virgola e.g. ['A,Alfa', 'B, Bravo'] = [['A', 'Alfa], ['B', 'bravo']
    nato_phonetic_alphabet_dict = {letter: word for (letter, word) in content} #Costruisco il dizionario nel formato {'A': 'Alfa', 'B': 'Bravo'}

while in_app:

    try:
        user_string = input("Insert your words: ").upper()

        # Solution with list comprehension
        solution_string = [nato_phonetic_alphabet_dict[letter] for letter in user_string]
        print(solution_string)
        in_app = False

    except KeyError:
        print("You can insert only letters, please try again")


input("Press ENTER for quit the program ")