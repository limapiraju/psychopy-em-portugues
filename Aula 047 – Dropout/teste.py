'''
arquivo = open("cycle_1.csv", "r").readlines()
print(arquivo)
'''

import random, shutil, os
from os.path import exists

expInfo = dict()
expInfo["participant"] = "kily"

my_directory = f"{expInfo['participant']}"
if not exists(my_directory):
    os.mkdir(my_directory)
    
study_file = test_file = "cycle_1.csv"

# caminho de destino
destination = f"{expInfo['participant']}/{study_file}"

# copiando o conteúdo de uma fonte para um destino
dest = shutil.copyfile(study_file, destination)
