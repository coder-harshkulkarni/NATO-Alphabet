import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

no_error = True
while no_error:
    user_word = input("Enter the Word: ").upper()
    try:
        word_list = [nato_phonetic_alphabet[word] for word in user_word]
    except KeyError:
        print("Sorry, only letters in alphabets please.")
    else:
        no_error = False
        print(word_list)
