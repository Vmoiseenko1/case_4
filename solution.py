# Case-study 4
# Developers: Vlasov V., Moiseenko V.
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
            lines[z] = lines[z].replace('\n', '')
            lines[z] = lines[z].replace(' .', '.')
            lines[z] = lines[z].replace(' !', '!')
            lines[z] = lines[z].replace(' ?', '?')
            lines[z] = lines[z].replace(' ,', ',')
        return lines

file = input('Имя файла: ')
print(check_text(file))

# For Victoria:
def start_words(): #получить список стартовых слов
    pass


# For Vlas:
def get_parts(): #получить звенья
    pass


# For Vlas:
def text_generating(): #сгенерировать текст
    pass