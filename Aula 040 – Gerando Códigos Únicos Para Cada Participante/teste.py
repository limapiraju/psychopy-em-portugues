import random
from os.path import exists


def codigo(caracteres = 15):
    """
    Função gera um código contendo letras (exceto O) e números.
    Retorna um código de N caracteres (default = 15).
    """
    string = list("ABCDEFGHIJKLMNPQRSTUVXYZW0123456789")

    if caracteres > len(string):
        caracteres = len(string)
   
    random.shuffle(string)
    return "".join(string[:caracteres])

# simulando mil participantes
N = 2 # número de caracteres no código simulado
for i in range(1_000):
    new_ID = codigo(N)
    choque = False
    
    if not exists("unique_IDs.txt"):
        arquivo = open("unique_IDs.txt", "w")
        arquivo.write(new_ID + "\n")
        arquivo.close()
    else:
        arquivo = open("unique_IDs.txt", "r").readlines()
        arquivo.sort()
        if new_ID + "\n" in arquivo:
            temp_new_ID = new_ID + "\n"
            print("CHOQUE DE IDs!", end = " ")
            print(f"""O novo ID gerado ({new_ID}) é igual ao ID na posição {arquivo.index(temp_new_ID)}!""")
            choque = True
            
        if not choque:
            novo_arquivo = open("unique_IDs.txt", "w")
            for elemento in arquivo:
                novo_arquivo.write(elemento)
            novo_arquivo.write(new_ID + "\n")
            novo_arquivo.close()


    if i % 500 == 0:
        print(f"{i} iterações concluídas.")
        input("Pressione ENTER para continuar: ")

        
            
            
        
        
