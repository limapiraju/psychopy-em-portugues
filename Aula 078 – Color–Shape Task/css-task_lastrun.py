#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on September 20, 2025, at 21:32
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


# Run 'Before Experiment' code from code
my_color = [0.0000, 0.0000, 0.0000]


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'css-task'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 078 – Color–Shape Task\\css-task_lastrun.py',
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
    monitor='testMonitor', color=my_color, colorSpace='rgb',
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
"""
Color-Shape Switch (CSS) Task (Miyake et al., 2004; Pennington et al., 2024) - Gerador de tentativas

Requisitos da tarefa:

- Participante será exposto às pistas "Forma" ou "Cor";
- Em seguida, aparecerá uma forma geométrica (triângulo ou círculo) em uma dada cor (azul ou verde);
- Participante deverá identificar forma ou cor do objeto, usando as setas do teclado, a depender da pista anterior;
- Designação das setas às alternativas (e.g., left --> triângulo ou círculo/azul ou verde; right --> idem) será
aleatoriamente definida para cada participante;
- N tentativas:
    - N/2 switch trials (uma tentativa com uma pista é sucedida por uma tentativa com a outra pista);
    - N/2 no-switch trials (uma tentativa com uma pista é sucedida por uma tentativa com a mesma pista);
- Para cada tentativa, salvar:
    - Número da tentativa;
    - Pista;
    - Alvo;
    - Tipo de tentativa;
- Separadamente, cria função que define relação entre setas e alternativas.
"""
import random

COLOR_TRIALS = 20
SHAPE_TRIALS = 20
TRIALS = 20

def random_alternatives():
    """
    Define, de forma aleatória, o mapeamento entre teclas (left/right)
    e as respostas corretas para cada dimensão (forma e cor).
    
    Existem 4 possibilidades (equiprováveis), garantindo que:
    - Para as formas: triangle ↔ circle
    - Para as cores: green ↔ blue
    """
    num = random.random()  # sorteia um número entre 0 e 1
    if num > .75:
        return {"triangle": "left", "circle": "right",
                "green": "left", "blue": "right"}
    elif num > .50:
        return {"triangle": "left", "circle": "right",
                "green": "right", "blue": "left"}
    elif num > .25:
        return {"triangle": "right", "circle": "left",
                "green": "left", "blue": "right"}
    else:
        return {"triangle": "right", "circle": "left",
                "green": "right", "blue": "left"}

my_buttons = random_alternatives()      # define mapeamento das teclas para este participante
my_buttons2 = {}                        # representa setas com setas de verdade
             
for k, v in my_buttons.items():         # itera sobre o my_buttons original
    if v == "left":
        my_buttons2[k] = "←"
    elif v == "right":
        my_buttons2[k] = "→"

# define mapeamento dos botões
if my_buttons["triangle"] == "left" and my_buttons["green"] == "left":
    left_text = "Verde OU\nTriângulo"
    right_text = "Azul OU\nCírculo"
elif my_buttons["triangle"] == "left" and my_buttons["green"] == "right":
    left_text = "Azul OU\nTriângulo"
    right_text = "Verde OU\nCírculo"
if my_buttons["triangle"] == "right" and my_buttons["green"] == "left":
    left_text = "Verde OU\nCírculo"
    right_text = "Azul OU\nTriângulo"
if my_buttons["triangle"] == "right" and my_buttons["green"] == "right":
    left_text = "Azul OU\nCírculo"
    right_text = "Verde OU\nTriângulo"

# índices de instruções
current_instruction = 0
block_instruction = 0
 
instruction_list = [[
"""
Neste estudo, você verá formas geométricas na tela (círculos ou triângulos, nas cores azul ou verde).

A sessão terá três etapas. As duas primeiras etapas serão de treino, enquanto a terceira etapa será de teste.
""",
f"""
Na primeira etapa, você verá uma cruz de fixação, seguido de uma forma geométrica. Sua tarefa será identificar a COR de cada forma geométrica:
    
    - Responda [{my_buttons2['blue']}] para a forma geométrica na cor AZUL.
    - Responda [{my_buttons2['green']}] para a forma geométrica na cor VERDE.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à primeira etapa da tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""],
[
"""
Concluímos a primeira etapa da tarefa.

Em seguida, passaremos à segunda etapa.
""",
f"""
Na segunda etapa, você verá uma cruz de fixação, seguido de uma forma geométrica. Sua tarefa será identificar qual é a FORMA geométrica:
    
    - Responda [{my_buttons2['circle']}] para a forma geométrica CÍRCULO.
    - Responda [{my_buttons2['triangle']}] para a forma geométrica TRIÂNGULO.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à segunda etapa da tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""],
[
"""
Concluímos a segunda etapa da tarefa.

Em seguida, passaremos à terceira e mais importante etapa da tarefa.
""",
"""
Agora, no início de cada tentativa, você verá uma cruz de fixação ("+"), seguido de uma de duas palavras:
    
    - "Cor": você deverá identificar a cor da forma (azul ou verde), ignorando a forma em si.
    - "Forma": você deverá identificar a forma propriamente dita (círculo ou triângulo), ignorando a cor da forma.
""",
f"""
Você usará as setas do teclado para dar suas respostas. Nas tentativas com a palavra "Cor":

    - Responda [{my_buttons2['blue']}] para AZUL.
    - Responda [{my_buttons2['green']}] para a forma geométrica na cor VERDE.
""",
f"""
Nas tentativas com a palavra "Forma":
    
    - Responda [{my_buttons2['circle']}] para a forma geométrica CÍRCULO.
    - Responda [{my_buttons2['triangle']}] para a forma geométrica TRIÂNGULO.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à terceira etapa tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]

                   
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
    units='norm', pos=(0, 0.2), height=0.1, wrapWidth=1.8, ori=0.0, 
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

# --- Initialize components for Routine "training_trial" ---
# Run 'Begin Experiment' code from code_2
color_training_check = True
shape_training_check = False
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.4, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_2 = keyboard.Keyboard()
circle_2 = visual.ShapeStim(
    win=win, name='circle_2',units='norm', 
    size=(0.56, 0.80), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
triangle_2 = visual.ShapeStim(
    win=win, name='triangle_2',units='norm', 
    size=(0.56, 0.80), vertices='triangle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
left_msg_2 = visual.TextStim(win=win, name='left_msg_2',
    text='',
    font='Times New Roman',
    units='norm', pos=(-0.5, -0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
right_msg_2 = visual.TextStim(win=win, name='right_msg_2',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.5, -0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
left_button_2 = visual.TextStim(win=win, name='left_button_2',
    text='←',
    font='Times New Roman',
    units='norm', pos=(-0.2, -0.75), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
right_button_2 = visual.TextStim(win=win, name='right_button_2',
    text='→',
    font='Times New Roman',
    units='norm', pos=(0.2, -0.75), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
"""
Color-Shape Switch (CSS) Task (Miyake et al., 2004; Pennington et al., 2024) - Gerador de tentativas

Requisitos da tarefa:

- Participante será exposto às pistas "Forma" ou "Cor";
- Em seguida, aparecerá uma forma geométrica (triângulo ou círculo) em uma dada cor (azul ou verde);
- Participante deverá identificar forma ou cor do objeto, usando as setas do teclado, a depender da pista anterior;
- Designação das setas às alternativas (e.g., left --> triângulo ou círculo/azul ou verde; right --> idem) será
aleatoriamente definida para cada participante;
- N tentativas:
    - N/2 switch trials (uma tentativa com uma pista é sucedida por uma tentativa com a outra pista);
    - N/2 no-switch trials (uma tentativa com uma pista é sucedida por uma tentativa com a mesma pista);
- Para cada tentativa, salvar:
    - Número da tentativa;
    - Pista;
    - Alvo;
    - Tipo de tentativa;
- Separadamente, cria função que define relação entre setas e alternativas.
"""
import random

COLOR_TRIALS = 20
SHAPE_TRIALS = 20
TRIALS = 20

def random_alternatives():
    """
    Define, de forma aleatória, o mapeamento entre teclas (left/right)
    e as respostas corretas para cada dimensão (forma e cor).
    
    Existem 4 possibilidades (equiprováveis), garantindo que:
    - Para as formas: triangle ↔ circle
    - Para as cores: green ↔ blue
    """
    num = random.random()  # sorteia um número entre 0 e 1
    if num > .75:
        return {"triangle": "left", "circle": "right",
                "green": "left", "blue": "right"}
    elif num > .50:
        return {"triangle": "left", "circle": "right",
                "green": "right", "blue": "left"}
    elif num > .25:
        return {"triangle": "right", "circle": "left",
                "green": "left", "blue": "right"}
    else:
        return {"triangle": "right", "circle": "left",
                "green": "right", "blue": "left"}

my_buttons = random_alternatives()      # define mapeamento das teclas para este participante
my_buttons2 = {}                        # representa setas com setas de verdade
             
for k, v in my_buttons.items():         # itera sobre o my_buttons original
    if v == "left":
        my_buttons2[k] = "←"
    elif v == "right":
        my_buttons2[k] = "→"

# define mapeamento dos botões
if my_buttons["triangle"] == "left" and my_buttons["green"] == "left":
    left_text = "Verde OU\nTriângulo"
    right_text = "Azul OU\nCírculo"
elif my_buttons["triangle"] == "left" and my_buttons["green"] == "right":
    left_text = "Azul OU\nTriângulo"
    right_text = "Verde OU\nCírculo"
if my_buttons["triangle"] == "right" and my_buttons["green"] == "left":
    left_text = "Verde OU\nCírculo"
    right_text = "Azul OU\nTriângulo"
if my_buttons["triangle"] == "right" and my_buttons["green"] == "right":
    left_text = "Azul OU\nCírculo"
    right_text = "Verde OU\nTriângulo"

# índices de instruções
current_instruction = 0
block_instruction = 0
 
instruction_list = [[
"""
Neste estudo, você verá formas geométricas na tela (círculos ou triângulos, nas cores azul ou verde).

A sessão terá três etapas. As duas primeiras etapas serão de treino, enquanto a terceira etapa será de teste.
""",
f"""
Na primeira etapa, você verá uma cruz de fixação, seguido de uma forma geométrica. Sua tarefa será identificar a COR de cada forma geométrica:
    
    - Responda [{my_buttons2['blue']}] para a forma geométrica na cor AZUL.
    - Responda [{my_buttons2['green']}] para a forma geométrica na cor VERDE.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à primeira etapa da tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""],
[
"""
Concluímos a primeira etapa da tarefa.

Em seguida, passaremos à segunda etapa.
""",
f"""
Na segunda etapa, você verá uma cruz de fixação, seguido de uma forma geométrica. Sua tarefa será identificar qual é a FORMA geométrica:
    
    - Responda [{my_buttons2['circle']}] para a forma geométrica CÍRCULO.
    - Responda [{my_buttons2['triangle']}] para a forma geométrica TRIÂNGULO.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à segunda etapa da tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""],
[
"""
Concluímos a segunda etapa da tarefa.

Em seguida, passaremos à terceira e mais importante etapa da tarefa.
""",
"""
Agora, no início de cada tentativa, você verá uma cruz de fixação ("+"), seguido de uma de duas palavras:
    
    - "Cor": você deverá identificar a cor da forma (azul ou verde), ignorando a forma em si.
    - "Forma": você deverá identificar a forma propriamente dita (círculo ou triângulo), ignorando a cor da forma.
""",
f"""
Você usará as setas do teclado para dar suas respostas. Nas tentativas com a palavra "Cor":

    - Responda [{my_buttons2['blue']}] para AZUL.
    - Responda [{my_buttons2['green']}] para a forma geométrica na cor VERDE.
""",
f"""
Nas tentativas com a palavra "Forma":
    
    - Responda [{my_buttons2['circle']}] para a forma geométrica CÍRCULO.
    - Responda [{my_buttons2['triangle']}] para a forma geométrica TRIÂNGULO.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à terceira etapa tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]

                   
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
    units='norm', pos=(0, 0.2), height=0.1, wrapWidth=1.8, ori=0.0, 
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

# --- Initialize components for Routine "training_trial" ---
# Run 'Begin Experiment' code from code_2
color_training_check = True
shape_training_check = False
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.4, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_2 = keyboard.Keyboard()
circle_2 = visual.ShapeStim(
    win=win, name='circle_2',units='norm', 
    size=(0.56, 0.80), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
triangle_2 = visual.ShapeStim(
    win=win, name='triangle_2',units='norm', 
    size=(0.56, 0.80), vertices='triangle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
left_msg_2 = visual.TextStim(win=win, name='left_msg_2',
    text='',
    font='Times New Roman',
    units='norm', pos=(-0.5, -0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
right_msg_2 = visual.TextStim(win=win, name='right_msg_2',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.5, -0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
left_button_2 = visual.TextStim(win=win, name='left_button_2',
    text='←',
    font='Times New Roman',
    units='norm', pos=(-0.2, -0.75), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
right_button_2 = visual.TextStim(win=win, name='right_button_2',
    text='→',
    font='Times New Roman',
    units='norm', pos=(0.2, -0.75), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
"""
Color-Shape Switch (CSS) Task (Miyake et al., 2004; Pennington et al., 2024) - Gerador de tentativas

Requisitos da tarefa:

- Participante será exposto às pistas "Forma" ou "Cor";
- Em seguida, aparecerá uma forma geométrica (triângulo ou círculo) em uma dada cor (azul ou verde);
- Participante deverá identificar forma ou cor do objeto, usando as setas do teclado, a depender da pista anterior;
- Designação das setas às alternativas (e.g., left --> triângulo ou círculo/azul ou verde; right --> idem) será
aleatoriamente definida para cada participante;
- N tentativas:
    - N/2 switch trials (uma tentativa com uma pista é sucedida por uma tentativa com a outra pista);
    - N/2 no-switch trials (uma tentativa com uma pista é sucedida por uma tentativa com a mesma pista);
- Para cada tentativa, salvar:
    - Número da tentativa;
    - Pista;
    - Alvo;
    - Tipo de tentativa;
- Separadamente, cria função que define relação entre setas e alternativas.
"""
import random

COLOR_TRIALS = 20
SHAPE_TRIALS = 20
TRIALS = 20

def random_alternatives():
    """
    Define, de forma aleatória, o mapeamento entre teclas (left/right)
    e as respostas corretas para cada dimensão (forma e cor).
    
    Existem 4 possibilidades (equiprováveis), garantindo que:
    - Para as formas: triangle ↔ circle
    - Para as cores: green ↔ blue
    """
    num = random.random()  # sorteia um número entre 0 e 1
    if num > .75:
        return {"triangle": "left", "circle": "right",
                "green": "left", "blue": "right"}
    elif num > .50:
        return {"triangle": "left", "circle": "right",
                "green": "right", "blue": "left"}
    elif num > .25:
        return {"triangle": "right", "circle": "left",
                "green": "left", "blue": "right"}
    else:
        return {"triangle": "right", "circle": "left",
                "green": "right", "blue": "left"}

my_buttons = random_alternatives()      # define mapeamento das teclas para este participante
my_buttons2 = {}                        # representa setas com setas de verdade
             
for k, v in my_buttons.items():         # itera sobre o my_buttons original
    if v == "left":
        my_buttons2[k] = "←"
    elif v == "right":
        my_buttons2[k] = "→"

# define mapeamento dos botões
if my_buttons["triangle"] == "left" and my_buttons["green"] == "left":
    left_text = "Verde OU\nTriângulo"
    right_text = "Azul OU\nCírculo"
elif my_buttons["triangle"] == "left" and my_buttons["green"] == "right":
    left_text = "Azul OU\nTriângulo"
    right_text = "Verde OU\nCírculo"
if my_buttons["triangle"] == "right" and my_buttons["green"] == "left":
    left_text = "Verde OU\nCírculo"
    right_text = "Azul OU\nTriângulo"
if my_buttons["triangle"] == "right" and my_buttons["green"] == "right":
    left_text = "Azul OU\nCírculo"
    right_text = "Verde OU\nTriângulo"

# índices de instruções
current_instruction = 0
block_instruction = 0
 
instruction_list = [[
"""
Neste estudo, você verá formas geométricas na tela (círculos ou triângulos, nas cores azul ou verde).

A sessão terá três etapas. As duas primeiras etapas serão de treino, enquanto a terceira etapa será de teste.
""",
f"""
Na primeira etapa, você verá uma cruz de fixação, seguido de uma forma geométrica. Sua tarefa será identificar a COR de cada forma geométrica:
    
    - Responda [{my_buttons2['blue']}] para a forma geométrica na cor AZUL.
    - Responda [{my_buttons2['green']}] para a forma geométrica na cor VERDE.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à primeira etapa da tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""],
[
"""
Concluímos a primeira etapa da tarefa.

Em seguida, passaremos à segunda etapa.
""",
f"""
Na segunda etapa, você verá uma cruz de fixação, seguido de uma forma geométrica. Sua tarefa será identificar qual é a FORMA geométrica:
    
    - Responda [{my_buttons2['circle']}] para a forma geométrica CÍRCULO.
    - Responda [{my_buttons2['triangle']}] para a forma geométrica TRIÂNGULO.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à segunda etapa da tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""],
[
"""
Concluímos a segunda etapa da tarefa.

Em seguida, passaremos à terceira e mais importante etapa da tarefa.
""",
"""
Agora, no início de cada tentativa, você verá uma cruz de fixação ("+"), seguido de uma de duas palavras:
    
    - "Cor": você deverá identificar a cor da forma (azul ou verde), ignorando a forma em si.
    - "Forma": você deverá identificar a forma propriamente dita (círculo ou triângulo), ignorando a cor da forma.
""",
f"""
Você usará as setas do teclado para dar suas respostas. Nas tentativas com a palavra "Cor":

    - Responda [{my_buttons2['blue']}] para AZUL.
    - Responda [{my_buttons2['green']}] para a forma geométrica na cor VERDE.
""",
f"""
Nas tentativas com a palavra "Forma":
    
    - Responda [{my_buttons2['circle']}] para a forma geométrica CÍRCULO.
    - Responda [{my_buttons2['triangle']}] para a forma geométrica TRIÂNGULO.
""",
"""
Para te ajudar, deixaremos as alternativas de resposta na tela durante a tarefa.

Em seguida, daremos início à terceira etapa tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]]

                   
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
    units='norm', pos=(0, 0.2), height=0.1, wrapWidth=1.8, ori=0.0, 
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

# --- Initialize components for Routine "new_trial" ---
new_trial_prompt = visual.TextStim(win=win, name='new_trial_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
new_trial_next = visual.ImageStim(
    win=win,
    name='new_trial_next', units='norm', 
    image='images/next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
new_trial_resp = event.Mouse(win=win)
x, y = [None, None]
new_trial_resp.mouseClock = core.Clock()

# --- Initialize components for Routine "trial" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.4, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
cue_msg = visual.TextStim(win=win, name='cue_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.8), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()
circle = visual.ShapeStim(
    win=win, name='circle',units='norm', 
    size=(0.56, 0.80), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
triangle = visual.ShapeStim(
    win=win, name='triangle',units='norm', 
    size=(0.56, 0.80), vertices='triangle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
left_msg = visual.TextStim(win=win, name='left_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(-0.5, -0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
right_msg = visual.TextStim(win=win, name='right_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.5, -0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
left_button = visual.TextStim(win=win, name='left_button',
    text='←',
    font='Times New Roman',
    units='norm', pos=(-0.2, -0.75), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
right_button = visual.TextStim(win=win, name='right_button',
    text='→',
    font='Times New Roman',
    units='norm', pos=(0.2, -0.75), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

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
color_instructions = data.TrialHandler(nReps=999, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='color_instructions')
thisExp.addLoop(color_instructions)  # add the loop to the experiment
thisColor_instruction = color_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisColor_instruction.rgb)
if thisColor_instruction != None:
    for paramName in thisColor_instruction:
        exec('{} = thisColor_instruction[paramName]'.format(paramName))

for thisColor_instruction in color_instructions:
    currentLoop = color_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisColor_instruction.rgb)
    if thisColor_instruction != None:
        for paramName in thisColor_instruction:
            exec('{} = thisColor_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    instr_msg.setText(instruction_list[block_instruction][current_instruction])
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
    elif current_instruction == len(instruction_list[block_instruction]):
        if block_instruction == 0:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            color_instructions.finished = True
        elif block_instruction == 1:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            shape_instructions.finished = True
        elif block_instruction == 2:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            color_shape_instructions.finished = True
    
    
    # store data for color_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999 repeats of 'color_instructions'


# set up handler to look after randomisation of conditions etc
color_training = data.TrialHandler(nReps=COLOR_TRIALS, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='color_training')
thisExp.addLoop(color_training)  # add the loop to the experiment
thisColor_training = color_training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisColor_training.rgb)
if thisColor_training != None:
    for paramName in thisColor_training:
        exec('{} = thisColor_training[paramName]'.format(paramName))

for thisColor_training in color_training:
    currentLoop = color_training
    # abbreviate parameter names if possible (e.g. rgb = thisColor_training.rgb)
    if thisColor_training != None:
        for paramName in thisColor_training:
            exec('{} = thisColor_training[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "training_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    if color_training_check:
        # se estamos em color trials
        if color_training.thisN == 0:
            # =========================
            # PARÂMETROS DA TAREFA
            # =========================
            colors = ["blue", "green"]           # possíveis cores
            shapes = ["circle", "triangle"]      # possíveis formas
    
            # =========================
            # GERAR TENTATIVAS
            # =========================
            training_trials = []                 # lista que armazenará os dicionários de cada tentativa
    
            for i in range(COLOR_TRIALS):
                # Sorteia aleatoriamente os atributos do estímulo
                color = random.choice(colors)
                shape = random.choice(shapes)
                
                # Registra os metadados da tentativa em um dicionário
                training_trials.append({
                    "color": color,       # cor do estímulo
                    "shape": shape,       # forma do estímulo
                })
    
        curr_shape = training_trials[color_training.thisN]["shape"]
        curr_color = training_trials[color_training.thisN]["color"]
        curr_phase = "color"
    
        resp_corr = my_buttons[curr_color]
    
        if curr_shape == "circle":
            opa_circle, opa_triangle = 1, 0
        elif curr_shape == "triangle":
            opa_circle, opa_triangle = 0, 1
            
        # buttons
        if my_buttons["blue"] == "left":
            training_left_text, training_right_text = "Azul", "Verde"
        else:
            training_left_text, training_right_text = "Verde", "Azul"
    
    if shape_training_check:
        # se estamos em shape trials
        if shape_training.thisN == 0:
            # =========================
            # PARÂMETROS DA TAREFA
            # =========================
            colors = ["blue", "green"]           # possíveis cores
            shapes = ["circle", "triangle"]      # possíveis formas
    
            # =========================
            # GERAR TENTATIVAS
            # =========================
            training_trials = []                 # lista que armazenará os dicionários de cada tentativa
    
            for i in range(SHAPE_TRIALS):
                # Sorteia aleatoriamente os atributos do estímulo
                color = random.choice(colors)
                shape = random.choice(shapes)
                
                # Registra os metadados da tentativa em um dicionário
                training_trials.append({
                    "color": color,       # cor do estímulo
                    "shape": shape,       # forma do estímulo
                })
    
        curr_shape = training_trials[shape_training.thisN]["shape"]
        curr_color = training_trials[shape_training.thisN]["color"]
        curr_phase = "shape"
    
        resp_corr = my_buttons[curr_shape]
    
        if curr_shape == "circle":
            opa_circle, opa_triangle = 1, 0
        elif curr_shape == "triangle":
            opa_circle, opa_triangle = 0, 1
    
        # buttons
        if my_buttons["triangle"] == "left":
            training_left_text, training_right_text = "Triângulo", "Círculo"
        else:
            training_left_text, training_right_text = "Círculo", "Triângulo"
    resp_2.keys = []
    resp_2.rt = []
    _resp_2_allKeys = []
    circle_2.setFillColor(curr_color)
    circle_2.setOpacity(opa_circle)
    triangle_2.setFillColor(curr_color)
    triangle_2.setOpacity(opa_triangle)
    left_msg_2.setText(training_left_text)
    right_msg_2.setText(training_right_text)
    # keep track of which components have finished
    training_trialComponents = [fixation_2, resp_2, circle_2, triangle_2, left_msg_2, right_msg_2, left_button_2, right_button_2]
    for thisComponent in training_trialComponents:
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
    
    # --- Run Routine "training_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_2.started')
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_2.tStartRefresh + 0.350-frameTolerance:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                fixation_2.setAutoDraw(False)
        
        # *resp_2* updates
        waitOnFlip = False
        if resp_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            resp_2.frameNStart = frameN  # exact frame index
            resp_2.tStart = t  # local t and not account for scr refresh
            resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_2.started')
            resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_2.status == STARTED and not waitOnFlip:
            theseKeys = resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp_2_allKeys.extend(theseKeys)
            if len(_resp_2_allKeys):
                resp_2.keys = _resp_2_allKeys[0].name  # just the first key pressed
                resp_2.rt = _resp_2_allKeys[0].rt
                # was this correct?
                if (resp_2.keys == str(resp_corr)) or (resp_2.keys == resp_corr):
                    resp_2.corr = 1
                else:
                    resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *circle_2* updates
        if circle_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            circle_2.frameNStart = frameN  # exact frame index
            circle_2.tStart = t  # local t and not account for scr refresh
            circle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle_2.started')
            circle_2.setAutoDraw(True)
        
        # *triangle_2* updates
        if triangle_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            triangle_2.frameNStart = frameN  # exact frame index
            triangle_2.tStart = t  # local t and not account for scr refresh
            triangle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triangle_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'triangle_2.started')
            triangle_2.setAutoDraw(True)
        
        # *left_msg_2* updates
        if left_msg_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            left_msg_2.frameNStart = frameN  # exact frame index
            left_msg_2.tStart = t  # local t and not account for scr refresh
            left_msg_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_msg_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_msg_2.started')
            left_msg_2.setAutoDraw(True)
        
        # *right_msg_2* updates
        if right_msg_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            right_msg_2.frameNStart = frameN  # exact frame index
            right_msg_2.tStart = t  # local t and not account for scr refresh
            right_msg_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_msg_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_msg_2.started')
            right_msg_2.setAutoDraw(True)
        
        # *left_button_2* updates
        if left_button_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            left_button_2.frameNStart = frameN  # exact frame index
            left_button_2.tStart = t  # local t and not account for scr refresh
            left_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_button_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_button_2.started')
            left_button_2.setAutoDraw(True)
        
        # *right_button_2* updates
        if right_button_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            right_button_2.frameNStart = frameN  # exact frame index
            right_button_2.tStart = t  # local t and not account for scr refresh
            right_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_button_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_button_2.started')
            right_button_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_trial" ---
    for thisComponent in training_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    thisExp.addData('participant_code', participant_code)
    thisExp.addData("condition", "homogeneous")
    thisExp.addData("phase", curr_phase)
    thisExp.addData("block", None)
    thisExp.addData('cue', None)
    thisExp.addData('shape', curr_shape)
    thisExp.addData('color', curr_color)
    thisExp.addData('trial_type', None)
    thisExp.addData('resp_corr', resp_corr)
    thisExp.addData('opa_circle', opa_circle)
    thisExp.addData('opa_triangle', opa_triangle)
    
    # se estamos na última tentativa do treino de cores
    if color_training.thisN == (COLOR_TRIALS - 1):
        shape_training_check = True
        color_training_check = False
    
    
    # check responses
    if resp_2.keys in ['', [], None]:  # No response was made
        resp_2.keys = None
        # was no response the correct answer?!
        if str(resp_corr).lower() == 'none':
           resp_2.corr = 1;  # correct non-response
        else:
           resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for color_training (TrialHandler)
    color_training.addData('resp_2.keys',resp_2.keys)
    color_training.addData('resp_2.corr', resp_2.corr)
    if resp_2.keys != None:  # we had a response
        color_training.addData('resp_2.rt', resp_2.rt)
    # the Routine "training_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed COLOR_TRIALS repeats of 'color_training'


# set up handler to look after randomisation of conditions etc
shape_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='shape_instructions')
thisExp.addLoop(shape_instructions)  # add the loop to the experiment
thisShape_instruction = shape_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisShape_instruction.rgb)
if thisShape_instruction != None:
    for paramName in thisShape_instruction:
        exec('{} = thisShape_instruction[paramName]'.format(paramName))

for thisShape_instruction in shape_instructions:
    currentLoop = shape_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisShape_instruction.rgb)
    if thisShape_instruction != None:
        for paramName in thisShape_instruction:
            exec('{} = thisShape_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    instr_msg.setText(instruction_list[block_instruction][current_instruction])
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
    elif current_instruction == len(instruction_list[block_instruction]):
        if block_instruction == 0:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            color_instructions.finished = True
        elif block_instruction == 1:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            shape_instructions.finished = True
        elif block_instruction == 2:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            color_shape_instructions.finished = True
    
    
    # store data for shape_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'shape_instructions'


# set up handler to look after randomisation of conditions etc
shape_training = data.TrialHandler(nReps=SHAPE_TRIALS, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='shape_training')
thisExp.addLoop(shape_training)  # add the loop to the experiment
thisShape_training = shape_training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisShape_training.rgb)
if thisShape_training != None:
    for paramName in thisShape_training:
        exec('{} = thisShape_training[paramName]'.format(paramName))

for thisShape_training in shape_training:
    currentLoop = shape_training
    # abbreviate parameter names if possible (e.g. rgb = thisShape_training.rgb)
    if thisShape_training != None:
        for paramName in thisShape_training:
            exec('{} = thisShape_training[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "training_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    if color_training_check:
        # se estamos em color trials
        if color_training.thisN == 0:
            # =========================
            # PARÂMETROS DA TAREFA
            # =========================
            colors = ["blue", "green"]           # possíveis cores
            shapes = ["circle", "triangle"]      # possíveis formas
    
            # =========================
            # GERAR TENTATIVAS
            # =========================
            training_trials = []                 # lista que armazenará os dicionários de cada tentativa
    
            for i in range(COLOR_TRIALS):
                # Sorteia aleatoriamente os atributos do estímulo
                color = random.choice(colors)
                shape = random.choice(shapes)
                
                # Registra os metadados da tentativa em um dicionário
                training_trials.append({
                    "color": color,       # cor do estímulo
                    "shape": shape,       # forma do estímulo
                })
    
        curr_shape = training_trials[color_training.thisN]["shape"]
        curr_color = training_trials[color_training.thisN]["color"]
        curr_phase = "color"
    
        resp_corr = my_buttons[curr_color]
    
        if curr_shape == "circle":
            opa_circle, opa_triangle = 1, 0
        elif curr_shape == "triangle":
            opa_circle, opa_triangle = 0, 1
            
        # buttons
        if my_buttons["blue"] == "left":
            training_left_text, training_right_text = "Azul", "Verde"
        else:
            training_left_text, training_right_text = "Verde", "Azul"
    
    if shape_training_check:
        # se estamos em shape trials
        if shape_training.thisN == 0:
            # =========================
            # PARÂMETROS DA TAREFA
            # =========================
            colors = ["blue", "green"]           # possíveis cores
            shapes = ["circle", "triangle"]      # possíveis formas
    
            # =========================
            # GERAR TENTATIVAS
            # =========================
            training_trials = []                 # lista que armazenará os dicionários de cada tentativa
    
            for i in range(SHAPE_TRIALS):
                # Sorteia aleatoriamente os atributos do estímulo
                color = random.choice(colors)
                shape = random.choice(shapes)
                
                # Registra os metadados da tentativa em um dicionário
                training_trials.append({
                    "color": color,       # cor do estímulo
                    "shape": shape,       # forma do estímulo
                })
    
        curr_shape = training_trials[shape_training.thisN]["shape"]
        curr_color = training_trials[shape_training.thisN]["color"]
        curr_phase = "shape"
    
        resp_corr = my_buttons[curr_shape]
    
        if curr_shape == "circle":
            opa_circle, opa_triangle = 1, 0
        elif curr_shape == "triangle":
            opa_circle, opa_triangle = 0, 1
    
        # buttons
        if my_buttons["triangle"] == "left":
            training_left_text, training_right_text = "Triângulo", "Círculo"
        else:
            training_left_text, training_right_text = "Círculo", "Triângulo"
    resp_2.keys = []
    resp_2.rt = []
    _resp_2_allKeys = []
    circle_2.setFillColor(curr_color)
    circle_2.setOpacity(opa_circle)
    triangle_2.setFillColor(curr_color)
    triangle_2.setOpacity(opa_triangle)
    left_msg_2.setText(training_left_text)
    right_msg_2.setText(training_right_text)
    # keep track of which components have finished
    training_trialComponents = [fixation_2, resp_2, circle_2, triangle_2, left_msg_2, right_msg_2, left_button_2, right_button_2]
    for thisComponent in training_trialComponents:
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
    
    # --- Run Routine "training_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_2.started')
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_2.tStartRefresh + 0.350-frameTolerance:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                fixation_2.setAutoDraw(False)
        
        # *resp_2* updates
        waitOnFlip = False
        if resp_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            resp_2.frameNStart = frameN  # exact frame index
            resp_2.tStart = t  # local t and not account for scr refresh
            resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_2.started')
            resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_2.status == STARTED and not waitOnFlip:
            theseKeys = resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp_2_allKeys.extend(theseKeys)
            if len(_resp_2_allKeys):
                resp_2.keys = _resp_2_allKeys[0].name  # just the first key pressed
                resp_2.rt = _resp_2_allKeys[0].rt
                # was this correct?
                if (resp_2.keys == str(resp_corr)) or (resp_2.keys == resp_corr):
                    resp_2.corr = 1
                else:
                    resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *circle_2* updates
        if circle_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            circle_2.frameNStart = frameN  # exact frame index
            circle_2.tStart = t  # local t and not account for scr refresh
            circle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle_2.started')
            circle_2.setAutoDraw(True)
        
        # *triangle_2* updates
        if triangle_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            triangle_2.frameNStart = frameN  # exact frame index
            triangle_2.tStart = t  # local t and not account for scr refresh
            triangle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triangle_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'triangle_2.started')
            triangle_2.setAutoDraw(True)
        
        # *left_msg_2* updates
        if left_msg_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            left_msg_2.frameNStart = frameN  # exact frame index
            left_msg_2.tStart = t  # local t and not account for scr refresh
            left_msg_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_msg_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_msg_2.started')
            left_msg_2.setAutoDraw(True)
        
        # *right_msg_2* updates
        if right_msg_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            right_msg_2.frameNStart = frameN  # exact frame index
            right_msg_2.tStart = t  # local t and not account for scr refresh
            right_msg_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_msg_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_msg_2.started')
            right_msg_2.setAutoDraw(True)
        
        # *left_button_2* updates
        if left_button_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            left_button_2.frameNStart = frameN  # exact frame index
            left_button_2.tStart = t  # local t and not account for scr refresh
            left_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_button_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_button_2.started')
            left_button_2.setAutoDraw(True)
        
        # *right_button_2* updates
        if right_button_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            right_button_2.frameNStart = frameN  # exact frame index
            right_button_2.tStart = t  # local t and not account for scr refresh
            right_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_button_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_button_2.started')
            right_button_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_trial" ---
    for thisComponent in training_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    thisExp.addData('participant_code', participant_code)
    thisExp.addData("condition", "homogeneous")
    thisExp.addData("phase", curr_phase)
    thisExp.addData("block", None)
    thisExp.addData('cue', None)
    thisExp.addData('shape', curr_shape)
    thisExp.addData('color', curr_color)
    thisExp.addData('trial_type', None)
    thisExp.addData('resp_corr', resp_corr)
    thisExp.addData('opa_circle', opa_circle)
    thisExp.addData('opa_triangle', opa_triangle)
    
    # se estamos na última tentativa do treino de cores
    if color_training.thisN == (COLOR_TRIALS - 1):
        shape_training_check = True
        color_training_check = False
    
    
    # check responses
    if resp_2.keys in ['', [], None]:  # No response was made
        resp_2.keys = None
        # was no response the correct answer?!
        if str(resp_corr).lower() == 'none':
           resp_2.corr = 1;  # correct non-response
        else:
           resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for shape_training (TrialHandler)
    shape_training.addData('resp_2.keys',resp_2.keys)
    shape_training.addData('resp_2.corr', resp_2.corr)
    if resp_2.keys != None:  # we had a response
        shape_training.addData('resp_2.rt', resp_2.rt)
    # the Routine "training_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed SHAPE_TRIALS repeats of 'shape_training'


# set up handler to look after randomisation of conditions etc
color_shape_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='color_shape_instructions')
thisExp.addLoop(color_shape_instructions)  # add the loop to the experiment
thisColor_shape_instruction = color_shape_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisColor_shape_instruction.rgb)
if thisColor_shape_instruction != None:
    for paramName in thisColor_shape_instruction:
        exec('{} = thisColor_shape_instruction[paramName]'.format(paramName))

for thisColor_shape_instruction in color_shape_instructions:
    currentLoop = color_shape_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisColor_shape_instruction.rgb)
    if thisColor_shape_instruction != None:
        for paramName in thisColor_shape_instruction:
            exec('{} = thisColor_shape_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    instr_msg.setText(instruction_list[block_instruction][current_instruction])
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
    elif current_instruction == len(instruction_list[block_instruction]):
        if block_instruction == 0:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            color_instructions.finished = True
        elif block_instruction == 1:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            shape_instructions.finished = True
        elif block_instruction == 2:
            block_instruction += 1
            current_instruction = 0 # zera contador de instruções
            color_shape_instructions.finished = True
    
    
    # store data for color_shape_instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'color_shape_instructions'


# set up handler to look after randomisation of conditions etc
css_blocks = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='css_blocks')
thisExp.addLoop(css_blocks)  # add the loop to the experiment
thisCss_block = css_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCss_block.rgb)
if thisCss_block != None:
    for paramName in thisCss_block:
        exec('{} = thisCss_block[paramName]'.format(paramName))

for thisCss_block in css_blocks:
    currentLoop = css_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisCss_block.rgb)
    if thisCss_block != None:
        for paramName in thisCss_block:
            exec('{} = thisCss_block[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "new_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from new_trial_code
    if css_blocks.thisN == 0:
        block_msg = "Clique em [Avançar] para iniciar o PRIMEIRO BLOCO de tentativas."
    
    elif css_blocks.thisN == 1:
        block_msg = "Pausa para descanso.\n\nClique em [Avançar] quando estiver pronto para iniciar o SEGUNDO BLOCO de tentativas."
    
    elif css_blocks.thisN == 2:
        block_msg = "Pausa para descanso.\n\nClique em [Avançar] quando estiver pronto para iniciar o TERCEIRO BLOCO de tentativas."
        
    elif css_blocks.thisN == 3:
        block_msg = "Pausa para descanso.\n\nClique em [Avançar] quando estiver pronto para iniciar o QUARTO BLOCO de tentativas."
    
    elif css_blocks.thisN == 4:
        block_msg = "Pausa para descanso.\n\nClique em [Avançar] quando estiver pronto para iniciar o QUINTO BLOCO de tentativas."
    
    new_trial_prompt.setText(block_msg)
    # setup some python lists for storing info about the new_trial_resp
    new_trial_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    new_trialComponents = [new_trial_prompt, new_trial_next, new_trial_resp]
    for thisComponent in new_trialComponents:
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
    
    # --- Run Routine "new_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *new_trial_prompt* updates
        if new_trial_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_trial_prompt.frameNStart = frameN  # exact frame index
            new_trial_prompt.tStart = t  # local t and not account for scr refresh
            new_trial_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_trial_prompt.started')
            new_trial_prompt.setAutoDraw(True)
        
        # *new_trial_next* updates
        if new_trial_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_trial_next.frameNStart = frameN  # exact frame index
            new_trial_next.tStart = t  # local t and not account for scr refresh
            new_trial_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_trial_next.started')
            new_trial_next.setAutoDraw(True)
        # *new_trial_resp* updates
        if new_trial_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_trial_resp.frameNStart = frameN  # exact frame index
            new_trial_resp.tStart = t  # local t and not account for scr refresh
            new_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('new_trial_resp.started', t)
            new_trial_resp.status = STARTED
            new_trial_resp.mouseClock.reset()
            prevButtonState = new_trial_resp.getPressed()  # if button is down already this ISN'T a new click
        if new_trial_resp.status == STARTED:  # only update if started and not finished!
            buttons = new_trial_resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(new_trial_next)
                        clickableList = new_trial_next
                    except:
                        clickableList = [new_trial_next]
                    for obj in clickableList:
                        if obj.contains(new_trial_resp):
                            gotValidClick = True
                            new_trial_resp.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in new_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "new_trial" ---
    for thisComponent in new_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from new_trial_code
    thisExp.addData('participant_code', participant_code)
    # store data for css_blocks (TrialHandler)
    # the Routine "new_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    css_trials = data.TrialHandler(nReps=TRIALS, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='css_trials')
    thisExp.addLoop(css_trials)  # add the loop to the experiment
    thisCss_trial = css_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCss_trial.rgb)
    if thisCss_trial != None:
        for paramName in thisCss_trial:
            exec('{} = thisCss_trial[paramName]'.format(paramName))
    
    for thisCss_trial in css_trials:
        currentLoop = css_trials
        # abbreviate parameter names if possible (e.g. rgb = thisCss_trial.rgb)
        if thisCss_trial != None:
            for paramName in thisCss_trial:
                exec('{} = thisCss_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if css_trials.thisN == 0:
            # =========================
            # PARÂMETROS DA TAREFA
            # =========================
            cues = ["Cor", "Forma"]              # possíveis pistas
            colors = ["blue", "green"]             # possíveis cores
            shapes = ["circle", "triangle"]      # possíveis formas
        
            # -----------------------------------------
            # Criação da lista de switch vs no-switch
            # -----------------------------------------
            # Primeira tentativa sempre "no-switch"
            switch_trials = ["no-switch"]
        
            # Restante: metade switch, metade no-switch, mas já usamos um no-switch no início
            remaining = ["switch"] * (TRIALS // 2) + ["no-switch"] * (TRIALS // 2 - 1)
            random.shuffle(remaining)
        
            # Junta tudo
            switch_trials.extend(remaining)
        
            # =========================
            # GERAR TENTATIVAS
            # =========================
            trials = []                          # lista que armazenará os dicionários de cada tentativa
        
            for i in range(TRIALS):
                # Sorteia aleatoriamente os atributos do estímulo
                color = random.choice(colors)
                shape = random.choice(shapes)
        
                # Define se a tentativa é "switch" ou "no-switch"
                trial_type = switch_trials[i]
        
                # Se for a primeira tentativa, sorteamos a pista livremente
                if i == 0:
                    cue = random.choice(cues)
                    last_cue = cue  # armazena para comparar na próxima iteração
        
                else:
                    # Caso seja trial de troca, alterna a pista em relação à anterior
                    if trial_type == "switch":
                        cue = "Forma" if last_cue == "Cor" else "Cor"
        
                    # Caso seja no-switch, mantém a mesma pista da anterior
                    else:
                        cue = last_cue
        
                    # Atualiza o "último cue" para próxima rodada
                    last_cue = cue
        
                # Registra os metadados da tentativa em um dicionário
                trials.append({
                    "trial": i + 1,       # número da tentativa (1 a N)
                    "cue": cue,           # pista ("Cor" ou "Forma")
                    "color": color,       # cor do estímulo
                    "shape": shape,       # forma do estímulo
                    "type": trial_type    # tipo de tentativa ("switch" ou "no-switch")
                })
        
        curr_phase = "color-shape"
        curr_cue = trials[css_trials.thisN]["cue"]
        curr_shape = trials[css_trials.thisN]["shape"]
        curr_color = trials[css_trials.thisN]["color"]
        curr_trial = trials[css_trials.thisN]["type"]
        
        # define qual é o gabarito
        if curr_cue == "Cor":
            resp_corr = my_buttons[curr_color]
        elif curr_cue == "Forma":
            resp_corr = my_buttons[curr_shape]
        
        if curr_shape == "circle":
            opa_circle, opa_triangle = 1, 0
        elif curr_shape == "triangle":
            opa_circle, opa_triangle = 0, 1
        
        
        cue_msg.setText(curr_cue)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        circle.setFillColor(curr_color)
        circle.setOpacity(opa_circle)
        triangle.setFillColor(curr_color)
        triangle.setOpacity(opa_triangle)
        left_msg.setText(left_text)
        right_msg.setText(right_text)
        # keep track of which components have finished
        trialComponents = [fixation, cue_msg, resp, circle, triangle, left_msg, right_msg, left_button, right_button]
        for thisComponent in trialComponents:
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
        
        # --- Run Routine "trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.350-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    fixation.setAutoDraw(False)
            
            # *cue_msg* updates
            if cue_msg.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
                # keep track of start time/frame for later
                cue_msg.frameNStart = frameN  # exact frame index
                cue_msg.tStart = t  # local t and not account for scr refresh
                cue_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue_msg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_msg.started')
                cue_msg.setAutoDraw(True)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp.started')
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[0].name  # just the first key pressed
                    resp.rt = _resp_allKeys[0].rt
                    # was this correct?
                    if (resp.keys == str(resp_corr)) or (resp.keys == resp_corr):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *circle* updates
            if circle.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                circle.frameNStart = frameN  # exact frame index
                circle.tStart = t  # local t and not account for scr refresh
                circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle.started')
                circle.setAutoDraw(True)
            
            # *triangle* updates
            if triangle.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                triangle.frameNStart = frameN  # exact frame index
                triangle.tStart = t  # local t and not account for scr refresh
                triangle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(triangle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'triangle.started')
                triangle.setAutoDraw(True)
            
            # *left_msg* updates
            if left_msg.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                left_msg.frameNStart = frameN  # exact frame index
                left_msg.tStart = t  # local t and not account for scr refresh
                left_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_msg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_msg.started')
                left_msg.setAutoDraw(True)
            
            # *right_msg* updates
            if right_msg.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                right_msg.frameNStart = frameN  # exact frame index
                right_msg.tStart = t  # local t and not account for scr refresh
                right_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_msg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_msg.started')
                right_msg.setAutoDraw(True)
            
            # *left_button* updates
            if left_button.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                left_button.frameNStart = frameN  # exact frame index
                left_button.tStart = t  # local t and not account for scr refresh
                left_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_button.started')
                left_button.setAutoDraw(True)
            
            # *right_button* updates
            if right_button.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                right_button.frameNStart = frameN  # exact frame index
                right_button.tStart = t  # local t and not account for scr refresh
                right_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_button.started')
                right_button.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        thisExp.addData('participant_code', participant_code)
        thisExp.addData("condition", "heterogeneous")
        thisExp.addData("phase", curr_phase)
        thisExp.addData("block", css_blocks.thisN + 1)
        
        if curr_cue == "Cor":
            curr_cue_en = "color"
        else:
            curr_cue_en = "shape"
        
        thisExp.addData('cue', curr_cue_en)
        thisExp.addData('shape', curr_shape)
        thisExp.addData('color', curr_color)
        thisExp.addData('trial_type', curr_trial)
        thisExp.addData('resp_corr', resp_corr)
        thisExp.addData('opa_circle', opa_circle)
        thisExp.addData('opa_triangle', opa_triangle)
        
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(resp_corr).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for css_trials (TrialHandler)
        css_trials.addData('resp.keys',resp.keys)
        css_trials.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            css_trials.addData('resp.rt', resp.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed TRIALS repeats of 'css_trials'
    
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'css_blocks'


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

# Run 'End Experiment' code from instr_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())

# Run 'End Experiment' code from instr_code
# código do participante
thisExp.addData("participant_code", participant_code)

# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())


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
