import numpy as np

# https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
# https://www.youtube.com/watch?v=2ox5u4W04-w
def levenshtein_distance(token1, token2):

    # Inicialização
    
    # Passos 1 e 2. Inicializa matriz D (m + 1) x (n + 1), contendo zeros
    distances = np.zeros((len(token1) + 1, len(token2) + 1))

    # Passo 3. Modifica conteúdo. agora a primeira linha conterá 0, 1, ..., m
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    # Passo 4. Modifica conteudo. agora a primeira coluna conterá 0, 1, ..., n
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    # 2. Processamento
    
    # inicializa valores
    a = 0
    b = 0
    c = 0

    # Passo 1. percorre letras da palavra alvo
    for t1 in range(1, len(token1) + 1):
        # Passo 2. percorre letras da palavra fonte
        for t2 in range(1, len(token2) + 1):
            # Passo 3. Se duas letras são iguais
            if (token1[t1 - 1] == token2[t2 - 1]):
                # a distância entre elas sera igual à distância do valor na diagonal imediatamente acima (que começa em zero)
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                # Se não, checa valores de outras células
                a = distances[t1][t2 - 1] # célula acima
                b = distances[t1 - 1][t2] # célula à esquerda
                c = distances[t1 - 1][t2 - 1] # diagonal acima

                # e atualiza valor da célula (distância) como sendo o menor dos três valores (a, b, c) + custo (1)
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    # retorna o valor da distância ná célula D[n][m] dividido pelo comprimento da maior string
    print(distances[len(token1)][len(token2)])
    return distances[len(token1)][len(token2)] / max(len(token1), len(token2))


#print(levenshtein_distance("gumbo", "gambol"))
#print(levenshtein_distance("gambol", "gumbo"))
print(levenshtein_distance("pato", "lagoa"))
