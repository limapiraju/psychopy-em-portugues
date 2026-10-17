import random

def serial_reaction_time_task(n_trials: int = 63,
                              block_trials: str = "random",
                              locations: list = [1, 2, 3, 4]):

    """
    Cria posições do alvo nas tentativas, a depender do bloco ser aleatório ou sequencial.
    - n_trials = número de tentativas do bloco;
    - block_trials = tipo de tentativas do bloco;
    - locations: representação numérica de quatro localizações da tela onde o alvo pode aparecer.

    Retorna a sequência de tentativas.
    """

    if block_trials == "random":

        last = None
        trials = []


        for i in range(n_trials):

            # reduz lista para posições diferentes da última tentativa
            # para evitar repetições
            possible = [x for x in locations if x != last]
            temp = random.choice(possible)
                
            last = temp
            trials.append(temp)

    if block_trials == "repeating":
        
        cohen_et_al = [4, 2, 3, 1, 3, 4, 2]  # see unsworth and engle (2005, p. 215)
        trials = (cohen_et_al * ((n_trials // len(cohen_et_al)) + 1))[:n_trials]


    return trials


# parâmetros do experimento
BLOCKS = ["practice", "random", "repeating", "repeating", "repeating", "repeating", "repeating",
          "random", "random", "random", "random", "repeating", "repeating"]

trial_counter = 0
experiment_trials = []

for i, blk in enumerate(BLOCKS):

    if blk == "practice":

        trials = serial_reaction_time_task()


    elif blk == "random":

        trials = serial_reaction_time_task(n_trials = 70)


    elif blk == "repeating":

        trials = serial_reaction_time_task(n_trials = 70,
                                           block_trials = "repeating")

    for trial in trials:

        trial_dict = {
            "trial_number": trial_counter,
            "block_number": i,
             "block_type": blk,
             "location_trial": trial}

        experiment_trials.append(trial_dict)

        trial_counter += 1
        

        

print(experiment_trials[-1])
    


          
