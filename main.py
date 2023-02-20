import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

user_word = input("Enter the Word: ").upper()
word_list = [nato_phonetic_alphabet[word] for word in user_word]
print(word_list)
