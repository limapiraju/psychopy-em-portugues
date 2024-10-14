import csv
import random
import itertools

def block_randomization(*condition_lists,
                        blocks=1,
                        digits=9,
                        output_file = "randomized_conditions.csv"):
    """
    Gera todas as combinações de condições, repetidas em blocos, e salva em um arquivo CSV.
    
    Parâmetros:
        *condition_lists: k listas, onde cada lista contém as condições de uma variável independente (VI).
        blocks (int): número de repetições dos blocos.
        digits (int): número de dígitos aleatórios do código.
        output_file (str): nome do arquivo CSV para salvar os resultados.
    """

    # Verifica se alguma das listas de condições tem mais de 10 níveis
    for VI in condition_lists:
        if len(VI) > 10:
            print("Erro! Pelo menos uma das VIs tem mais de 10 níveis.\nA função só aceita VIs com até 10 níveis.")
            return
    
    # Gera todas as combinações possíveis entre os elementos das k listas
    combinations = list(itertools.product(*condition_lists))
    
    # Armazena IDs já gerados para garantir unicidade
    generated_ids = set()
    
    def generate_unique_id(combination):
        """
        Gera um ID único com base nas condições e números aleatórios.
        """
        while True:
            # Gera uma parte do ID com base nas condições
            # Usa str.zfill para garantir o comprimento mínimo mas não adicionar zeros extras
            condition_part = "ID" + ''.join(str(condition_lists[i].index(cond)) 
                                    for i, cond in enumerate(combination))
            # Gera uma parte aleatória do ID
            random_part = ''.join(random.choices('0123456789', k = digits))
            # Concatena ambas as partes
            new_id = condition_part + random_part
            if new_id not in generated_ids:
                generated_ids.add(new_id)
                return new_id
    
    # Abre o arquivo CSV para escrita
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        # Escreve o cabeçalho no arquivo CSV com o ID primeiro, seguido pelos nomes das variáveis independentes
        header = ["ID"] + [f"VI{i + 1}" for i in range(len(condition_lists))]
        writer.writerow(header)
        
        # Para cada bloco, randomiza as combinações e escreve no arquivo
        for _ in range(blocks):
            random.shuffle(combinations)  # Embaralha as combinações
            for combination in combinations:
                # Gera um ID único
                unique_id = generate_unique_id(combination)
                # Escreve o ID seguido pela combinação no arquivo CSV
                writer.writerow([unique_id] + list(combination))

    print(f"Arquivo '{output_file}' gerado com sucesso!")

"""
# Exemplo de uso:
VI1 = ["0", "1"]
VI2 = ["0", "1"]
VI3 = ["0", "1"]
blocks = 3
"""

tarefas = ["palavras", "imagens"]
ordens = ["pré", "pós"]
intervalos = ["1 dia", "2 dias", "3 dias", "4 dias", "5 dias"]
blocks = 5

block_randomization(tarefas, ordens, intervalos,
                    blocks = blocks,
                    output_file = "experiment_test.csv")

