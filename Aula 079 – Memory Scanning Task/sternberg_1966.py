import random
import itertools


def sternberg_trials(
    n_trials = 144,
    loads = range(1, 7),
    stimuli = range(10)
    ):
    """
    Gera trials para a tarefa de busca serial em memória
    de curto prazo de Sternberg (1966).

    Retorna uma lista de dicionários, cada um contendo:
    - load: tamanho do conjunto de memória
    - trial_type: 'positive' (probe presente) ou 'negative' (probe ausente)
    - sequence: sequência de estímulos memorizados
    - probe: estímulo de teste
    - position: posição serial do probe na sequência (1-indexada);
                0 se probe ausente
    """

    # Lista que armazenará todos os trials
    trials = []

    # Cria todas as combinações possíveis de carga × tipo de trial
    # Ex.: (1, 'positive'), (1, 'negative'), ..., (6, 'negative')
    conditions = list(itertools.product(loads, ["positive", "negative"]))

    # Número de repetições por condição
    # n_trials deve ser múltiplo do número de condições (12)
    n_reps = n_trials // len(conditions)

    # Repete o conjunto completo de condições n_reps vezes
    for _ in range(n_reps):

        # Itera por cada combinação de carga e tipo de trial
        for load, trial_type in conditions:

            # Sorteia uma sequência de estímulos SEM repetição
            # O comprimento da sequência é igual à carga do trial
            seq = random.sample(stimuli, load)

            # Caso positivo: o probe pertence à sequência memorizada
            if trial_type == "positive":

                # Escolhe aleatoriamente um item da sequência como probe
                probe = random.choice(seq)

                # Registra a posição serial do probe (começando em 1)
                position = seq.index(probe) + 1

            # Caso negativo: o probe NÃO pertence à sequência memorizada
            else:

                # Conjunto de estímulos possíveis menos os já usados na sequência
                available = list(set(stimuli) - set(seq))

                # Escolhe aleatoriamente um estímulo que não está na memória
                probe = random.choice(available)

                # Posição 0 indica ausência do probe na sequência
                position = 0

            # Armazena o trial como um dicionário
            trials.append({
                "load": load,
                "trial_type": trial_type,
                "sequence": seq,
                "probe": probe,
                "position": position
            })

    # Embaralha a ordem final dos trials
    random.shuffle(trials)

    return trials

        
teste = sternberg_trials()
print(teste)
                
