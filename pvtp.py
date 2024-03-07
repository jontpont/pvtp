from importexport import *
from random import randint
from time import sleep
from os import system, listdir
from os.path import exists, splitext
import datetime
system('cls')
Test = []
x = datetime.datetime.now()
filename = f'{x.year}-{x.month}-{x.day}'

files = listdir('./Textfiles/pvtp/Unknown')
for f in range(len(files)):
    split = splitext(files[f])
    if split[1] == '.txt':
        print(f'Unknown/{split[0]}')
print()
files = listdir('./Textfiles/pvtp')
for f in range(len(files)):
    split = splitext(files[f])
    if split[1] == '.txt':
        print(split[0])
        
var = ''
print()
while var != 'done':
    var = input('Filename:\n    > ')
    if var != 'done':
        List = Import(f"pvtp/{var}")
        if isinstance(List, list):
            for i in range(len(List)):
                Test.append(List[i])
    print()
        

Scramble = []
if exists(f"Textfiles/pvtp/Unknown/{filename}") == True:
    Unlearnt = Import(f"pvtp/{filename}")
else:
    Unlearnt = []
print('~'*100)
system('cls')
quantity = int(input(f'Quantity 1 - {len(Test)}:  '))
for i in range(quantity):
    random = randint(1,len(Test))
    random -= 1
    Scramble.append(Test[random])
    Test.pop(random)
number = 0
length = 1
leng = len(Scramble)
while len(Scramble) > 0:
    print('~'*100)
    system('cls')
    answers = []
    complete = 0
    print(f'( {length}/{leng} ) {round((length-1)*10000 / leng)/100} %', '\n   ä ë ï ö ß ü\n')

    if randint(1,2) == 1:
        
        if randint(1,2) == 1:
            for a in range(len(Scramble[0])-2):
                answers.append(Scramble[0][a+1])
            quantity = len(answers)
            while len(answers) > 0:
                correct = 0
                print(f'{quantity-len(answers)} / {quantity} answers -\n')
                while correct == 0:
                    answer = input(f'    {Scramble[0][0]}:  ')
                    if answer == 'help':
                        number += 1
                        leng += 1
                        exists = 0
                        for c in range(len(Unlearnt)):
                            if Scramble[0] == Unlearnt[c]:
                                exists = 1
                        if exists == 0:
                            Unlearnt.append(Scramble[0])
                            Export(f'pvtp/Unknown/{filename}', Unlearnt)
                        for i in range(len(Scramble[0])-2):
                            print(i+1,')',Scramble[0][i+1])
                        Scramble.insert(randint(1,len(Scramble)),Scramble[0])
                    for b in range(quantity-complete):
                        if correct == 0:
                            if answer == answers[b]:
                                complete += 1
                                correct = 1
                                answers.pop(b)
                                b = len(answers)-1
        else:
            answers.append(Scramble[0][0])
            word = randint(1,len(Scramble[0])-2)
            while len(answers) > 0:
                correct = 0
                print('0 / 1 answer -\n')
                while correct == 0:
                    answer = input(f'>     {Scramble[0][word]}:  ')
                    if answer == 'help':
                        number += 1
                        leng += 1
                        print('1 )',Scramble[0][0])
                        exists = 0
                        for c in range(len(Unlearnt)):
                            if Scramble[0] == Unlearnt[c]:
                                exists = 1
                        if exists == 0:
                            Unlearnt.append(Scramble[0])
                            Export(f'pvtp/Unknown/{filename}', Unlearnt)
                        Scramble.insert(randint(1,len(Scramble)),Scramble[0])
                    if correct == 0:
                        if answer == answers[0]:
                            complete += 1
                            correct = 1
                            answers.pop(0)

    else:
        if randint(1,2) == 1:
            answer = Scramble[0][randint(1,len(Scramble[0])-2)]
            print(Scramble[0][0],'\n')
            decoy = [answer]
            same_types = []
            for v in range(len(Scramble)-1):
                if Scramble[v+1][len(Scramble[v+1])-1] == Scramble[0][len(Scramble[0])-1]:
                    same_types.append(Scramble[v+1][randint(1,len(Scramble[v+1])-2)])
            while len(same_types) < 5:
                extra = 0
                while extra == 0:
                    extra = randint(1, len(Scramble)-1)
                    defi = randint(1, len(Scramble[extra])-2)
                    for n in range(len(same_types)):
                        if Scramble[extra][defi] == same_types[n]:
                            extra = 0
                
                same_types.append(Scramble[extra][defi])
            for d in range(5):
                rando = randint(0, len(same_types)-1)
                indexrand = randint(0, len(decoy))
                decoy.insert(indexrand, same_types[rando])
                same_types.pop(rando)
            for d in range(len(decoy)):
                print(d+1, ')', decoy[d])
            intput = ''
            while intput != answer:
                intput = decoy[int(input('    > '))-1]
        else:
            answer = Scramble[0][0]
            print(Scramble[0][randint(1,len(Scramble[0])-2)],'\n')
            decoy = [answer]
            same_types = []
            for v in range(len(Scramble)-1):
                if Scramble[v+1][len(Scramble[v+1])-1] == Scramble[0][len(Scramble[0])-1]:
                    same_types.append(Scramble[v+1][0])
            while len(same_types) < 5:
                extra = 0
                while extra == 0:
                    extra = randint(1, len(Scramble)-1)
                    for n in range(len(same_types)):
                        if Scramble[extra][0] == same_types[n]:
                            extra = 0
                
                same_types.append(Scramble[extra][0])
            for d in range(5):
                rando = randint(0, len(same_types)-1)
                indexrand = randint(0, len(decoy))
                decoy.insert(indexrand, same_types[rando])
                same_types.pop(rando)
            for d in range(len(decoy)):
                print(d+1, ')', decoy[d])
            intput = ''
            while intput != answer:
                intput = decoy[int(input('    > '))-1]

    Scramble.pop(0)
    length += 1
system('cls')
print('Set Completed')
