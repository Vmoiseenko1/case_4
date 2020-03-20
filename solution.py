# Case-study 6 "Generating of sentences"
# Developers: Vlasov V. (%)
#             Moiseenko V. (%)
# The aim: to develop a program for generating the number of offers from a file using Markov algorithms

import random
import re

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
def get_parts(f): #получить звенья
    with open(f) as f1:
        lines = f1.readlines()
    t = []
    text = []
    yn = []
    pov = []

    k = 1
    for i in lines:
        l = lines[k - 1].split()
        t.append(l)
        k += 1

    for e in t:
        for r in e:
            text.append(r)

    for q in text:
        n = text.count(q)
        if n == 1:
            yn.append(q)
        elif n != 1:
            pov.append(q)

    st = ''
    for j in text:
        st += j + ' '
    predl = re.split("\. ", st)
    lpredl = len(predl)
    if predl[lpredl - 1] == '':
        predl.remove(predl[lpredl - 1])

    part = ''
    g = 2
    ltext = len(text)
    for b in text:
        p = []
        co = text.count(b)
        if co == 1 and ltext >= g:
            p.append(text[g - 1])
            p = str(p)
            part += b + ' ' + p + '\n'
            g += 1
        elif co != 1 and ltext >= g:
            vrem = []
            for po in text:
                vrem.append(po)
            zx = vrem.count(b)
            while zx != 0:
                ind = vrem.index(b)
                p.append(vrem[ind + 1])
                vrem.pop(ind)
                zx -= 1
            p = str(p)
            part += b + ' ' + p + '\n'
            g += 1
    return part


# For Vlas:
def text_generating(): #сгенерировать текст
    pass


file = input('Имя файла: ')
text = check_text(file)
print(start_words(text))
print(check_text(file))
print(get_parts(file))
