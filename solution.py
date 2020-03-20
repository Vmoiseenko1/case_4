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
def get_parts(f):
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

#For Vlas:
def start_words(file): #получить список стартовых слов
    with open(file) as f1:
        lines = f1.readlines()
    t = []
    text = []

    k = 1
    for i in lines:
        l = lines[k - 1].split()
        t.append(l)
        k += 1

    for e in t:
        for r in e:
            text.append(r)

    st = ''
    for j in text:
        st += j + ' '
    predl = re.split("\. ", st)
    lpredl = len(predl)
    if predl[lpredl - 1] == '':
        predl.remove(predl[lpredl - 1])

    start = []
    for y in predl:
        n = y.find(' ')
        word = y[0:n]
        start.append(word)
    return start

#For Vlas:
def text_generating(file):
    with open(file) as f1:
        lines = f1.readlines()
    t = []
    text = []

    k = 1
    for i in lines:
        l = lines[k - 1].split()
        t.append(l)
        k += 1

    for e in t:
        for r in e:
            text.append(r)

    st = ''
    for j in text:
        st += j + ' '
    predl = re.split("\. ", st)
    lpredl = len(predl)
    if predl[lpredl - 1] == '':
        predl.remove(predl[lpredl - 1])

    word = []
    for y in predl:
        w = y.count(' ') + 1
        word.append(w)


    zven = get_parts(file)
    start = start_words(file)

    COLpred = len(word)

    zv = zveno(zven)

    with open('pro.txt') as f1:
        line = f1.readlines()

    z = []
    for i in line:
        z.append(i)

    ans = ''
    while COLpred != 0:
        stw = random.choice(start)
        ans += stw + ' ' + '\n'
        cols = random.choice(word)
        while cols != 0:
            ranSTR = random.choice(z)
            ranslov = ranSTR[0:ranSTR.find(' ')]
            le = len(ranSTR)
            ranOSt = ranSTR[ranSTR.find(' ') + 1:le]

            rez = []
            slovo = ''
            ranOSt = ranOSt[2:]

            for i in ranOSt:
                if i != "'" and i != ' ' and i != ']' and i != ',':
                    slovo += i
                elif i == "'":
                    rez.append(slovo)
                    slovo = ''

            for i in rez:
                if i == '':
                    rez.remove('')
            lDOp = len(rez)
            ans += ranslov + ' '
            while lDOp != 0:
                randDOP = random.choice(rez)
                ans += randDOP + ' '
                lDOp -= 1
            cols -= 1
        COLpred -= 1
    return ans


def zveno(z):
    fo = open('pro.txt', 'w')
    fo.write(z)
    fo.close()
    return fo


file = input('Имя файла: ')
print(text_generating(file))