import pandas
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_data = pandas.DataFrame(data)

alphabet_code = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}
print(alphabet_code)


def generate_alphabet():
    word = input("Please type a word: ").upper()
    try:
        new_code = [alphabet_code[letter] for letter in word]
    except KeyError:
        print("Please enter a valid letter")
        generate_alphabet()
    else:
        print(new_code)


generate_alphabet()
