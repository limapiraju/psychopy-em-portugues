import random, time

# cria as condições
conditions = ["somente estudo", "acumulação", "diminuição"] * 2
random.shuffle(conditions)


# cria palavras em Iñupiaq
Inupiaq = ['kamik', 'ikpik', 'mitiq', 'apyuq', 'qixak', 'taqtu'] 
random.shuffle(Inupiaq)

# DICIONARIO MONITORA PALAVRAS
Inupiaq_dict = dict()

# mimetizando os loops do PsychoPy
for practice_phase_cycles_thisN in range(0, 6):

    print('Ciclo {} de 6:'. format(practice_phase_cycles_thisN + 1))

    for practice_phase_trials_thisN in range(0, len(conditions)):

        # ACRESCENTA NOVAS PALAVRAS AO DICIONÁRIO NO CICLO 1
        if practice_phase_cycles_thisN == 0:
            Inupiaq_dict[Inupiaq[practice_phase_trials_thisN]] = Inupiaq[practice_phase_trials_thisN]
            # Inupiaq_dict['kamik'] = 'kamik'

        # pista a ser apresentada ao participante
        Inupiaq_cue = ""

        current_condition = conditions[practice_phase_trials_thisN] # [0, 1, 2, 3, 4, 5]

        if current_condition == "acumulação":

            # LETS TENTAR
            if practice_phase_cycles_thisN == 0:
                Inupiaq_cue = "_____"

            else:
                while True:
                    auxiliar = random.randint(0, 4)
                    if Inupiaq_dict[Inupiaq[practice_phase_trials_thisN]][auxiliar] == "_":
                        break

                for position, letter in enumerate(Inupiaq[practice_phase_trials_thisN]):
                    
                    if Inupiaq[practice_phase_trials_thisN][position] == Inupiaq_dict[Inupiaq[practice_phase_trials_thisN]][position]:
                        Inupiaq_cue += Inupiaq[practice_phase_trials_thisN][position]
                        
                    elif auxiliar == position:
                        Inupiaq_cue += Inupiaq[practice_phase_trials_thisN][position]
                        
                    else:
                        Inupiaq_cue += "_"


            Inupiaq_dict[Inupiaq[practice_phase_trials_thisN]] = Inupiaq_cue
                        

        elif current_condition == "diminuição":

            # LETS TENTAR
            if practice_phase_cycles_thisN == 0:
                Inupiaq_cue = Inupiaq[practice_phase_trials_thisN]

            else:
                while True:
                    auxiliar = random.randint(0, 4)
                    if Inupiaq_dict[Inupiaq[practice_phase_trials_thisN]][auxiliar] != "_":
                        break

                for position, letter in enumerate(Inupiaq[practice_phase_trials_thisN]):
                    
                    if Inupiaq_dict[Inupiaq[practice_phase_trials_thisN]][position] == "_":
                        Inupiaq_cue += "_"
                        
                    elif auxiliar == position:
                        Inupiaq_cue += "_"
                        
                    else:
                        Inupiaq_cue += Inupiaq[practice_phase_trials_thisN][position]

            
            Inupiaq_dict[Inupiaq[practice_phase_trials_thisN]] = Inupiaq_cue

        else:
            Inupiaq_cue = Inupiaq[practice_phase_trials_thisN]
            

        Inupiaq_cue = " ".join(Inupiaq_cue)

        print('{}:\t\t{}' .format(current_condition, Inupiaq_cue))

    time.sleep(2)

    print(Inupiaq_dict)
            


