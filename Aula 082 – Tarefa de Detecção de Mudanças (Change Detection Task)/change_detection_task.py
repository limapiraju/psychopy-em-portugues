import random

# ============================================================
# PARÂMETROS GERAIS DO EXPERIMENTO
# ============================================================

# Tamanhos das matrizes (Phillips, 1974)
# O número representa o número de linhas e também de colunas
# Portanto:
#   4 = matriz 4 × 4 = 16 células
#   6 = matriz 6 × 6 = 36 células
#   8 = matriz 8 × 8 = 64 células
matrix_sizes = [4, 6, 8]

# Intervalos entre a primeira e a segunda matriz (em segundos)
# 0.02 = 20 ms
isi_values = [0.02, 1.0, 3.0, 9.0]

# Número de tentativas por combinação de:
# tamanho da matriz × ISI
# 3 tamanhos × 4 ISIs = 12 condições
# 30 tentativas por condição:
# 12 × 30 = 360 tentativas no total
n_trials_per_condition = 30

# Número de blocos
n_blocks = 5

# ============================================================
# PARÂMETROS GEOMÉTRICOS
# ============================================================

# Tamanho TOTAL da matriz na tela, em unidades "norm" do PsychoPy
# onde (0, 0) = centro da tela
# -1 e +1 = limites horizontais/verticais da tela
cell_size = 0.10

# ============================================================
# GERAR A ESTRUTURA DAS TENTATIVAS
# ============================================================

# Lista que receberá todas as tentativas do experimento
trials = []

# Vamos construir cada condição separadamente.
#   - tamanho da matriz (4, 6 ou 8)
#   - ISI (0.02, 1, 3 ou 9 s)
#   - 30 tentativas por condição
#   - 5 blocos
#   - 30 tentativas ÷ 5 blocos = 6 tentativas (de cada condição) por bloco
# Portanto, cada bloco terá exatamente 6 tentativas
# de cada uma das 12 condições.

# ------------------------------------------------------------
# Loop pelas condições experimentais
# ------------------------------------------------------------

for size in matrix_sizes:

    for isi in isi_values:

        # Criamos as 30 tentativas desta condição
        condition_trials = []

        for trial_number in range(n_trials_per_condition):

            # Sorteia independentemente se a tentativa será
            # "same" ou "different".
            condition = random.choice(['same', 'different'])

            # Guarda as informações desta tentativa.
            trial = {
                'size': size,
                'isi': isi,
                'condition': condition
            }

            condition_trials.append(trial)


        # ----------------------------------------------------
        # Distribuir as 30 tentativas entre os 5 blocos
        # ----------------------------------------------------

        # Cada bloco receberá 6 tentativas desta condição.
        trials_per_block = n_trials_per_condition // n_blocks

        for block in range(n_blocks):

            # Índices correspondentes às 6 tentativas deste bloco.
            start = block * trials_per_block
            end = start + trials_per_block

            # Seleciona as 6 tentativas.
            block_trials = condition_trials[start:end]

            # Registra a qual bloco elas pertencem.
            for trial in block_trials:
                trial['block'] = block + 1

                # Adicionamos à lista geral.
                trials.append(trial)

# ============================================================
# ALEATORIZAR A ORDEM DAS TENTATIVAS DENTRO DE CADA BLOCO
# ============================================================

# randomização dentro de cada bloco, para que:
#   - cada bloco continue contendo 72 tentativas
#   - cada bloco continue contendo 6 tentativas de cada condição
#   - apenas a ORDEM das tentativas seja aleatorizada

randomized_trials = []

for block in range(1, n_blocks + 1):

    # Seleciona as tentativas pertencentes a este bloco.
    block_trials = [
        trial for trial in trials
        if trial['block'] == block
    ]

    # Embaralha a ordem das 72 tentativas
    random.shuffle(block_trials)

    # Acrescenta as tentativas embaralhadas à lista final
    randomized_trials.extend(block_trials)

# Substituímos a lista original pela lista final aleatorizada.
trials = randomized_trials

# ============================================================
# CONFERÊNCIAS
# ============================================================

# Número total de tentativas.
print("Número total de tentativas:", len(trials))


# Conferir quantas tentativas há em cada bloco.
for block in range(1, n_blocks + 1):

    n_in_block = sum(
        trial['block'] == block
        for trial in trials
    )

    print(
        "Bloco", block,
        ":", n_in_block,
        "tentativas"
    )


# Conferir a quantidade de cada condição em cada bloco.
for block in range(1, n_blocks + 1):

    print("\nBloco", block)

    for size in matrix_sizes:

        for isi in isi_values:

            n_condition = sum(
                trial['block'] == block
                and trial['size'] == size
                and trial['isi'] == isi
                for trial in trials
            )

            print(
                size, "x", size,
                "| ISI =", isi,
                "| n =", n_condition
            )
            

# ============================================================
# FUNÇÃO PARA CRIAR UMA MATRIZ ALEATÓRIA
# ============================================================

def create_random_matrix(size):
    """
    Cria uma matriz quadrada de tamanho 'size × size'.

    Cada célula recebe aleatoriamente:
        0 = branco
        1 = preto

    Como usamos random.choice([0, 1]), cada valor tem
    probabilidade de 0.5 de ser escolhido.
    """

    # Lista que armazenará os valores de todas as células.
    matrix = []

    # Percorremos cada linha da matriz.
    for row in range(size):

        # Criamos uma nova linha vazia.
        current_row = []

        # Percorremos cada coluna da matriz.
        for col in range(size):

            # Sorteamos o valor da célula.
            value = random.choice([0, 1])

            # Adicionamos o valor à linha.
            current_row.append(value)

        # Adicionamos a linha completa à matriz.
        matrix.append(current_row)

    return matrix


# ============================================================
# CRIAR A MATRIZ 1 DE CADA TENTATIVA
# ============================================================

for trial in trials:

    # O tamanho da matriz é definido pela condição da tentativa
    size = trial['size']

    # Gera a matriz aleatória correspondente.
    trial['matrix1'] = create_random_matrix(size)
    
# ============================================================
# CONFERÊNCIA
# ============================================================

print("\nExemplo de matriz 1:")

print(trials[0]['matrix1'])

print("\nTamanho da matriz:", trials[0]['size'])
