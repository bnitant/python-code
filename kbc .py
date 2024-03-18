name=input('Enter name: ')
question=['Q1.People who work together\nA.Worker\nB.Superhuman\nC.colleagues\nD.Expert\nChoose any one from (A,B,C,D) : ','Q2.One who goes on foot\nA.Machination\nB.Pedestrian\nC.Transmigration\nD.Eccentric\nChoose any one from (A,B,C,D) : ','Q3.One who can speak two languages\nA.Bilingual\nB.Polylingual\nC.Polygamy\nD.Oligarchy\nChoose any one from (A,B,C,D) : ','Q4.Word with same meaning\nA.Antonyms\nB.Idioms\nC.Noun\nD.Synonyms\nChoose any one from (A,B,C,D) : ','Q5.The person who works for free\nA.Member\nB.Volunteer\nC.Organiser\nD.Servant\nChoose any one from (A,B,C,D) : ','Q6.One who speak less\nA.Reticent\nB.Misogynist\nC.Hypocrite\nD.Obsolete\nChoose any one from (A,B,C,D) : ','Q7.One who talks in sleep\nA.Celibate\nB.Intestate\nC.Somniloquy\nD.Gullible\nChoose any one from (A,B,C,D) : ']
money=0
for i in question:
    if question.index(i)==0:
        a=input(i)
        if a=='C' or a=='c':
            money+=1
            print(f'\nCorrect!! , you won {money}CR\n')
        else:
            print('\nReally sorry!! you lose this match and you have to go ')
            print(f'{name} you won total {money}CR')
            break

    elif question.index(i)==1:
        a=input(i)
        if a=='B' or a=='b':
            money+=1
            print(f'\nCorrect!! , you won {money}CR\n')
        else:
            print('\nReally sorry!! you lose this match and you have to go ')
            print(f'{name} you won total {money}CR')
            break

    elif question.index(i)==2:
        a=input(i)
        if a=='A' or a=='a':
            money+=1
            print(f'\nCorrect!! , you won {money}CR\n')
        else:
            print('\nReally sorry!! you lose this match and you have to go ')
            print(f'{name} you won total {money}CR')
            break

    elif question.index(i)==3:
        a=input(i)
        if a=='D' or a=='d':
            money+=1
            print(f'\nCorrect!! , you won {money}CR\n')
        else:
            print('\nReally sorry!! you lose this match and you have to go ')
            print(f'{name} you won total {money}CR')
            break

    elif question.index(i)==4:
        a=input(i)
        if a=='B' or a=='b':
            money+=1
            print(f'\nCorrect!! , you won {money}CR\n')
        else:
            print('\nReally sorry!! you lose this match and you have to go ')
            print(f'{name} you won total {money}CR')
            break

    elif question.index(i)==5:
        a=input(i)
        if a=='A' or a=='a':
            money+=1
            print(f'\nCorrect!! , you won {money}CR\n')
        else:
            print('\nReally sorry!! you lose this match and you have to go ')
            print(f'{name} you won total {money}CR')
            break

    elif question.index(i)==6:
        a=input(i)
        if a=='C' or a=='c':
            money+=1
            print(f'\nCorrect!! , you won {money}CR\n')
        else:
            print('\nReally sorry!! you lose this match and you have to go ')
            print(f'{name} you won total {money}CR')
            break
    if money==7:
        print('\n Congratulations!!! , you got all correct and 7crores are totally yours now')
