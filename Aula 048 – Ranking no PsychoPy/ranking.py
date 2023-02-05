import random
from os.path import exists
import time
import copy

'''
# abre arquivo contendo ranking
ranking = open("ranking.csv", "r").readlines()[1:]

# cria listas que armazenará top 5
nicknames = list()
scores = list()

# separando nicknames e pontuações
for i, position in enumerate(ranking):
     ranking[i] = position.split(",")
     nicknames.append(ranking[i][1])
     scores.append(ranking[i][2])

print(nicknames)
print(scores)

my_nickname = "MCS"
my_score = 600
is_my_score_saved = False

new_ranking = list()

ranking_auxiliar = copy.deepcopy(ranking)

for i, position in enumerate(ranking_auxiliar):
    # se minha pontuação foi maior que a pontuação na posição i   
    if (my_score > int(scores[i])) and (is_my_score_saved == False):
        new_ranking.append(f"{i + 1},{my_nickname},{my_score}\n")
        ranking.pop()
        is_my_score_saved = True

    elif is_my_score_saved:
        new_ranking.append(f"{i + 1},{nicknames[i - 1]},{scores[i - 1]}")

    else:
        new_ranking.append(f"{i + 1},{nicknames[i]},{scores[i]}")

updated_ranking = open("ranking.csv", "w")
updated_ranking.write("position,nickname,score\n")

for position in new_ranking:
    updated_ranking.write(position)

updated_ranking.close()
'''

for i in range(20):

    # abre arquivo contendo ranking
    ranking = open("ranking.csv", "r").readlines()[1:]

    # cria listas que armazenará top 5
    nicknames = list()
    scores = list()

    # separando nicknames e pontuações
    for i, position in enumerate(ranking):
         ranking[i] = position.split(",")
         nicknames.append(ranking[i][1])
         scores.append(ranking[i][2])

    print(nicknames)
    print(scores)
    time.sleep(2)

    my_nickname = list("ABCDEFGHIJKLMNOPQRSTUVXYZW")
    random.shuffle(my_nickname)
    my_nickname = "".join(my_nickname[:3])
    
    my_score = random.randint(0, 100_000)
    is_my_score_saved = False

    print(f"{my_nickname} fez {my_score} pontos!")
    time.sleep(2)

    new_ranking = list()

    # ABC = 100, DEF = 50, GHI = 10, JKL = 5, MNO = 1
    # MAR = 55

    # i = 0
    # ABC > MAR 
    # salvar:    
    # ABC = 100

    # i = 1
    # DEF < = MAR
    # salvar:
    # ABC = 100, MAR = 55

    # i = 2
    # abordagem incorreta
    # ABC = 100, MAR = 55, GHI = 10, JKL = 5, MNO = 1

    # abordagem correta
    # ABC = 100, MAR = 55, DEF = 50, GHI = 10, JKL = 5

    

    ranking_auxiliar = copy.deepcopy(ranking)

    for i, position in enumerate(ranking_auxiliar):
        # se minha pontuação foi maior que a pontuação na posição i
        # coloca minha pontuação no ranking
        if (my_score > int(scores[i])) and (is_my_score_saved == False):
            new_ranking.append(f"{i + 1},{my_nickname},{my_score}\n")
            ranking.pop()
            is_my_score_saved = True

        # derruba todo mundo que ficou atrás de mim uma posição no ranking
        elif is_my_score_saved:
            new_ranking.append(f"{i + 1},{nicknames[i - 1]},{scores[i - 1]}")

        # salva todo mundo na mesma posição no raking
        else:
            new_ranking.append(f"{i + 1},{nicknames[i]},{scores[i]}")

    print(new_ranking)
    time.sleep(2)

    updated_ranking = open("ranking.csv", "w")
    updated_ranking.write("position,nickname,score\n")

    for position in new_ranking:
        updated_ranking.write(position)

    updated_ranking.close()

    x = input("Pressione ENTER para continuar: ")
    
