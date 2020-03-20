# Case-study 6 "Generating of sentences"
# Developers: Vlasov V. (%)
#             Moiseenko V. (%)
# The aim: to develop a program for generating the number of offers from a file using Markov algorithms

import random

# For Victoria:
def check_text(file): # to check the text
    with open(file) as file1:
        lines = file1.readlines()
        symbols = ['@', '#', '$', '%', '^', '&', '*', '(', ')']
        for symbol in symbols:
            for i in range(len(lines)):
                lines[i] = lines[i].replace(symbol, '')
        for z in range(len(lines)):
            lines[z] = lines[z].replace('\n', ' ')
            lines[z] = lines[z].replace(' .', '.')
            lines[z] = lines[z].replace(' !', '!')
            lines[z] = lines[z].replace(' ?', '?')
            lines[z] = lines[z].replace(' ,', ',')
        return lines

# For Victoria:
def start_words(text): #получить список стартовых слов
    start_words = []
    for word in text:
        lst = word.split()
        for w in lst:
            start_words.append(w)
    return start_words

# For Vlas:
def get_parts(): #получить звенья
    pass


# For Vlas:
def text_generating(): #сгенерировать текст
    pass


file = input('Имя файла: ')
text = check_text(file)
print(start_words(text))
print(check_text(file))
