import random, time

# cria as condições
conditions = ["somente estudo", "acumulação", "diminuição"] * 2
random.shuffle(conditions)


# cria palavras em Iñupiaq
Inupiaq = ['kamik', 'ikpik', 'mitiq', 'apyuq', 'qixak', 'taqtu'] 
random.shuffle(Inupiaq)



# mimetizando os loops do PsychoPy
for practice_phase_cycles_thisN in range(0, 6):

    print('Ciclo {} de 6:'. format(practice_phase_cycles_thisN + 1))

    for practice_phase_trials_thisN in range(0, len(conditions)):

        # pista a ser apresentada ao participante
        Inupiaq_cue = ""

        current_condition = conditions[practice_phase_trials_thisN] # [0, 1, 2, 3, 4, 5]

        if current_condition == "acumulação":
            # 1 = a letra é apresentada
            # 0 = um underscore é apresentado no lugar da letra
            # letters = [1, 1, 0, 1, 1]
            # positions [0, 1, 2, 3, 4]
            # rodada 1: x = 5, y = 0
            # rodada 2: x = 4, y = 1
            # ...
            # rodada 6: x = 0, y = 5
            letters = [0] * (5 - practice_phase_cycles_thisN) + [1] * practice_phase_cycles_thisN
            
            random.shuffle(letters)
            
            for position, letter in enumerate(letters):
                if letter == 1:
                    Inupiaq_cue += Inupiaq[practice_phase_trials_thisN][position]
                else:
                    Inupiaq_cue += "_"

        elif current_condition == "diminuição":
            # 1 = a letra é apresentada
            # 0 = um underscore é apresentado no lugar da letra
            # letters = [1, 1, 0, 1, 1]
            # positions [0, 1, 2, 3, 4]
            # rodada 1: x = 0, y = 5
            # rodada 2: x = 1, y = 4
            # ...
            # rodada 6: x = 5, y = 0
            letters = [0] * (practice_phase_cycles_thisN) + [1] * (5 - practice_phase_cycles_thisN)
            
            random.shuffle(letters)
            
            for position, letter in enumerate(letters):
                if letter == 1:
                    Inupiaq_cue += Inupiaq[practice_phase_trials_thisN][position]
                else:
                    Inupiaq_cue += "_"

        else:
            Inupiaq_cue = Inupiaq[practice_phase_trials_thisN]
            

        Inupiaq_cue = " ".join(Inupiaq_cue)

        print('{}:\t\t{}' .format(current_condition, Inupiaq_cue))

    time.sleep(2)
            


