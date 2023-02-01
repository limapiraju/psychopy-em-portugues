import random
from os.path import exists
import time

cycles = 4

correct = [(0, 0, 0, 1),
           (0, 0, 1, 1),
           (0, 1, 1, 1),
           (1, 1, 1, 1)]

for i, cycle in enumerate(range(1, cycles + 1)):

    all_pairs = list()

    # ciclo 1, estudo
    if i == 1:

        cycle_1 = open("study_cycle_1.csv", "r").readlines()
        # print(cycle_1)

        for pair in cycle_1[1:]:
            temp = (pair.split(",")[0], pair.split(",")[1][:-1])
            all_pairs.append(temp)

        # print(all_pairs)

        random.shuffle(all_pairs)

        print("Ciclo 1")
        time.sleep(1)
        for pair in all_pairs:

            print(f"{pair[0]} - {pair[1]}")
            time.sleep(1)

    else:

        if not exists(f"cycle_{cycle}.csv"):
            arquivo = open(f"cycle_{cycle}.csv", "w")
            # cria cabeçalho do arquivo
            arquivo.write("Swahili,Portuguese\n")
            arquivo.close()
            
        for j, pair in enumerate(all_pairs[1:]):       
            novo_arquivo = open(f"cycle_{cycle}.csv", "a")
            if not correct[j][i]:
                novo_arquivo.write(pair[0] + "," + pair[1] + "\n")
            print(novo_arquivo)
            novo_arquivo.close()

        random.shuffle(all_pairs)

        print(f"Ciclo {cycle}")
        time.sleep(1)
        
        for pair in all_pairs:

            print(f"{pair[0]} - {pair[1]}")
            time.sleep(1)


