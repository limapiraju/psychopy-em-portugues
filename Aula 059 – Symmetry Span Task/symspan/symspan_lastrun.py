#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on October 13, 2024, at 19:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.1')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from instr_code


# Run 'Before Experiment' code from instr_code


# Run 'Before Experiment' code from instr_code


# Run 'Before Experiment' code from instr_code




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'symspan'  # from the Builder filename that created this script
expInfo = {
    'ID': f"{randint(1, 999999999):06.0f}",
    'Nome Completo': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['ID'].zfill(9), expInfo['date'], expInfo['Nome Completo'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 059 – Symmetry Span Task\\symspan\\symspan_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[900, 600], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='0.0000, 0.0000, 0.0000', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "welcome" ---
# Run 'Begin Experiment' code from welcome_code
import random
from os.path import exists

expInfo["ID"] = expInfo["ID"].zfill(9)

participant_code = expInfo["ID"]

if not exists("unique_IDs.txt"):
    arquivo = open("unique_IDs.txt", "w")
    # cria cabeçalho do arquivo
    arquivo.write("ID_number\tName\n")
    arquivo.write(participant_code + "\t" + expInfo["Nome Completo"] + "\n")
    arquivo.close()
else:
    novo_arquivo = open("unique_IDs.txt", "a")
    novo_arquivo.write(participant_code + "\t" + expInfo["Nome Completo"] + "\n")
    novo_arquivo.close()
welcome_msg = visual.TextStim(win=win, name='welcome_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
welcome_next = visual.ImageStim(
    win=win,
    name='welcome_next', units='norm', 
    image='images/next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
welcome_resp = event.Mouse(win=win)
x, y = [None, None]
welcome_resp.mouseClock = core.Clock()

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
# índices de instruções
current_instruction = 0
instruction_block = 0
 
instruction_list = [# grid (memory) task
                   ["""
Neste experimento, você tentará memorizar quadrados vermelhos que você verá na tela enquanto você avalia se grades quadriculadas são simétricas em relação ao eixo vertical.

Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a tarefa de memória com os quadrados vermelhos.""",
"""
Para essa prática, quadrados vermelhos aparecerão em uma matriz, um de cada vez. Tente lembrar a posição de cada quadrado na ordem em que ele apareceu.

Depois que 2 quadrados aparecerem, você verá uma tela com 16 possíveis localizações dos quadrados. Seu trabalho é clicar na posição que cada quadrado apareceu na mesma ordem em que eles foram apresentados. 

Para fazer isso, use o mouse para clicar nos quadrados para selecioná-las. Os quadrados selecionados serão indicados por números, que representarão a sequência em que você clicou neles.""",
"""
Depois que selecionar todos os quadrados que compõem sua resposta, e eles estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.

Se errar sua resposta, aperte o botão [Limpar] para começar novamente. Se esquecer a posição de um dos quadrados, aperte o botão [Branco] para marcar a posição que o quadrado esquecido deve estar.

Lembre-se, é muito importante selecionar os quadrados na mesma ordem que foram apresentados. Se você esquecer um quadrado, use o botão [Branco] para marcar a sua posição.""",
"""
Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a prática com os quadrados.
"""], 
# distractor (symmetry) task
["""
Agora você irá praticar a tarefa de simetria deste experimento. Um grade quadriculada aparecerá na tela, tal como a exemplificada a seguir:
""",
"""
Sua tarefa será avaliar se a grade é simétrica em relação ao eixo vertical (que é representado abaixo pela linha vertical vermelha).
""",
"""
Note que a reta vertical vermelha foi anteriormente apresentada apenas para fins didáticos. Ela NÃO aparecerá durante a realização da tarefa.

Depois que tiver avaliado a simetria da grade quadriculada em relação ao eixo vertical, clique no botão [Continuar].
""",
"""
Em seguida, você deverá emitir uma resposta. Se a grade que você acabou de ver for simétrica, clique no botão [Sim]. 

Se a grade que você acabou de ver for assimétrica, clique no botão [Não].

Depois que clicar em um dos botões, o computador irá lhe dizer se fez a escolha certa.
""",
"""
Por exemplo, se você vir a grade abaixo, clique no botão [Sim], pois essa grade é simétrica.
""",
"""
Agora, se você vir a grade abaixo, clique no botão [Não], pois essa grade é assimétrica.
""",
"""
É muito importante que você consiga avaliar a simetria das grades quadriculadas corretamente. Também é importante que você consiga fazer essa avaliação o mais rapidamente possível.

Favor chamar o pesquisador se você tiver perguntas.

Quando você estiver pronto, clique em [Avançar] para começar a praticar.
"""],
# SYMSPAN training
["""
Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá avaliar a simetria de grades quadriculadas. Assim que decidir a sua resposta, um quadrado vermelho aparecerá na tela. Tente se lembrar da posição desse quadrado.

Na etapa anterior na qual você apenas avaliou a simetria de grades quadriculadas, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar pela grade quadriculada, pular a tela de resposta e contar o problema como erro.

Por isso é muito importante você resolver os problemas o mais rápido e corretamente possível.""",
"""
Depois que o quadrado vermelho desaparecer, outra grade quadriculada irá aparecer, e depois outro quadrado vermelho. No final de cada sequência, uma tela de resposta aparecerá na tela. Use o mouse para indicar as posições da sequência de quadrados vermelhos que acabou de ver.

Tente lembrar a ordem correta dos quadrados vermelhos. É muito importante que você trabalhe rapidamente e corretamente nas grades quadriculadas. Tenha certeza que você sabe a resposta do problema de simetria antes de ir para a próxima tela.

O computador não irá dizer se a resposta está correta. Depois da tela de resposta, você receberá o resultado do seu desempenho para o número quadrados vermelhos lembrados e a porcentagem de respostas corretas nos problemas de simetria.
""",
"""
Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas de simetria que você respondeu corretamente para o experimento inteiro.

É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas de simetria.

Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas de simetria E lembrar o máximo de quadrados vermelhos possíveis.

Favor chamar o pesquisador se tiver perguntas.
"""
],
# SYMSPAN testing
["""
Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.

Primeiro você terá que resolver um problema de simetria, depois terá que memorizar um quadrado vermelho. Quando ver a tela de resposta, indique as posições dos quadrados vermelhos na ordem em que foram apresentados. Se esquecer de um quadrado vermelho, clique no botão [Branco] para marcar onde o quadrado vermelho deve ir.

Algumas combinações terão mais problemas de simetria e quadrados vermelhos do que outras.
""",
"""
É importante que você faça o melhor possível nos problemas de simetria e na parte onde tiver que lembrar os quadrados vermelhos. 

Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas de simetria. Também lembre-se de acertar 85% dos problemas.

Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]
                   
# cor do feedback das operações matemáticas
symmetry_color = [0.0000, 0.0000, 0.0000]

# primeiro nome do participante
if expInfo["Nome Completo"] == "":
    first_name = "participante"
else:
    first_name = expInfo["Nome Completo"].strip().split()[0].title()

welcome_txt = f"""Olá, {first_name}! 

Agradecemos sua disponibilidade em colaborar com nossa pesquisa!

Clique em [Avançar] para iniciar."""

thanks_txt = f"""Esta atividade acabou, {first_name}.

Favor chamar o pesquisador! ☺"""



grid_example = "images/symm1_prac.jpg"
grid_opacity = 0
pos_y = 0.2

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.09, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
previous = visual.ImageStim(
    win=win,
    name='previous', units='norm', 
    image='images/previous_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
next = visual.ImageStim(
    win=win,
    name='next', units='norm', 
    image='images/next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
instr_resp = event.Mouse(win=win)
x, y = [None, None]
instr_resp.mouseClock = core.Clock()
symmetry_example = visual.ImageStim(
    win=win,
    name='symmetry_example', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0.05), size=(0.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "grid_memory" ---
# Run 'Begin Experiment' code from grid_memory_code
fixed_grid_positions = [[-0.225, 0.225], [-0.075, 0.225], [0.075, 0.225], [0.225, 0.225],
                        [-0.225, 0.075], [-0.075, 0.075], [0.075, 0.075], [0.225, 0.075],  
                        [-0.225, -0.075], [-0.075, -0.075], [0.075, -0.075], [0.225, -0.075], 
                        [-0.225, -0.225], [-0.075, -0.225], [0.075, -0.225], [0.225, -0.225]
                        ]

grid_positions = [([-0.225, 0.225], "A"), ([-0.075, 0.225], "B"),
                  ([0.075, 0.225], "C"), ([0.225, 0.225], "D"),
                  ([-0.225, 0.075], "E"), ([-0.075, 0.075], "F"),
                  ([0.075, 0.075], "G"), ([0.225, 0.075], "H"),
                  ([-0.225, -0.075], "I"), ([-0.075, -0.075], "J"),
                  ([0.075, -0.075], "K"), ([0.225, -0.075], "L"),
                  ([-0.225, -0.225], "M"), ([-0.075, -0.225], "N"),
                  ([0.075, -0.225], "O"), ([0.225, -0.225], "P"),
                  ]

grid_positions_list = list()

for i in range(16):
    grid_positions_list.append("images/selected_square_0.jpg")
grid_memory_task = visual.ImageStim(
    win=win,
    name='grid_memory_task', units='height', 
    image='grid.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
square_position = visual.Rect(
    win=win, name='square_position',units='height', 
    width=(0.14, 0.14)[0], height=(0.14, 0.14)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=None, fillColor=[0.804,-1.000,-1.000],
    opacity=1, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "recall" ---
# Run 'Begin Experiment' code from code_recall
def EditDistanceScore(target, recall):
    """
    Recebe duas strings que serão comparadas. Retorna o edit distance score,
    que consiste em len(target) – distância de Damerau–Levenshtein. Se a substração resultar em 
    valor negativo, fixa valor em 0.
    """
    # se strings são idênticas
    if recall == target:
        return len(target) # edit distance = tamanho da string
    # se nada foi lembrado
    elif recall == "": # edit distance = 0
        return 0

    stimDict = {target[0]: "0"}

    for targetIndex in range(0, len(target)):
        if target[targetIndex] not in stimDict:
            stimDict[target[targetIndex]] = "0"

    for recallIndex in range(0, len(recall)):
        if recall[recallIndex] not in stimDict:
            stimDict[recall[recallIndex]] = "0"

    disMatrix = np.zeros(shape=(len(target) + 2, len(recall) + 2))

    inf = len(target) + len(recall)

    for targetIndex in range(0, len(target) + 1):
        disMatrix[targetIndex + 1, 0] = inf
        disMatrix[targetIndex + 1, 1] = targetIndex

    for recallIndex in range(0, len(recall)+1):
        disMatrix[0, recallIndex + 1] = inf
        disMatrix[1, recallIndex + 1] = recallIndex

    for targetIndex in range(1, len(target)+1):
        present = 0
        for recallIndex in range(1, len(recall) + 1):
            if recall[recallIndex-1] in stimDict:
                targetIndex2 = int(stimDict[recall[recallIndex - 1]])

            recallIndex2 = present
            cost = 1

            if target[targetIndex - 1] == recall[recallIndex - 1]:
                cost = 0
                present = recallIndex

            Substitution = disMatrix[targetIndex, recallIndex] + cost
            Insertion = disMatrix[targetIndex + 1, recallIndex] + 1
            Deletion = disMatrix[targetIndex, recallIndex + 1] + 1
            Transposition = disMatrix[targetIndex2, recallIndex2] + (targetIndex - targetIndex2 - 1) + 1 + (recallIndex - recallIndex2 - 1)

            if Substitution < Insertion and Substitution < Deletion and Substitution < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Substitution
            elif Insertion < Deletion and Insertion < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Insertion
            elif Deletion < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Deletion
            else:
                disMatrix[targetIndex + 1, recallIndex + 1] = Transposition


        stimDict[target[targetIndex - 1]] = str(targetIndex)

    # se edit distance < 0, fixa valor em zero
    if len(target) - disMatrix[len(target) + 1, len(recall) + 1] < 0:
        return 0
    # caso contrário, retorna o valor da medida
    else:
        return(int(len(target) - disMatrix[len(target) + 1, len(recall) + 1]))

def partial_credit(string1, string2):
    score = 0
    for letter1, letter2 in zip(string1, string2):
        if letter1 == letter2:
            score += 1
            
    return score

final_full_credit_score = final_partial_credit_score = final_edit_distance_score = 0


prompt_recall = visual.TextStim(win=win, name='prompt_recall',
    text='Selecione os quadrados na mesma ordem em que foram apresentadas. Use o botão [Branco] para preencher quadrados que esqueceu.',
    font='Times New Roman',
    units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
grid_recall = visual.ImageStim(
    win=win,
    name='grid_recall', units='height', 
    image='grid.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
A = visual.ImageStim(
    win=win,
    name='A', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
B = visual.ImageStim(
    win=win,
    name='B', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
C = visual.ImageStim(
    win=win,
    name='C', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[fixed_grid_positions[2]], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
D = visual.ImageStim(
    win=win,
    name='D', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
E = visual.ImageStim(
    win=win,
    name='E', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
F = visual.ImageStim(
    win=win,
    name='F', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
G = visual.ImageStim(
    win=win,
    name='G', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
H = visual.ImageStim(
    win=win,
    name='H', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
I = visual.ImageStim(
    win=win,
    name='I', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
J = visual.ImageStim(
    win=win,
    name='J', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
K = visual.ImageStim(
    win=win,
    name='K', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
L = visual.ImageStim(
    win=win,
    name='L', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
M = visual.ImageStim(
    win=win,
    name='M', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
N = visual.ImageStim(
    win=win,
    name='N', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
O = visual.ImageStim(
    win=win,
    name='O', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P = visual.ImageStim(
    win=win,
    name='P', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
clear_ = visual.ImageStim(
    win=win,
    name='clear_', units='norm', 
    image='images/clear_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
blank = visual.ImageStim(
    win=win,
    name='blank', units='norm', 
    image='images/blank_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
send = visual.ImageStim(
    win=win,
    name='send', units='norm', 
    image='images/send_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
recall_response = event.Mouse(win=win)
x, y = [None, None]
recall_response.mouseClock = core.Clock()

# --- Initialize components for Routine "recall_feedback" ---
recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
symmetry_feedback_prompt = visual.TextStim(win=win, name='symmetry_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
symmetry_feedback_performance = visual.TextStim(win=win, name='symmetry_feedback_performance',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.9, 0.9), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
# índices de instruções
current_instruction = 0
instruction_block = 0
 
instruction_list = [# grid (memory) task
                   ["""
Neste experimento, você tentará memorizar quadrados vermelhos que você verá na tela enquanto você avalia se grades quadriculadas são simétricas em relação ao eixo vertical.

Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a tarefa de memória com os quadrados vermelhos.""",
"""
Para essa prática, quadrados vermelhos aparecerão em uma matriz, um de cada vez. Tente lembrar a posição de cada quadrado na ordem em que ele apareceu.

Depois que 2 quadrados aparecerem, você verá uma tela com 16 possíveis localizações dos quadrados. Seu trabalho é clicar na posição que cada quadrado apareceu na mesma ordem em que eles foram apresentados. 

Para fazer isso, use o mouse para clicar nos quadrados para selecioná-las. Os quadrados selecionados serão indicados por números, que representarão a sequência em que você clicou neles.""",
"""
Depois que selecionar todos os quadrados que compõem sua resposta, e eles estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.

Se errar sua resposta, aperte o botão [Limpar] para começar novamente. Se esquecer a posição de um dos quadrados, aperte o botão [Branco] para marcar a posição que o quadrado esquecido deve estar.

Lembre-se, é muito importante selecionar os quadrados na mesma ordem que foram apresentados. Se você esquecer um quadrado, use o botão [Branco] para marcar a sua posição.""",
"""
Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a prática com os quadrados.
"""], 
# distractor (symmetry) task
["""
Agora você irá praticar a tarefa de simetria deste experimento. Um grade quadriculada aparecerá na tela, tal como a exemplificada a seguir:
""",
"""
Sua tarefa será avaliar se a grade é simétrica em relação ao eixo vertical (que é representado abaixo pela linha vertical vermelha).
""",
"""
Note que a reta vertical vermelha foi anteriormente apresentada apenas para fins didáticos. Ela NÃO aparecerá durante a realização da tarefa.

Depois que tiver avaliado a simetria da grade quadriculada em relação ao eixo vertical, clique no botão [Continuar].
""",
"""
Em seguida, você deverá emitir uma resposta. Se a grade que você acabou de ver for simétrica, clique no botão [Sim]. 

Se a grade que você acabou de ver for assimétrica, clique no botão [Não].

Depois que clicar em um dos botões, o computador irá lhe dizer se fez a escolha certa.
""",
"""
Por exemplo, se você vir a grade abaixo, clique no botão [Sim], pois essa grade é simétrica.
""",
"""
Agora, se você vir a grade abaixo, clique no botão [Não], pois essa grade é assimétrica.
""",
"""
É muito importante que você consiga avaliar a simetria das grades quadriculadas corretamente. Também é importante que você consiga fazer essa avaliação o mais rapidamente possível.

Favor chamar o pesquisador se você tiver perguntas.

Quando você estiver pronto, clique em [Avançar] para começar a praticar.
"""],
# SYMSPAN training
["""
Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá avaliar a simetria de grades quadriculadas. Assim que decidir a sua resposta, um quadrado vermelho aparecerá na tela. Tente se lembrar da posição desse quadrado.

Na etapa anterior na qual você apenas avaliou a simetria de grades quadriculadas, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar pela grade quadriculada, pular a tela de resposta e contar o problema como erro.

Por isso é muito importante você resolver os problemas o mais rápido e corretamente possível.""",
"""
Depois que o quadrado vermelho desaparecer, outra grade quadriculada irá aparecer, e depois outro quadrado vermelho. No final de cada sequência, uma tela de resposta aparecerá na tela. Use o mouse para indicar as posições da sequência de quadrados vermelhos que acabou de ver.

Tente lembrar a ordem correta dos quadrados vermelhos. É muito importante que você trabalhe rapidamente e corretamente nas grades quadriculadas. Tenha certeza que você sabe a resposta do problema de simetria antes de ir para a próxima tela.

O computador não irá dizer se a resposta está correta. Depois da tela de resposta, você receberá o resultado do seu desempenho para o número quadrados vermelhos lembrados e a porcentagem de respostas corretas nos problemas de simetria.
""",
"""
Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas de simetria que você respondeu corretamente para o experimento inteiro.

É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas de simetria.

Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas de simetria E lembrar o máximo de quadrados vermelhos possíveis.

Favor chamar o pesquisador se tiver perguntas.
"""
],
# SYMSPAN testing
["""
Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.

Primeiro você terá que resolver um problema de simetria, depois terá que memorizar um quadrado vermelho. Quando ver a tela de resposta, indique as posições dos quadrados vermelhos na ordem em que foram apresentados. Se esquecer de um quadrado vermelho, clique no botão [Branco] para marcar onde o quadrado vermelho deve ir.

Algumas combinações terão mais problemas de simetria e quadrados vermelhos do que outras.
""",
"""
É importante que você faça o melhor possível nos problemas de simetria e na parte onde tiver que lembrar os quadrados vermelhos. 

Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas de simetria. Também lembre-se de acertar 85% dos problemas.

Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]
                   
# cor do feedback das operações matemáticas
symmetry_color = [0.0000, 0.0000, 0.0000]

# primeiro nome do participante
if expInfo["Nome Completo"] == "":
    first_name = "participante"
else:
    first_name = expInfo["Nome Completo"].strip().split()[0].title()

welcome_txt = f"""Olá, {first_name}! 

Agradecemos sua disponibilidade em colaborar com nossa pesquisa!

Clique em [Avançar] para iniciar."""

thanks_txt = f"""Esta atividade acabou, {first_name}.

Favor chamar o pesquisador! ☺"""



grid_example = "images/symm1_prac.jpg"
grid_opacity = 0
pos_y = 0.2

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.09, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
previous = visual.ImageStim(
    win=win,
    name='previous', units='norm', 
    image='images/previous_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
next = visual.ImageStim(
    win=win,
    name='next', units='norm', 
    image='images/next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
instr_resp = event.Mouse(win=win)
x, y = [None, None]
instr_resp.mouseClock = core.Clock()
symmetry_example = visual.ImageStim(
    win=win,
    name='symmetry_example', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0.05), size=(0.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "symmetry" ---
# Run 'Begin Experiment' code from symmetry_code
# cria lista de estímulos
grids = list()

for j in range(2):
    for i in range(1, 49):
        if i <= 24:
            grids.append((f"images/symm{i}.jpg", "symmetric", "yes"))
        else:
            grids.append((f"images/symm{i}.jpg", "asymmetric", "no"))

random.shuffle(grids)
    
# contador de grids
grid_count = 0

# contador de tentativas e acertos na tarefa de simetria
symmetry_total_trials = symmetry_trials_correct = speed_errors = 0
abort_trial = False # controla interrupção da tarefa de simetria

# contador de tempo no treino
symmetry_training_time = list()

symmetry_prompt = visual.TextStim(win=win, name='symmetry_prompt',
    text='Quando você tiver resolvido o problema, clique em [Continuar]',
    font='Times New Roman',
    units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_ = visual.ImageStim(
    win=win,
    name='continue_', units='norm', 
    image='images/continue_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
symmetry_problem_next = event.Mouse(win=win)
x, y = [None, None]
symmetry_problem_next.mouseClock = core.Clock()
symmetry_problem = visual.ImageStim(
    win=win,
    name='symmetry_problem', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0.2), size=(0.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "symmetry_answer" ---
symmetry_answer_screen = visual.TextStim(win=win, name='symmetry_answer_screen',
    text='A imagem é simétrica?',
    font='Times New Roman',
    units='norm', pos=(0, 0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
yes = visual.ImageStim(
    win=win,
    name='yes', units='norm', 
    image='images/yes_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
no = visual.ImageStim(
    win=win,
    name='no', units='norm', 
    image='images/no_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
symmetry_response = event.Mouse(win=win)
x, y = [None, None]
symmetry_response.mouseClock = core.Clock()

# --- Initialize components for Routine "symmetry_answer_feedback" ---
true_feedback = visual.ImageStim(
    win=win,
    name='true_feedback', units='norm', 
    image='images/yes_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
false_feedback = visual.ImageStim(
    win=win,
    name='false_feedback', units='norm', 
    image='images/no_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
symmetry_corrective_feedback_msg = visual.TextStim(win=win, name='symmetry_corrective_feedback_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color=[-1.0000, -1.0000, 0.0902], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
# índices de instruções
current_instruction = 0
instruction_block = 0
 
instruction_list = [# grid (memory) task
                   ["""
Neste experimento, você tentará memorizar quadrados vermelhos que você verá na tela enquanto você avalia se grades quadriculadas são simétricas em relação ao eixo vertical.

Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a tarefa de memória com os quadrados vermelhos.""",
"""
Para essa prática, quadrados vermelhos aparecerão em uma matriz, um de cada vez. Tente lembrar a posição de cada quadrado na ordem em que ele apareceu.

Depois que 2 quadrados aparecerem, você verá uma tela com 16 possíveis localizações dos quadrados. Seu trabalho é clicar na posição que cada quadrado apareceu na mesma ordem em que eles foram apresentados. 

Para fazer isso, use o mouse para clicar nos quadrados para selecioná-las. Os quadrados selecionados serão indicados por números, que representarão a sequência em que você clicou neles.""",
"""
Depois que selecionar todos os quadrados que compõem sua resposta, e eles estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.

Se errar sua resposta, aperte o botão [Limpar] para começar novamente. Se esquecer a posição de um dos quadrados, aperte o botão [Branco] para marcar a posição que o quadrado esquecido deve estar.

Lembre-se, é muito importante selecionar os quadrados na mesma ordem que foram apresentados. Se você esquecer um quadrado, use o botão [Branco] para marcar a sua posição.""",
"""
Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a prática com os quadrados.
"""], 
# distractor (symmetry) task
["""
Agora você irá praticar a tarefa de simetria deste experimento. Um grade quadriculada aparecerá na tela, tal como a exemplificada a seguir:
""",
"""
Sua tarefa será avaliar se a grade é simétrica em relação ao eixo vertical (que é representado abaixo pela linha vertical vermelha).
""",
"""
Note que a reta vertical vermelha foi anteriormente apresentada apenas para fins didáticos. Ela NÃO aparecerá durante a realização da tarefa.

Depois que tiver avaliado a simetria da grade quadriculada em relação ao eixo vertical, clique no botão [Continuar].
""",
"""
Em seguida, você deverá emitir uma resposta. Se a grade que você acabou de ver for simétrica, clique no botão [Sim]. 

Se a grade que você acabou de ver for assimétrica, clique no botão [Não].

Depois que clicar em um dos botões, o computador irá lhe dizer se fez a escolha certa.
""",
"""
Por exemplo, se você vir a grade abaixo, clique no botão [Sim], pois essa grade é simétrica.
""",
"""
Agora, se você vir a grade abaixo, clique no botão [Não], pois essa grade é assimétrica.
""",
"""
É muito importante que você consiga avaliar a simetria das grades quadriculadas corretamente. Também é importante que você consiga fazer essa avaliação o mais rapidamente possível.

Favor chamar o pesquisador se você tiver perguntas.

Quando você estiver pronto, clique em [Avançar] para começar a praticar.
"""],
# SYMSPAN training
["""
Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá avaliar a simetria de grades quadriculadas. Assim que decidir a sua resposta, um quadrado vermelho aparecerá na tela. Tente se lembrar da posição desse quadrado.

Na etapa anterior na qual você apenas avaliou a simetria de grades quadriculadas, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar pela grade quadriculada, pular a tela de resposta e contar o problema como erro.

Por isso é muito importante você resolver os problemas o mais rápido e corretamente possível.""",
"""
Depois que o quadrado vermelho desaparecer, outra grade quadriculada irá aparecer, e depois outro quadrado vermelho. No final de cada sequência, uma tela de resposta aparecerá na tela. Use o mouse para indicar as posições da sequência de quadrados vermelhos que acabou de ver.

Tente lembrar a ordem correta dos quadrados vermelhos. É muito importante que você trabalhe rapidamente e corretamente nas grades quadriculadas. Tenha certeza que você sabe a resposta do problema de simetria antes de ir para a próxima tela.

O computador não irá dizer se a resposta está correta. Depois da tela de resposta, você receberá o resultado do seu desempenho para o número quadrados vermelhos lembrados e a porcentagem de respostas corretas nos problemas de simetria.
""",
"""
Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas de simetria que você respondeu corretamente para o experimento inteiro.

É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas de simetria.

Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas de simetria E lembrar o máximo de quadrados vermelhos possíveis.

Favor chamar o pesquisador se tiver perguntas.
"""
],
# SYMSPAN testing
["""
Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.

Primeiro você terá que resolver um problema de simetria, depois terá que memorizar um quadrado vermelho. Quando ver a tela de resposta, indique as posições dos quadrados vermelhos na ordem em que foram apresentados. Se esquecer de um quadrado vermelho, clique no botão [Branco] para marcar onde o quadrado vermelho deve ir.

Algumas combinações terão mais problemas de simetria e quadrados vermelhos do que outras.
""",
"""
É importante que você faça o melhor possível nos problemas de simetria e na parte onde tiver que lembrar os quadrados vermelhos. 

Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas de simetria. Também lembre-se de acertar 85% dos problemas.

Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]
                   
# cor do feedback das operações matemáticas
symmetry_color = [0.0000, 0.0000, 0.0000]

# primeiro nome do participante
if expInfo["Nome Completo"] == "":
    first_name = "participante"
else:
    first_name = expInfo["Nome Completo"].strip().split()[0].title()

welcome_txt = f"""Olá, {first_name}! 

Agradecemos sua disponibilidade em colaborar com nossa pesquisa!

Clique em [Avançar] para iniciar."""

thanks_txt = f"""Esta atividade acabou, {first_name}.

Favor chamar o pesquisador! ☺"""



grid_example = "images/symm1_prac.jpg"
grid_opacity = 0
pos_y = 0.2

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.09, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
previous = visual.ImageStim(
    win=win,
    name='previous', units='norm', 
    image='images/previous_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
next = visual.ImageStim(
    win=win,
    name='next', units='norm', 
    image='images/next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
instr_resp = event.Mouse(win=win)
x, y = [None, None]
instr_resp.mouseClock = core.Clock()
symmetry_example = visual.ImageStim(
    win=win,
    name='symmetry_example', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0.05), size=(0.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "symmetry" ---
# Run 'Begin Experiment' code from symmetry_code
# cria lista de estímulos
grids = list()

for j in range(2):
    for i in range(1, 49):
        if i <= 24:
            grids.append((f"images/symm{i}.jpg", "symmetric", "yes"))
        else:
            grids.append((f"images/symm{i}.jpg", "asymmetric", "no"))

random.shuffle(grids)
    
# contador de grids
grid_count = 0

# contador de tentativas e acertos na tarefa de simetria
symmetry_total_trials = symmetry_trials_correct = speed_errors = 0
abort_trial = False # controla interrupção da tarefa de simetria

# contador de tempo no treino
symmetry_training_time = list()

symmetry_prompt = visual.TextStim(win=win, name='symmetry_prompt',
    text='Quando você tiver resolvido o problema, clique em [Continuar]',
    font='Times New Roman',
    units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_ = visual.ImageStim(
    win=win,
    name='continue_', units='norm', 
    image='images/continue_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
symmetry_problem_next = event.Mouse(win=win)
x, y = [None, None]
symmetry_problem_next.mouseClock = core.Clock()
symmetry_problem = visual.ImageStim(
    win=win,
    name='symmetry_problem', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0.2), size=(0.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "symmetry_answer" ---
symmetry_answer_screen = visual.TextStim(win=win, name='symmetry_answer_screen',
    text='A imagem é simétrica?',
    font='Times New Roman',
    units='norm', pos=(0, 0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
yes = visual.ImageStim(
    win=win,
    name='yes', units='norm', 
    image='images/yes_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
no = visual.ImageStim(
    win=win,
    name='no', units='norm', 
    image='images/no_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
symmetry_response = event.Mouse(win=win)
x, y = [None, None]
symmetry_response.mouseClock = core.Clock()

# --- Initialize components for Routine "grid_memory" ---
# Run 'Begin Experiment' code from grid_memory_code
fixed_grid_positions = [[-0.225, 0.225], [-0.075, 0.225], [0.075, 0.225], [0.225, 0.225],
                        [-0.225, 0.075], [-0.075, 0.075], [0.075, 0.075], [0.225, 0.075],  
                        [-0.225, -0.075], [-0.075, -0.075], [0.075, -0.075], [0.225, -0.075], 
                        [-0.225, -0.225], [-0.075, -0.225], [0.075, -0.225], [0.225, -0.225]
                        ]

grid_positions = [([-0.225, 0.225], "A"), ([-0.075, 0.225], "B"),
                  ([0.075, 0.225], "C"), ([0.225, 0.225], "D"),
                  ([-0.225, 0.075], "E"), ([-0.075, 0.075], "F"),
                  ([0.075, 0.075], "G"), ([0.225, 0.075], "H"),
                  ([-0.225, -0.075], "I"), ([-0.075, -0.075], "J"),
                  ([0.075, -0.075], "K"), ([0.225, -0.075], "L"),
                  ([-0.225, -0.225], "M"), ([-0.075, -0.225], "N"),
                  ([0.075, -0.225], "O"), ([0.225, -0.225], "P"),
                  ]

grid_positions_list = list()

for i in range(16):
    grid_positions_list.append("images/selected_square_0.jpg")
grid_memory_task = visual.ImageStim(
    win=win,
    name='grid_memory_task', units='height', 
    image='grid.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
square_position = visual.Rect(
    win=win, name='square_position',units='height', 
    width=(0.14, 0.14)[0], height=(0.14, 0.14)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=None, fillColor=[0.804,-1.000,-1.000],
    opacity=1, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "recall" ---
# Run 'Begin Experiment' code from code_recall
def EditDistanceScore(target, recall):
    """
    Recebe duas strings que serão comparadas. Retorna o edit distance score,
    que consiste em len(target) – distância de Damerau–Levenshtein. Se a substração resultar em 
    valor negativo, fixa valor em 0.
    """
    # se strings são idênticas
    if recall == target:
        return len(target) # edit distance = tamanho da string
    # se nada foi lembrado
    elif recall == "": # edit distance = 0
        return 0

    stimDict = {target[0]: "0"}

    for targetIndex in range(0, len(target)):
        if target[targetIndex] not in stimDict:
            stimDict[target[targetIndex]] = "0"

    for recallIndex in range(0, len(recall)):
        if recall[recallIndex] not in stimDict:
            stimDict[recall[recallIndex]] = "0"

    disMatrix = np.zeros(shape=(len(target) + 2, len(recall) + 2))

    inf = len(target) + len(recall)

    for targetIndex in range(0, len(target) + 1):
        disMatrix[targetIndex + 1, 0] = inf
        disMatrix[targetIndex + 1, 1] = targetIndex

    for recallIndex in range(0, len(recall)+1):
        disMatrix[0, recallIndex + 1] = inf
        disMatrix[1, recallIndex + 1] = recallIndex

    for targetIndex in range(1, len(target)+1):
        present = 0
        for recallIndex in range(1, len(recall) + 1):
            if recall[recallIndex-1] in stimDict:
                targetIndex2 = int(stimDict[recall[recallIndex - 1]])

            recallIndex2 = present
            cost = 1

            if target[targetIndex - 1] == recall[recallIndex - 1]:
                cost = 0
                present = recallIndex

            Substitution = disMatrix[targetIndex, recallIndex] + cost
            Insertion = disMatrix[targetIndex + 1, recallIndex] + 1
            Deletion = disMatrix[targetIndex, recallIndex + 1] + 1
            Transposition = disMatrix[targetIndex2, recallIndex2] + (targetIndex - targetIndex2 - 1) + 1 + (recallIndex - recallIndex2 - 1)

            if Substitution < Insertion and Substitution < Deletion and Substitution < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Substitution
            elif Insertion < Deletion and Insertion < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Insertion
            elif Deletion < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Deletion
            else:
                disMatrix[targetIndex + 1, recallIndex + 1] = Transposition


        stimDict[target[targetIndex - 1]] = str(targetIndex)

    # se edit distance < 0, fixa valor em zero
    if len(target) - disMatrix[len(target) + 1, len(recall) + 1] < 0:
        return 0
    # caso contrário, retorna o valor da medida
    else:
        return(int(len(target) - disMatrix[len(target) + 1, len(recall) + 1]))

def partial_credit(string1, string2):
    score = 0
    for letter1, letter2 in zip(string1, string2):
        if letter1 == letter2:
            score += 1
            
    return score

final_full_credit_score = final_partial_credit_score = final_edit_distance_score = 0


prompt_recall = visual.TextStim(win=win, name='prompt_recall',
    text='Selecione os quadrados na mesma ordem em que foram apresentadas. Use o botão [Branco] para preencher quadrados que esqueceu.',
    font='Times New Roman',
    units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
grid_recall = visual.ImageStim(
    win=win,
    name='grid_recall', units='height', 
    image='grid.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
A = visual.ImageStim(
    win=win,
    name='A', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
B = visual.ImageStim(
    win=win,
    name='B', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
C = visual.ImageStim(
    win=win,
    name='C', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[fixed_grid_positions[2]], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
D = visual.ImageStim(
    win=win,
    name='D', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
E = visual.ImageStim(
    win=win,
    name='E', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
F = visual.ImageStim(
    win=win,
    name='F', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
G = visual.ImageStim(
    win=win,
    name='G', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
H = visual.ImageStim(
    win=win,
    name='H', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
I = visual.ImageStim(
    win=win,
    name='I', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
J = visual.ImageStim(
    win=win,
    name='J', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
K = visual.ImageStim(
    win=win,
    name='K', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
L = visual.ImageStim(
    win=win,
    name='L', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
M = visual.ImageStim(
    win=win,
    name='M', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
N = visual.ImageStim(
    win=win,
    name='N', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
O = visual.ImageStim(
    win=win,
    name='O', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P = visual.ImageStim(
    win=win,
    name='P', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
clear_ = visual.ImageStim(
    win=win,
    name='clear_', units='norm', 
    image='images/clear_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
blank = visual.ImageStim(
    win=win,
    name='blank', units='norm', 
    image='images/blank_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
send = visual.ImageStim(
    win=win,
    name='send', units='norm', 
    image='images/send_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
recall_response = event.Mouse(win=win)
x, y = [None, None]
recall_response.mouseClock = core.Clock()

# --- Initialize components for Routine "recall_feedback" ---
recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
symmetry_feedback_prompt = visual.TextStim(win=win, name='symmetry_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
symmetry_feedback_performance = visual.TextStim(win=win, name='symmetry_feedback_performance',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.9, 0.9), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
# índices de instruções
current_instruction = 0
instruction_block = 0
 
instruction_list = [# grid (memory) task
                   ["""
Neste experimento, você tentará memorizar quadrados vermelhos que você verá na tela enquanto você avalia se grades quadriculadas são simétricas em relação ao eixo vertical.

Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a tarefa de memória com os quadrados vermelhos.""",
"""
Para essa prática, quadrados vermelhos aparecerão em uma matriz, um de cada vez. Tente lembrar a posição de cada quadrado na ordem em que ele apareceu.

Depois que 2 quadrados aparecerem, você verá uma tela com 16 possíveis localizações dos quadrados. Seu trabalho é clicar na posição que cada quadrado apareceu na mesma ordem em que eles foram apresentados. 

Para fazer isso, use o mouse para clicar nos quadrados para selecioná-las. Os quadrados selecionados serão indicados por números, que representarão a sequência em que você clicou neles.""",
"""
Depois que selecionar todos os quadrados que compõem sua resposta, e eles estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.

Se errar sua resposta, aperte o botão [Limpar] para começar novamente. Se esquecer a posição de um dos quadrados, aperte o botão [Branco] para marcar a posição que o quadrado esquecido deve estar.

Lembre-se, é muito importante selecionar os quadrados na mesma ordem que foram apresentados. Se você esquecer um quadrado, use o botão [Branco] para marcar a sua posição.""",
"""
Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a prática com os quadrados.
"""], 
# distractor (symmetry) task
["""
Agora você irá praticar a tarefa de simetria deste experimento. Um grade quadriculada aparecerá na tela, tal como a exemplificada a seguir:
""",
"""
Sua tarefa será avaliar se a grade é simétrica em relação ao eixo vertical (que é representado abaixo pela linha vertical vermelha).
""",
"""
Note que a reta vertical vermelha foi anteriormente apresentada apenas para fins didáticos. Ela NÃO aparecerá durante a realização da tarefa.

Depois que tiver avaliado a simetria da grade quadriculada em relação ao eixo vertical, clique no botão [Continuar].
""",
"""
Em seguida, você deverá emitir uma resposta. Se a grade que você acabou de ver for simétrica, clique no botão [Sim]. 

Se a grade que você acabou de ver for assimétrica, clique no botão [Não].

Depois que clicar em um dos botões, o computador irá lhe dizer se fez a escolha certa.
""",
"""
Por exemplo, se você vir a grade abaixo, clique no botão [Sim], pois essa grade é simétrica.
""",
"""
Agora, se você vir a grade abaixo, clique no botão [Não], pois essa grade é assimétrica.
""",
"""
É muito importante que você consiga avaliar a simetria das grades quadriculadas corretamente. Também é importante que você consiga fazer essa avaliação o mais rapidamente possível.

Favor chamar o pesquisador se você tiver perguntas.

Quando você estiver pronto, clique em [Avançar] para começar a praticar.
"""],
# SYMSPAN training
["""
Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá avaliar a simetria de grades quadriculadas. Assim que decidir a sua resposta, um quadrado vermelho aparecerá na tela. Tente se lembrar da posição desse quadrado.

Na etapa anterior na qual você apenas avaliou a simetria de grades quadriculadas, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar pela grade quadriculada, pular a tela de resposta e contar o problema como erro.

Por isso é muito importante você resolver os problemas o mais rápido e corretamente possível.""",
"""
Depois que o quadrado vermelho desaparecer, outra grade quadriculada irá aparecer, e depois outro quadrado vermelho. No final de cada sequência, uma tela de resposta aparecerá na tela. Use o mouse para indicar as posições da sequência de quadrados vermelhos que acabou de ver.

Tente lembrar a ordem correta dos quadrados vermelhos. É muito importante que você trabalhe rapidamente e corretamente nas grades quadriculadas. Tenha certeza que você sabe a resposta do problema de simetria antes de ir para a próxima tela.

O computador não irá dizer se a resposta está correta. Depois da tela de resposta, você receberá o resultado do seu desempenho para o número quadrados vermelhos lembrados e a porcentagem de respostas corretas nos problemas de simetria.
""",
"""
Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas de simetria que você respondeu corretamente para o experimento inteiro.

É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas de simetria.

Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas de simetria E lembrar o máximo de quadrados vermelhos possíveis.

Favor chamar o pesquisador se tiver perguntas.
"""
],
# SYMSPAN testing
["""
Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.

Primeiro você terá que resolver um problema de simetria, depois terá que memorizar um quadrado vermelho. Quando ver a tela de resposta, indique as posições dos quadrados vermelhos na ordem em que foram apresentados. Se esquecer de um quadrado vermelho, clique no botão [Branco] para marcar onde o quadrado vermelho deve ir.

Algumas combinações terão mais problemas de simetria e quadrados vermelhos do que outras.
""",
"""
É importante que você faça o melhor possível nos problemas de simetria e na parte onde tiver que lembrar os quadrados vermelhos. 

Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas de simetria. Também lembre-se de acertar 85% dos problemas.

Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]
                   
# cor do feedback das operações matemáticas
symmetry_color = [0.0000, 0.0000, 0.0000]

# primeiro nome do participante
if expInfo["Nome Completo"] == "":
    first_name = "participante"
else:
    first_name = expInfo["Nome Completo"].strip().split()[0].title()

welcome_txt = f"""Olá, {first_name}! 

Agradecemos sua disponibilidade em colaborar com nossa pesquisa!

Clique em [Avançar] para iniciar."""

thanks_txt = f"""Esta atividade acabou, {first_name}.

Favor chamar o pesquisador! ☺"""



grid_example = "images/symm1_prac.jpg"
grid_opacity = 0
pos_y = 0.2

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.09, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
previous = visual.ImageStim(
    win=win,
    name='previous', units='norm', 
    image='images/previous_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
next = visual.ImageStim(
    win=win,
    name='next', units='norm', 
    image='images/next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
instr_resp = event.Mouse(win=win)
x, y = [None, None]
instr_resp.mouseClock = core.Clock()
symmetry_example = visual.ImageStim(
    win=win,
    name='symmetry_example', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0.05), size=(0.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "symmetry" ---
# Run 'Begin Experiment' code from symmetry_code
# cria lista de estímulos
grids = list()

for j in range(2):
    for i in range(1, 49):
        if i <= 24:
            grids.append((f"images/symm{i}.jpg", "symmetric", "yes"))
        else:
            grids.append((f"images/symm{i}.jpg", "asymmetric", "no"))

random.shuffle(grids)
    
# contador de grids
grid_count = 0

# contador de tentativas e acertos na tarefa de simetria
symmetry_total_trials = symmetry_trials_correct = speed_errors = 0
abort_trial = False # controla interrupção da tarefa de simetria

# contador de tempo no treino
symmetry_training_time = list()

symmetry_prompt = visual.TextStim(win=win, name='symmetry_prompt',
    text='Quando você tiver resolvido o problema, clique em [Continuar]',
    font='Times New Roman',
    units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_ = visual.ImageStim(
    win=win,
    name='continue_', units='norm', 
    image='images/continue_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
symmetry_problem_next = event.Mouse(win=win)
x, y = [None, None]
symmetry_problem_next.mouseClock = core.Clock()
symmetry_problem = visual.ImageStim(
    win=win,
    name='symmetry_problem', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0.2), size=(0.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "symmetry_answer" ---
symmetry_answer_screen = visual.TextStim(win=win, name='symmetry_answer_screen',
    text='A imagem é simétrica?',
    font='Times New Roman',
    units='norm', pos=(0, 0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
yes = visual.ImageStim(
    win=win,
    name='yes', units='norm', 
    image='images/yes_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
no = visual.ImageStim(
    win=win,
    name='no', units='norm', 
    image='images/no_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
symmetry_response = event.Mouse(win=win)
x, y = [None, None]
symmetry_response.mouseClock = core.Clock()

# --- Initialize components for Routine "grid_memory" ---
# Run 'Begin Experiment' code from grid_memory_code
fixed_grid_positions = [[-0.225, 0.225], [-0.075, 0.225], [0.075, 0.225], [0.225, 0.225],
                        [-0.225, 0.075], [-0.075, 0.075], [0.075, 0.075], [0.225, 0.075],  
                        [-0.225, -0.075], [-0.075, -0.075], [0.075, -0.075], [0.225, -0.075], 
                        [-0.225, -0.225], [-0.075, -0.225], [0.075, -0.225], [0.225, -0.225]
                        ]

grid_positions = [([-0.225, 0.225], "A"), ([-0.075, 0.225], "B"),
                  ([0.075, 0.225], "C"), ([0.225, 0.225], "D"),
                  ([-0.225, 0.075], "E"), ([-0.075, 0.075], "F"),
                  ([0.075, 0.075], "G"), ([0.225, 0.075], "H"),
                  ([-0.225, -0.075], "I"), ([-0.075, -0.075], "J"),
                  ([0.075, -0.075], "K"), ([0.225, -0.075], "L"),
                  ([-0.225, -0.225], "M"), ([-0.075, -0.225], "N"),
                  ([0.075, -0.225], "O"), ([0.225, -0.225], "P"),
                  ]

grid_positions_list = list()

for i in range(16):
    grid_positions_list.append("images/selected_square_0.jpg")
grid_memory_task = visual.ImageStim(
    win=win,
    name='grid_memory_task', units='height', 
    image='grid.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
square_position = visual.Rect(
    win=win, name='square_position',units='height', 
    width=(0.14, 0.14)[0], height=(0.14, 0.14)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=None, fillColor=[0.804,-1.000,-1.000],
    opacity=1, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "recall" ---
# Run 'Begin Experiment' code from code_recall
def EditDistanceScore(target, recall):
    """
    Recebe duas strings que serão comparadas. Retorna o edit distance score,
    que consiste em len(target) – distância de Damerau–Levenshtein. Se a substração resultar em 
    valor negativo, fixa valor em 0.
    """
    # se strings são idênticas
    if recall == target:
        return len(target) # edit distance = tamanho da string
    # se nada foi lembrado
    elif recall == "": # edit distance = 0
        return 0

    stimDict = {target[0]: "0"}

    for targetIndex in range(0, len(target)):
        if target[targetIndex] not in stimDict:
            stimDict[target[targetIndex]] = "0"

    for recallIndex in range(0, len(recall)):
        if recall[recallIndex] not in stimDict:
            stimDict[recall[recallIndex]] = "0"

    disMatrix = np.zeros(shape=(len(target) + 2, len(recall) + 2))

    inf = len(target) + len(recall)

    for targetIndex in range(0, len(target) + 1):
        disMatrix[targetIndex + 1, 0] = inf
        disMatrix[targetIndex + 1, 1] = targetIndex

    for recallIndex in range(0, len(recall)+1):
        disMatrix[0, recallIndex + 1] = inf
        disMatrix[1, recallIndex + 1] = recallIndex

    for targetIndex in range(1, len(target)+1):
        present = 0
        for recallIndex in range(1, len(recall) + 1):
            if recall[recallIndex-1] in stimDict:
                targetIndex2 = int(stimDict[recall[recallIndex - 1]])

            recallIndex2 = present
            cost = 1

            if target[targetIndex - 1] == recall[recallIndex - 1]:
                cost = 0
                present = recallIndex

            Substitution = disMatrix[targetIndex, recallIndex] + cost
            Insertion = disMatrix[targetIndex + 1, recallIndex] + 1
            Deletion = disMatrix[targetIndex, recallIndex + 1] + 1
            Transposition = disMatrix[targetIndex2, recallIndex2] + (targetIndex - targetIndex2 - 1) + 1 + (recallIndex - recallIndex2 - 1)

            if Substitution < Insertion and Substitution < Deletion and Substitution < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Substitution
            elif Insertion < Deletion and Insertion < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Insertion
            elif Deletion < Transposition:
                disMatrix[targetIndex + 1, recallIndex + 1] = Deletion
            else:
                disMatrix[targetIndex + 1, recallIndex + 1] = Transposition


        stimDict[target[targetIndex - 1]] = str(targetIndex)

    # se edit distance < 0, fixa valor em zero
    if len(target) - disMatrix[len(target) + 1, len(recall) + 1] < 0:
        return 0
    # caso contrário, retorna o valor da medida
    else:
        return(int(len(target) - disMatrix[len(target) + 1, len(recall) + 1]))

def partial_credit(string1, string2):
    score = 0
    for letter1, letter2 in zip(string1, string2):
        if letter1 == letter2:
            score += 1
            
    return score

final_full_credit_score = final_partial_credit_score = final_edit_distance_score = 0


prompt_recall = visual.TextStim(win=win, name='prompt_recall',
    text='Selecione os quadrados na mesma ordem em que foram apresentadas. Use o botão [Branco] para preencher quadrados que esqueceu.',
    font='Times New Roman',
    units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
grid_recall = visual.ImageStim(
    win=win,
    name='grid_recall', units='height', 
    image='grid.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
A = visual.ImageStim(
    win=win,
    name='A', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
B = visual.ImageStim(
    win=win,
    name='B', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
C = visual.ImageStim(
    win=win,
    name='C', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[fixed_grid_positions[2]], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
D = visual.ImageStim(
    win=win,
    name='D', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
E = visual.ImageStim(
    win=win,
    name='E', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
F = visual.ImageStim(
    win=win,
    name='F', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
G = visual.ImageStim(
    win=win,
    name='G', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
H = visual.ImageStim(
    win=win,
    name='H', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
I = visual.ImageStim(
    win=win,
    name='I', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
J = visual.ImageStim(
    win=win,
    name='J', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
K = visual.ImageStim(
    win=win,
    name='K', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
L = visual.ImageStim(
    win=win,
    name='L', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
M = visual.ImageStim(
    win=win,
    name='M', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
N = visual.ImageStim(
    win=win,
    name='N', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
O = visual.ImageStim(
    win=win,
    name='O', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P = visual.ImageStim(
    win=win,
    name='P', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.14, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
clear_ = visual.ImageStim(
    win=win,
    name='clear_', units='norm', 
    image='images/clear_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
blank = visual.ImageStim(
    win=win,
    name='blank', units='norm', 
    image='images/blank_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
send = visual.ImageStim(
    win=win,
    name='send', units='norm', 
    image='images/send_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
recall_response = event.Mouse(win=win)
x, y = [None, None]
recall_response.mouseClock = core.Clock()

# --- Initialize components for Routine "recall_feedback" ---
recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
symmetry_feedback_prompt = visual.TextStim(win=win, name='symmetry_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
symmetry_feedback_performance = visual.TextStim(win=win, name='symmetry_feedback_performance',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.9, 0.9), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "thanks" ---
thanks_prompt = visual.TextStim(win=win, name='thanks_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
thanks_spacebar = visual.TextStim(win=win, name='thanks_spacebar',
    text='Pressione [BARRA DE ESPAÇO] para fechar a janela.',
    font='Times New Roman',
    units='norm', pos=(0, -0.8), height=0.07, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
thanks_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
# update component parameters for each repeat
welcome_msg.setText(welcome_txt)
# setup some python lists for storing info about the welcome_resp
welcome_resp.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
welcomeComponents = [welcome_msg, welcome_next, welcome_resp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_msg* updates
    if welcome_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_msg.frameNStart = frameN  # exact frame index
        welcome_msg.tStart = t  # local t and not account for scr refresh
        welcome_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_msg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_msg.started')
        welcome_msg.setAutoDraw(True)
    
    # *welcome_next* updates
    if welcome_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_next.frameNStart = frameN  # exact frame index
        welcome_next.tStart = t  # local t and not account for scr refresh
        welcome_next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_next, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_next.started')
        welcome_next.setAutoDraw(True)
    # *welcome_resp* updates
    if welcome_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('welcome_resp.started', t)
        welcome_resp.status = STARTED
        welcome_resp.mouseClock.reset()
        prevButtonState = welcome_resp.getPressed()  # if button is down already this ISN'T a new click
    if welcome_resp.status == STARTED:  # only update if started and not finished!
        buttons = welcome_resp.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(welcome_next)
                    clickableList = welcome_next
                except:
                    clickableList = [welcome_next]
                for obj in clickableList:
                    if obj.contains(welcome_resp):
                        gotValidClick = True
                        welcome_resp.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from welcome_code
thisExp.addData('participant_code', participant_code)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
grid_memory_instructions = data.TrialHandler(nReps=999, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='grid_memory_instructions')
thisExp.addLoop(grid_memory_instructions)  # add the loop to the experiment
thisGrid_memory_instruction = grid_memory_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGrid_memory_instruction.rgb)
if thisGrid_memory_instruction != None:
    for paramName in thisGrid_memory_instruction:
        exec('{} = thisGrid_memory_instruction[paramName]'.format(paramName))

for thisGrid_memory_instruction in grid_memory_instructions:
    currentLoop = grid_memory_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisGrid_memory_instruction.rgb)
    if thisGrid_memory_instruction != None:
        for paramName in thisGrid_memory_instruction:
            exec('{} = thisGrid_memory_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instr_code
    my_count = 0 # contador de tentativas da tarefa distratora
    instr_msg.setPos((0, pos_y))
    instr_msg.setText(instruction_list[instruction_block][current_instruction])
    # setup some python lists for storing info about the instr_resp
    instr_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    symmetry_example.setOpacity(grid_opacity)
    symmetry_example.setImage(grid_example)
    # keep track of which components have finished
    instructionComponents = [instr_msg, previous, next, instr_resp, symmetry_example]
    for thisComponent in instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_msg* updates
        if instr_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_msg.frameNStart = frameN  # exact frame index
            instr_msg.tStart = t  # local t and not account for scr refresh
            instr_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_msg.started')
            instr_msg.setAutoDraw(True)
        
        # *previous* updates
        if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            previous.frameNStart = frameN  # exact frame index
            previous.tStart = t  # local t and not account for scr refresh
            previous.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'previous.started')
            previous.setAutoDraw(True)
        
        # *next* updates
        if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next.frameNStart = frameN  # exact frame index
            next.tStart = t  # local t and not account for scr refresh
            next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next.started')
            next.setAutoDraw(True)
        # *instr_resp* updates
        if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('instr_resp.started', t)
            instr_resp.status = STARTED
            instr_resp.mouseClock.reset()
            prevButtonState = instr_resp.getPressed()  # if button is down already this ISN'T a new click
        if instr_resp.status == STARTED:  # only update if started and not finished!
            buttons = instr_resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([previous, next])
                        clickableList = [previous, next]
                    except:
                        clickableList = [[previous, next]]
                    for obj in clickableList:
                        if obj.contains(instr_resp):
                            gotValidClick = True
                            instr_resp.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *symmetry_example* updates
        if symmetry_example.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_example.frameNStart = frameN  # exact frame index
            symmetry_example.tStart = t  # local t and not account for scr refresh
            symmetry_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_example, 'tStartRefresh')  # time at next scr refresh
            symmetry_example.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from instr_code
    thisExp.addData('participant_code', participant_code)
    
    if instr_resp.clicked_name[0] == "previous":
        current_instruction -= 1
    elif instr_resp.clicked_name[0] == "next":
        current_instruction += 1
    
    # Se a instrução atual for -1
    if current_instruction == -1:
        # Resete o valor para ser 0
        current_instruction = 0
    # Se a instrução atual é igual ao comprimento da lista de instruções
    elif current_instruction == len(instruction_list[instruction_block]):
        current_instruction = 0 # zera contador de instruções
        if instruction_block == 0:
            instruction_block += 1
            grid_memory_instructions.finished = True # encerra o loop do treino da tarefa de memória
        elif instruction_block == 1:
            instruction_block += 1
            symmetry_instructions.finished = True # encerra o loop do treino da tarefa matemática
        elif instruction_block == 2:
            instruction_block += 1
            symspan_training_instructions.finished = True # encerra o loop de treino do OSPAN
        elif instruction_block == 3:
            instruction_block += 1
            symspan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
    
    # definindo se a imagem aparece nas instruções
    if (instruction_block == 1):
        if current_instruction in [0, 1, 4, 5]:
            grid_opacity = 1
            pos_y = 0.8
        else:
            grid_opacity = 0
            pos_y = 0.2
        
        if current_instruction != 5:
            grid_example = "images/symm1_prac.jpg"
        else:
            grid_example = "images/symm26_prac.jpg"
            
    if (instruction_block > 1):
        grid_opacity = 0
        pos_y = 0.2
    # store data for grid_memory_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999 repeats of 'grid_memory_instructions'


# set up handler to look after randomisation of conditions etc
grid_memory_practice_trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('span.xlsx', selection='0:1'),
    seed=None, name='grid_memory_practice_trials')
thisExp.addLoop(grid_memory_practice_trials)  # add the loop to the experiment
thisGrid_memory_practice_trial = grid_memory_practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGrid_memory_practice_trial.rgb)
if thisGrid_memory_practice_trial != None:
    for paramName in thisGrid_memory_practice_trial:
        exec('{} = thisGrid_memory_practice_trial[paramName]'.format(paramName))

for thisGrid_memory_practice_trial in grid_memory_practice_trials:
    currentLoop = grid_memory_practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisGrid_memory_practice_trial.rgb)
    if thisGrid_memory_practice_trial != None:
        for paramName in thisGrid_memory_practice_trial:
            exec('{} = thisGrid_memory_practice_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    grid_memory_practice = data.TrialHandler(nReps=current_span, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='grid_memory_practice')
    thisExp.addLoop(grid_memory_practice)  # add the loop to the experiment
    thisGrid_memory_practice = grid_memory_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGrid_memory_practice.rgb)
    if thisGrid_memory_practice != None:
        for paramName in thisGrid_memory_practice:
            exec('{} = thisGrid_memory_practice[paramName]'.format(paramName))
    
    for thisGrid_memory_practice in grid_memory_practice:
        currentLoop = grid_memory_practice
        # abbreviate parameter names if possible (e.g. rgb = thisGrid_memory_practice.rgb)
        if thisGrid_memory_practice != None:
            for paramName in thisGrid_memory_practice:
                exec('{} = thisGrid_memory_practice[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "grid_memory" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from grid_memory_code
        # tenta atribuir o valor da repetição do loop atual à variável index
        # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
        try:
            index = grid_memory_practice.thisN
        except:
            pass
            
        try:
            index = symspan_training_trial.thisN
        except:
            pass
        
        try:
            index = symspan_testing_trial.thisN
        except:
            pass
        
        # tenta embaralhar as posições do grid sempre que estivermos em uma nova tentativa
        try:
            # se é a primeira execução do loop...
            if grid_memory_practice.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if symspan_training_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if symspan_testing_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        
        except:
            pass
        
        
        
        square_position.setPos([correct_positions[index]])
        # keep track of which components have finished
        grid_memoryComponents = [grid_memory_task, square_position]
        for thisComponent in grid_memoryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "grid_memory" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *grid_memory_task* updates
            if grid_memory_task.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                grid_memory_task.frameNStart = frameN  # exact frame index
                grid_memory_task.tStart = t  # local t and not account for scr refresh
                grid_memory_task.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grid_memory_task, 'tStartRefresh')  # time at next scr refresh
                grid_memory_task.setAutoDraw(True)
            if grid_memory_task.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grid_memory_task.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    grid_memory_task.tStop = t  # not accounting for scr refresh
                    grid_memory_task.frameNStop = frameN  # exact frame index
                    grid_memory_task.setAutoDraw(False)
            
            # *square_position* updates
            if square_position.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_position.frameNStart = frameN  # exact frame index
                square_position.tStart = t  # local t and not account for scr refresh
                square_position.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_position, 'tStartRefresh')  # time at next scr refresh
                square_position.setAutoDraw(True)
            if square_position.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_position.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    square_position.tStop = t  # not accounting for scr refresh
                    square_position.frameNStop = frameN  # exact frame index
                    square_position.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in grid_memoryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "grid_memory" ---
        for thisComponent in grid_memoryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed current_span repeats of 'grid_memory_practice'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_recall
    clicked_things = []
    clicked_images = ["selected_square_1.jpg", "selected_square_2.jpg", "selected_square_3.jpg", "selected_square_4.jpg",
                      "selected_square_5.jpg", "selected_square_6.jpg", "selected_square_7.jpg", "selected_square_8.jpg",
                      "selected_square_9.jpg", "selected_square_10.jpg", "selected_square_11.jpg", "selected_square_12.jpg",
                      "selected_square_13.jpg", "selected_square_14.jpg", "selected_square_15.jpg", "selected_square_16.jpg"]
    
    clickables = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]
    allowed_send = False
    allowed_blank = True
    
    my_response = list()
    
    try:
        if grid_memory_practice_trials.thisN == 0:
            task_phase = "grid_memory_practice_phase"
    except:
        pass
    
    try:
        if symspan_training_trials.thisN == 0:
            task_phase = "symspan_training_trials"
    except:
        pass
    
    try:
        if symspan_testing_trials.thisN == 0:
            task_phase = "symspan_testing_trials"
    except:
        pass
    
    
    A.setPos([fixed_grid_positions[0]])
    A.setImage(grid_positions_list[0])
    B.setPos([fixed_grid_positions[1]])
    B.setImage(grid_positions_list[1])
    C.setImage(grid_positions_list[2])
    D.setPos([fixed_grid_positions[3]])
    D.setImage(grid_positions_list[3])
    E.setPos([fixed_grid_positions[4]])
    E.setImage(grid_positions_list[4])
    F.setPos([fixed_grid_positions[5]])
    F.setImage(grid_positions_list[5])
    G.setPos([fixed_grid_positions[6]])
    G.setImage(grid_positions_list[6])
    H.setPos([fixed_grid_positions[7]])
    H.setImage(grid_positions_list[7])
    I.setPos([fixed_grid_positions[8]])
    I.setImage(grid_positions_list[8])
    J.setPos([fixed_grid_positions[9]])
    J.setImage(grid_positions_list[9])
    K.setPos([fixed_grid_positions[10]])
    K.setImage(grid_positions_list[10])
    L.setPos([fixed_grid_positions[11]])
    L.setImage(grid_positions_list[11])
    M.setPos([fixed_grid_positions[12]])
    M.setImage(grid_positions_list[12])
    N.setPos([fixed_grid_positions[13]])
    N.setImage(grid_positions_list[13])
    O.setPos([fixed_grid_positions[14]])
    O.setImage(grid_positions_list[14])
    P.setPos([fixed_grid_positions[15]])
    P.setImage(grid_positions_list[15])
    # setup some python lists for storing info about the recall_response
    recall_response.x = []
    recall_response.y = []
    recall_response.leftButton = []
    recall_response.midButton = []
    recall_response.rightButton = []
    recall_response.time = []
    recall_response.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    recallComponents = [prompt_recall, grid_recall, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, clear_, blank, send, recall_response]
    for thisComponent in recallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "recall" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_recall
        for i, clickable in enumerate(clickables):
            # and it was the blank button:
            if recall_response.isPressedIn(clickable) and (clickable == blank) and (allowed_blank == True):
                if len(clicked_things) <= 15:
                    clicked_things.append(clickable.name)
                    # to prevent two consecutive responses
                    allowed_blank = False 
                    blank_clock = core.Clock() 
                    #clicked_things.append(clickable.name)
                    my_response.append("–")
                    allowed_send = True
            # if a button was pressed in
            elif recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                # and it wasn't send, clear_, and blank buttons
                if (clickable != send) and (clickable != clear_) and (clickable != blank):
                    if len(clicked_things) <= 15:
                        clicked_things.append(clickable.name)
                        clickable.setImage(f"images/{clicked_images[len(clicked_things) - 1]}.jpg", log = False)
                        my_response.append(clickable.name)
                        allowed_send = True
                # and it was the clear_ button
                elif clickable == clear_:
                    for i, clickable in enumerate(clickables[:-3]):
                        clickable.setImage(f"images/selected_square_0.jpg", log = False)
                    # reset values
                    clicked_things = []
                    my_response = list()
                    allowed_send = False # reset
                elif (clickable == send) and (allowed_send == True):
                    continueRoutine = False
        
        # it allows the blank button again
        try:
            if blank_clock.getTime() > 1:
                allowed_blank = True
        except NameError:
            pass
        
        # *prompt_recall* updates
        if prompt_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_recall.frameNStart = frameN  # exact frame index
            prompt_recall.tStart = t  # local t and not account for scr refresh
            prompt_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_recall, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_recall.started')
            prompt_recall.setAutoDraw(True)
        
        # *grid_recall* updates
        if grid_recall.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            grid_recall.frameNStart = frameN  # exact frame index
            grid_recall.tStart = t  # local t and not account for scr refresh
            grid_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grid_recall, 'tStartRefresh')  # time at next scr refresh
            grid_recall.setAutoDraw(True)
        
        # *A* updates
        if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A.frameNStart = frameN  # exact frame index
            A.tStart = t  # local t and not account for scr refresh
            A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A.started')
            A.setAutoDraw(True)
        
        # *B* updates
        if B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B.frameNStart = frameN  # exact frame index
            B.tStart = t  # local t and not account for scr refresh
            B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'B.started')
            B.setAutoDraw(True)
        
        # *C* updates
        if C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C.frameNStart = frameN  # exact frame index
            C.tStart = t  # local t and not account for scr refresh
            C.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'C.started')
            C.setAutoDraw(True)
        
        # *D* updates
        if D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D.frameNStart = frameN  # exact frame index
            D.tStart = t  # local t and not account for scr refresh
            D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D.started')
            D.setAutoDraw(True)
        
        # *E* updates
        if E.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E.frameNStart = frameN  # exact frame index
            E.tStart = t  # local t and not account for scr refresh
            E.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'E.started')
            E.setAutoDraw(True)
        
        # *F* updates
        if F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F.frameNStart = frameN  # exact frame index
            F.tStart = t  # local t and not account for scr refresh
            F.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'F.started')
            F.setAutoDraw(True)
        
        # *G* updates
        if G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            G.frameNStart = frameN  # exact frame index
            G.tStart = t  # local t and not account for scr refresh
            G.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(G, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'G.started')
            G.setAutoDraw(True)
        
        # *H* updates
        if H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            H.frameNStart = frameN  # exact frame index
            H.tStart = t  # local t and not account for scr refresh
            H.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(H, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'H.started')
            H.setAutoDraw(True)
        
        # *I* updates
        if I.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            I.frameNStart = frameN  # exact frame index
            I.tStart = t  # local t and not account for scr refresh
            I.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(I, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'I.started')
            I.setAutoDraw(True)
        
        # *J* updates
        if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J.frameNStart = frameN  # exact frame index
            J.tStart = t  # local t and not account for scr refresh
            J.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'J.started')
            J.setAutoDraw(True)
        
        # *K* updates
        if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            K.frameNStart = frameN  # exact frame index
            K.tStart = t  # local t and not account for scr refresh
            K.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'K.started')
            K.setAutoDraw(True)
        
        # *L* updates
        if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L.frameNStart = frameN  # exact frame index
            L.tStart = t  # local t and not account for scr refresh
            L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L.started')
            L.setAutoDraw(True)
        
        # *M* updates
        if M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            M.frameNStart = frameN  # exact frame index
            M.tStart = t  # local t and not account for scr refresh
            M.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(M, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'M.started')
            M.setAutoDraw(True)
        
        # *N* updates
        if N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            N.frameNStart = frameN  # exact frame index
            N.tStart = t  # local t and not account for scr refresh
            N.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(N, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'N.started')
            N.setAutoDraw(True)
        
        # *O* updates
        if O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            O.frameNStart = frameN  # exact frame index
            O.tStart = t  # local t and not account for scr refresh
            O.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(O, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'O.started')
            O.setAutoDraw(True)
        
        # *P* updates
        if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P.frameNStart = frameN  # exact frame index
            P.tStart = t  # local t and not account for scr refresh
            P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P.started')
            P.setAutoDraw(True)
        
        # *clear_* updates
        if clear_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clear_.frameNStart = frameN  # exact frame index
            clear_.tStart = t  # local t and not account for scr refresh
            clear_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clear_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'clear_.started')
            clear_.setAutoDraw(True)
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank.started')
            blank.setAutoDraw(True)
        
        # *send* updates
        if send.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            send.frameNStart = frameN  # exact frame index
            send.tStart = t  # local t and not account for scr refresh
            send.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(send, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'send.started')
            send.setAutoDraw(True)
        # *recall_response* updates
        if recall_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_response.frameNStart = frameN  # exact frame index
            recall_response.tStart = t  # local t and not account for scr refresh
            recall_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('recall_response.started', t)
            recall_response.status = STARTED
            recall_response.mouseClock.reset()
            prevButtonState = recall_response.getPressed()  # if button is down already this ISN'T a new click
        if recall_response.status == STARTED:  # only update if started and not finished!
            buttons = recall_response.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank])
                        clickableList = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]
                    except:
                        clickableList = [[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]]
                    for obj in clickableList:
                        if obj.contains(recall_response):
                            gotValidClick = True
                            recall_response.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = recall_response.getPos()
                        recall_response.x.append(x)
                        recall_response.y.append(y)
                        buttons = recall_response.getPressed()
                        recall_response.leftButton.append(buttons[0])
                        recall_response.midButton.append(buttons[1])
                        recall_response.rightButton.append(buttons[2])
                        recall_response.time.append(recall_response.mouseClock.getTime())
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recall" ---
    for thisComponent in recallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_recall
    # juntando respostas, mas eliminando respostas repetidas e "send"
    participant_response = "".join(my_response)
    
    # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
    if participant_response == correct_response:
        full_credit_score = current_span
    else:
        full_credit_score = 0
    
    # crédito parcial (pontua apenas acertos na mesma posição serial)
    partial_credit_score = partial_credit(participant_response, correct_response)
    
    # edit distance score
    edit_distance_score = EditDistanceScore(correct_response, participant_response)
    
    # créditos completo parcial e edit distance, somatório da sessão (máx. 42)
    try:
        if symspan_testing_trials.thisN >= 0:
            final_full_credit_score += full_credit_score
            final_partial_credit_score += partial_credit_score
            final_edit_distance_score += edit_distance_score
    except:
        pass
    
    # criando texto para feedback
    if partial_credit_score > 1:
        word = "quadrados"    
    elif partial_credit_score <= 1:
        word = "quadrado"
    
    # mensagens de feedback de recordação e das operações matemáticas
    recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
    
    try:
        symmetry_percent_correct = (symmetry_trials_correct / symmetry_total_trials) * 100
    except ZeroDivisionError:
        symmetry_percent_correct = 0
    
    symmetry_performance_msg = f"{symmetry_percent_correct:.0f}%"
    
    try:
        if symmetry_errors > 1:
            symmetry_feedback_msg = f"Você cometeu {symmetry_errors} erros neste conjunto de tentativas" 
        elif symmetry_errors == 1:
            symmetry_feedback_msg = f"Você cometeu {symmetry_errors} erro neste conjunto de tentativas"
        else:
            symmetry_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
    except:
        symmetry_feedback_msg = ""
       
    # salva respostas
    thisExp.addData("correct_response", correct_response)
    thisExp.addData("participant_response", participant_response)
    thisExp.addData("full_credit_score", full_credit_score)
    thisExp.addData("partial_credit_score", partial_credit_score)
    thisExp.addData("edit_distance_score", edit_distance_score)
    thisExp.addData("task_phase", task_phase)
    thisExp.addData("symmetry_trials_correct", symmetry_trials_correct)
    thisExp.addData("symmetry_total_trials", symmetry_total_trials)
    thisExp.addData("symmetry_percent_correct", symmetry_percent_correct)
    try:
        thisExp.addData("symmetry_errors", symmetry_errors)
    except:
        pass
    
    # store data for grid_memory_practice_trials (TrialHandler)
    grid_memory_practice_trials.addData('recall_response.x', recall_response.x)
    grid_memory_practice_trials.addData('recall_response.y', recall_response.y)
    grid_memory_practice_trials.addData('recall_response.leftButton', recall_response.leftButton)
    grid_memory_practice_trials.addData('recall_response.midButton', recall_response.midButton)
    grid_memory_practice_trials.addData('recall_response.rightButton', recall_response.rightButton)
    grid_memory_practice_trials.addData('recall_response.time', recall_response.time)
    grid_memory_practice_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "recall_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    recall_feedback_prompt.setText(recall_feedback_msg)
    symmetry_feedback_prompt.setText(symmetry_feedback_msg)
    symmetry_feedback_performance.setColor(symmetry_color, colorSpace='rgb')
    symmetry_feedback_performance.setText(symmetry_performance_msg)
    # keep track of which components have finished
    recall_feedbackComponents = [recall_feedback_prompt, symmetry_feedback_prompt, symmetry_feedback_performance]
    for thisComponent in recall_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "recall_feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_feedback_prompt* updates
        if recall_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_feedback_prompt.frameNStart = frameN  # exact frame index
            recall_feedback_prompt.tStart = t  # local t and not account for scr refresh
            recall_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_feedback_prompt.started')
            recall_feedback_prompt.setAutoDraw(True)
        if recall_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recall_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                recall_feedback_prompt.tStop = t  # not accounting for scr refresh
                recall_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_feedback_prompt.stopped')
                recall_feedback_prompt.setAutoDraw(False)
        
        # *symmetry_feedback_prompt* updates
        if symmetry_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_feedback_prompt.frameNStart = frameN  # exact frame index
            symmetry_feedback_prompt.tStart = t  # local t and not account for scr refresh
            symmetry_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_feedback_prompt.started')
            symmetry_feedback_prompt.setAutoDraw(True)
        if symmetry_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > symmetry_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                symmetry_feedback_prompt.tStop = t  # not accounting for scr refresh
                symmetry_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_feedback_prompt.stopped')
                symmetry_feedback_prompt.setAutoDraw(False)
        
        # *symmetry_feedback_performance* updates
        if symmetry_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_feedback_performance.frameNStart = frameN  # exact frame index
            symmetry_feedback_performance.tStart = t  # local t and not account for scr refresh
            symmetry_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_feedback_performance, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_feedback_performance.started')
            symmetry_feedback_performance.setAutoDraw(True)
        if symmetry_feedback_performance.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > symmetry_feedback_performance.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                symmetry_feedback_performance.tStop = t  # not accounting for scr refresh
                symmetry_feedback_performance.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_feedback_performance.stopped')
                symmetry_feedback_performance.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recall_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recall_feedback" ---
    for thisComponent in recall_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'grid_memory_practice_trials'


# set up handler to look after randomisation of conditions etc
symmetry_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='symmetry_instructions')
thisExp.addLoop(symmetry_instructions)  # add the loop to the experiment
thisSymmetry_instruction = symmetry_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSymmetry_instruction.rgb)
if thisSymmetry_instruction != None:
    for paramName in thisSymmetry_instruction:
        exec('{} = thisSymmetry_instruction[paramName]'.format(paramName))

for thisSymmetry_instruction in symmetry_instructions:
    currentLoop = symmetry_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisSymmetry_instruction.rgb)
    if thisSymmetry_instruction != None:
        for paramName in thisSymmetry_instruction:
            exec('{} = thisSymmetry_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instr_code
    my_count = 0 # contador de tentativas da tarefa distratora
    instr_msg.setPos((0, pos_y))
    instr_msg.setText(instruction_list[instruction_block][current_instruction])
    # setup some python lists for storing info about the instr_resp
    instr_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    symmetry_example.setOpacity(grid_opacity)
    symmetry_example.setImage(grid_example)
    # keep track of which components have finished
    instructionComponents = [instr_msg, previous, next, instr_resp, symmetry_example]
    for thisComponent in instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_msg* updates
        if instr_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_msg.frameNStart = frameN  # exact frame index
            instr_msg.tStart = t  # local t and not account for scr refresh
            instr_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_msg.started')
            instr_msg.setAutoDraw(True)
        
        # *previous* updates
        if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            previous.frameNStart = frameN  # exact frame index
            previous.tStart = t  # local t and not account for scr refresh
            previous.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'previous.started')
            previous.setAutoDraw(True)
        
        # *next* updates
        if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next.frameNStart = frameN  # exact frame index
            next.tStart = t  # local t and not account for scr refresh
            next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next.started')
            next.setAutoDraw(True)
        # *instr_resp* updates
        if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('instr_resp.started', t)
            instr_resp.status = STARTED
            instr_resp.mouseClock.reset()
            prevButtonState = instr_resp.getPressed()  # if button is down already this ISN'T a new click
        if instr_resp.status == STARTED:  # only update if started and not finished!
            buttons = instr_resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([previous, next])
                        clickableList = [previous, next]
                    except:
                        clickableList = [[previous, next]]
                    for obj in clickableList:
                        if obj.contains(instr_resp):
                            gotValidClick = True
                            instr_resp.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *symmetry_example* updates
        if symmetry_example.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_example.frameNStart = frameN  # exact frame index
            symmetry_example.tStart = t  # local t and not account for scr refresh
            symmetry_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_example, 'tStartRefresh')  # time at next scr refresh
            symmetry_example.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from instr_code
    thisExp.addData('participant_code', participant_code)
    
    if instr_resp.clicked_name[0] == "previous":
        current_instruction -= 1
    elif instr_resp.clicked_name[0] == "next":
        current_instruction += 1
    
    # Se a instrução atual for -1
    if current_instruction == -1:
        # Resete o valor para ser 0
        current_instruction = 0
    # Se a instrução atual é igual ao comprimento da lista de instruções
    elif current_instruction == len(instruction_list[instruction_block]):
        current_instruction = 0 # zera contador de instruções
        if instruction_block == 0:
            instruction_block += 1
            grid_memory_instructions.finished = True # encerra o loop do treino da tarefa de memória
        elif instruction_block == 1:
            instruction_block += 1
            symmetry_instructions.finished = True # encerra o loop do treino da tarefa matemática
        elif instruction_block == 2:
            instruction_block += 1
            symspan_training_instructions.finished = True # encerra o loop de treino do OSPAN
        elif instruction_block == 3:
            instruction_block += 1
            symspan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
    
    # definindo se a imagem aparece nas instruções
    if (instruction_block == 1):
        if current_instruction in [0, 1, 4, 5]:
            grid_opacity = 1
            pos_y = 0.8
        else:
            grid_opacity = 0
            pos_y = 0.2
        
        if current_instruction != 5:
            grid_example = "images/symm1_prac.jpg"
        else:
            grid_example = "images/symm26_prac.jpg"
            
    if (instruction_block > 1):
        grid_opacity = 0
        pos_y = 0.2
    # store data for symmetry_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'symmetry_instructions'


# set up handler to look after randomisation of conditions etc
symmetry_practice_trials = data.TrialHandler(nReps=15.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='symmetry_practice_trials')
thisExp.addLoop(symmetry_practice_trials)  # add the loop to the experiment
thisSymmetry_practice_trial = symmetry_practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSymmetry_practice_trial.rgb)
if thisSymmetry_practice_trial != None:
    for paramName in thisSymmetry_practice_trial:
        exec('{} = thisSymmetry_practice_trial[paramName]'.format(paramName))

for thisSymmetry_practice_trial in symmetry_practice_trials:
    currentLoop = symmetry_practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSymmetry_practice_trial.rgb)
    if thisSymmetry_practice_trial != None:
        for paramName in thisSymmetry_practice_trial:
            exec('{} = thisSymmetry_practice_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "symmetry" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from symmetry_code
    symmetry_clock = core.Clock()
    
    try:
        # se é a primeira execução do loop...
        if symmetry_practice_trials.thisN == 0:
            symmetry_color = "red" # agora teremos feedback na cor vermelha
            symmetry_errors = 0
    except:
        pass
        
    try:
        # se é a primeira execução do loop...
        if symspan_training_trial.thisN == 0:
            symmetry_errors = 0
    except:
        pass
        
    try:
        # se é a primeira execução do loop...
        if symspan_testing_trial.thisN == 0:
            symmetry_errors = 0
    except:
        pass
        
    # reseta os contadores quando começa o SYMSPAN para valer
    try:
        if (symspan_testing_trials.thisN == 0) and (symspan_testing_trial.thisN == 0):
            symmetry_total_trials = symmetry_trials_correct = speed_errors = 0
    except:
        pass
    # setup some python lists for storing info about the symmetry_problem_next
    symmetry_problem_next.clicked_name = []
    gotValidClick = False  # until a click is received
    symmetry_problem.setImage(grids[grid_count][0])
    # keep track of which components have finished
    symmetryComponents = [symmetry_prompt, continue_, symmetry_problem_next, symmetry_problem]
    for thisComponent in symmetryComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "symmetry" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from symmetry_code
        try:
            # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
            if symmetry_clock.getTime() >= symmetry_criterion:
                speed_errors += 1
                abort_trial = True
                continueRoutine = False
        except:
            pass
          
        
        # *symmetry_prompt* updates
        if symmetry_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_prompt.frameNStart = frameN  # exact frame index
            symmetry_prompt.tStart = t  # local t and not account for scr refresh
            symmetry_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_prompt.started')
            symmetry_prompt.setAutoDraw(True)
        
        # *continue_* updates
        if continue_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            continue_.frameNStart = frameN  # exact frame index
            continue_.tStart = t  # local t and not account for scr refresh
            continue_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_.started')
            continue_.setAutoDraw(True)
        # *symmetry_problem_next* updates
        if symmetry_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_problem_next.frameNStart = frameN  # exact frame index
            symmetry_problem_next.tStart = t  # local t and not account for scr refresh
            symmetry_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_problem_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('symmetry_problem_next.started', t)
            symmetry_problem_next.status = STARTED
            symmetry_problem_next.mouseClock.reset()
            prevButtonState = symmetry_problem_next.getPressed()  # if button is down already this ISN'T a new click
        if symmetry_problem_next.status == STARTED:  # only update if started and not finished!
            buttons = symmetry_problem_next.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(continue_)
                        clickableList = continue_
                    except:
                        clickableList = [continue_]
                    for obj in clickableList:
                        if obj.contains(symmetry_problem_next):
                            gotValidClick = True
                            symmetry_problem_next.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *symmetry_problem* updates
        if symmetry_problem.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_problem.frameNStart = frameN  # exact frame index
            symmetry_problem.tStart = t  # local t and not account for scr refresh
            symmetry_problem.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_problem, 'tStartRefresh')  # time at next scr refresh
            symmetry_problem.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in symmetryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "symmetry" ---
    for thisComponent in symmetryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from symmetry_code
    # salva variáveis
    thisExp.addData("symmetry_problem", grids[grid_count][0]) # nome da imagem
    thisExp.addData("symmetry_status", grids[grid_count][1]) # symmetric vs. asymmetric
    thisExp.addData("symmetry_corr", grids[grid_count][2]) # gabarito
    
    if abort_trial:
        symmetry_speed_error = 1 # abortou devido a velocidade
    else:
        symmetry_speed_error = 0 # abortou devido a velocidade
    
    try:
        thisExp.addData("problem_rt", symmetry_clock.getTime()) # problem RT
    except:
        pass
    
    # store data for symmetry_practice_trials (TrialHandler)
    # the Routine "symmetry" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "symmetry_answer" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from symmetry_answer_code
    answer_clock = core.Clock()
    
    if abort_trial:
        continueRoutine = False
    # setup some python lists for storing info about the symmetry_response
    symmetry_response.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    symmetry_answerComponents = [symmetry_answer_screen, yes, no, symmetry_response]
    for thisComponent in symmetry_answerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "symmetry_answer" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from symmetry_answer_code
        try:
            # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
            if symmetry_clock.getTime() >= symmetry_criterion:
                speed_errors += 1
                abort_trial = True
                continueRoutine = False
        except:
            pass
        
        
        # *symmetry_answer_screen* updates
        if symmetry_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_answer_screen.frameNStart = frameN  # exact frame index
            symmetry_answer_screen.tStart = t  # local t and not account for scr refresh
            symmetry_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_answer_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_answer_screen.started')
            symmetry_answer_screen.setAutoDraw(True)
        
        # *yes* updates
        if yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yes.frameNStart = frameN  # exact frame index
            yes.tStart = t  # local t and not account for scr refresh
            yes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'yes.started')
            yes.setAutoDraw(True)
        
        # *no* updates
        if no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no.frameNStart = frameN  # exact frame index
            no.tStart = t  # local t and not account for scr refresh
            no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'no.started')
            no.setAutoDraw(True)
        # *symmetry_response* updates
        if symmetry_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_response.frameNStart = frameN  # exact frame index
            symmetry_response.tStart = t  # local t and not account for scr refresh
            symmetry_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('symmetry_response.started', t)
            symmetry_response.status = STARTED
            symmetry_response.mouseClock.reset()
            prevButtonState = symmetry_response.getPressed()  # if button is down already this ISN'T a new click
        if symmetry_response.status == STARTED:  # only update if started and not finished!
            buttons = symmetry_response.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([yes, no])
                        clickableList = [yes, no]
                    except:
                        clickableList = [[yes, no]]
                    for obj in clickableList:
                        if obj.contains(symmetry_response):
                            gotValidClick = True
                            symmetry_response.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in symmetry_answerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "symmetry_answer" ---
    for thisComponent in symmetry_answerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from symmetry_answer_code
    try:
        if symmetry_response.clicked_name[0] == "yes":
            symmetry_participant_response = "yes"
        else:
            symmetry_participant_response = "no"
    except:
        symmetry_participant_response = ""
        symmetry_speed_error = 1
    
    try:
        thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
    except:
        pass
    
    # se o participante acertou
    if symmetry_participant_response == grids[grid_count][2]:
        symmetry_participant_corr = 1
        symmetry_accuracy_error = 0 # contagem de erros de acurácia
        symmetry_trials_correct += 1 # incrementa número de acertos da sessão toda
        symmetry_corrective_feedback = "Correto"
    else:
        symmetry_participant_corr = 0
        symmetry_corrective_feedback = "Incorreto"
        symmetry_errors += 1 # incrementa o número de erros apenas da presente tentativa
    
        if symmetry_speed_error == 0:
            symmetry_accuracy_error = 1
        else:
            symmetry_accuracy_error = 0
    
    # sempre incrementa o contador de tentativas
    symmetry_total_trials += 1
    
    if abort_trial:
        thisExp.addData("symmetry_speed_error", 1) # erro de velocidade
        abort_trial = False # reseta para a próxima tentativa
    else:
        thisExp.addData("symmetry_speed_error", 0)
    
    # salva variáveis
    thisExp.addData("symmetry_accuracy_error", symmetry_accuracy_error) # erro de acurácia
    thisExp.addData("symmetry_participant_corr", symmetry_participant_corr) # 1 = acerto, 0 = erro
    thisExp.addData("symmetry_problem", grids[grid_count][0]) # enunciado
    thisExp.addData("symmetry_status", grids[grid_count][1]) # gabarito
    thisExp.addData("symmetry_corr", grids[grid_count][2]) # resposta correta
    thisExp.addData("symmetry_participant_response", symmetry_participant_response) # resposta do participante
    
    # incrementa operação para próxima iteração
    grid_count += 1
    
    # soma a duração da tarefa matemática
    try:
        if symmetry_practice_trials.thisN < 15:
            symmetry_training_time.append(symmetry_clock.getTime()) # e guarda tempo em uma lista
            # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
            if symmetry_practice_trials.thisN == 14:
                symmetry_time_mean = np.mean(np.array(symmetry_training_time))
                symmetry_time_sd = np.std(np.array(symmetry_training_time), ddof = 1)
                symmetry_criterion = symmetry_time_mean + 2 * symmetry_time_sd
                
    except:
        pass
    
    # store data for symmetry_practice_trials (TrialHandler)
    # the Routine "symmetry_answer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "symmetry_answer_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    symmetry_corrective_feedback_msg.setText(symmetry_corrective_feedback)
    # keep track of which components have finished
    symmetry_answer_feedbackComponents = [true_feedback, false_feedback, symmetry_corrective_feedback_msg]
    for thisComponent in symmetry_answer_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "symmetry_answer_feedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *true_feedback* updates
        if true_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            true_feedback.frameNStart = frameN  # exact frame index
            true_feedback.tStart = t  # local t and not account for scr refresh
            true_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(true_feedback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'true_feedback.started')
            true_feedback.setAutoDraw(True)
        if true_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > true_feedback.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                true_feedback.tStop = t  # not accounting for scr refresh
                true_feedback.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'true_feedback.stopped')
                true_feedback.setAutoDraw(False)
        
        # *false_feedback* updates
        if false_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            false_feedback.frameNStart = frameN  # exact frame index
            false_feedback.tStart = t  # local t and not account for scr refresh
            false_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(false_feedback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'false_feedback.started')
            false_feedback.setAutoDraw(True)
        if false_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > false_feedback.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                false_feedback.tStop = t  # not accounting for scr refresh
                false_feedback.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'false_feedback.stopped')
                false_feedback.setAutoDraw(False)
        
        # *symmetry_corrective_feedback_msg* updates
        if symmetry_corrective_feedback_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_corrective_feedback_msg.frameNStart = frameN  # exact frame index
            symmetry_corrective_feedback_msg.tStart = t  # local t and not account for scr refresh
            symmetry_corrective_feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_corrective_feedback_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_corrective_feedback_msg.started')
            symmetry_corrective_feedback_msg.setAutoDraw(True)
        if symmetry_corrective_feedback_msg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > symmetry_corrective_feedback_msg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                symmetry_corrective_feedback_msg.tStop = t  # not accounting for scr refresh
                symmetry_corrective_feedback_msg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_corrective_feedback_msg.stopped')
                symmetry_corrective_feedback_msg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in symmetry_answer_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "symmetry_answer_feedback" ---
    for thisComponent in symmetry_answer_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 15.0 repeats of 'symmetry_practice_trials'


# set up handler to look after randomisation of conditions etc
symspan_training_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='symspan_training_instructions')
thisExp.addLoop(symspan_training_instructions)  # add the loop to the experiment
thisSymspan_training_instruction = symspan_training_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSymspan_training_instruction.rgb)
if thisSymspan_training_instruction != None:
    for paramName in thisSymspan_training_instruction:
        exec('{} = thisSymspan_training_instruction[paramName]'.format(paramName))

for thisSymspan_training_instruction in symspan_training_instructions:
    currentLoop = symspan_training_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisSymspan_training_instruction.rgb)
    if thisSymspan_training_instruction != None:
        for paramName in thisSymspan_training_instruction:
            exec('{} = thisSymspan_training_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instr_code
    my_count = 0 # contador de tentativas da tarefa distratora
    instr_msg.setPos((0, pos_y))
    instr_msg.setText(instruction_list[instruction_block][current_instruction])
    # setup some python lists for storing info about the instr_resp
    instr_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    symmetry_example.setOpacity(grid_opacity)
    symmetry_example.setImage(grid_example)
    # keep track of which components have finished
    instructionComponents = [instr_msg, previous, next, instr_resp, symmetry_example]
    for thisComponent in instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_msg* updates
        if instr_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_msg.frameNStart = frameN  # exact frame index
            instr_msg.tStart = t  # local t and not account for scr refresh
            instr_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_msg.started')
            instr_msg.setAutoDraw(True)
        
        # *previous* updates
        if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            previous.frameNStart = frameN  # exact frame index
            previous.tStart = t  # local t and not account for scr refresh
            previous.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'previous.started')
            previous.setAutoDraw(True)
        
        # *next* updates
        if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next.frameNStart = frameN  # exact frame index
            next.tStart = t  # local t and not account for scr refresh
            next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next.started')
            next.setAutoDraw(True)
        # *instr_resp* updates
        if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('instr_resp.started', t)
            instr_resp.status = STARTED
            instr_resp.mouseClock.reset()
            prevButtonState = instr_resp.getPressed()  # if button is down already this ISN'T a new click
        if instr_resp.status == STARTED:  # only update if started and not finished!
            buttons = instr_resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([previous, next])
                        clickableList = [previous, next]
                    except:
                        clickableList = [[previous, next]]
                    for obj in clickableList:
                        if obj.contains(instr_resp):
                            gotValidClick = True
                            instr_resp.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *symmetry_example* updates
        if symmetry_example.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_example.frameNStart = frameN  # exact frame index
            symmetry_example.tStart = t  # local t and not account for scr refresh
            symmetry_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_example, 'tStartRefresh')  # time at next scr refresh
            symmetry_example.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from instr_code
    thisExp.addData('participant_code', participant_code)
    
    if instr_resp.clicked_name[0] == "previous":
        current_instruction -= 1
    elif instr_resp.clicked_name[0] == "next":
        current_instruction += 1
    
    # Se a instrução atual for -1
    if current_instruction == -1:
        # Resete o valor para ser 0
        current_instruction = 0
    # Se a instrução atual é igual ao comprimento da lista de instruções
    elif current_instruction == len(instruction_list[instruction_block]):
        current_instruction = 0 # zera contador de instruções
        if instruction_block == 0:
            instruction_block += 1
            grid_memory_instructions.finished = True # encerra o loop do treino da tarefa de memória
        elif instruction_block == 1:
            instruction_block += 1
            symmetry_instructions.finished = True # encerra o loop do treino da tarefa matemática
        elif instruction_block == 2:
            instruction_block += 1
            symspan_training_instructions.finished = True # encerra o loop de treino do OSPAN
        elif instruction_block == 3:
            instruction_block += 1
            symspan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
    
    # definindo se a imagem aparece nas instruções
    if (instruction_block == 1):
        if current_instruction in [0, 1, 4, 5]:
            grid_opacity = 1
            pos_y = 0.8
        else:
            grid_opacity = 0
            pos_y = 0.2
        
        if current_instruction != 5:
            grid_example = "images/symm1_prac.jpg"
        else:
            grid_example = "images/symm26_prac.jpg"
            
    if (instruction_block > 1):
        grid_opacity = 0
        pos_y = 0.2
    # store data for symspan_training_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'symspan_training_instructions'


# set up handler to look after randomisation of conditions etc
symspan_training_trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('span.xlsx', selection='0'),
    seed=None, name='symspan_training_trials')
thisExp.addLoop(symspan_training_trials)  # add the loop to the experiment
thisSymspan_training_trial = symspan_training_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSymspan_training_trial.rgb)
if thisSymspan_training_trial != None:
    for paramName in thisSymspan_training_trial:
        exec('{} = thisSymspan_training_trial[paramName]'.format(paramName))

for thisSymspan_training_trial in symspan_training_trials:
    currentLoop = symspan_training_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSymspan_training_trial.rgb)
    if thisSymspan_training_trial != None:
        for paramName in thisSymspan_training_trial:
            exec('{} = thisSymspan_training_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    symspan_training_trial = data.TrialHandler(nReps=current_span, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='symspan_training_trial')
    thisExp.addLoop(symspan_training_trial)  # add the loop to the experiment
    thisSymspan_training_trial = symspan_training_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSymspan_training_trial.rgb)
    if thisSymspan_training_trial != None:
        for paramName in thisSymspan_training_trial:
            exec('{} = thisSymspan_training_trial[paramName]'.format(paramName))
    
    for thisSymspan_training_trial in symspan_training_trial:
        currentLoop = symspan_training_trial
        # abbreviate parameter names if possible (e.g. rgb = thisSymspan_training_trial.rgb)
        if thisSymspan_training_trial != None:
            for paramName in thisSymspan_training_trial:
                exec('{} = thisSymspan_training_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "symmetry" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from symmetry_code
        symmetry_clock = core.Clock()
        
        try:
            # se é a primeira execução do loop...
            if symmetry_practice_trials.thisN == 0:
                symmetry_color = "red" # agora teremos feedback na cor vermelha
                symmetry_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if symspan_training_trial.thisN == 0:
                symmetry_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if symspan_testing_trial.thisN == 0:
                symmetry_errors = 0
        except:
            pass
            
        # reseta os contadores quando começa o SYMSPAN para valer
        try:
            if (symspan_testing_trials.thisN == 0) and (symspan_testing_trial.thisN == 0):
                symmetry_total_trials = symmetry_trials_correct = speed_errors = 0
        except:
            pass
        # setup some python lists for storing info about the symmetry_problem_next
        symmetry_problem_next.clicked_name = []
        gotValidClick = False  # until a click is received
        symmetry_problem.setImage(grids[grid_count][0])
        # keep track of which components have finished
        symmetryComponents = [symmetry_prompt, continue_, symmetry_problem_next, symmetry_problem]
        for thisComponent in symmetryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "symmetry" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from symmetry_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if symmetry_clock.getTime() >= symmetry_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
              
            
            # *symmetry_prompt* updates
            if symmetry_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_prompt.frameNStart = frameN  # exact frame index
                symmetry_prompt.tStart = t  # local t and not account for scr refresh
                symmetry_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_prompt.started')
                symmetry_prompt.setAutoDraw(True)
            
            # *continue_* updates
            if continue_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_.frameNStart = frameN  # exact frame index
                continue_.tStart = t  # local t and not account for scr refresh
                continue_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_.started')
                continue_.setAutoDraw(True)
            # *symmetry_problem_next* updates
            if symmetry_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_problem_next.frameNStart = frameN  # exact frame index
                symmetry_problem_next.tStart = t  # local t and not account for scr refresh
                symmetry_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_problem_next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('symmetry_problem_next.started', t)
                symmetry_problem_next.status = STARTED
                symmetry_problem_next.mouseClock.reset()
                prevButtonState = symmetry_problem_next.getPressed()  # if button is down already this ISN'T a new click
            if symmetry_problem_next.status == STARTED:  # only update if started and not finished!
                buttons = symmetry_problem_next.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(continue_)
                            clickableList = continue_
                        except:
                            clickableList = [continue_]
                        for obj in clickableList:
                            if obj.contains(symmetry_problem_next):
                                gotValidClick = True
                                symmetry_problem_next.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *symmetry_problem* updates
            if symmetry_problem.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_problem.frameNStart = frameN  # exact frame index
                symmetry_problem.tStart = t  # local t and not account for scr refresh
                symmetry_problem.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_problem, 'tStartRefresh')  # time at next scr refresh
                symmetry_problem.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in symmetryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "symmetry" ---
        for thisComponent in symmetryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from symmetry_code
        # salva variáveis
        thisExp.addData("symmetry_problem", grids[grid_count][0]) # nome da imagem
        thisExp.addData("symmetry_status", grids[grid_count][1]) # symmetric vs. asymmetric
        thisExp.addData("symmetry_corr", grids[grid_count][2]) # gabarito
        
        if abort_trial:
            symmetry_speed_error = 1 # abortou devido a velocidade
        else:
            symmetry_speed_error = 0 # abortou devido a velocidade
        
        try:
            thisExp.addData("problem_rt", symmetry_clock.getTime()) # problem RT
        except:
            pass
        
        # store data for symspan_training_trial (TrialHandler)
        # the Routine "symmetry" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "symmetry_answer" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from symmetry_answer_code
        answer_clock = core.Clock()
        
        if abort_trial:
            continueRoutine = False
        # setup some python lists for storing info about the symmetry_response
        symmetry_response.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        symmetry_answerComponents = [symmetry_answer_screen, yes, no, symmetry_response]
        for thisComponent in symmetry_answerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "symmetry_answer" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from symmetry_answer_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if symmetry_clock.getTime() >= symmetry_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
            
            
            # *symmetry_answer_screen* updates
            if symmetry_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_answer_screen.frameNStart = frameN  # exact frame index
                symmetry_answer_screen.tStart = t  # local t and not account for scr refresh
                symmetry_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_answer_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_answer_screen.started')
                symmetry_answer_screen.setAutoDraw(True)
            
            # *yes* updates
            if yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                yes.frameNStart = frameN  # exact frame index
                yes.tStart = t  # local t and not account for scr refresh
                yes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yes, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yes.started')
                yes.setAutoDraw(True)
            
            # *no* updates
            if no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                no.frameNStart = frameN  # exact frame index
                no.tStart = t  # local t and not account for scr refresh
                no.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no.started')
                no.setAutoDraw(True)
            # *symmetry_response* updates
            if symmetry_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_response.frameNStart = frameN  # exact frame index
                symmetry_response.tStart = t  # local t and not account for scr refresh
                symmetry_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('symmetry_response.started', t)
                symmetry_response.status = STARTED
                symmetry_response.mouseClock.reset()
                prevButtonState = symmetry_response.getPressed()  # if button is down already this ISN'T a new click
            if symmetry_response.status == STARTED:  # only update if started and not finished!
                buttons = symmetry_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([yes, no])
                            clickableList = [yes, no]
                        except:
                            clickableList = [[yes, no]]
                        for obj in clickableList:
                            if obj.contains(symmetry_response):
                                gotValidClick = True
                                symmetry_response.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in symmetry_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "symmetry_answer" ---
        for thisComponent in symmetry_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from symmetry_answer_code
        try:
            if symmetry_response.clicked_name[0] == "yes":
                symmetry_participant_response = "yes"
            else:
                symmetry_participant_response = "no"
        except:
            symmetry_participant_response = ""
            symmetry_speed_error = 1
        
        try:
            thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
        except:
            pass
        
        # se o participante acertou
        if symmetry_participant_response == grids[grid_count][2]:
            symmetry_participant_corr = 1
            symmetry_accuracy_error = 0 # contagem de erros de acurácia
            symmetry_trials_correct += 1 # incrementa número de acertos da sessão toda
            symmetry_corrective_feedback = "Correto"
        else:
            symmetry_participant_corr = 0
            symmetry_corrective_feedback = "Incorreto"
            symmetry_errors += 1 # incrementa o número de erros apenas da presente tentativa
        
            if symmetry_speed_error == 0:
                symmetry_accuracy_error = 1
            else:
                symmetry_accuracy_error = 0
        
        # sempre incrementa o contador de tentativas
        symmetry_total_trials += 1
        
        if abort_trial:
            thisExp.addData("symmetry_speed_error", 1) # erro de velocidade
            abort_trial = False # reseta para a próxima tentativa
        else:
            thisExp.addData("symmetry_speed_error", 0)
        
        # salva variáveis
        thisExp.addData("symmetry_accuracy_error", symmetry_accuracy_error) # erro de acurácia
        thisExp.addData("symmetry_participant_corr", symmetry_participant_corr) # 1 = acerto, 0 = erro
        thisExp.addData("symmetry_problem", grids[grid_count][0]) # enunciado
        thisExp.addData("symmetry_status", grids[grid_count][1]) # gabarito
        thisExp.addData("symmetry_corr", grids[grid_count][2]) # resposta correta
        thisExp.addData("symmetry_participant_response", symmetry_participant_response) # resposta do participante
        
        # incrementa operação para próxima iteração
        grid_count += 1
        
        # soma a duração da tarefa matemática
        try:
            if symmetry_practice_trials.thisN < 15:
                symmetry_training_time.append(symmetry_clock.getTime()) # e guarda tempo em uma lista
                # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
                if symmetry_practice_trials.thisN == 14:
                    symmetry_time_mean = np.mean(np.array(symmetry_training_time))
                    symmetry_time_sd = np.std(np.array(symmetry_training_time), ddof = 1)
                    symmetry_criterion = symmetry_time_mean + 2 * symmetry_time_sd
                    
        except:
            pass
        
        # store data for symspan_training_trial (TrialHandler)
        # the Routine "symmetry_answer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "grid_memory" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from grid_memory_code
        # tenta atribuir o valor da repetição do loop atual à variável index
        # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
        try:
            index = grid_memory_practice.thisN
        except:
            pass
            
        try:
            index = symspan_training_trial.thisN
        except:
            pass
        
        try:
            index = symspan_testing_trial.thisN
        except:
            pass
        
        # tenta embaralhar as posições do grid sempre que estivermos em uma nova tentativa
        try:
            # se é a primeira execução do loop...
            if grid_memory_practice.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if symspan_training_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if symspan_testing_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        
        except:
            pass
        
        
        
        square_position.setPos([correct_positions[index]])
        # keep track of which components have finished
        grid_memoryComponents = [grid_memory_task, square_position]
        for thisComponent in grid_memoryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "grid_memory" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *grid_memory_task* updates
            if grid_memory_task.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                grid_memory_task.frameNStart = frameN  # exact frame index
                grid_memory_task.tStart = t  # local t and not account for scr refresh
                grid_memory_task.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grid_memory_task, 'tStartRefresh')  # time at next scr refresh
                grid_memory_task.setAutoDraw(True)
            if grid_memory_task.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grid_memory_task.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    grid_memory_task.tStop = t  # not accounting for scr refresh
                    grid_memory_task.frameNStop = frameN  # exact frame index
                    grid_memory_task.setAutoDraw(False)
            
            # *square_position* updates
            if square_position.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_position.frameNStart = frameN  # exact frame index
                square_position.tStart = t  # local t and not account for scr refresh
                square_position.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_position, 'tStartRefresh')  # time at next scr refresh
                square_position.setAutoDraw(True)
            if square_position.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_position.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    square_position.tStop = t  # not accounting for scr refresh
                    square_position.frameNStop = frameN  # exact frame index
                    square_position.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in grid_memoryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "grid_memory" ---
        for thisComponent in grid_memoryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed current_span repeats of 'symspan_training_trial'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_recall
    clicked_things = []
    clicked_images = ["selected_square_1.jpg", "selected_square_2.jpg", "selected_square_3.jpg", "selected_square_4.jpg",
                      "selected_square_5.jpg", "selected_square_6.jpg", "selected_square_7.jpg", "selected_square_8.jpg",
                      "selected_square_9.jpg", "selected_square_10.jpg", "selected_square_11.jpg", "selected_square_12.jpg",
                      "selected_square_13.jpg", "selected_square_14.jpg", "selected_square_15.jpg", "selected_square_16.jpg"]
    
    clickables = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]
    allowed_send = False
    allowed_blank = True
    
    my_response = list()
    
    try:
        if grid_memory_practice_trials.thisN == 0:
            task_phase = "grid_memory_practice_phase"
    except:
        pass
    
    try:
        if symspan_training_trials.thisN == 0:
            task_phase = "symspan_training_trials"
    except:
        pass
    
    try:
        if symspan_testing_trials.thisN == 0:
            task_phase = "symspan_testing_trials"
    except:
        pass
    
    
    A.setPos([fixed_grid_positions[0]])
    A.setImage(grid_positions_list[0])
    B.setPos([fixed_grid_positions[1]])
    B.setImage(grid_positions_list[1])
    C.setImage(grid_positions_list[2])
    D.setPos([fixed_grid_positions[3]])
    D.setImage(grid_positions_list[3])
    E.setPos([fixed_grid_positions[4]])
    E.setImage(grid_positions_list[4])
    F.setPos([fixed_grid_positions[5]])
    F.setImage(grid_positions_list[5])
    G.setPos([fixed_grid_positions[6]])
    G.setImage(grid_positions_list[6])
    H.setPos([fixed_grid_positions[7]])
    H.setImage(grid_positions_list[7])
    I.setPos([fixed_grid_positions[8]])
    I.setImage(grid_positions_list[8])
    J.setPos([fixed_grid_positions[9]])
    J.setImage(grid_positions_list[9])
    K.setPos([fixed_grid_positions[10]])
    K.setImage(grid_positions_list[10])
    L.setPos([fixed_grid_positions[11]])
    L.setImage(grid_positions_list[11])
    M.setPos([fixed_grid_positions[12]])
    M.setImage(grid_positions_list[12])
    N.setPos([fixed_grid_positions[13]])
    N.setImage(grid_positions_list[13])
    O.setPos([fixed_grid_positions[14]])
    O.setImage(grid_positions_list[14])
    P.setPos([fixed_grid_positions[15]])
    P.setImage(grid_positions_list[15])
    # setup some python lists for storing info about the recall_response
    recall_response.x = []
    recall_response.y = []
    recall_response.leftButton = []
    recall_response.midButton = []
    recall_response.rightButton = []
    recall_response.time = []
    recall_response.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    recallComponents = [prompt_recall, grid_recall, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, clear_, blank, send, recall_response]
    for thisComponent in recallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "recall" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_recall
        for i, clickable in enumerate(clickables):
            # and it was the blank button:
            if recall_response.isPressedIn(clickable) and (clickable == blank) and (allowed_blank == True):
                if len(clicked_things) <= 15:
                    clicked_things.append(clickable.name)
                    # to prevent two consecutive responses
                    allowed_blank = False 
                    blank_clock = core.Clock() 
                    #clicked_things.append(clickable.name)
                    my_response.append("–")
                    allowed_send = True
            # if a button was pressed in
            elif recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                # and it wasn't send, clear_, and blank buttons
                if (clickable != send) and (clickable != clear_) and (clickable != blank):
                    if len(clicked_things) <= 15:
                        clicked_things.append(clickable.name)
                        clickable.setImage(f"images/{clicked_images[len(clicked_things) - 1]}.jpg", log = False)
                        my_response.append(clickable.name)
                        allowed_send = True
                # and it was the clear_ button
                elif clickable == clear_:
                    for i, clickable in enumerate(clickables[:-3]):
                        clickable.setImage(f"images/selected_square_0.jpg", log = False)
                    # reset values
                    clicked_things = []
                    my_response = list()
                    allowed_send = False # reset
                elif (clickable == send) and (allowed_send == True):
                    continueRoutine = False
        
        # it allows the blank button again
        try:
            if blank_clock.getTime() > 1:
                allowed_blank = True
        except NameError:
            pass
        
        # *prompt_recall* updates
        if prompt_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_recall.frameNStart = frameN  # exact frame index
            prompt_recall.tStart = t  # local t and not account for scr refresh
            prompt_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_recall, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_recall.started')
            prompt_recall.setAutoDraw(True)
        
        # *grid_recall* updates
        if grid_recall.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            grid_recall.frameNStart = frameN  # exact frame index
            grid_recall.tStart = t  # local t and not account for scr refresh
            grid_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grid_recall, 'tStartRefresh')  # time at next scr refresh
            grid_recall.setAutoDraw(True)
        
        # *A* updates
        if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A.frameNStart = frameN  # exact frame index
            A.tStart = t  # local t and not account for scr refresh
            A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A.started')
            A.setAutoDraw(True)
        
        # *B* updates
        if B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B.frameNStart = frameN  # exact frame index
            B.tStart = t  # local t and not account for scr refresh
            B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'B.started')
            B.setAutoDraw(True)
        
        # *C* updates
        if C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C.frameNStart = frameN  # exact frame index
            C.tStart = t  # local t and not account for scr refresh
            C.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'C.started')
            C.setAutoDraw(True)
        
        # *D* updates
        if D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D.frameNStart = frameN  # exact frame index
            D.tStart = t  # local t and not account for scr refresh
            D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D.started')
            D.setAutoDraw(True)
        
        # *E* updates
        if E.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E.frameNStart = frameN  # exact frame index
            E.tStart = t  # local t and not account for scr refresh
            E.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'E.started')
            E.setAutoDraw(True)
        
        # *F* updates
        if F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F.frameNStart = frameN  # exact frame index
            F.tStart = t  # local t and not account for scr refresh
            F.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'F.started')
            F.setAutoDraw(True)
        
        # *G* updates
        if G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            G.frameNStart = frameN  # exact frame index
            G.tStart = t  # local t and not account for scr refresh
            G.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(G, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'G.started')
            G.setAutoDraw(True)
        
        # *H* updates
        if H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            H.frameNStart = frameN  # exact frame index
            H.tStart = t  # local t and not account for scr refresh
            H.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(H, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'H.started')
            H.setAutoDraw(True)
        
        # *I* updates
        if I.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            I.frameNStart = frameN  # exact frame index
            I.tStart = t  # local t and not account for scr refresh
            I.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(I, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'I.started')
            I.setAutoDraw(True)
        
        # *J* updates
        if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J.frameNStart = frameN  # exact frame index
            J.tStart = t  # local t and not account for scr refresh
            J.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'J.started')
            J.setAutoDraw(True)
        
        # *K* updates
        if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            K.frameNStart = frameN  # exact frame index
            K.tStart = t  # local t and not account for scr refresh
            K.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'K.started')
            K.setAutoDraw(True)
        
        # *L* updates
        if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L.frameNStart = frameN  # exact frame index
            L.tStart = t  # local t and not account for scr refresh
            L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L.started')
            L.setAutoDraw(True)
        
        # *M* updates
        if M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            M.frameNStart = frameN  # exact frame index
            M.tStart = t  # local t and not account for scr refresh
            M.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(M, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'M.started')
            M.setAutoDraw(True)
        
        # *N* updates
        if N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            N.frameNStart = frameN  # exact frame index
            N.tStart = t  # local t and not account for scr refresh
            N.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(N, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'N.started')
            N.setAutoDraw(True)
        
        # *O* updates
        if O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            O.frameNStart = frameN  # exact frame index
            O.tStart = t  # local t and not account for scr refresh
            O.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(O, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'O.started')
            O.setAutoDraw(True)
        
        # *P* updates
        if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P.frameNStart = frameN  # exact frame index
            P.tStart = t  # local t and not account for scr refresh
            P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P.started')
            P.setAutoDraw(True)
        
        # *clear_* updates
        if clear_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clear_.frameNStart = frameN  # exact frame index
            clear_.tStart = t  # local t and not account for scr refresh
            clear_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clear_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'clear_.started')
            clear_.setAutoDraw(True)
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank.started')
            blank.setAutoDraw(True)
        
        # *send* updates
        if send.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            send.frameNStart = frameN  # exact frame index
            send.tStart = t  # local t and not account for scr refresh
            send.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(send, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'send.started')
            send.setAutoDraw(True)
        # *recall_response* updates
        if recall_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_response.frameNStart = frameN  # exact frame index
            recall_response.tStart = t  # local t and not account for scr refresh
            recall_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('recall_response.started', t)
            recall_response.status = STARTED
            recall_response.mouseClock.reset()
            prevButtonState = recall_response.getPressed()  # if button is down already this ISN'T a new click
        if recall_response.status == STARTED:  # only update if started and not finished!
            buttons = recall_response.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank])
                        clickableList = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]
                    except:
                        clickableList = [[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]]
                    for obj in clickableList:
                        if obj.contains(recall_response):
                            gotValidClick = True
                            recall_response.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = recall_response.getPos()
                        recall_response.x.append(x)
                        recall_response.y.append(y)
                        buttons = recall_response.getPressed()
                        recall_response.leftButton.append(buttons[0])
                        recall_response.midButton.append(buttons[1])
                        recall_response.rightButton.append(buttons[2])
                        recall_response.time.append(recall_response.mouseClock.getTime())
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recall" ---
    for thisComponent in recallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_recall
    # juntando respostas, mas eliminando respostas repetidas e "send"
    participant_response = "".join(my_response)
    
    # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
    if participant_response == correct_response:
        full_credit_score = current_span
    else:
        full_credit_score = 0
    
    # crédito parcial (pontua apenas acertos na mesma posição serial)
    partial_credit_score = partial_credit(participant_response, correct_response)
    
    # edit distance score
    edit_distance_score = EditDistanceScore(correct_response, participant_response)
    
    # créditos completo parcial e edit distance, somatório da sessão (máx. 42)
    try:
        if symspan_testing_trials.thisN >= 0:
            final_full_credit_score += full_credit_score
            final_partial_credit_score += partial_credit_score
            final_edit_distance_score += edit_distance_score
    except:
        pass
    
    # criando texto para feedback
    if partial_credit_score > 1:
        word = "quadrados"    
    elif partial_credit_score <= 1:
        word = "quadrado"
    
    # mensagens de feedback de recordação e das operações matemáticas
    recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
    
    try:
        symmetry_percent_correct = (symmetry_trials_correct / symmetry_total_trials) * 100
    except ZeroDivisionError:
        symmetry_percent_correct = 0
    
    symmetry_performance_msg = f"{symmetry_percent_correct:.0f}%"
    
    try:
        if symmetry_errors > 1:
            symmetry_feedback_msg = f"Você cometeu {symmetry_errors} erros neste conjunto de tentativas" 
        elif symmetry_errors == 1:
            symmetry_feedback_msg = f"Você cometeu {symmetry_errors} erro neste conjunto de tentativas"
        else:
            symmetry_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
    except:
        symmetry_feedback_msg = ""
       
    # salva respostas
    thisExp.addData("correct_response", correct_response)
    thisExp.addData("participant_response", participant_response)
    thisExp.addData("full_credit_score", full_credit_score)
    thisExp.addData("partial_credit_score", partial_credit_score)
    thisExp.addData("edit_distance_score", edit_distance_score)
    thisExp.addData("task_phase", task_phase)
    thisExp.addData("symmetry_trials_correct", symmetry_trials_correct)
    thisExp.addData("symmetry_total_trials", symmetry_total_trials)
    thisExp.addData("symmetry_percent_correct", symmetry_percent_correct)
    try:
        thisExp.addData("symmetry_errors", symmetry_errors)
    except:
        pass
    
    # store data for symspan_training_trials (TrialHandler)
    symspan_training_trials.addData('recall_response.x', recall_response.x)
    symspan_training_trials.addData('recall_response.y', recall_response.y)
    symspan_training_trials.addData('recall_response.leftButton', recall_response.leftButton)
    symspan_training_trials.addData('recall_response.midButton', recall_response.midButton)
    symspan_training_trials.addData('recall_response.rightButton', recall_response.rightButton)
    symspan_training_trials.addData('recall_response.time', recall_response.time)
    symspan_training_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "recall_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    recall_feedback_prompt.setText(recall_feedback_msg)
    symmetry_feedback_prompt.setText(symmetry_feedback_msg)
    symmetry_feedback_performance.setColor(symmetry_color, colorSpace='rgb')
    symmetry_feedback_performance.setText(symmetry_performance_msg)
    # keep track of which components have finished
    recall_feedbackComponents = [recall_feedback_prompt, symmetry_feedback_prompt, symmetry_feedback_performance]
    for thisComponent in recall_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "recall_feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_feedback_prompt* updates
        if recall_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_feedback_prompt.frameNStart = frameN  # exact frame index
            recall_feedback_prompt.tStart = t  # local t and not account for scr refresh
            recall_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_feedback_prompt.started')
            recall_feedback_prompt.setAutoDraw(True)
        if recall_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recall_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                recall_feedback_prompt.tStop = t  # not accounting for scr refresh
                recall_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_feedback_prompt.stopped')
                recall_feedback_prompt.setAutoDraw(False)
        
        # *symmetry_feedback_prompt* updates
        if symmetry_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_feedback_prompt.frameNStart = frameN  # exact frame index
            symmetry_feedback_prompt.tStart = t  # local t and not account for scr refresh
            symmetry_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_feedback_prompt.started')
            symmetry_feedback_prompt.setAutoDraw(True)
        if symmetry_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > symmetry_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                symmetry_feedback_prompt.tStop = t  # not accounting for scr refresh
                symmetry_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_feedback_prompt.stopped')
                symmetry_feedback_prompt.setAutoDraw(False)
        
        # *symmetry_feedback_performance* updates
        if symmetry_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_feedback_performance.frameNStart = frameN  # exact frame index
            symmetry_feedback_performance.tStart = t  # local t and not account for scr refresh
            symmetry_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_feedback_performance, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_feedback_performance.started')
            symmetry_feedback_performance.setAutoDraw(True)
        if symmetry_feedback_performance.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > symmetry_feedback_performance.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                symmetry_feedback_performance.tStop = t  # not accounting for scr refresh
                symmetry_feedback_performance.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_feedback_performance.stopped')
                symmetry_feedback_performance.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recall_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recall_feedback" ---
    for thisComponent in recall_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'symspan_training_trials'


# set up handler to look after randomisation of conditions etc
symspan_testing_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='symspan_testing_instructions')
thisExp.addLoop(symspan_testing_instructions)  # add the loop to the experiment
thisSymspan_testing_instruction = symspan_testing_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSymspan_testing_instruction.rgb)
if thisSymspan_testing_instruction != None:
    for paramName in thisSymspan_testing_instruction:
        exec('{} = thisSymspan_testing_instruction[paramName]'.format(paramName))

for thisSymspan_testing_instruction in symspan_testing_instructions:
    currentLoop = symspan_testing_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisSymspan_testing_instruction.rgb)
    if thisSymspan_testing_instruction != None:
        for paramName in thisSymspan_testing_instruction:
            exec('{} = thisSymspan_testing_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instr_code
    my_count = 0 # contador de tentativas da tarefa distratora
    instr_msg.setPos((0, pos_y))
    instr_msg.setText(instruction_list[instruction_block][current_instruction])
    # setup some python lists for storing info about the instr_resp
    instr_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    symmetry_example.setOpacity(grid_opacity)
    symmetry_example.setImage(grid_example)
    # keep track of which components have finished
    instructionComponents = [instr_msg, previous, next, instr_resp, symmetry_example]
    for thisComponent in instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_msg* updates
        if instr_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_msg.frameNStart = frameN  # exact frame index
            instr_msg.tStart = t  # local t and not account for scr refresh
            instr_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_msg.started')
            instr_msg.setAutoDraw(True)
        
        # *previous* updates
        if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            previous.frameNStart = frameN  # exact frame index
            previous.tStart = t  # local t and not account for scr refresh
            previous.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'previous.started')
            previous.setAutoDraw(True)
        
        # *next* updates
        if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next.frameNStart = frameN  # exact frame index
            next.tStart = t  # local t and not account for scr refresh
            next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next.started')
            next.setAutoDraw(True)
        # *instr_resp* updates
        if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('instr_resp.started', t)
            instr_resp.status = STARTED
            instr_resp.mouseClock.reset()
            prevButtonState = instr_resp.getPressed()  # if button is down already this ISN'T a new click
        if instr_resp.status == STARTED:  # only update if started and not finished!
            buttons = instr_resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([previous, next])
                        clickableList = [previous, next]
                    except:
                        clickableList = [[previous, next]]
                    for obj in clickableList:
                        if obj.contains(instr_resp):
                            gotValidClick = True
                            instr_resp.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *symmetry_example* updates
        if symmetry_example.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_example.frameNStart = frameN  # exact frame index
            symmetry_example.tStart = t  # local t and not account for scr refresh
            symmetry_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_example, 'tStartRefresh')  # time at next scr refresh
            symmetry_example.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from instr_code
    thisExp.addData('participant_code', participant_code)
    
    if instr_resp.clicked_name[0] == "previous":
        current_instruction -= 1
    elif instr_resp.clicked_name[0] == "next":
        current_instruction += 1
    
    # Se a instrução atual for -1
    if current_instruction == -1:
        # Resete o valor para ser 0
        current_instruction = 0
    # Se a instrução atual é igual ao comprimento da lista de instruções
    elif current_instruction == len(instruction_list[instruction_block]):
        current_instruction = 0 # zera contador de instruções
        if instruction_block == 0:
            instruction_block += 1
            grid_memory_instructions.finished = True # encerra o loop do treino da tarefa de memória
        elif instruction_block == 1:
            instruction_block += 1
            symmetry_instructions.finished = True # encerra o loop do treino da tarefa matemática
        elif instruction_block == 2:
            instruction_block += 1
            symspan_training_instructions.finished = True # encerra o loop de treino do OSPAN
        elif instruction_block == 3:
            instruction_block += 1
            symspan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
    
    # definindo se a imagem aparece nas instruções
    if (instruction_block == 1):
        if current_instruction in [0, 1, 4, 5]:
            grid_opacity = 1
            pos_y = 0.8
        else:
            grid_opacity = 0
            pos_y = 0.2
        
        if current_instruction != 5:
            grid_example = "images/symm1_prac.jpg"
        else:
            grid_example = "images/symm26_prac.jpg"
            
    if (instruction_block > 1):
        grid_opacity = 0
        pos_y = 0.2
    # store data for symspan_testing_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'symspan_testing_instructions'


# set up handler to look after randomisation of conditions etc
symspan_testing_trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('span.xlsx', selection='1:'),
    seed=None, name='symspan_testing_trials')
thisExp.addLoop(symspan_testing_trials)  # add the loop to the experiment
thisSymspan_testing_trial = symspan_testing_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSymspan_testing_trial.rgb)
if thisSymspan_testing_trial != None:
    for paramName in thisSymspan_testing_trial:
        exec('{} = thisSymspan_testing_trial[paramName]'.format(paramName))

for thisSymspan_testing_trial in symspan_testing_trials:
    currentLoop = symspan_testing_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSymspan_testing_trial.rgb)
    if thisSymspan_testing_trial != None:
        for paramName in thisSymspan_testing_trial:
            exec('{} = thisSymspan_testing_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    symspan_testing_trial = data.TrialHandler(nReps=current_span, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='symspan_testing_trial')
    thisExp.addLoop(symspan_testing_trial)  # add the loop to the experiment
    thisSymspan_testing_trial = symspan_testing_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSymspan_testing_trial.rgb)
    if thisSymspan_testing_trial != None:
        for paramName in thisSymspan_testing_trial:
            exec('{} = thisSymspan_testing_trial[paramName]'.format(paramName))
    
    for thisSymspan_testing_trial in symspan_testing_trial:
        currentLoop = symspan_testing_trial
        # abbreviate parameter names if possible (e.g. rgb = thisSymspan_testing_trial.rgb)
        if thisSymspan_testing_trial != None:
            for paramName in thisSymspan_testing_trial:
                exec('{} = thisSymspan_testing_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "symmetry" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from symmetry_code
        symmetry_clock = core.Clock()
        
        try:
            # se é a primeira execução do loop...
            if symmetry_practice_trials.thisN == 0:
                symmetry_color = "red" # agora teremos feedback na cor vermelha
                symmetry_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if symspan_training_trial.thisN == 0:
                symmetry_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if symspan_testing_trial.thisN == 0:
                symmetry_errors = 0
        except:
            pass
            
        # reseta os contadores quando começa o SYMSPAN para valer
        try:
            if (symspan_testing_trials.thisN == 0) and (symspan_testing_trial.thisN == 0):
                symmetry_total_trials = symmetry_trials_correct = speed_errors = 0
        except:
            pass
        # setup some python lists for storing info about the symmetry_problem_next
        symmetry_problem_next.clicked_name = []
        gotValidClick = False  # until a click is received
        symmetry_problem.setImage(grids[grid_count][0])
        # keep track of which components have finished
        symmetryComponents = [symmetry_prompt, continue_, symmetry_problem_next, symmetry_problem]
        for thisComponent in symmetryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "symmetry" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from symmetry_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if symmetry_clock.getTime() >= symmetry_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
              
            
            # *symmetry_prompt* updates
            if symmetry_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_prompt.frameNStart = frameN  # exact frame index
                symmetry_prompt.tStart = t  # local t and not account for scr refresh
                symmetry_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_prompt.started')
                symmetry_prompt.setAutoDraw(True)
            
            # *continue_* updates
            if continue_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_.frameNStart = frameN  # exact frame index
                continue_.tStart = t  # local t and not account for scr refresh
                continue_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_.started')
                continue_.setAutoDraw(True)
            # *symmetry_problem_next* updates
            if symmetry_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_problem_next.frameNStart = frameN  # exact frame index
                symmetry_problem_next.tStart = t  # local t and not account for scr refresh
                symmetry_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_problem_next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('symmetry_problem_next.started', t)
                symmetry_problem_next.status = STARTED
                symmetry_problem_next.mouseClock.reset()
                prevButtonState = symmetry_problem_next.getPressed()  # if button is down already this ISN'T a new click
            if symmetry_problem_next.status == STARTED:  # only update if started and not finished!
                buttons = symmetry_problem_next.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(continue_)
                            clickableList = continue_
                        except:
                            clickableList = [continue_]
                        for obj in clickableList:
                            if obj.contains(symmetry_problem_next):
                                gotValidClick = True
                                symmetry_problem_next.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *symmetry_problem* updates
            if symmetry_problem.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_problem.frameNStart = frameN  # exact frame index
                symmetry_problem.tStart = t  # local t and not account for scr refresh
                symmetry_problem.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_problem, 'tStartRefresh')  # time at next scr refresh
                symmetry_problem.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in symmetryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "symmetry" ---
        for thisComponent in symmetryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from symmetry_code
        # salva variáveis
        thisExp.addData("symmetry_problem", grids[grid_count][0]) # nome da imagem
        thisExp.addData("symmetry_status", grids[grid_count][1]) # symmetric vs. asymmetric
        thisExp.addData("symmetry_corr", grids[grid_count][2]) # gabarito
        
        if abort_trial:
            symmetry_speed_error = 1 # abortou devido a velocidade
        else:
            symmetry_speed_error = 0 # abortou devido a velocidade
        
        try:
            thisExp.addData("problem_rt", symmetry_clock.getTime()) # problem RT
        except:
            pass
        
        # store data for symspan_testing_trial (TrialHandler)
        # the Routine "symmetry" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "symmetry_answer" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from symmetry_answer_code
        answer_clock = core.Clock()
        
        if abort_trial:
            continueRoutine = False
        # setup some python lists for storing info about the symmetry_response
        symmetry_response.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        symmetry_answerComponents = [symmetry_answer_screen, yes, no, symmetry_response]
        for thisComponent in symmetry_answerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "symmetry_answer" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from symmetry_answer_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if symmetry_clock.getTime() >= symmetry_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
            
            
            # *symmetry_answer_screen* updates
            if symmetry_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_answer_screen.frameNStart = frameN  # exact frame index
                symmetry_answer_screen.tStart = t  # local t and not account for scr refresh
                symmetry_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_answer_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_answer_screen.started')
                symmetry_answer_screen.setAutoDraw(True)
            
            # *yes* updates
            if yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                yes.frameNStart = frameN  # exact frame index
                yes.tStart = t  # local t and not account for scr refresh
                yes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yes, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yes.started')
                yes.setAutoDraw(True)
            
            # *no* updates
            if no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                no.frameNStart = frameN  # exact frame index
                no.tStart = t  # local t and not account for scr refresh
                no.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no.started')
                no.setAutoDraw(True)
            # *symmetry_response* updates
            if symmetry_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_response.frameNStart = frameN  # exact frame index
                symmetry_response.tStart = t  # local t and not account for scr refresh
                symmetry_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('symmetry_response.started', t)
                symmetry_response.status = STARTED
                symmetry_response.mouseClock.reset()
                prevButtonState = symmetry_response.getPressed()  # if button is down already this ISN'T a new click
            if symmetry_response.status == STARTED:  # only update if started and not finished!
                buttons = symmetry_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([yes, no])
                            clickableList = [yes, no]
                        except:
                            clickableList = [[yes, no]]
                        for obj in clickableList:
                            if obj.contains(symmetry_response):
                                gotValidClick = True
                                symmetry_response.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in symmetry_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "symmetry_answer" ---
        for thisComponent in symmetry_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from symmetry_answer_code
        try:
            if symmetry_response.clicked_name[0] == "yes":
                symmetry_participant_response = "yes"
            else:
                symmetry_participant_response = "no"
        except:
            symmetry_participant_response = ""
            symmetry_speed_error = 1
        
        try:
            thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
        except:
            pass
        
        # se o participante acertou
        if symmetry_participant_response == grids[grid_count][2]:
            symmetry_participant_corr = 1
            symmetry_accuracy_error = 0 # contagem de erros de acurácia
            symmetry_trials_correct += 1 # incrementa número de acertos da sessão toda
            symmetry_corrective_feedback = "Correto"
        else:
            symmetry_participant_corr = 0
            symmetry_corrective_feedback = "Incorreto"
            symmetry_errors += 1 # incrementa o número de erros apenas da presente tentativa
        
            if symmetry_speed_error == 0:
                symmetry_accuracy_error = 1
            else:
                symmetry_accuracy_error = 0
        
        # sempre incrementa o contador de tentativas
        symmetry_total_trials += 1
        
        if abort_trial:
            thisExp.addData("symmetry_speed_error", 1) # erro de velocidade
            abort_trial = False # reseta para a próxima tentativa
        else:
            thisExp.addData("symmetry_speed_error", 0)
        
        # salva variáveis
        thisExp.addData("symmetry_accuracy_error", symmetry_accuracy_error) # erro de acurácia
        thisExp.addData("symmetry_participant_corr", symmetry_participant_corr) # 1 = acerto, 0 = erro
        thisExp.addData("symmetry_problem", grids[grid_count][0]) # enunciado
        thisExp.addData("symmetry_status", grids[grid_count][1]) # gabarito
        thisExp.addData("symmetry_corr", grids[grid_count][2]) # resposta correta
        thisExp.addData("symmetry_participant_response", symmetry_participant_response) # resposta do participante
        
        # incrementa operação para próxima iteração
        grid_count += 1
        
        # soma a duração da tarefa matemática
        try:
            if symmetry_practice_trials.thisN < 15:
                symmetry_training_time.append(symmetry_clock.getTime()) # e guarda tempo em uma lista
                # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
                if symmetry_practice_trials.thisN == 14:
                    symmetry_time_mean = np.mean(np.array(symmetry_training_time))
                    symmetry_time_sd = np.std(np.array(symmetry_training_time), ddof = 1)
                    symmetry_criterion = symmetry_time_mean + 2 * symmetry_time_sd
                    
        except:
            pass
        
        # store data for symspan_testing_trial (TrialHandler)
        # the Routine "symmetry_answer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "grid_memory" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from grid_memory_code
        # tenta atribuir o valor da repetição do loop atual à variável index
        # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
        try:
            index = grid_memory_practice.thisN
        except:
            pass
            
        try:
            index = symspan_training_trial.thisN
        except:
            pass
        
        try:
            index = symspan_testing_trial.thisN
        except:
            pass
        
        # tenta embaralhar as posições do grid sempre que estivermos em uma nova tentativa
        try:
            # se é a primeira execução do loop...
            if grid_memory_practice.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if symspan_training_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if symspan_testing_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(grid_positions) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_positions = list()
                temp = list()
                for i in range(current_span):
                    correct_positions.append(grid_positions[i][0])
                    temp.append(grid_positions[i][1])
                    
                correct_response = "".join(temp)
        
        except:
            pass
        
        
        
        square_position.setPos([correct_positions[index]])
        # keep track of which components have finished
        grid_memoryComponents = [grid_memory_task, square_position]
        for thisComponent in grid_memoryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "grid_memory" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *grid_memory_task* updates
            if grid_memory_task.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                grid_memory_task.frameNStart = frameN  # exact frame index
                grid_memory_task.tStart = t  # local t and not account for scr refresh
                grid_memory_task.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grid_memory_task, 'tStartRefresh')  # time at next scr refresh
                grid_memory_task.setAutoDraw(True)
            if grid_memory_task.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grid_memory_task.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    grid_memory_task.tStop = t  # not accounting for scr refresh
                    grid_memory_task.frameNStop = frameN  # exact frame index
                    grid_memory_task.setAutoDraw(False)
            
            # *square_position* updates
            if square_position.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_position.frameNStart = frameN  # exact frame index
                square_position.tStart = t  # local t and not account for scr refresh
                square_position.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_position, 'tStartRefresh')  # time at next scr refresh
                square_position.setAutoDraw(True)
            if square_position.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_position.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    square_position.tStop = t  # not accounting for scr refresh
                    square_position.frameNStop = frameN  # exact frame index
                    square_position.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in grid_memoryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "grid_memory" ---
        for thisComponent in grid_memoryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed current_span repeats of 'symspan_testing_trial'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_recall
    clicked_things = []
    clicked_images = ["selected_square_1.jpg", "selected_square_2.jpg", "selected_square_3.jpg", "selected_square_4.jpg",
                      "selected_square_5.jpg", "selected_square_6.jpg", "selected_square_7.jpg", "selected_square_8.jpg",
                      "selected_square_9.jpg", "selected_square_10.jpg", "selected_square_11.jpg", "selected_square_12.jpg",
                      "selected_square_13.jpg", "selected_square_14.jpg", "selected_square_15.jpg", "selected_square_16.jpg"]
    
    clickables = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]
    allowed_send = False
    allowed_blank = True
    
    my_response = list()
    
    try:
        if grid_memory_practice_trials.thisN == 0:
            task_phase = "grid_memory_practice_phase"
    except:
        pass
    
    try:
        if symspan_training_trials.thisN == 0:
            task_phase = "symspan_training_trials"
    except:
        pass
    
    try:
        if symspan_testing_trials.thisN == 0:
            task_phase = "symspan_testing_trials"
    except:
        pass
    
    
    A.setPos([fixed_grid_positions[0]])
    A.setImage(grid_positions_list[0])
    B.setPos([fixed_grid_positions[1]])
    B.setImage(grid_positions_list[1])
    C.setImage(grid_positions_list[2])
    D.setPos([fixed_grid_positions[3]])
    D.setImage(grid_positions_list[3])
    E.setPos([fixed_grid_positions[4]])
    E.setImage(grid_positions_list[4])
    F.setPos([fixed_grid_positions[5]])
    F.setImage(grid_positions_list[5])
    G.setPos([fixed_grid_positions[6]])
    G.setImage(grid_positions_list[6])
    H.setPos([fixed_grid_positions[7]])
    H.setImage(grid_positions_list[7])
    I.setPos([fixed_grid_positions[8]])
    I.setImage(grid_positions_list[8])
    J.setPos([fixed_grid_positions[9]])
    J.setImage(grid_positions_list[9])
    K.setPos([fixed_grid_positions[10]])
    K.setImage(grid_positions_list[10])
    L.setPos([fixed_grid_positions[11]])
    L.setImage(grid_positions_list[11])
    M.setPos([fixed_grid_positions[12]])
    M.setImage(grid_positions_list[12])
    N.setPos([fixed_grid_positions[13]])
    N.setImage(grid_positions_list[13])
    O.setPos([fixed_grid_positions[14]])
    O.setImage(grid_positions_list[14])
    P.setPos([fixed_grid_positions[15]])
    P.setImage(grid_positions_list[15])
    # setup some python lists for storing info about the recall_response
    recall_response.x = []
    recall_response.y = []
    recall_response.leftButton = []
    recall_response.midButton = []
    recall_response.rightButton = []
    recall_response.time = []
    recall_response.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    recallComponents = [prompt_recall, grid_recall, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, clear_, blank, send, recall_response]
    for thisComponent in recallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "recall" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_recall
        for i, clickable in enumerate(clickables):
            # and it was the blank button:
            if recall_response.isPressedIn(clickable) and (clickable == blank) and (allowed_blank == True):
                if len(clicked_things) <= 15:
                    clicked_things.append(clickable.name)
                    # to prevent two consecutive responses
                    allowed_blank = False 
                    blank_clock = core.Clock() 
                    #clicked_things.append(clickable.name)
                    my_response.append("–")
                    allowed_send = True
            # if a button was pressed in
            elif recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                # and it wasn't send, clear_, and blank buttons
                if (clickable != send) and (clickable != clear_) and (clickable != blank):
                    if len(clicked_things) <= 15:
                        clicked_things.append(clickable.name)
                        clickable.setImage(f"images/{clicked_images[len(clicked_things) - 1]}.jpg", log = False)
                        my_response.append(clickable.name)
                        allowed_send = True
                # and it was the clear_ button
                elif clickable == clear_:
                    for i, clickable in enumerate(clickables[:-3]):
                        clickable.setImage(f"images/selected_square_0.jpg", log = False)
                    # reset values
                    clicked_things = []
                    my_response = list()
                    allowed_send = False # reset
                elif (clickable == send) and (allowed_send == True):
                    continueRoutine = False
        
        # it allows the blank button again
        try:
            if blank_clock.getTime() > 1:
                allowed_blank = True
        except NameError:
            pass
        
        # *prompt_recall* updates
        if prompt_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_recall.frameNStart = frameN  # exact frame index
            prompt_recall.tStart = t  # local t and not account for scr refresh
            prompt_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_recall, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_recall.started')
            prompt_recall.setAutoDraw(True)
        
        # *grid_recall* updates
        if grid_recall.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            grid_recall.frameNStart = frameN  # exact frame index
            grid_recall.tStart = t  # local t and not account for scr refresh
            grid_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grid_recall, 'tStartRefresh')  # time at next scr refresh
            grid_recall.setAutoDraw(True)
        
        # *A* updates
        if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A.frameNStart = frameN  # exact frame index
            A.tStart = t  # local t and not account for scr refresh
            A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A.started')
            A.setAutoDraw(True)
        
        # *B* updates
        if B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B.frameNStart = frameN  # exact frame index
            B.tStart = t  # local t and not account for scr refresh
            B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'B.started')
            B.setAutoDraw(True)
        
        # *C* updates
        if C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C.frameNStart = frameN  # exact frame index
            C.tStart = t  # local t and not account for scr refresh
            C.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'C.started')
            C.setAutoDraw(True)
        
        # *D* updates
        if D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D.frameNStart = frameN  # exact frame index
            D.tStart = t  # local t and not account for scr refresh
            D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D.started')
            D.setAutoDraw(True)
        
        # *E* updates
        if E.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E.frameNStart = frameN  # exact frame index
            E.tStart = t  # local t and not account for scr refresh
            E.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'E.started')
            E.setAutoDraw(True)
        
        # *F* updates
        if F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F.frameNStart = frameN  # exact frame index
            F.tStart = t  # local t and not account for scr refresh
            F.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'F.started')
            F.setAutoDraw(True)
        
        # *G* updates
        if G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            G.frameNStart = frameN  # exact frame index
            G.tStart = t  # local t and not account for scr refresh
            G.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(G, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'G.started')
            G.setAutoDraw(True)
        
        # *H* updates
        if H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            H.frameNStart = frameN  # exact frame index
            H.tStart = t  # local t and not account for scr refresh
            H.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(H, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'H.started')
            H.setAutoDraw(True)
        
        # *I* updates
        if I.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            I.frameNStart = frameN  # exact frame index
            I.tStart = t  # local t and not account for scr refresh
            I.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(I, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'I.started')
            I.setAutoDraw(True)
        
        # *J* updates
        if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J.frameNStart = frameN  # exact frame index
            J.tStart = t  # local t and not account for scr refresh
            J.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'J.started')
            J.setAutoDraw(True)
        
        # *K* updates
        if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            K.frameNStart = frameN  # exact frame index
            K.tStart = t  # local t and not account for scr refresh
            K.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'K.started')
            K.setAutoDraw(True)
        
        # *L* updates
        if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L.frameNStart = frameN  # exact frame index
            L.tStart = t  # local t and not account for scr refresh
            L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L.started')
            L.setAutoDraw(True)
        
        # *M* updates
        if M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            M.frameNStart = frameN  # exact frame index
            M.tStart = t  # local t and not account for scr refresh
            M.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(M, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'M.started')
            M.setAutoDraw(True)
        
        # *N* updates
        if N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            N.frameNStart = frameN  # exact frame index
            N.tStart = t  # local t and not account for scr refresh
            N.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(N, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'N.started')
            N.setAutoDraw(True)
        
        # *O* updates
        if O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            O.frameNStart = frameN  # exact frame index
            O.tStart = t  # local t and not account for scr refresh
            O.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(O, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'O.started')
            O.setAutoDraw(True)
        
        # *P* updates
        if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P.frameNStart = frameN  # exact frame index
            P.tStart = t  # local t and not account for scr refresh
            P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P.started')
            P.setAutoDraw(True)
        
        # *clear_* updates
        if clear_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clear_.frameNStart = frameN  # exact frame index
            clear_.tStart = t  # local t and not account for scr refresh
            clear_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clear_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'clear_.started')
            clear_.setAutoDraw(True)
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank.started')
            blank.setAutoDraw(True)
        
        # *send* updates
        if send.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            send.frameNStart = frameN  # exact frame index
            send.tStart = t  # local t and not account for scr refresh
            send.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(send, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'send.started')
            send.setAutoDraw(True)
        # *recall_response* updates
        if recall_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_response.frameNStart = frameN  # exact frame index
            recall_response.tStart = t  # local t and not account for scr refresh
            recall_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('recall_response.started', t)
            recall_response.status = STARTED
            recall_response.mouseClock.reset()
            prevButtonState = recall_response.getPressed()  # if button is down already this ISN'T a new click
        if recall_response.status == STARTED:  # only update if started and not finished!
            buttons = recall_response.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank])
                        clickableList = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]
                    except:
                        clickableList = [[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank]]
                    for obj in clickableList:
                        if obj.contains(recall_response):
                            gotValidClick = True
                            recall_response.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = recall_response.getPos()
                        recall_response.x.append(x)
                        recall_response.y.append(y)
                        buttons = recall_response.getPressed()
                        recall_response.leftButton.append(buttons[0])
                        recall_response.midButton.append(buttons[1])
                        recall_response.rightButton.append(buttons[2])
                        recall_response.time.append(recall_response.mouseClock.getTime())
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recall" ---
    for thisComponent in recallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_recall
    # juntando respostas, mas eliminando respostas repetidas e "send"
    participant_response = "".join(my_response)
    
    # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
    if participant_response == correct_response:
        full_credit_score = current_span
    else:
        full_credit_score = 0
    
    # crédito parcial (pontua apenas acertos na mesma posição serial)
    partial_credit_score = partial_credit(participant_response, correct_response)
    
    # edit distance score
    edit_distance_score = EditDistanceScore(correct_response, participant_response)
    
    # créditos completo parcial e edit distance, somatório da sessão (máx. 42)
    try:
        if symspan_testing_trials.thisN >= 0:
            final_full_credit_score += full_credit_score
            final_partial_credit_score += partial_credit_score
            final_edit_distance_score += edit_distance_score
    except:
        pass
    
    # criando texto para feedback
    if partial_credit_score > 1:
        word = "quadrados"    
    elif partial_credit_score <= 1:
        word = "quadrado"
    
    # mensagens de feedback de recordação e das operações matemáticas
    recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
    
    try:
        symmetry_percent_correct = (symmetry_trials_correct / symmetry_total_trials) * 100
    except ZeroDivisionError:
        symmetry_percent_correct = 0
    
    symmetry_performance_msg = f"{symmetry_percent_correct:.0f}%"
    
    try:
        if symmetry_errors > 1:
            symmetry_feedback_msg = f"Você cometeu {symmetry_errors} erros neste conjunto de tentativas" 
        elif symmetry_errors == 1:
            symmetry_feedback_msg = f"Você cometeu {symmetry_errors} erro neste conjunto de tentativas"
        else:
            symmetry_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
    except:
        symmetry_feedback_msg = ""
       
    # salva respostas
    thisExp.addData("correct_response", correct_response)
    thisExp.addData("participant_response", participant_response)
    thisExp.addData("full_credit_score", full_credit_score)
    thisExp.addData("partial_credit_score", partial_credit_score)
    thisExp.addData("edit_distance_score", edit_distance_score)
    thisExp.addData("task_phase", task_phase)
    thisExp.addData("symmetry_trials_correct", symmetry_trials_correct)
    thisExp.addData("symmetry_total_trials", symmetry_total_trials)
    thisExp.addData("symmetry_percent_correct", symmetry_percent_correct)
    try:
        thisExp.addData("symmetry_errors", symmetry_errors)
    except:
        pass
    
    # store data for symspan_testing_trials (TrialHandler)
    symspan_testing_trials.addData('recall_response.x', recall_response.x)
    symspan_testing_trials.addData('recall_response.y', recall_response.y)
    symspan_testing_trials.addData('recall_response.leftButton', recall_response.leftButton)
    symspan_testing_trials.addData('recall_response.midButton', recall_response.midButton)
    symspan_testing_trials.addData('recall_response.rightButton', recall_response.rightButton)
    symspan_testing_trials.addData('recall_response.time', recall_response.time)
    symspan_testing_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "recall_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    recall_feedback_prompt.setText(recall_feedback_msg)
    symmetry_feedback_prompt.setText(symmetry_feedback_msg)
    symmetry_feedback_performance.setColor(symmetry_color, colorSpace='rgb')
    symmetry_feedback_performance.setText(symmetry_performance_msg)
    # keep track of which components have finished
    recall_feedbackComponents = [recall_feedback_prompt, symmetry_feedback_prompt, symmetry_feedback_performance]
    for thisComponent in recall_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "recall_feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_feedback_prompt* updates
        if recall_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_feedback_prompt.frameNStart = frameN  # exact frame index
            recall_feedback_prompt.tStart = t  # local t and not account for scr refresh
            recall_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_feedback_prompt.started')
            recall_feedback_prompt.setAutoDraw(True)
        if recall_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recall_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                recall_feedback_prompt.tStop = t  # not accounting for scr refresh
                recall_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_feedback_prompt.stopped')
                recall_feedback_prompt.setAutoDraw(False)
        
        # *symmetry_feedback_prompt* updates
        if symmetry_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_feedback_prompt.frameNStart = frameN  # exact frame index
            symmetry_feedback_prompt.tStart = t  # local t and not account for scr refresh
            symmetry_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_feedback_prompt.started')
            symmetry_feedback_prompt.setAutoDraw(True)
        if symmetry_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > symmetry_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                symmetry_feedback_prompt.tStop = t  # not accounting for scr refresh
                symmetry_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_feedback_prompt.stopped')
                symmetry_feedback_prompt.setAutoDraw(False)
        
        # *symmetry_feedback_performance* updates
        if symmetry_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symmetry_feedback_performance.frameNStart = frameN  # exact frame index
            symmetry_feedback_performance.tStart = t  # local t and not account for scr refresh
            symmetry_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symmetry_feedback_performance, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'symmetry_feedback_performance.started')
            symmetry_feedback_performance.setAutoDraw(True)
        if symmetry_feedback_performance.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > symmetry_feedback_performance.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                symmetry_feedback_performance.tStop = t  # not accounting for scr refresh
                symmetry_feedback_performance.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symmetry_feedback_performance.stopped')
                symmetry_feedback_performance.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recall_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recall_feedback" ---
    for thisComponent in recall_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'symspan_testing_trials'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
# update component parameters for each repeat
thanks_prompt.setText(thanks_txt)
thanks_resp.keys = []
thanks_resp.rt = []
_thanks_resp_allKeys = []
# keep track of which components have finished
thanksComponents = [thanks_prompt, thanks_spacebar, thanks_resp]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "thanks" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_prompt* updates
    if thanks_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_prompt.frameNStart = frameN  # exact frame index
        thanks_prompt.tStart = t  # local t and not account for scr refresh
        thanks_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thanks_prompt.started')
        thanks_prompt.setAutoDraw(True)
    
    # *thanks_spacebar* updates
    if thanks_spacebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_spacebar.frameNStart = frameN  # exact frame index
        thanks_spacebar.tStart = t  # local t and not account for scr refresh
        thanks_spacebar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_spacebar, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thanks_spacebar.started')
        thanks_spacebar.setAutoDraw(True)
    
    # *thanks_resp* updates
    waitOnFlip = False
    if thanks_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_resp.frameNStart = frameN  # exact frame index
        thanks_resp.tStart = t  # local t and not account for scr refresh
        thanks_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thanks_resp.started')
        thanks_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(thanks_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(thanks_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if thanks_resp.status == STARTED and not waitOnFlip:
        theseKeys = thanks_resp.getKeys(keyList=['space'], waitRelease=False)
        _thanks_resp_allKeys.extend(theseKeys)
        if len(_thanks_resp_allKeys):
            thanks_resp.keys = _thanks_resp_allKeys[-1].name  # just the last key pressed
            thanks_resp.rt = _thanks_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from welcome_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())
# Run 'End Experiment' code from instr_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())

# Run 'End Experiment' code from code_recall
thisExp.addData("final_full_credit_score", final_full_credit_score)
thisExp.addData("final_partial_credit_score", final_partial_credit_score)
thisExp.addData("final_edit_distance_score", final_edit_distance_score)

# Run 'End Experiment' code from instr_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())

# Run 'End Experiment' code from symmetry_answer_code
thisExp.addData("symmetry_time_mean", symmetry_time_mean)
thisExp.addData("symmetry_time_sd", symmetry_time_sd)
thisExp.addData("symmetry_criterion", symmetry_criterion)
# Run 'End Experiment' code from instr_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())

# Run 'End Experiment' code from symmetry_answer_code
thisExp.addData("symmetry_time_mean", symmetry_time_mean)
thisExp.addData("symmetry_time_sd", symmetry_time_sd)
thisExp.addData("symmetry_criterion", symmetry_criterion)
# Run 'End Experiment' code from code_recall
thisExp.addData("final_full_credit_score", final_full_credit_score)
thisExp.addData("final_partial_credit_score", final_partial_credit_score)
thisExp.addData("final_edit_distance_score", final_edit_distance_score)

# Run 'End Experiment' code from instr_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())

# Run 'End Experiment' code from symmetry_answer_code
thisExp.addData("symmetry_time_mean", symmetry_time_mean)
thisExp.addData("symmetry_time_sd", symmetry_time_sd)
thisExp.addData("symmetry_criterion", symmetry_criterion)
# Run 'End Experiment' code from code_recall
thisExp.addData("final_full_credit_score", final_full_credit_score)
thisExp.addData("final_partial_credit_score", final_partial_credit_score)
thisExp.addData("final_edit_distance_score", final_edit_distance_score)


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
