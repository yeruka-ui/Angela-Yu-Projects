import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:


    nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_alphabet_df = pandas.DataFrame(nato_alphabet)
    phonetic_dict = {row.letter:row.code for (index, row) in nato_alphabet_df.iterrows()}

def generate_code():
    user_input = input("Enter a word: ").upper()
    try:
        #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
        user_letters = list(user_input)
        word_dict = [phonetic_dict[letter] for letter in user_letters]
    except KeyError:
        print("Only letters in the alphabet!")
        generate_code()
    else:
        print(word_dict)

generate_code()