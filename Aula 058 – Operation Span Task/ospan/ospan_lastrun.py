#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on October 11, 2024, at 10:36
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
expName = 'ospan'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\ospan\\ospan_lastrun.py',
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
 
instruction_list = [# memory (letter) task
                   ["""
Neste experimento, você tentará memorizar letras que você verá na tela enquanto você resolve problemas de matemática simples.

Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a parte do experimento com as letras.""",
"""
Para essa prática, letras aparecerão na tela uma de cada vez. Tente lembrar cada letra na ordem em que foram apresentadas.

Depois que 2 letras aparecerem, você verá uma tela com 12 possíveis letras e uma caixa para marcar ao lado de cada letra. Seu trabalho é selecionar cada letra na ordem em que foram apresentadas. 

Para fazer isso, use o mouse para clicar nas letras para selecioná-las. As letras selecionadas irão aparecer na parte de baixo da tela.""",
"""
Depois que selecionar todas as letras, e elas estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.

Se errar, aperte o botão [Limpar] para começar novamente. Se esquecer uma das letras, aperte o botão [Branco] para marcar onde a letra esquecida deve estar.

Lembre-se, é muito importante colocar as letras na mesma ordem que foram apresentadas. Se você esquecer uma letra, use o botão [Branco] para marcar a sua posição.""",
"""
Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a prática com as letras.
"""], 
# distractor (math) task
["""
Agora você irá praticar a parte da matemática deste experimento. Um problema matemático aparecerá na tela, deste jeito: (2 × 1) + 1 = ?

Assim que ver um problema matemático, você deve calcular a resposta correta. No problema acima, a resposta correta é 3.

Quando souber a resposta correta, clique no botão [Continuar].
""",
"""
Você verá um número na próxima tela. 

Se o número na tela for a resposta correta para o problema que você viu, clique no botão [Verdadeiro].

Se o número não for a resposta correta, clique no botão [Falso].
""",
"""
Por exemplo, se você ver o problema (2 × 2) + 1 = ?, e o número na próxima tela for 5, clique no botão [Verdadeiro], pois a resposta está correta.

Se você ver o problema (2 × 2) + 1 = ?, e o número na próxima tela for 6, clique no botão [Falso], pois a resposta correta é 5, não 6.

Depois que clicar em uma das caixas, o computador irá lhe dizer se fez a escolha certa.
""",
"""
É muito importante que você consiga resolver os problemas matemáticos corretamente. Também é importante que você consiga resolvê-los o mais rápido possível.

Favor chamar o pesquisador se você tiver perguntas.

Quando você estiver pronto, clique em [Avançar] para começar a praticar.
"""],
# OSPAN training
["""
Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá fazer um dos problemas matemáticos. Assim que decidir a sua resposta, uma letra aparecerá na tela. Tente se lembrar dessa letra.

Na etapa anterior na qual você apenas resolveu problemas matemáticos, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar para a letra, pular o verdadeiro ou falso e contar o problema como erro.

Por isso é muito importante você resolver os problemas o mais rápido e corretamente possível.
""",
"""
Depois que a letra desaparecer, outro problema matemático irá aparecer, e depois outra letra. No final de cada combinação de letras e problemas, uma tela com letras aparecerá. Use o mouse para selecionar as letras que acabou de ver.

Tente lembrar a ordem correta das letras. É muito importante que você trabalhe rapidamente e corretamente nos problemas matemáticos. Tenha certeza que você sabe a resposta do problema antes de ir para a próxima tela.

O computador não irá dizer se a resposta está correta. Depois da tela com as letras você receberá o resultado do seu desempenho para o número de letras lembradas e a porcentagem de respostas corretas nos problemas matemáticos. Favor chamar o pesquisador se tiver perguntas
""",
"""
Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas matemáticos que você respondeu corretamente para o experimento inteiro.

É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas matemáticos.

Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas matemáticos E lembrar o máximo de letras possíveis.

Favor chamar o pesquisador se tiver perguntas.
"""
],
["""
Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.

Primeiro você terá que resolver um problema, depois terá que memorizar uma letra. Quando ver a tela com as letras, selecione as letras na ordem em que foram apresentadas. Se esquecer de uma letra, clique no botão [Branco] para marcar onde a letra deve ir.

Algumas combinações terão mais problemas matemáticos e letras do que outras.
""",
"""
É importante que você faça o melhor possível nos problemas matemáticos e na parte onde tiver que lembras as letras. 

Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas matemáticos. Também lembre-se de acertar 85% dos problemas.

Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]
                   
# cor do feedback das operações matemáticas
math_color = [0.0000, 0.0000, 0.0000]

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

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.09, wrapWidth=1.8, ori=0.0, 
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

# --- Initialize components for Routine "letter" ---
# Run 'Begin Experiment' code from letters_code
fixed_letters = list("FHJKLNPQRSTY")
letters = list("FHJKLNPQRSTY")

letter_list = list()
to_be_remembered = visual.TextStim(win=win, name='to_be_remembered',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

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
    text='Selecione as letras na mesma ordem em que foram apresentadas. Use o botão [Branco] para escrever letras que esqueceu.',
    font='Times New Roman',
    units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
F = visual.ImageStim(
    win=win,
    name='F', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
H = visual.ImageStim(
    win=win,
    name='H', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
J = visual.ImageStim(
    win=win,
    name='J', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
K = visual.ImageStim(
    win=win,
    name='K', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
L = visual.ImageStim(
    win=win,
    name='L', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
N = visual.ImageStim(
    win=win,
    name='N', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P = visual.ImageStim(
    win=win,
    name='P', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
Q = visual.ImageStim(
    win=win,
    name='Q', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
R = visual.ImageStim(
    win=win,
    name='R', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
S = visual.ImageStim(
    win=win,
    name='S', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
T = visual.ImageStim(
    win=win,
    name='T', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
Y = visual.ImageStim(
    win=win,
    name='Y', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
clear_ = visual.ImageStim(
    win=win,
    name='clear_', units='norm', 
    image='images/clear_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
blank = visual.ImageStim(
    win=win,
    name='blank', units='norm', 
    image='images/blank_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
send = visual.ImageStim(
    win=win,
    name='send', units='norm', 
    image='images/send_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
recall_response = event.Mouse(win=win)
x, y = [None, None]
recall_response.mouseClock = core.Clock()
response_recall = visual.TextStim(win=win, name='response_recall',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.6), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='darkblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);

# --- Initialize components for Routine "recall_feedback" ---
recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
math_feedback_prompt = visual.TextStim(win=win, name='math_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
math_feedback_performance = visual.TextStim(win=win, name='math_feedback_performance',
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
 
instruction_list = [# memory (letter) task
                   ["""
Neste experimento, você tentará memorizar letras que você verá na tela enquanto você resolve problemas de matemática simples.

Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a parte do experimento com as letras.""",
"""
Para essa prática, letras aparecerão na tela uma de cada vez. Tente lembrar cada letra na ordem em que foram apresentadas.

Depois que 2 letras aparecerem, você verá uma tela com 12 possíveis letras e uma caixa para marcar ao lado de cada letra. Seu trabalho é selecionar cada letra na ordem em que foram apresentadas. 

Para fazer isso, use o mouse para clicar nas letras para selecioná-las. As letras selecionadas irão aparecer na parte de baixo da tela.""",
"""
Depois que selecionar todas as letras, e elas estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.

Se errar, aperte o botão [Limpar] para começar novamente. Se esquecer uma das letras, aperte o botão [Branco] para marcar onde a letra esquecida deve estar.

Lembre-se, é muito importante colocar as letras na mesma ordem que foram apresentadas. Se você esquecer uma letra, use o botão [Branco] para marcar a sua posição.""",
"""
Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a prática com as letras.
"""], 
# distractor (math) task
["""
Agora você irá praticar a parte da matemática deste experimento. Um problema matemático aparecerá na tela, deste jeito: (2 × 1) + 1 = ?

Assim que ver um problema matemático, você deve calcular a resposta correta. No problema acima, a resposta correta é 3.

Quando souber a resposta correta, clique no botão [Continuar].
""",
"""
Você verá um número na próxima tela. 

Se o número na tela for a resposta correta para o problema que você viu, clique no botão [Verdadeiro].

Se o número não for a resposta correta, clique no botão [Falso].
""",
"""
Por exemplo, se você ver o problema (2 × 2) + 1 = ?, e o número na próxima tela for 5, clique no botão [Verdadeiro], pois a resposta está correta.

Se você ver o problema (2 × 2) + 1 = ?, e o número na próxima tela for 6, clique no botão [Falso], pois a resposta correta é 5, não 6.

Depois que clicar em uma das caixas, o computador irá lhe dizer se fez a escolha certa.
""",
"""
É muito importante que você consiga resolver os problemas matemáticos corretamente. Também é importante que você consiga resolvê-los o mais rápido possível.

Favor chamar o pesquisador se você tiver perguntas.

Quando você estiver pronto, clique em [Avançar] para começar a praticar.
"""],
# OSPAN training
["""
Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá fazer um dos problemas matemáticos. Assim que decidir a sua resposta, uma letra aparecerá na tela. Tente se lembrar dessa letra.

Na etapa anterior na qual você apenas resolveu problemas matemáticos, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar para a letra, pular o verdadeiro ou falso e contar o problema como erro.

Por isso é muito importante você resolver os problemas o mais rápido e corretamente possível.
""",
"""
Depois que a letra desaparecer, outro problema matemático irá aparecer, e depois outra letra. No final de cada combinação de letras e problemas, uma tela com letras aparecerá. Use o mouse para selecionar as letras que acabou de ver.

Tente lembrar a ordem correta das letras. É muito importante que você trabalhe rapidamente e corretamente nos problemas matemáticos. Tenha certeza que você sabe a resposta do problema antes de ir para a próxima tela.

O computador não irá dizer se a resposta está correta. Depois da tela com as letras você receberá o resultado do seu desempenho para o número de letras lembradas e a porcentagem de respostas corretas nos problemas matemáticos. Favor chamar o pesquisador se tiver perguntas
""",
"""
Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas matemáticos que você respondeu corretamente para o experimento inteiro.

É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas matemáticos.

Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas matemáticos E lembrar o máximo de letras possíveis.

Favor chamar o pesquisador se tiver perguntas.
"""
],
["""
Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.

Primeiro você terá que resolver um problema, depois terá que memorizar uma letra. Quando ver a tela com as letras, selecione as letras na ordem em que foram apresentadas. Se esquecer de uma letra, clique no botão [Branco] para marcar onde a letra deve ir.

Algumas combinações terão mais problemas matemáticos e letras do que outras.
""",
"""
É importante que você faça o melhor possível nos problemas matemáticos e na parte onde tiver que lembras as letras. 

Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas matemáticos. Também lembre-se de acertar 85% dos problemas.

Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]
                   
# cor do feedback das operações matemáticas
math_color = [0.0000, 0.0000, 0.0000]

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

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.09, wrapWidth=1.8, ori=0.0, 
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

# --- Initialize components for Routine "math" ---
# Run 'Begin Experiment' code from math_code
# apenas uma função gigante para criar os diferentes problemas do OSpan
def math_problems():
    math = []

    for OP1 in ["mult", "div"]:
        for OP2 in ["add", "sub"]:
            for i in range(2, 10):
                for j in range(2, 5):
                    for k in range(1, 3):

                        if OP1 == "mult" and OP2 == "add":
                            op1, op2 = "×", "+"
                            result = i * j + k                       
                        elif OP1 == "mult" and OP2 == "sub":
                            op1, op2 = "×", "–"
                            result = i * j - k
                        elif OP1 == "div" and OP2 == "add":
                            op1, op2 = "/", "+"
                            result = i / j + k
                        elif OP1 == "div" and OP2 == "sub":
                            op1, op2 = "/", "–"
                            result = i / j - k

                        if i < j or result <= 0 or result > 10 or not float(result).is_integer():
                            continue

                        # correct problems    
                        string = f"({i} {op1} {j}) {op2} {k} = ?"
                        math.append(("yes", string, f"{int(result)}"))

                        # incorrect problems
                        while True:
                            noise = np.random.choice([-3, -2, -1, 1, 2, 3])
                            check = result + noise
                            if check > 0:
                                result += noise
                                break
                                
                        string = f"({i} {op1} {j}) {op2} {k} = ?"
                        math.append(("no", string, f"{int(result)}"))

    return math

# chamada da função para criar a lista de problemas
math = list()
for i in range(2):
    math.extend(math_problems())

# embaralha a lista
np.random.shuffle(math)
math_count = 0

# contador de tentativas e acertos em matemática
math_total_trials = math_trials_correct = speed_errors = 0
abort_trial = False # controla interrupção da tarefa matemática

# contador de tempo no treino
math_training_time = list()

math_problem = visual.TextStim(win=win, name='math_problem',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
math_prompt = visual.TextStim(win=win, name='math_prompt',
    text='Quando você tiver resolvido o problema matemático, clique em [Continuar]',
    font='Times New Roman',
    units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
continue_ = visual.ImageStim(
    win=win,
    name='continue_', units='norm', 
    image='images/continue_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
math_problem_next = event.Mouse(win=win)
x, y = [None, None]
math_problem_next.mouseClock = core.Clock()

# --- Initialize components for Routine "math_answer" ---
math_answer_screen = visual.TextStim(win=win, name='math_answer_screen',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
true = visual.ImageStim(
    win=win,
    name='true', units='norm', 
    image='images/true_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
false = visual.ImageStim(
    win=win,
    name='false', units='norm', 
    image='images/false_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
math_response = event.Mouse(win=win)
x, y = [None, None]
math_response.mouseClock = core.Clock()

# --- Initialize components for Routine "math_answer_feedback" ---
math_answer_screen_feedback = visual.TextStim(win=win, name='math_answer_screen_feedback',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
true_feedback = visual.ImageStim(
    win=win,
    name='true_feedback', units='norm', 
    image='images/true_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
false_feedback = visual.ImageStim(
    win=win,
    name='false_feedback', units='norm', 
    image='images/false_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
math_corrective_feedback_msg = visual.TextStim(win=win, name='math_corrective_feedback_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color=[-1.0000, -1.0000, 0.0902], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
# índices de instruções
current_instruction = 0
instruction_block = 0
 
instruction_list = [# memory (letter) task
                   ["""
Neste experimento, você tentará memorizar letras que você verá na tela enquanto você resolve problemas de matemática simples.

Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a parte do experimento com as letras.""",
"""
Para essa prática, letras aparecerão na tela uma de cada vez. Tente lembrar cada letra na ordem em que foram apresentadas.

Depois que 2 letras aparecerem, você verá uma tela com 12 possíveis letras e uma caixa para marcar ao lado de cada letra. Seu trabalho é selecionar cada letra na ordem em que foram apresentadas. 

Para fazer isso, use o mouse para clicar nas letras para selecioná-las. As letras selecionadas irão aparecer na parte de baixo da tela.""",
"""
Depois que selecionar todas as letras, e elas estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.

Se errar, aperte o botão [Limpar] para começar novamente. Se esquecer uma das letras, aperte o botão [Branco] para marcar onde a letra esquecida deve estar.

Lembre-se, é muito importante colocar as letras na mesma ordem que foram apresentadas. Se você esquecer uma letra, use o botão [Branco] para marcar a sua posição.""",
"""
Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a prática com as letras.
"""], 
# distractor (math) task
["""
Agora você irá praticar a parte da matemática deste experimento. Um problema matemático aparecerá na tela, deste jeito: (2 × 1) + 1 = ?

Assim que ver um problema matemático, você deve calcular a resposta correta. No problema acima, a resposta correta é 3.

Quando souber a resposta correta, clique no botão [Continuar].
""",
"""
Você verá um número na próxima tela. 

Se o número na tela for a resposta correta para o problema que você viu, clique no botão [Verdadeiro].

Se o número não for a resposta correta, clique no botão [Falso].
""",
"""
Por exemplo, se você ver o problema (2 × 2) + 1 = ?, e o número na próxima tela for 5, clique no botão [Verdadeiro], pois a resposta está correta.

Se você ver o problema (2 × 2) + 1 = ?, e o número na próxima tela for 6, clique no botão [Falso], pois a resposta correta é 5, não 6.

Depois que clicar em uma das caixas, o computador irá lhe dizer se fez a escolha certa.
""",
"""
É muito importante que você consiga resolver os problemas matemáticos corretamente. Também é importante que você consiga resolvê-los o mais rápido possível.

Favor chamar o pesquisador se você tiver perguntas.

Quando você estiver pronto, clique em [Avançar] para começar a praticar.
"""],
# OSPAN training
["""
Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá fazer um dos problemas matemáticos. Assim que decidir a sua resposta, uma letra aparecerá na tela. Tente se lembrar dessa letra.

Na etapa anterior na qual você apenas resolveu problemas matemáticos, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar para a letra, pular o verdadeiro ou falso e contar o problema como erro.

Por isso é muito importante você resolver os problemas o mais rápido e corretamente possível.
""",
"""
Depois que a letra desaparecer, outro problema matemático irá aparecer, e depois outra letra. No final de cada combinação de letras e problemas, uma tela com letras aparecerá. Use o mouse para selecionar as letras que acabou de ver.

Tente lembrar a ordem correta das letras. É muito importante que você trabalhe rapidamente e corretamente nos problemas matemáticos. Tenha certeza que você sabe a resposta do problema antes de ir para a próxima tela.

O computador não irá dizer se a resposta está correta. Depois da tela com as letras você receberá o resultado do seu desempenho para o número de letras lembradas e a porcentagem de respostas corretas nos problemas matemáticos. Favor chamar o pesquisador se tiver perguntas
""",
"""
Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas matemáticos que você respondeu corretamente para o experimento inteiro.

É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas matemáticos.

Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas matemáticos E lembrar o máximo de letras possíveis.

Favor chamar o pesquisador se tiver perguntas.
"""
],
["""
Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.

Primeiro você terá que resolver um problema, depois terá que memorizar uma letra. Quando ver a tela com as letras, selecione as letras na ordem em que foram apresentadas. Se esquecer de uma letra, clique no botão [Branco] para marcar onde a letra deve ir.

Algumas combinações terão mais problemas matemáticos e letras do que outras.
""",
"""
É importante que você faça o melhor possível nos problemas matemáticos e na parte onde tiver que lembras as letras. 

Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas matemáticos. Também lembre-se de acertar 85% dos problemas.

Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]
                   
# cor do feedback das operações matemáticas
math_color = [0.0000, 0.0000, 0.0000]

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

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.09, wrapWidth=1.8, ori=0.0, 
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

# --- Initialize components for Routine "math" ---
# Run 'Begin Experiment' code from math_code
# apenas uma função gigante para criar os diferentes problemas do OSpan
def math_problems():
    math = []

    for OP1 in ["mult", "div"]:
        for OP2 in ["add", "sub"]:
            for i in range(2, 10):
                for j in range(2, 5):
                    for k in range(1, 3):

                        if OP1 == "mult" and OP2 == "add":
                            op1, op2 = "×", "+"
                            result = i * j + k                       
                        elif OP1 == "mult" and OP2 == "sub":
                            op1, op2 = "×", "–"
                            result = i * j - k
                        elif OP1 == "div" and OP2 == "add":
                            op1, op2 = "/", "+"
                            result = i / j + k
                        elif OP1 == "div" and OP2 == "sub":
                            op1, op2 = "/", "–"
                            result = i / j - k

                        if i < j or result <= 0 or result > 10 or not float(result).is_integer():
                            continue

                        # correct problems    
                        string = f"({i} {op1} {j}) {op2} {k} = ?"
                        math.append(("yes", string, f"{int(result)}"))

                        # incorrect problems
                        while True:
                            noise = np.random.choice([-3, -2, -1, 1, 2, 3])
                            check = result + noise
                            if check > 0:
                                result += noise
                                break
                                
                        string = f"({i} {op1} {j}) {op2} {k} = ?"
                        math.append(("no", string, f"{int(result)}"))

    return math

# chamada da função para criar a lista de problemas
math = list()
for i in range(2):
    math.extend(math_problems())

# embaralha a lista
np.random.shuffle(math)
math_count = 0

# contador de tentativas e acertos em matemática
math_total_trials = math_trials_correct = speed_errors = 0
abort_trial = False # controla interrupção da tarefa matemática

# contador de tempo no treino
math_training_time = list()

math_problem = visual.TextStim(win=win, name='math_problem',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
math_prompt = visual.TextStim(win=win, name='math_prompt',
    text='Quando você tiver resolvido o problema matemático, clique em [Continuar]',
    font='Times New Roman',
    units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
continue_ = visual.ImageStim(
    win=win,
    name='continue_', units='norm', 
    image='images/continue_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
math_problem_next = event.Mouse(win=win)
x, y = [None, None]
math_problem_next.mouseClock = core.Clock()

# --- Initialize components for Routine "math_answer" ---
math_answer_screen = visual.TextStim(win=win, name='math_answer_screen',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
true = visual.ImageStim(
    win=win,
    name='true', units='norm', 
    image='images/true_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
false = visual.ImageStim(
    win=win,
    name='false', units='norm', 
    image='images/false_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
math_response = event.Mouse(win=win)
x, y = [None, None]
math_response.mouseClock = core.Clock()

# --- Initialize components for Routine "letter" ---
# Run 'Begin Experiment' code from letters_code
fixed_letters = list("FHJKLNPQRSTY")
letters = list("FHJKLNPQRSTY")

letter_list = list()
to_be_remembered = visual.TextStim(win=win, name='to_be_remembered',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

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
    text='Selecione as letras na mesma ordem em que foram apresentadas. Use o botão [Branco] para escrever letras que esqueceu.',
    font='Times New Roman',
    units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
F = visual.ImageStim(
    win=win,
    name='F', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
H = visual.ImageStim(
    win=win,
    name='H', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
J = visual.ImageStim(
    win=win,
    name='J', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
K = visual.ImageStim(
    win=win,
    name='K', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
L = visual.ImageStim(
    win=win,
    name='L', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
N = visual.ImageStim(
    win=win,
    name='N', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P = visual.ImageStim(
    win=win,
    name='P', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
Q = visual.ImageStim(
    win=win,
    name='Q', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
R = visual.ImageStim(
    win=win,
    name='R', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
S = visual.ImageStim(
    win=win,
    name='S', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
T = visual.ImageStim(
    win=win,
    name='T', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
Y = visual.ImageStim(
    win=win,
    name='Y', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
clear_ = visual.ImageStim(
    win=win,
    name='clear_', units='norm', 
    image='images/clear_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
blank = visual.ImageStim(
    win=win,
    name='blank', units='norm', 
    image='images/blank_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
send = visual.ImageStim(
    win=win,
    name='send', units='norm', 
    image='images/send_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
recall_response = event.Mouse(win=win)
x, y = [None, None]
recall_response.mouseClock = core.Clock()
response_recall = visual.TextStim(win=win, name='response_recall',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.6), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='darkblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);

# --- Initialize components for Routine "recall_feedback" ---
recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
math_feedback_prompt = visual.TextStim(win=win, name='math_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
math_feedback_performance = visual.TextStim(win=win, name='math_feedback_performance',
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
 
instruction_list = [# memory (letter) task
                   ["""
Neste experimento, você tentará memorizar letras que você verá na tela enquanto você resolve problemas de matemática simples.

Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a parte do experimento com as letras.""",
"""
Para essa prática, letras aparecerão na tela uma de cada vez. Tente lembrar cada letra na ordem em que foram apresentadas.

Depois que 2 letras aparecerem, você verá uma tela com 12 possíveis letras e uma caixa para marcar ao lado de cada letra. Seu trabalho é selecionar cada letra na ordem em que foram apresentadas. 

Para fazer isso, use o mouse para clicar nas letras para selecioná-las. As letras selecionadas irão aparecer na parte de baixo da tela.""",
"""
Depois que selecionar todas as letras, e elas estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.

Se errar, aperte o botão [Limpar] para começar novamente. Se esquecer uma das letras, aperte o botão [Branco] para marcar onde a letra esquecida deve estar.

Lembre-se, é muito importante colocar as letras na mesma ordem que foram apresentadas. Se você esquecer uma letra, use o botão [Branco] para marcar a sua posição.""",
"""
Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a prática com as letras.
"""], 
# distractor (math) task
["""
Agora você irá praticar a parte da matemática deste experimento. Um problema matemático aparecerá na tela, deste jeito: (2 × 1) + 1 = ?

Assim que ver um problema matemático, você deve calcular a resposta correta. No problema acima, a resposta correta é 3.

Quando souber a resposta correta, clique no botão [Continuar].
""",
"""
Você verá um número na próxima tela. 

Se o número na tela for a resposta correta para o problema que você viu, clique no botão [Verdadeiro].

Se o número não for a resposta correta, clique no botão [Falso].
""",
"""
Por exemplo, se você ver o problema (2 × 2) + 1 = ?, e o número na próxima tela for 5, clique no botão [Verdadeiro], pois a resposta está correta.

Se você ver o problema (2 × 2) + 1 = ?, e o número na próxima tela for 6, clique no botão [Falso], pois a resposta correta é 5, não 6.

Depois que clicar em uma das caixas, o computador irá lhe dizer se fez a escolha certa.
""",
"""
É muito importante que você consiga resolver os problemas matemáticos corretamente. Também é importante que você consiga resolvê-los o mais rápido possível.

Favor chamar o pesquisador se você tiver perguntas.

Quando você estiver pronto, clique em [Avançar] para começar a praticar.
"""],
# OSPAN training
["""
Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá fazer um dos problemas matemáticos. Assim que decidir a sua resposta, uma letra aparecerá na tela. Tente se lembrar dessa letra.

Na etapa anterior na qual você apenas resolveu problemas matemáticos, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar para a letra, pular o verdadeiro ou falso e contar o problema como erro.

Por isso é muito importante você resolver os problemas o mais rápido e corretamente possível.
""",
"""
Depois que a letra desaparecer, outro problema matemático irá aparecer, e depois outra letra. No final de cada combinação de letras e problemas, uma tela com letras aparecerá. Use o mouse para selecionar as letras que acabou de ver.

Tente lembrar a ordem correta das letras. É muito importante que você trabalhe rapidamente e corretamente nos problemas matemáticos. Tenha certeza que você sabe a resposta do problema antes de ir para a próxima tela.

O computador não irá dizer se a resposta está correta. Depois da tela com as letras você receberá o resultado do seu desempenho para o número de letras lembradas e a porcentagem de respostas corretas nos problemas matemáticos. Favor chamar o pesquisador se tiver perguntas
""",
"""
Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas matemáticos que você respondeu corretamente para o experimento inteiro.

É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas matemáticos.

Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas matemáticos E lembrar o máximo de letras possíveis.

Favor chamar o pesquisador se tiver perguntas.
"""
],
["""
Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.

Primeiro você terá que resolver um problema, depois terá que memorizar uma letra. Quando ver a tela com as letras, selecione as letras na ordem em que foram apresentadas. Se esquecer de uma letra, clique no botão [Branco] para marcar onde a letra deve ir.

Algumas combinações terão mais problemas matemáticos e letras do que outras.
""",
"""
É importante que você faça o melhor possível nos problemas matemáticos e na parte onde tiver que lembras as letras. 

Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas matemáticos. Também lembre-se de acertar 85% dos problemas.

Favor chamar o pesquisador se tiver alguma pergunta.

Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]
                   
# cor do feedback das operações matemáticas
math_color = [0.0000, 0.0000, 0.0000]

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

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.09, wrapWidth=1.8, ori=0.0, 
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

# --- Initialize components for Routine "math" ---
# Run 'Begin Experiment' code from math_code
# apenas uma função gigante para criar os diferentes problemas do OSpan
def math_problems():
    math = []

    for OP1 in ["mult", "div"]:
        for OP2 in ["add", "sub"]:
            for i in range(2, 10):
                for j in range(2, 5):
                    for k in range(1, 3):

                        if OP1 == "mult" and OP2 == "add":
                            op1, op2 = "×", "+"
                            result = i * j + k                       
                        elif OP1 == "mult" and OP2 == "sub":
                            op1, op2 = "×", "–"
                            result = i * j - k
                        elif OP1 == "div" and OP2 == "add":
                            op1, op2 = "/", "+"
                            result = i / j + k
                        elif OP1 == "div" and OP2 == "sub":
                            op1, op2 = "/", "–"
                            result = i / j - k

                        if i < j or result <= 0 or result > 10 or not float(result).is_integer():
                            continue

                        # correct problems    
                        string = f"({i} {op1} {j}) {op2} {k} = ?"
                        math.append(("yes", string, f"{int(result)}"))

                        # incorrect problems
                        while True:
                            noise = np.random.choice([-3, -2, -1, 1, 2, 3])
                            check = result + noise
                            if check > 0:
                                result += noise
                                break
                                
                        string = f"({i} {op1} {j}) {op2} {k} = ?"
                        math.append(("no", string, f"{int(result)}"))

    return math

# chamada da função para criar a lista de problemas
math = list()
for i in range(2):
    math.extend(math_problems())

# embaralha a lista
np.random.shuffle(math)
math_count = 0

# contador de tentativas e acertos em matemática
math_total_trials = math_trials_correct = speed_errors = 0
abort_trial = False # controla interrupção da tarefa matemática

# contador de tempo no treino
math_training_time = list()

math_problem = visual.TextStim(win=win, name='math_problem',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
math_prompt = visual.TextStim(win=win, name='math_prompt',
    text='Quando você tiver resolvido o problema matemático, clique em [Continuar]',
    font='Times New Roman',
    units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
continue_ = visual.ImageStim(
    win=win,
    name='continue_', units='norm', 
    image='images/continue_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
math_problem_next = event.Mouse(win=win)
x, y = [None, None]
math_problem_next.mouseClock = core.Clock()

# --- Initialize components for Routine "math_answer" ---
math_answer_screen = visual.TextStim(win=win, name='math_answer_screen',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
true = visual.ImageStim(
    win=win,
    name='true', units='norm', 
    image='images/true_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
false = visual.ImageStim(
    win=win,
    name='false', units='norm', 
    image='images/false_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
math_response = event.Mouse(win=win)
x, y = [None, None]
math_response.mouseClock = core.Clock()

# --- Initialize components for Routine "letter" ---
# Run 'Begin Experiment' code from letters_code
fixed_letters = list("FHJKLNPQRSTY")
letters = list("FHJKLNPQRSTY")

letter_list = list()
to_be_remembered = visual.TextStim(win=win, name='to_be_remembered',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

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
    text='Selecione as letras na mesma ordem em que foram apresentadas. Use o botão [Branco] para escrever letras que esqueceu.',
    font='Times New Roman',
    units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
F = visual.ImageStim(
    win=win,
    name='F', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
H = visual.ImageStim(
    win=win,
    name='H', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
J = visual.ImageStim(
    win=win,
    name='J', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
K = visual.ImageStim(
    win=win,
    name='K', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
L = visual.ImageStim(
    win=win,
    name='L', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
N = visual.ImageStim(
    win=win,
    name='N', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P = visual.ImageStim(
    win=win,
    name='P', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
Q = visual.ImageStim(
    win=win,
    name='Q', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
R = visual.ImageStim(
    win=win,
    name='R', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
S = visual.ImageStim(
    win=win,
    name='S', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
T = visual.ImageStim(
    win=win,
    name='T', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
Y = visual.ImageStim(
    win=win,
    name='Y', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
clear_ = visual.ImageStim(
    win=win,
    name='clear_', units='norm', 
    image='images/clear_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
blank = visual.ImageStim(
    win=win,
    name='blank', units='norm', 
    image='images/blank_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
send = visual.ImageStim(
    win=win,
    name='send', units='norm', 
    image='images/send_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
recall_response = event.Mouse(win=win)
x, y = [None, None]
recall_response.mouseClock = core.Clock()
response_recall = visual.TextStim(win=win, name='response_recall',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.6), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='darkblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);

# --- Initialize components for Routine "recall_feedback" ---
recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
math_feedback_prompt = visual.TextStim(win=win, name='math_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
math_feedback_performance = visual.TextStim(win=win, name='math_feedback_performance',
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
letter_instructions = data.TrialHandler(nReps=999, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='letter_instructions')
thisExp.addLoop(letter_instructions)  # add the loop to the experiment
thisLetter_instruction = letter_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLetter_instruction.rgb)
if thisLetter_instruction != None:
    for paramName in thisLetter_instruction:
        exec('{} = thisLetter_instruction[paramName]'.format(paramName))

for thisLetter_instruction in letter_instructions:
    currentLoop = letter_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisLetter_instruction.rgb)
    if thisLetter_instruction != None:
        for paramName in thisLetter_instruction:
            exec('{} = thisLetter_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instr_code
    my_count = 0 # contador de tentativas da tarefa distratora
    instr_msg.setText(instruction_list[instruction_block][current_instruction])
    # setup some python lists for storing info about the instr_resp
    instr_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionComponents = [instr_msg, previous, next, instr_resp]
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
            letter_instructions.finished = True # encerra o loop do treino da tarefa de memória
        elif instruction_block == 1:
            instruction_block += 1
            math_instructions.finished = True # encerra o loop do treino da tarefa matemática
        elif instruction_block == 2:
            instruction_block += 1
            ospan_training_instructions.finished = True # encerra o loop de treino do OSPAN
        elif instruction_block == 3:
            instruction_block += 1
            ospan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
    
    # store data for letter_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999 repeats of 'letter_instructions'


# set up handler to look after randomisation of conditions etc
letter_practice_trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('span.xlsx', selection='0:1'),
    seed=None, name='letter_practice_trials')
thisExp.addLoop(letter_practice_trials)  # add the loop to the experiment
thisLetter_practice_trial = letter_practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLetter_practice_trial.rgb)
if thisLetter_practice_trial != None:
    for paramName in thisLetter_practice_trial:
        exec('{} = thisLetter_practice_trial[paramName]'.format(paramName))

for thisLetter_practice_trial in letter_practice_trials:
    currentLoop = letter_practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLetter_practice_trial.rgb)
    if thisLetter_practice_trial != None:
        for paramName in thisLetter_practice_trial:
            exec('{} = thisLetter_practice_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    letter_practice = data.TrialHandler(nReps=current_span, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='letter_practice')
    thisExp.addLoop(letter_practice)  # add the loop to the experiment
    thisLetter_practice = letter_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLetter_practice.rgb)
    if thisLetter_practice != None:
        for paramName in thisLetter_practice:
            exec('{} = thisLetter_practice[paramName]'.format(paramName))
    
    for thisLetter_practice in letter_practice:
        currentLoop = letter_practice
        # abbreviate parameter names if possible (e.g. rgb = thisLetter_practice.rgb)
        if thisLetter_practice != None:
            for paramName in thisLetter_practice:
                exec('{} = thisLetter_practice[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "letter" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from letters_code
        # tenta atribuir o valor da repetição do loop atual à variável index
        # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
        try:
            index = letter_practice.thisN
        except:
            pass
            
        try:
            index = ospan_training_trial.thisN
        except:
            pass
        
        try:
            index = ospan_testing_trial.thisN
        except:
            pass
        
        # tenta embaralhar as letras sempre que estivermos em uma nova tentativa
        try:
            # se é a primeira execução do loop...
            if letter_practice.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if ospan_training_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if ospan_testing_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        # cria uma lista de imagens (que está na subpasta "images")
        for letter in fixed_letters:
            letter_list.append(f"images/{letter}_gray.jpg")
        to_be_remembered.setText(correct_response[index])
        # keep track of which components have finished
        letterComponents = [to_be_remembered]
        for thisComponent in letterComponents:
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
        
        # --- Run Routine "letter" ---
        while continueRoutine and routineTimer.getTime() < 0.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *to_be_remembered* updates
            if to_be_remembered.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                to_be_remembered.frameNStart = frameN  # exact frame index
                to_be_remembered.tStart = t  # local t and not account for scr refresh
                to_be_remembered.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(to_be_remembered, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'to_be_remembered.started')
                to_be_remembered.setAutoDraw(True)
            if to_be_remembered.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > to_be_remembered.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    to_be_remembered.tStop = t  # not accounting for scr refresh
                    to_be_remembered.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'to_be_remembered.stopped')
                    to_be_remembered.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in letterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "letter" ---
        for thisComponent in letterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-0.800000)
        thisExp.nextEntry()
        
    # completed current_span repeats of 'letter_practice'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_recall
    clicked_things = []
    clickables = [F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]
    allowed_send = False
    allowed_blank = True
    
    my_response = "Minha resposta: "
    
    try:
        if letter_practice_trials.thisN == 0:
            task_phase = "letter_practice_phase"
    except:
        pass
    
    try:
        if ospan_training_trials.thisN == 0:
            task_phase = "ospan_training_trials"
    except:
        pass
    
    try:
        if ospan_testing_trials.thisN == 0:
            task_phase = "ospan_testing_trials"
    except:
        pass
    
    F.setImage(letter_list[0])
    H.setImage(letter_list[1])
    J.setImage(letter_list[2])
    K.setImage(letter_list[3])
    L.setImage(letter_list[4])
    N.setImage(letter_list[5])
    P.setImage(letter_list[6])
    Q.setImage(letter_list[7])
    R.setImage(letter_list[8])
    S.setImage(letter_list[9])
    T.setImage(letter_list[10])
    Y.setImage(letter_list[11])
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
    recallComponents = [prompt_recall, F, H, J, K, L, N, P, Q, R, S, T, Y, clear_, blank, send, recall_response, response_recall]
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
            # if a button was pressed in
            if recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                # and it wasn't send, clear_, and blank buttons
                if (clickable != send) and (clickable != clear_) and (clickable != blank):
                    clicked_things.append(clickable.name)
                    clickable.setImage(f"images/{fixed_letters[i]}_blue.jpg", log = False)
                    my_response = f"{my_response}{fixed_letters[i]}"
                    allowed_send = True
                # and it was the clear_ button
                elif clickable == clear_:
                    for i, clickable in enumerate(clickables[:-3]):
                        clickable.setImage(f"images/{fixed_letters[i]}_gray.jpg", log = False)
                    # reset values
                    clicked_things = []
                    my_response = "Minha resposta: "
                    allowed_send = False # reset
                # and it was the blank button:
                elif (clickable == blank) and (allowed_blank == True):
                    # to prevent two consecutive responses
                    allowed_blank = False 
                    blank_clock = core.Clock() 
                    #clicked_things.append(clickable.name)
                    my_response = f"{my_response}–"
                    allowed_send = True
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
        
        # *Q* updates
        if Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q.frameNStart = frameN  # exact frame index
            Q.tStart = t  # local t and not account for scr refresh
            Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q.started')
            Q.setAutoDraw(True)
        
        # *R* updates
        if R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R.frameNStart = frameN  # exact frame index
            R.tStart = t  # local t and not account for scr refresh
            R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R.started')
            R.setAutoDraw(True)
        
        # *S* updates
        if S.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            S.frameNStart = frameN  # exact frame index
            S.tStart = t  # local t and not account for scr refresh
            S.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(S, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'S.started')
            S.setAutoDraw(True)
        
        # *T* updates
        if T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T.frameNStart = frameN  # exact frame index
            T.tStart = t  # local t and not account for scr refresh
            T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'T.started')
            T.setAutoDraw(True)
        
        # *Y* updates
        if Y.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Y.frameNStart = frameN  # exact frame index
            Y.tStart = t  # local t and not account for scr refresh
            Y.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Y, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Y.started')
            Y.setAutoDraw(True)
        
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
                        iter([F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank])
                        clickableList = [F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]
                    except:
                        clickableList = [[F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]]
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
        
        # *response_recall* updates
        if response_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_recall.frameNStart = frameN  # exact frame index
            response_recall.tStart = t  # local t and not account for scr refresh
            response_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_recall, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_recall.started')
            response_recall.setAutoDraw(True)
        if response_recall.status == STARTED:  # only update if drawing
            response_recall.setText(my_response, log=False)
        
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
    participant_response = my_response[16:]
    
    # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
    if participant_response == correct_response:
        full_credit_score = current_span
    else:
        full_credit_score = 0
    
    # crédito parcial (pontua apenas acertos na mesma posição serial)
    partial_credit_score = partial_credit(participant_response, correct_response)
    
    # edit distance score
    edit_distance_score = EditDistanceScore(correct_response, participant_response)
    
    # créditos completo parcial e edit distance, somatório da sessão (máx. 75)
    try:
        if ospan_testing_trials.thisN >= 0:
            final_full_credit_score += full_credit_score
            final_partial_credit_score += partial_credit_score
            final_edit_distance_score += edit_distance_score
    except:
        pass
    
    # criando texto para feedback
    if partial_credit_score > 1:
        word = "letras"    
    elif partial_credit_score <= 1:
        word = "letra"
    
    # mensagens de feedback de recordação e das operações matemáticas
    recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
    
    try:
        math_percent_correct = (math_trials_correct / math_total_trials) * 100
    except ZeroDivisionError:
        math_percent_correct = 0
    
    math_performance_msg = f"{math_percent_correct:.0f}%"
    
    try:
        if math_errors > 1:
            math_feedback_msg = f"Você cometeu {math_errors} erros neste conjunto de tentativas" 
        elif math_errors == 1:
            math_feedback_msg = f"Você cometeu {math_errors} erro neste conjunto de tentativas"
        else:
            math_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
    except:
        math_feedback_msg = ""
       
    # salva respostas
    thisExp.addData("correct_response", correct_response)
    thisExp.addData("participant_response", participant_response)
    thisExp.addData("full_credit_score", full_credit_score)
    thisExp.addData("partial_credit_score", partial_credit_score)
    thisExp.addData("edit_distance_score", edit_distance_score)
    thisExp.addData("task_phase", task_phase)
    thisExp.addData("math_trials_correct", math_trials_correct)
    thisExp.addData("math_total_trials", math_total_trials)
    thisExp.addData("math_percent_correct", math_percent_correct)
    try:
        thisExp.addData("math_errors", math_errors)
    except:
        pass
    
    # store data for letter_practice_trials (TrialHandler)
    letter_practice_trials.addData('recall_response.x', recall_response.x)
    letter_practice_trials.addData('recall_response.y', recall_response.y)
    letter_practice_trials.addData('recall_response.leftButton', recall_response.leftButton)
    letter_practice_trials.addData('recall_response.midButton', recall_response.midButton)
    letter_practice_trials.addData('recall_response.rightButton', recall_response.rightButton)
    letter_practice_trials.addData('recall_response.time', recall_response.time)
    letter_practice_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "recall_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    recall_feedback_prompt.setText(recall_feedback_msg)
    math_feedback_prompt.setText(math_feedback_msg)
    math_feedback_performance.setColor(math_color, colorSpace='rgb')
    math_feedback_performance.setText(math_performance_msg)
    # keep track of which components have finished
    recall_feedbackComponents = [recall_feedback_prompt, math_feedback_prompt, math_feedback_performance]
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
        
        # *math_feedback_prompt* updates
        if math_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_feedback_prompt.frameNStart = frameN  # exact frame index
            math_feedback_prompt.tStart = t  # local t and not account for scr refresh
            math_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_feedback_prompt.started')
            math_feedback_prompt.setAutoDraw(True)
        if math_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                math_feedback_prompt.tStop = t  # not accounting for scr refresh
                math_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_feedback_prompt.stopped')
                math_feedback_prompt.setAutoDraw(False)
        
        # *math_feedback_performance* updates
        if math_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_feedback_performance.frameNStart = frameN  # exact frame index
            math_feedback_performance.tStart = t  # local t and not account for scr refresh
            math_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_feedback_performance, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_feedback_performance.started')
            math_feedback_performance.setAutoDraw(True)
        if math_feedback_performance.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_feedback_performance.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                math_feedback_performance.tStop = t  # not accounting for scr refresh
                math_feedback_performance.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_feedback_performance.stopped')
                math_feedback_performance.setAutoDraw(False)
        
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
    
# completed 3.0 repeats of 'letter_practice_trials'


# set up handler to look after randomisation of conditions etc
math_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='math_instructions')
thisExp.addLoop(math_instructions)  # add the loop to the experiment
thisMath_instruction = math_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMath_instruction.rgb)
if thisMath_instruction != None:
    for paramName in thisMath_instruction:
        exec('{} = thisMath_instruction[paramName]'.format(paramName))

for thisMath_instruction in math_instructions:
    currentLoop = math_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisMath_instruction.rgb)
    if thisMath_instruction != None:
        for paramName in thisMath_instruction:
            exec('{} = thisMath_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instr_code
    my_count = 0 # contador de tentativas da tarefa distratora
    instr_msg.setText(instruction_list[instruction_block][current_instruction])
    # setup some python lists for storing info about the instr_resp
    instr_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionComponents = [instr_msg, previous, next, instr_resp]
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
            letter_instructions.finished = True # encerra o loop do treino da tarefa de memória
        elif instruction_block == 1:
            instruction_block += 1
            math_instructions.finished = True # encerra o loop do treino da tarefa matemática
        elif instruction_block == 2:
            instruction_block += 1
            ospan_training_instructions.finished = True # encerra o loop de treino do OSPAN
        elif instruction_block == 3:
            instruction_block += 1
            ospan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
    
    # store data for math_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'math_instructions'


# set up handler to look after randomisation of conditions etc
math_practice_trials = data.TrialHandler(nReps=15.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='math_practice_trials')
thisExp.addLoop(math_practice_trials)  # add the loop to the experiment
thisMath_practice_trial = math_practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMath_practice_trial.rgb)
if thisMath_practice_trial != None:
    for paramName in thisMath_practice_trial:
        exec('{} = thisMath_practice_trial[paramName]'.format(paramName))

for thisMath_practice_trial in math_practice_trials:
    currentLoop = math_practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMath_practice_trial.rgb)
    if thisMath_practice_trial != None:
        for paramName in thisMath_practice_trial:
            exec('{} = thisMath_practice_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "math" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from math_code
    math_clock = core.Clock()
    
    try:
        # se é a primeira execução do loop...
        if math_practice_trials.thisN == 0:
            math_color = "red" # agora teremos feedback na cor vermelha
            math_errors = 0
    except:
        pass
        
    try:
        # se é a primeira execução do loop...
        if ospan_training_trial.thisN == 0:
            math_errors = 0
    except:
        pass
        
    try:
        # se é a primeira execução do loop...
        if ospan_testing_trial.thisN == 0:
            math_errors = 0
    except:
        pass
        
    # reseta os contadores quando começa o OSPAN para valer
    try:
        if (ospan_testing_trials.thisN == 0) and (ospan_testing_trial.thisN == 0):
            math_total_trials = math_trials_correct = speed_errors = 0
    except:
        pass
    math_problem.setText(math[math_count][1])
    # setup some python lists for storing info about the math_problem_next
    math_problem_next.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    mathComponents = [math_problem, math_prompt, continue_, math_problem_next]
    for thisComponent in mathComponents:
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
    
    # --- Run Routine "math" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from math_code
        try:
            # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
            if math_clock.getTime() >= math_criterion:
                speed_errors += 1
                abort_trial = True
                continueRoutine = False
        except:
            pass
          
        
        # *math_problem* updates
        if math_problem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_problem.frameNStart = frameN  # exact frame index
            math_problem.tStart = t  # local t and not account for scr refresh
            math_problem.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_problem, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_problem.started')
            math_problem.setAutoDraw(True)
        
        # *math_prompt* updates
        if math_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_prompt.frameNStart = frameN  # exact frame index
            math_prompt.tStart = t  # local t and not account for scr refresh
            math_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_prompt.started')
            math_prompt.setAutoDraw(True)
        
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
        # *math_problem_next* updates
        if math_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_problem_next.frameNStart = frameN  # exact frame index
            math_problem_next.tStart = t  # local t and not account for scr refresh
            math_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_problem_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('math_problem_next.started', t)
            math_problem_next.status = STARTED
            math_problem_next.mouseClock.reset()
            prevButtonState = math_problem_next.getPressed()  # if button is down already this ISN'T a new click
        if math_problem_next.status == STARTED:  # only update if started and not finished!
            buttons = math_problem_next.getPressed()
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
                        if obj.contains(math_problem_next):
                            gotValidClick = True
                            math_problem_next.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mathComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "math" ---
    for thisComponent in mathComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from math_code
    # salva variáveis
    thisExp.addData("math_problem", math[math_count][1]) # enunciado
    thisExp.addData("math_correct_response", math[math_count][0]) # gabarito
    thisExp.addData("math_problem_response", math[math_count][2]) # resultado da conta
    
    if abort_trial:
        math_speed_error = 1 # abortou devido a velocidade
    else:
        math_speed_error = 0 # abortou devido a velocidade
    
    try:
        thisExp.addData("problem_rt", math_clock.getTime()) # problem RT
    except:
        pass
    
    # store data for math_practice_trials (TrialHandler)
    # the Routine "math" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "math_answer" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from math_answer_code
    answer_clock = core.Clock()
    
    if abort_trial:
        continueRoutine = False
    math_answer_screen.setText(math[math_count][2])
    # setup some python lists for storing info about the math_response
    math_response.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    math_answerComponents = [math_answer_screen, true, false, math_response]
    for thisComponent in math_answerComponents:
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
    
    # --- Run Routine "math_answer" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from math_answer_code
        try:
            # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
            if math_clock.getTime() >= math_criterion:
                speed_errors += 1
                abort_trial = True
                continueRoutine = False
        except:
            pass
        
        
        # *math_answer_screen* updates
        if math_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_answer_screen.frameNStart = frameN  # exact frame index
            math_answer_screen.tStart = t  # local t and not account for scr refresh
            math_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_answer_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_answer_screen.started')
            math_answer_screen.setAutoDraw(True)
        
        # *true* updates
        if true.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            true.frameNStart = frameN  # exact frame index
            true.tStart = t  # local t and not account for scr refresh
            true.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(true, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'true.started')
            true.setAutoDraw(True)
        
        # *false* updates
        if false.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            false.frameNStart = frameN  # exact frame index
            false.tStart = t  # local t and not account for scr refresh
            false.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(false, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'false.started')
            false.setAutoDraw(True)
        # *math_response* updates
        if math_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_response.frameNStart = frameN  # exact frame index
            math_response.tStart = t  # local t and not account for scr refresh
            math_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('math_response.started', t)
            math_response.status = STARTED
            math_response.mouseClock.reset()
            prevButtonState = math_response.getPressed()  # if button is down already this ISN'T a new click
        if math_response.status == STARTED:  # only update if started and not finished!
            buttons = math_response.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([true, false])
                        clickableList = [true, false]
                    except:
                        clickableList = [[true, false]]
                    for obj in clickableList:
                        if obj.contains(math_response):
                            gotValidClick = True
                            math_response.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in math_answerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "math_answer" ---
    for thisComponent in math_answerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from math_answer_code
    try:
        if math_response.clicked_name[0] == "true":
            math_participant_response = "yes"
        else:
            math_participant_response = "no"
    except:
        math_participant_response = ""
        math_speed_error = 1
    
    try:
        thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
    except:
        pass
    
    # se o participante acertou
    if math_participant_response == math[math_count][0]:
        math_participant_corr = 1
        math_accuracy_error = 0 # contagem de erros de acurácia
        math_trials_correct += 1 # incrementa número de acertos da sessão toda
        math_corrective_feedback = "Correto"
    else:
        math_participant_corr = 0
        math_corrective_feedback = "Incorreto"
        math_errors += 1 # incrementa o número de erros apenas da presente tentativa
    
        if math_speed_error == 0:
            math_accuracy_error = 1
        else:
            math_accuracy_error = 0
    
    # sempre incrementa o contador de tentativas
    math_total_trials += 1
    
    if abort_trial:
        thisExp.addData("math_speed_error", 1) # erro de velocidade
        abort_trial = False # reseta para a próxima tentativa
    else:
        thisExp.addData("math_speed_error", 0)
    
    # salva variáveis
    thisExp.addData("math_accuracy_error", math_accuracy_error) # erro de acurácia
    thisExp.addData("math_participant_corr", math_participant_corr) # 1 = acerto, 0 = erro
    thisExp.addData("math_problem", math[math_count][1]) # enunciado
    thisExp.addData("math_correct_response", math[math_count][0]) # gabarito
    thisExp.addData("math_problem_response", math[math_count][2]) # resultado da conta
    thisExp.addData("math_participant_response", math_participant_response) # resposta do participante
    
    # incrementa operação para próxima iteração
    math_count += 1
    
    # soma a duração da tarefa matemática
    try:
        if math_practice_trials.thisN < 15:
            math_training_time.append(math_clock.getTime()) # e guarda tempo em uma lista
            # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
            if math_practice_trials.thisN == 14:
                math_time_mean = np.mean(np.array(math_training_time))
                math_time_sd = np.std(np.array(math_training_time), ddof = 1)
                math_criterion = math_time_mean + 2 * math_time_sd
                
    except:
        pass
    
    # store data for math_practice_trials (TrialHandler)
    # the Routine "math_answer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "math_answer_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    math_answer_screen_feedback.setText(math[math_count - 1][2])
    math_corrective_feedback_msg.setText(math_corrective_feedback)
    # keep track of which components have finished
    math_answer_feedbackComponents = [math_answer_screen_feedback, true_feedback, false_feedback, math_corrective_feedback_msg]
    for thisComponent in math_answer_feedbackComponents:
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
    
    # --- Run Routine "math_answer_feedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *math_answer_screen_feedback* updates
        if math_answer_screen_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_answer_screen_feedback.frameNStart = frameN  # exact frame index
            math_answer_screen_feedback.tStart = t  # local t and not account for scr refresh
            math_answer_screen_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_answer_screen_feedback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_answer_screen_feedback.started')
            math_answer_screen_feedback.setAutoDraw(True)
        if math_answer_screen_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_answer_screen_feedback.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                math_answer_screen_feedback.tStop = t  # not accounting for scr refresh
                math_answer_screen_feedback.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_answer_screen_feedback.stopped')
                math_answer_screen_feedback.setAutoDraw(False)
        
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
        
        # *math_corrective_feedback_msg* updates
        if math_corrective_feedback_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_corrective_feedback_msg.frameNStart = frameN  # exact frame index
            math_corrective_feedback_msg.tStart = t  # local t and not account for scr refresh
            math_corrective_feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_corrective_feedback_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_corrective_feedback_msg.started')
            math_corrective_feedback_msg.setAutoDraw(True)
        if math_corrective_feedback_msg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_corrective_feedback_msg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                math_corrective_feedback_msg.tStop = t  # not accounting for scr refresh
                math_corrective_feedback_msg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_corrective_feedback_msg.stopped')
                math_corrective_feedback_msg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in math_answer_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "math_answer_feedback" ---
    for thisComponent in math_answer_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 15.0 repeats of 'math_practice_trials'


# set up handler to look after randomisation of conditions etc
ospan_training_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ospan_training_instructions')
thisExp.addLoop(ospan_training_instructions)  # add the loop to the experiment
thisOspan_training_instruction = ospan_training_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOspan_training_instruction.rgb)
if thisOspan_training_instruction != None:
    for paramName in thisOspan_training_instruction:
        exec('{} = thisOspan_training_instruction[paramName]'.format(paramName))

for thisOspan_training_instruction in ospan_training_instructions:
    currentLoop = ospan_training_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisOspan_training_instruction.rgb)
    if thisOspan_training_instruction != None:
        for paramName in thisOspan_training_instruction:
            exec('{} = thisOspan_training_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instr_code
    my_count = 0 # contador de tentativas da tarefa distratora
    instr_msg.setText(instruction_list[instruction_block][current_instruction])
    # setup some python lists for storing info about the instr_resp
    instr_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionComponents = [instr_msg, previous, next, instr_resp]
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
            letter_instructions.finished = True # encerra o loop do treino da tarefa de memória
        elif instruction_block == 1:
            instruction_block += 1
            math_instructions.finished = True # encerra o loop do treino da tarefa matemática
        elif instruction_block == 2:
            instruction_block += 1
            ospan_training_instructions.finished = True # encerra o loop de treino do OSPAN
        elif instruction_block == 3:
            instruction_block += 1
            ospan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
    
    # store data for ospan_training_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'ospan_training_instructions'


# set up handler to look after randomisation of conditions etc
ospan_training_trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('span.xlsx', selection='0'),
    seed=None, name='ospan_training_trials')
thisExp.addLoop(ospan_training_trials)  # add the loop to the experiment
thisOspan_training_trial = ospan_training_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOspan_training_trial.rgb)
if thisOspan_training_trial != None:
    for paramName in thisOspan_training_trial:
        exec('{} = thisOspan_training_trial[paramName]'.format(paramName))

for thisOspan_training_trial in ospan_training_trials:
    currentLoop = ospan_training_trials
    # abbreviate parameter names if possible (e.g. rgb = thisOspan_training_trial.rgb)
    if thisOspan_training_trial != None:
        for paramName in thisOspan_training_trial:
            exec('{} = thisOspan_training_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    ospan_training_trial = data.TrialHandler(nReps=current_span, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ospan_training_trial')
    thisExp.addLoop(ospan_training_trial)  # add the loop to the experiment
    thisOspan_training_trial = ospan_training_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOspan_training_trial.rgb)
    if thisOspan_training_trial != None:
        for paramName in thisOspan_training_trial:
            exec('{} = thisOspan_training_trial[paramName]'.format(paramName))
    
    for thisOspan_training_trial in ospan_training_trial:
        currentLoop = ospan_training_trial
        # abbreviate parameter names if possible (e.g. rgb = thisOspan_training_trial.rgb)
        if thisOspan_training_trial != None:
            for paramName in thisOspan_training_trial:
                exec('{} = thisOspan_training_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "math" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from math_code
        math_clock = core.Clock()
        
        try:
            # se é a primeira execução do loop...
            if math_practice_trials.thisN == 0:
                math_color = "red" # agora teremos feedback na cor vermelha
                math_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if ospan_training_trial.thisN == 0:
                math_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if ospan_testing_trial.thisN == 0:
                math_errors = 0
        except:
            pass
            
        # reseta os contadores quando começa o OSPAN para valer
        try:
            if (ospan_testing_trials.thisN == 0) and (ospan_testing_trial.thisN == 0):
                math_total_trials = math_trials_correct = speed_errors = 0
        except:
            pass
        math_problem.setText(math[math_count][1])
        # setup some python lists for storing info about the math_problem_next
        math_problem_next.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mathComponents = [math_problem, math_prompt, continue_, math_problem_next]
        for thisComponent in mathComponents:
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
        
        # --- Run Routine "math" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from math_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if math_clock.getTime() >= math_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
              
            
            # *math_problem* updates
            if math_problem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_problem.frameNStart = frameN  # exact frame index
                math_problem.tStart = t  # local t and not account for scr refresh
                math_problem.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_problem, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_problem.started')
                math_problem.setAutoDraw(True)
            
            # *math_prompt* updates
            if math_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_prompt.frameNStart = frameN  # exact frame index
                math_prompt.tStart = t  # local t and not account for scr refresh
                math_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_prompt.started')
                math_prompt.setAutoDraw(True)
            
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
            # *math_problem_next* updates
            if math_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_problem_next.frameNStart = frameN  # exact frame index
                math_problem_next.tStart = t  # local t and not account for scr refresh
                math_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_problem_next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('math_problem_next.started', t)
                math_problem_next.status = STARTED
                math_problem_next.mouseClock.reset()
                prevButtonState = math_problem_next.getPressed()  # if button is down already this ISN'T a new click
            if math_problem_next.status == STARTED:  # only update if started and not finished!
                buttons = math_problem_next.getPressed()
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
                            if obj.contains(math_problem_next):
                                gotValidClick = True
                                math_problem_next.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mathComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "math" ---
        for thisComponent in mathComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from math_code
        # salva variáveis
        thisExp.addData("math_problem", math[math_count][1]) # enunciado
        thisExp.addData("math_correct_response", math[math_count][0]) # gabarito
        thisExp.addData("math_problem_response", math[math_count][2]) # resultado da conta
        
        if abort_trial:
            math_speed_error = 1 # abortou devido a velocidade
        else:
            math_speed_error = 0 # abortou devido a velocidade
        
        try:
            thisExp.addData("problem_rt", math_clock.getTime()) # problem RT
        except:
            pass
        
        # store data for ospan_training_trial (TrialHandler)
        # the Routine "math" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "math_answer" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from math_answer_code
        answer_clock = core.Clock()
        
        if abort_trial:
            continueRoutine = False
        math_answer_screen.setText(math[math_count][2])
        # setup some python lists for storing info about the math_response
        math_response.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        math_answerComponents = [math_answer_screen, true, false, math_response]
        for thisComponent in math_answerComponents:
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
        
        # --- Run Routine "math_answer" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from math_answer_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if math_clock.getTime() >= math_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
            
            
            # *math_answer_screen* updates
            if math_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_answer_screen.frameNStart = frameN  # exact frame index
                math_answer_screen.tStart = t  # local t and not account for scr refresh
                math_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_answer_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_answer_screen.started')
                math_answer_screen.setAutoDraw(True)
            
            # *true* updates
            if true.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                true.frameNStart = frameN  # exact frame index
                true.tStart = t  # local t and not account for scr refresh
                true.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(true, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'true.started')
                true.setAutoDraw(True)
            
            # *false* updates
            if false.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                false.frameNStart = frameN  # exact frame index
                false.tStart = t  # local t and not account for scr refresh
                false.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(false, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'false.started')
                false.setAutoDraw(True)
            # *math_response* updates
            if math_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_response.frameNStart = frameN  # exact frame index
                math_response.tStart = t  # local t and not account for scr refresh
                math_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('math_response.started', t)
                math_response.status = STARTED
                math_response.mouseClock.reset()
                prevButtonState = math_response.getPressed()  # if button is down already this ISN'T a new click
            if math_response.status == STARTED:  # only update if started and not finished!
                buttons = math_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([true, false])
                            clickableList = [true, false]
                        except:
                            clickableList = [[true, false]]
                        for obj in clickableList:
                            if obj.contains(math_response):
                                gotValidClick = True
                                math_response.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in math_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "math_answer" ---
        for thisComponent in math_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from math_answer_code
        try:
            if math_response.clicked_name[0] == "true":
                math_participant_response = "yes"
            else:
                math_participant_response = "no"
        except:
            math_participant_response = ""
            math_speed_error = 1
        
        try:
            thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
        except:
            pass
        
        # se o participante acertou
        if math_participant_response == math[math_count][0]:
            math_participant_corr = 1
            math_accuracy_error = 0 # contagem de erros de acurácia
            math_trials_correct += 1 # incrementa número de acertos da sessão toda
            math_corrective_feedback = "Correto"
        else:
            math_participant_corr = 0
            math_corrective_feedback = "Incorreto"
            math_errors += 1 # incrementa o número de erros apenas da presente tentativa
        
            if math_speed_error == 0:
                math_accuracy_error = 1
            else:
                math_accuracy_error = 0
        
        # sempre incrementa o contador de tentativas
        math_total_trials += 1
        
        if abort_trial:
            thisExp.addData("math_speed_error", 1) # erro de velocidade
            abort_trial = False # reseta para a próxima tentativa
        else:
            thisExp.addData("math_speed_error", 0)
        
        # salva variáveis
        thisExp.addData("math_accuracy_error", math_accuracy_error) # erro de acurácia
        thisExp.addData("math_participant_corr", math_participant_corr) # 1 = acerto, 0 = erro
        thisExp.addData("math_problem", math[math_count][1]) # enunciado
        thisExp.addData("math_correct_response", math[math_count][0]) # gabarito
        thisExp.addData("math_problem_response", math[math_count][2]) # resultado da conta
        thisExp.addData("math_participant_response", math_participant_response) # resposta do participante
        
        # incrementa operação para próxima iteração
        math_count += 1
        
        # soma a duração da tarefa matemática
        try:
            if math_practice_trials.thisN < 15:
                math_training_time.append(math_clock.getTime()) # e guarda tempo em uma lista
                # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
                if math_practice_trials.thisN == 14:
                    math_time_mean = np.mean(np.array(math_training_time))
                    math_time_sd = np.std(np.array(math_training_time), ddof = 1)
                    math_criterion = math_time_mean + 2 * math_time_sd
                    
        except:
            pass
        
        # store data for ospan_training_trial (TrialHandler)
        # the Routine "math_answer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "letter" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from letters_code
        # tenta atribuir o valor da repetição do loop atual à variável index
        # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
        try:
            index = letter_practice.thisN
        except:
            pass
            
        try:
            index = ospan_training_trial.thisN
        except:
            pass
        
        try:
            index = ospan_testing_trial.thisN
        except:
            pass
        
        # tenta embaralhar as letras sempre que estivermos em uma nova tentativa
        try:
            # se é a primeira execução do loop...
            if letter_practice.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if ospan_training_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if ospan_testing_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        # cria uma lista de imagens (que está na subpasta "images")
        for letter in fixed_letters:
            letter_list.append(f"images/{letter}_gray.jpg")
        to_be_remembered.setText(correct_response[index])
        # keep track of which components have finished
        letterComponents = [to_be_remembered]
        for thisComponent in letterComponents:
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
        
        # --- Run Routine "letter" ---
        while continueRoutine and routineTimer.getTime() < 0.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *to_be_remembered* updates
            if to_be_remembered.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                to_be_remembered.frameNStart = frameN  # exact frame index
                to_be_remembered.tStart = t  # local t and not account for scr refresh
                to_be_remembered.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(to_be_remembered, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'to_be_remembered.started')
                to_be_remembered.setAutoDraw(True)
            if to_be_remembered.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > to_be_remembered.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    to_be_remembered.tStop = t  # not accounting for scr refresh
                    to_be_remembered.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'to_be_remembered.stopped')
                    to_be_remembered.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in letterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "letter" ---
        for thisComponent in letterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-0.800000)
        thisExp.nextEntry()
        
    # completed current_span repeats of 'ospan_training_trial'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_recall
    clicked_things = []
    clickables = [F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]
    allowed_send = False
    allowed_blank = True
    
    my_response = "Minha resposta: "
    
    try:
        if letter_practice_trials.thisN == 0:
            task_phase = "letter_practice_phase"
    except:
        pass
    
    try:
        if ospan_training_trials.thisN == 0:
            task_phase = "ospan_training_trials"
    except:
        pass
    
    try:
        if ospan_testing_trials.thisN == 0:
            task_phase = "ospan_testing_trials"
    except:
        pass
    
    F.setImage(letter_list[0])
    H.setImage(letter_list[1])
    J.setImage(letter_list[2])
    K.setImage(letter_list[3])
    L.setImage(letter_list[4])
    N.setImage(letter_list[5])
    P.setImage(letter_list[6])
    Q.setImage(letter_list[7])
    R.setImage(letter_list[8])
    S.setImage(letter_list[9])
    T.setImage(letter_list[10])
    Y.setImage(letter_list[11])
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
    recallComponents = [prompt_recall, F, H, J, K, L, N, P, Q, R, S, T, Y, clear_, blank, send, recall_response, response_recall]
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
            # if a button was pressed in
            if recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                # and it wasn't send, clear_, and blank buttons
                if (clickable != send) and (clickable != clear_) and (clickable != blank):
                    clicked_things.append(clickable.name)
                    clickable.setImage(f"images/{fixed_letters[i]}_blue.jpg", log = False)
                    my_response = f"{my_response}{fixed_letters[i]}"
                    allowed_send = True
                # and it was the clear_ button
                elif clickable == clear_:
                    for i, clickable in enumerate(clickables[:-3]):
                        clickable.setImage(f"images/{fixed_letters[i]}_gray.jpg", log = False)
                    # reset values
                    clicked_things = []
                    my_response = "Minha resposta: "
                    allowed_send = False # reset
                # and it was the blank button:
                elif (clickable == blank) and (allowed_blank == True):
                    # to prevent two consecutive responses
                    allowed_blank = False 
                    blank_clock = core.Clock() 
                    #clicked_things.append(clickable.name)
                    my_response = f"{my_response}–"
                    allowed_send = True
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
        
        # *Q* updates
        if Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q.frameNStart = frameN  # exact frame index
            Q.tStart = t  # local t and not account for scr refresh
            Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q.started')
            Q.setAutoDraw(True)
        
        # *R* updates
        if R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R.frameNStart = frameN  # exact frame index
            R.tStart = t  # local t and not account for scr refresh
            R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R.started')
            R.setAutoDraw(True)
        
        # *S* updates
        if S.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            S.frameNStart = frameN  # exact frame index
            S.tStart = t  # local t and not account for scr refresh
            S.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(S, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'S.started')
            S.setAutoDraw(True)
        
        # *T* updates
        if T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T.frameNStart = frameN  # exact frame index
            T.tStart = t  # local t and not account for scr refresh
            T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'T.started')
            T.setAutoDraw(True)
        
        # *Y* updates
        if Y.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Y.frameNStart = frameN  # exact frame index
            Y.tStart = t  # local t and not account for scr refresh
            Y.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Y, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Y.started')
            Y.setAutoDraw(True)
        
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
                        iter([F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank])
                        clickableList = [F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]
                    except:
                        clickableList = [[F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]]
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
        
        # *response_recall* updates
        if response_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_recall.frameNStart = frameN  # exact frame index
            response_recall.tStart = t  # local t and not account for scr refresh
            response_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_recall, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_recall.started')
            response_recall.setAutoDraw(True)
        if response_recall.status == STARTED:  # only update if drawing
            response_recall.setText(my_response, log=False)
        
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
    participant_response = my_response[16:]
    
    # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
    if participant_response == correct_response:
        full_credit_score = current_span
    else:
        full_credit_score = 0
    
    # crédito parcial (pontua apenas acertos na mesma posição serial)
    partial_credit_score = partial_credit(participant_response, correct_response)
    
    # edit distance score
    edit_distance_score = EditDistanceScore(correct_response, participant_response)
    
    # créditos completo parcial e edit distance, somatório da sessão (máx. 75)
    try:
        if ospan_testing_trials.thisN >= 0:
            final_full_credit_score += full_credit_score
            final_partial_credit_score += partial_credit_score
            final_edit_distance_score += edit_distance_score
    except:
        pass
    
    # criando texto para feedback
    if partial_credit_score > 1:
        word = "letras"    
    elif partial_credit_score <= 1:
        word = "letra"
    
    # mensagens de feedback de recordação e das operações matemáticas
    recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
    
    try:
        math_percent_correct = (math_trials_correct / math_total_trials) * 100
    except ZeroDivisionError:
        math_percent_correct = 0
    
    math_performance_msg = f"{math_percent_correct:.0f}%"
    
    try:
        if math_errors > 1:
            math_feedback_msg = f"Você cometeu {math_errors} erros neste conjunto de tentativas" 
        elif math_errors == 1:
            math_feedback_msg = f"Você cometeu {math_errors} erro neste conjunto de tentativas"
        else:
            math_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
    except:
        math_feedback_msg = ""
       
    # salva respostas
    thisExp.addData("correct_response", correct_response)
    thisExp.addData("participant_response", participant_response)
    thisExp.addData("full_credit_score", full_credit_score)
    thisExp.addData("partial_credit_score", partial_credit_score)
    thisExp.addData("edit_distance_score", edit_distance_score)
    thisExp.addData("task_phase", task_phase)
    thisExp.addData("math_trials_correct", math_trials_correct)
    thisExp.addData("math_total_trials", math_total_trials)
    thisExp.addData("math_percent_correct", math_percent_correct)
    try:
        thisExp.addData("math_errors", math_errors)
    except:
        pass
    
    # store data for ospan_training_trials (TrialHandler)
    ospan_training_trials.addData('recall_response.x', recall_response.x)
    ospan_training_trials.addData('recall_response.y', recall_response.y)
    ospan_training_trials.addData('recall_response.leftButton', recall_response.leftButton)
    ospan_training_trials.addData('recall_response.midButton', recall_response.midButton)
    ospan_training_trials.addData('recall_response.rightButton', recall_response.rightButton)
    ospan_training_trials.addData('recall_response.time', recall_response.time)
    ospan_training_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "recall_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    recall_feedback_prompt.setText(recall_feedback_msg)
    math_feedback_prompt.setText(math_feedback_msg)
    math_feedback_performance.setColor(math_color, colorSpace='rgb')
    math_feedback_performance.setText(math_performance_msg)
    # keep track of which components have finished
    recall_feedbackComponents = [recall_feedback_prompt, math_feedback_prompt, math_feedback_performance]
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
        
        # *math_feedback_prompt* updates
        if math_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_feedback_prompt.frameNStart = frameN  # exact frame index
            math_feedback_prompt.tStart = t  # local t and not account for scr refresh
            math_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_feedback_prompt.started')
            math_feedback_prompt.setAutoDraw(True)
        if math_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                math_feedback_prompt.tStop = t  # not accounting for scr refresh
                math_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_feedback_prompt.stopped')
                math_feedback_prompt.setAutoDraw(False)
        
        # *math_feedback_performance* updates
        if math_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_feedback_performance.frameNStart = frameN  # exact frame index
            math_feedback_performance.tStart = t  # local t and not account for scr refresh
            math_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_feedback_performance, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_feedback_performance.started')
            math_feedback_performance.setAutoDraw(True)
        if math_feedback_performance.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_feedback_performance.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                math_feedback_performance.tStop = t  # not accounting for scr refresh
                math_feedback_performance.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_feedback_performance.stopped')
                math_feedback_performance.setAutoDraw(False)
        
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
    
# completed 3.0 repeats of 'ospan_training_trials'


# set up handler to look after randomisation of conditions etc
ospan_testing_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ospan_testing_instructions')
thisExp.addLoop(ospan_testing_instructions)  # add the loop to the experiment
thisOspan_testing_instruction = ospan_testing_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOspan_testing_instruction.rgb)
if thisOspan_testing_instruction != None:
    for paramName in thisOspan_testing_instruction:
        exec('{} = thisOspan_testing_instruction[paramName]'.format(paramName))

for thisOspan_testing_instruction in ospan_testing_instructions:
    currentLoop = ospan_testing_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisOspan_testing_instruction.rgb)
    if thisOspan_testing_instruction != None:
        for paramName in thisOspan_testing_instruction:
            exec('{} = thisOspan_testing_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instr_code
    my_count = 0 # contador de tentativas da tarefa distratora
    instr_msg.setText(instruction_list[instruction_block][current_instruction])
    # setup some python lists for storing info about the instr_resp
    instr_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionComponents = [instr_msg, previous, next, instr_resp]
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
            letter_instructions.finished = True # encerra o loop do treino da tarefa de memória
        elif instruction_block == 1:
            instruction_block += 1
            math_instructions.finished = True # encerra o loop do treino da tarefa matemática
        elif instruction_block == 2:
            instruction_block += 1
            ospan_training_instructions.finished = True # encerra o loop de treino do OSPAN
        elif instruction_block == 3:
            instruction_block += 1
            ospan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
    
    # store data for ospan_testing_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'ospan_testing_instructions'


# set up handler to look after randomisation of conditions etc
ospan_testing_trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('span.xlsx', selection='1:'),
    seed=None, name='ospan_testing_trials')
thisExp.addLoop(ospan_testing_trials)  # add the loop to the experiment
thisOspan_testing_trial = ospan_testing_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOspan_testing_trial.rgb)
if thisOspan_testing_trial != None:
    for paramName in thisOspan_testing_trial:
        exec('{} = thisOspan_testing_trial[paramName]'.format(paramName))

for thisOspan_testing_trial in ospan_testing_trials:
    currentLoop = ospan_testing_trials
    # abbreviate parameter names if possible (e.g. rgb = thisOspan_testing_trial.rgb)
    if thisOspan_testing_trial != None:
        for paramName in thisOspan_testing_trial:
            exec('{} = thisOspan_testing_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    ospan_testing_trial = data.TrialHandler(nReps=current_span, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ospan_testing_trial')
    thisExp.addLoop(ospan_testing_trial)  # add the loop to the experiment
    thisOspan_testing_trial = ospan_testing_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOspan_testing_trial.rgb)
    if thisOspan_testing_trial != None:
        for paramName in thisOspan_testing_trial:
            exec('{} = thisOspan_testing_trial[paramName]'.format(paramName))
    
    for thisOspan_testing_trial in ospan_testing_trial:
        currentLoop = ospan_testing_trial
        # abbreviate parameter names if possible (e.g. rgb = thisOspan_testing_trial.rgb)
        if thisOspan_testing_trial != None:
            for paramName in thisOspan_testing_trial:
                exec('{} = thisOspan_testing_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "math" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from math_code
        math_clock = core.Clock()
        
        try:
            # se é a primeira execução do loop...
            if math_practice_trials.thisN == 0:
                math_color = "red" # agora teremos feedback na cor vermelha
                math_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if ospan_training_trial.thisN == 0:
                math_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if ospan_testing_trial.thisN == 0:
                math_errors = 0
        except:
            pass
            
        # reseta os contadores quando começa o OSPAN para valer
        try:
            if (ospan_testing_trials.thisN == 0) and (ospan_testing_trial.thisN == 0):
                math_total_trials = math_trials_correct = speed_errors = 0
        except:
            pass
        math_problem.setText(math[math_count][1])
        # setup some python lists for storing info about the math_problem_next
        math_problem_next.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mathComponents = [math_problem, math_prompt, continue_, math_problem_next]
        for thisComponent in mathComponents:
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
        
        # --- Run Routine "math" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from math_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if math_clock.getTime() >= math_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
              
            
            # *math_problem* updates
            if math_problem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_problem.frameNStart = frameN  # exact frame index
                math_problem.tStart = t  # local t and not account for scr refresh
                math_problem.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_problem, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_problem.started')
                math_problem.setAutoDraw(True)
            
            # *math_prompt* updates
            if math_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_prompt.frameNStart = frameN  # exact frame index
                math_prompt.tStart = t  # local t and not account for scr refresh
                math_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_prompt.started')
                math_prompt.setAutoDraw(True)
            
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
            # *math_problem_next* updates
            if math_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_problem_next.frameNStart = frameN  # exact frame index
                math_problem_next.tStart = t  # local t and not account for scr refresh
                math_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_problem_next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('math_problem_next.started', t)
                math_problem_next.status = STARTED
                math_problem_next.mouseClock.reset()
                prevButtonState = math_problem_next.getPressed()  # if button is down already this ISN'T a new click
            if math_problem_next.status == STARTED:  # only update if started and not finished!
                buttons = math_problem_next.getPressed()
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
                            if obj.contains(math_problem_next):
                                gotValidClick = True
                                math_problem_next.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mathComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "math" ---
        for thisComponent in mathComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from math_code
        # salva variáveis
        thisExp.addData("math_problem", math[math_count][1]) # enunciado
        thisExp.addData("math_correct_response", math[math_count][0]) # gabarito
        thisExp.addData("math_problem_response", math[math_count][2]) # resultado da conta
        
        if abort_trial:
            math_speed_error = 1 # abortou devido a velocidade
        else:
            math_speed_error = 0 # abortou devido a velocidade
        
        try:
            thisExp.addData("problem_rt", math_clock.getTime()) # problem RT
        except:
            pass
        
        # store data for ospan_testing_trial (TrialHandler)
        # the Routine "math" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "math_answer" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from math_answer_code
        answer_clock = core.Clock()
        
        if abort_trial:
            continueRoutine = False
        math_answer_screen.setText(math[math_count][2])
        # setup some python lists for storing info about the math_response
        math_response.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        math_answerComponents = [math_answer_screen, true, false, math_response]
        for thisComponent in math_answerComponents:
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
        
        # --- Run Routine "math_answer" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from math_answer_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if math_clock.getTime() >= math_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
            
            
            # *math_answer_screen* updates
            if math_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_answer_screen.frameNStart = frameN  # exact frame index
                math_answer_screen.tStart = t  # local t and not account for scr refresh
                math_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_answer_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_answer_screen.started')
                math_answer_screen.setAutoDraw(True)
            
            # *true* updates
            if true.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                true.frameNStart = frameN  # exact frame index
                true.tStart = t  # local t and not account for scr refresh
                true.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(true, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'true.started')
                true.setAutoDraw(True)
            
            # *false* updates
            if false.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                false.frameNStart = frameN  # exact frame index
                false.tStart = t  # local t and not account for scr refresh
                false.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(false, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'false.started')
                false.setAutoDraw(True)
            # *math_response* updates
            if math_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                math_response.frameNStart = frameN  # exact frame index
                math_response.tStart = t  # local t and not account for scr refresh
                math_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('math_response.started', t)
                math_response.status = STARTED
                math_response.mouseClock.reset()
                prevButtonState = math_response.getPressed()  # if button is down already this ISN'T a new click
            if math_response.status == STARTED:  # only update if started and not finished!
                buttons = math_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([true, false])
                            clickableList = [true, false]
                        except:
                            clickableList = [[true, false]]
                        for obj in clickableList:
                            if obj.contains(math_response):
                                gotValidClick = True
                                math_response.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in math_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "math_answer" ---
        for thisComponent in math_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from math_answer_code
        try:
            if math_response.clicked_name[0] == "true":
                math_participant_response = "yes"
            else:
                math_participant_response = "no"
        except:
            math_participant_response = ""
            math_speed_error = 1
        
        try:
            thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
        except:
            pass
        
        # se o participante acertou
        if math_participant_response == math[math_count][0]:
            math_participant_corr = 1
            math_accuracy_error = 0 # contagem de erros de acurácia
            math_trials_correct += 1 # incrementa número de acertos da sessão toda
            math_corrective_feedback = "Correto"
        else:
            math_participant_corr = 0
            math_corrective_feedback = "Incorreto"
            math_errors += 1 # incrementa o número de erros apenas da presente tentativa
        
            if math_speed_error == 0:
                math_accuracy_error = 1
            else:
                math_accuracy_error = 0
        
        # sempre incrementa o contador de tentativas
        math_total_trials += 1
        
        if abort_trial:
            thisExp.addData("math_speed_error", 1) # erro de velocidade
            abort_trial = False # reseta para a próxima tentativa
        else:
            thisExp.addData("math_speed_error", 0)
        
        # salva variáveis
        thisExp.addData("math_accuracy_error", math_accuracy_error) # erro de acurácia
        thisExp.addData("math_participant_corr", math_participant_corr) # 1 = acerto, 0 = erro
        thisExp.addData("math_problem", math[math_count][1]) # enunciado
        thisExp.addData("math_correct_response", math[math_count][0]) # gabarito
        thisExp.addData("math_problem_response", math[math_count][2]) # resultado da conta
        thisExp.addData("math_participant_response", math_participant_response) # resposta do participante
        
        # incrementa operação para próxima iteração
        math_count += 1
        
        # soma a duração da tarefa matemática
        try:
            if math_practice_trials.thisN < 15:
                math_training_time.append(math_clock.getTime()) # e guarda tempo em uma lista
                # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
                if math_practice_trials.thisN == 14:
                    math_time_mean = np.mean(np.array(math_training_time))
                    math_time_sd = np.std(np.array(math_training_time), ddof = 1)
                    math_criterion = math_time_mean + 2 * math_time_sd
                    
        except:
            pass
        
        # store data for ospan_testing_trial (TrialHandler)
        # the Routine "math_answer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "letter" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from letters_code
        # tenta atribuir o valor da repetição do loop atual à variável index
        # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
        try:
            index = letter_practice.thisN
        except:
            pass
            
        try:
            index = ospan_training_trial.thisN
        except:
            pass
        
        try:
            index = ospan_testing_trial.thisN
        except:
            pass
        
        # tenta embaralhar as letras sempre que estivermos em uma nova tentativa
        try:
            # se é a primeira execução do loop...
            if letter_practice.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if ospan_training_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        try:
            # se é a primeira execução do loop...
            if ospan_testing_trial.thisN == 0:
                # embaralha letras usada na tarefa de armazenamento
                np.random.shuffle(letters) 
                # e seleciona a sequência que será o gabarito da atual rodada
                correct_response = "".join(letters[:current_span]) 
        except:
            pass
        
        # cria uma lista de imagens (que está na subpasta "images")
        for letter in fixed_letters:
            letter_list.append(f"images/{letter}_gray.jpg")
        to_be_remembered.setText(correct_response[index])
        # keep track of which components have finished
        letterComponents = [to_be_remembered]
        for thisComponent in letterComponents:
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
        
        # --- Run Routine "letter" ---
        while continueRoutine and routineTimer.getTime() < 0.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *to_be_remembered* updates
            if to_be_remembered.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                to_be_remembered.frameNStart = frameN  # exact frame index
                to_be_remembered.tStart = t  # local t and not account for scr refresh
                to_be_remembered.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(to_be_remembered, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'to_be_remembered.started')
                to_be_remembered.setAutoDraw(True)
            if to_be_remembered.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > to_be_remembered.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    to_be_remembered.tStop = t  # not accounting for scr refresh
                    to_be_remembered.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'to_be_remembered.stopped')
                    to_be_remembered.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in letterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "letter" ---
        for thisComponent in letterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-0.800000)
        thisExp.nextEntry()
        
    # completed current_span repeats of 'ospan_testing_trial'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_recall
    clicked_things = []
    clickables = [F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]
    allowed_send = False
    allowed_blank = True
    
    my_response = "Minha resposta: "
    
    try:
        if letter_practice_trials.thisN == 0:
            task_phase = "letter_practice_phase"
    except:
        pass
    
    try:
        if ospan_training_trials.thisN == 0:
            task_phase = "ospan_training_trials"
    except:
        pass
    
    try:
        if ospan_testing_trials.thisN == 0:
            task_phase = "ospan_testing_trials"
    except:
        pass
    
    F.setImage(letter_list[0])
    H.setImage(letter_list[1])
    J.setImage(letter_list[2])
    K.setImage(letter_list[3])
    L.setImage(letter_list[4])
    N.setImage(letter_list[5])
    P.setImage(letter_list[6])
    Q.setImage(letter_list[7])
    R.setImage(letter_list[8])
    S.setImage(letter_list[9])
    T.setImage(letter_list[10])
    Y.setImage(letter_list[11])
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
    recallComponents = [prompt_recall, F, H, J, K, L, N, P, Q, R, S, T, Y, clear_, blank, send, recall_response, response_recall]
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
            # if a button was pressed in
            if recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                # and it wasn't send, clear_, and blank buttons
                if (clickable != send) and (clickable != clear_) and (clickable != blank):
                    clicked_things.append(clickable.name)
                    clickable.setImage(f"images/{fixed_letters[i]}_blue.jpg", log = False)
                    my_response = f"{my_response}{fixed_letters[i]}"
                    allowed_send = True
                # and it was the clear_ button
                elif clickable == clear_:
                    for i, clickable in enumerate(clickables[:-3]):
                        clickable.setImage(f"images/{fixed_letters[i]}_gray.jpg", log = False)
                    # reset values
                    clicked_things = []
                    my_response = "Minha resposta: "
                    allowed_send = False # reset
                # and it was the blank button:
                elif (clickable == blank) and (allowed_blank == True):
                    # to prevent two consecutive responses
                    allowed_blank = False 
                    blank_clock = core.Clock() 
                    #clicked_things.append(clickable.name)
                    my_response = f"{my_response}–"
                    allowed_send = True
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
        
        # *Q* updates
        if Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q.frameNStart = frameN  # exact frame index
            Q.tStart = t  # local t and not account for scr refresh
            Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q.started')
            Q.setAutoDraw(True)
        
        # *R* updates
        if R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R.frameNStart = frameN  # exact frame index
            R.tStart = t  # local t and not account for scr refresh
            R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R.started')
            R.setAutoDraw(True)
        
        # *S* updates
        if S.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            S.frameNStart = frameN  # exact frame index
            S.tStart = t  # local t and not account for scr refresh
            S.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(S, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'S.started')
            S.setAutoDraw(True)
        
        # *T* updates
        if T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T.frameNStart = frameN  # exact frame index
            T.tStart = t  # local t and not account for scr refresh
            T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'T.started')
            T.setAutoDraw(True)
        
        # *Y* updates
        if Y.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Y.frameNStart = frameN  # exact frame index
            Y.tStart = t  # local t and not account for scr refresh
            Y.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Y, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Y.started')
            Y.setAutoDraw(True)
        
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
                        iter([F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank])
                        clickableList = [F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]
                    except:
                        clickableList = [[F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]]
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
        
        # *response_recall* updates
        if response_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_recall.frameNStart = frameN  # exact frame index
            response_recall.tStart = t  # local t and not account for scr refresh
            response_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_recall, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_recall.started')
            response_recall.setAutoDraw(True)
        if response_recall.status == STARTED:  # only update if drawing
            response_recall.setText(my_response, log=False)
        
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
    participant_response = my_response[16:]
    
    # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
    if participant_response == correct_response:
        full_credit_score = current_span
    else:
        full_credit_score = 0
    
    # crédito parcial (pontua apenas acertos na mesma posição serial)
    partial_credit_score = partial_credit(participant_response, correct_response)
    
    # edit distance score
    edit_distance_score = EditDistanceScore(correct_response, participant_response)
    
    # créditos completo parcial e edit distance, somatório da sessão (máx. 75)
    try:
        if ospan_testing_trials.thisN >= 0:
            final_full_credit_score += full_credit_score
            final_partial_credit_score += partial_credit_score
            final_edit_distance_score += edit_distance_score
    except:
        pass
    
    # criando texto para feedback
    if partial_credit_score > 1:
        word = "letras"    
    elif partial_credit_score <= 1:
        word = "letra"
    
    # mensagens de feedback de recordação e das operações matemáticas
    recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
    
    try:
        math_percent_correct = (math_trials_correct / math_total_trials) * 100
    except ZeroDivisionError:
        math_percent_correct = 0
    
    math_performance_msg = f"{math_percent_correct:.0f}%"
    
    try:
        if math_errors > 1:
            math_feedback_msg = f"Você cometeu {math_errors} erros neste conjunto de tentativas" 
        elif math_errors == 1:
            math_feedback_msg = f"Você cometeu {math_errors} erro neste conjunto de tentativas"
        else:
            math_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
    except:
        math_feedback_msg = ""
       
    # salva respostas
    thisExp.addData("correct_response", correct_response)
    thisExp.addData("participant_response", participant_response)
    thisExp.addData("full_credit_score", full_credit_score)
    thisExp.addData("partial_credit_score", partial_credit_score)
    thisExp.addData("edit_distance_score", edit_distance_score)
    thisExp.addData("task_phase", task_phase)
    thisExp.addData("math_trials_correct", math_trials_correct)
    thisExp.addData("math_total_trials", math_total_trials)
    thisExp.addData("math_percent_correct", math_percent_correct)
    try:
        thisExp.addData("math_errors", math_errors)
    except:
        pass
    
    # store data for ospan_testing_trials (TrialHandler)
    ospan_testing_trials.addData('recall_response.x', recall_response.x)
    ospan_testing_trials.addData('recall_response.y', recall_response.y)
    ospan_testing_trials.addData('recall_response.leftButton', recall_response.leftButton)
    ospan_testing_trials.addData('recall_response.midButton', recall_response.midButton)
    ospan_testing_trials.addData('recall_response.rightButton', recall_response.rightButton)
    ospan_testing_trials.addData('recall_response.time', recall_response.time)
    ospan_testing_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "recall_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    recall_feedback_prompt.setText(recall_feedback_msg)
    math_feedback_prompt.setText(math_feedback_msg)
    math_feedback_performance.setColor(math_color, colorSpace='rgb')
    math_feedback_performance.setText(math_performance_msg)
    # keep track of which components have finished
    recall_feedbackComponents = [recall_feedback_prompt, math_feedback_prompt, math_feedback_performance]
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
        
        # *math_feedback_prompt* updates
        if math_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_feedback_prompt.frameNStart = frameN  # exact frame index
            math_feedback_prompt.tStart = t  # local t and not account for scr refresh
            math_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_feedback_prompt.started')
            math_feedback_prompt.setAutoDraw(True)
        if math_feedback_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_feedback_prompt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                math_feedback_prompt.tStop = t  # not accounting for scr refresh
                math_feedback_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_feedback_prompt.stopped')
                math_feedback_prompt.setAutoDraw(False)
        
        # *math_feedback_performance* updates
        if math_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_feedback_performance.frameNStart = frameN  # exact frame index
            math_feedback_performance.tStart = t  # local t and not account for scr refresh
            math_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_feedback_performance, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_feedback_performance.started')
            math_feedback_performance.setAutoDraw(True)
        if math_feedback_performance.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_feedback_performance.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                math_feedback_performance.tStop = t  # not accounting for scr refresh
                math_feedback_performance.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_feedback_performance.stopped')
                math_feedback_performance.setAutoDraw(False)
        
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
    
# completed 3.0 repeats of 'ospan_testing_trials'


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

# Run 'End Experiment' code from math_answer_code
thisExp.addData("math_time_mean", math_time_mean)
thisExp.addData("math_time_sd", math_time_sd)
thisExp.addData("math_criterion", math_criterion)
# Run 'End Experiment' code from instr_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())

# Run 'End Experiment' code from math_answer_code
thisExp.addData("math_time_mean", math_time_mean)
thisExp.addData("math_time_sd", math_time_sd)
thisExp.addData("math_criterion", math_criterion)
# Run 'End Experiment' code from code_recall
thisExp.addData("final_full_credit_score", final_full_credit_score)
thisExp.addData("final_partial_credit_score", final_partial_credit_score)
thisExp.addData("final_edit_distance_score", final_edit_distance_score)

# Run 'End Experiment' code from instr_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())

# Run 'End Experiment' code from math_answer_code
thisExp.addData("math_time_mean", math_time_mean)
thisExp.addData("math_time_sd", math_time_sd)
thisExp.addData("math_criterion", math_criterion)
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
