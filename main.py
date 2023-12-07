import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)


# MY VERSION
# with open("./nato_phonetic_alphabet.csv") as file:
#     data = file.readlines()
#     data_1 = [words.strip() for words in data]
#     new = [tuple(word.split(",")) for word in data_1]
#     dict = {letter: code for (letter, code) in new}
#     del dict["letter"]
#     # print(dict)
