#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on October 02, 2026, at 15:38
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




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'change-detection-task'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 082 – Tarefa de Detecção de Mudanças (Change Detection Task)\\change-detection-task_lastrun.py',
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
import locale

locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')

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
 

instruction_list = [
"""
Neste estudo, você verá matrizes formadas por vários quadrados.

Em cada tentativa, você verá duas matrizes, uma após a outra.
""",

"""
Primeiro, uma matriz aparecerá na tela por alguns instantes.

Observe atentamente os quadrados, pois você deverá memorizar a posição dos elementos apresentados.
""",

"""
Depois de um breve intervalo, uma segunda matriz aparecerá.

Sua tarefa será comparar essa segunda matriz com a primeira e decidir se elas são iguais ou diferentes.
""",

"""
Se as duas matrizes forem exatamente iguais, pressione [ ← ].

Se houver alguma diferença entre elas, pressione [ → ].
""",

"""
Por exemplo:

Se a primeira matriz e a segunda matriz forem exatamente iguais:

        MATRIZ 1  =  MATRIZ 2

pressione [←].
""",

"""
Se uma das células tiver sido modificada entre a primeira e a segunda matriz:

        MATRIZ 1  ≠  MATRIZ 2

pressione [→].
""",

"""
Observe que, quando houver uma diferença, apenas uma célula será modificada entre as duas matrizes.

Portanto, compare cuidadosamente as posições apresentadas e responda assim que identificar se as matrizes são iguais ou diferentes.
""",

"""
Após sua resposta, você receberá um feedback indicando se sua resposta foi correta ou incorreta.

Tente responder da maneira mais rápida e acurada possível.
""",

"""
O tamanho das matrizes e o tempo entre os estímulos poderão variar ao longo das tentativas.

Você realizará várias tentativas e poderá descansar entre elas, se necessário.
""",

"""
Lembre-se:

    • Matrizes iguais → pressione [←]
    • Matrizes diferentes → pressione [→]

Responda com base na comparação entre a primeira e a segunda matriz.
""",

"""
Em seguida, iniciaremos a tarefa.

Quando estiver pronto(a), clique em [Avançar] para começar.
"""
]


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
new_trial_resp = keyboard.Keyboard()
idx_count = visual.TextStim(win=win, name='idx_count',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.90, -0.90), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "pre_trial" ---
pre_trial_text = visual.TextStim(win=win, name='pre_trial_text',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "matrix_1" ---
# Run 'Begin Experiment' code from matrix_1_code
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
# GERAR A ESTRUTURA DAS TENTATIVAS
# ============================================================

# Lista que receberá todas as tentativas do experimento
trials_list = []

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
            
            if condition == "same":
                corr_resp = "left"
            else:
                corr_resp = "right"

            # Guarda as informações desta tentativa.
            trial = {
                'size': size,
                'isi': isi,
                'condition': condition,
                'corr_resp': corr_resp
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
                trials_list.append(trial)

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
        trial for trial in trials_list
        if trial['block'] == block
    ]

    # Embaralha a ordem das 72 tentativas
    random.shuffle(block_trials)

    # Acrescenta as tentativas embaralhadas à lista final
    randomized_trials.extend(block_trials)

# Substituímos a lista original pela lista final aleatorizada.
trials_list = randomized_trials

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
# CRIAR AS MATRIZES 1 E 2 DE CADA TENTATIVA
# ============================================================

for trial in trials_list:

    # O tamanho da matriz é definido pela condição da tentativa
    size = trial['size']

    # Gera a matriz aleatória correspondente.
    matrix1 = create_random_matrix(size)
    trial['matrix1'] = matrix1
    
    # copia a matriz
    matrix2 = [row[:] for row in matrix1]

    # --------------------------------------------------------
    # TENTATIVAS "SAME"
    # --------------------------------------------------------

    if trial['condition'] == 'different':

        # Sorteamos aleatoriamente UMA célula da matriz
        row = random.randrange(trial['size'])
        col = random.randrange(trial['size'])

        # Invertemos o valor dessa célula
        matrix2[row][col] = 1 - matrix2[row][col]

        # Guardamos a posição da célula que foi modificada
        trial['changed_cell'] = col + row * col
        
    else:
        
        trial['changed_cell'] = None

    # Guardamos a segunda matriz na tentativa
    trial['matrix2'] = matrix2
    
# ============================================================
# PARÂMETROS GEOMÉTRICOS
# ============================================================
cell_size = 0.10

# ============================================================
# CRIAR OS RECTs DAS MATRIZES
# ============================================================

squares = {}

for size in matrix_sizes:

    squares[size] = []

    for row in range(size):

        for col in range(size):

            # ------------------------------------------------
            # POSIÇÃO DA CÉLULA
            # ------------------------------------------------

            # O tamanho da matriz depende de "size".
            # Como cell_size é constante, a matriz cresce
            # conforme aumentamos o número de células.
            matrix_size = size * cell_size

            # Coordenada horizontal:
            # centralizamos a matriz em x = 0.
            x = (
                (col + 0.5) * cell_size
                - matrix_size / 2
            )

            # Coordenada vertical:
            # a primeira linha fica no topo da matriz.
            y = (
                matrix_size / 2
                - (row + 0.5) * cell_size
            )

            # ------------------------------------------------
            # CRIAR O RECT
            # ------------------------------------------------

            square = visual.Rect(
                win=win,
                name=f'square_{size}_{row}_{col}',
                units='height',

                # Agora width e height representam a mesma
                # unidade física da tela.
                width=cell_size,
                height=cell_size,

                ori=0.0,
                pos=(x, y),
                anchor='center',

                lineWidth=1.0,
                colorSpace='rgb',
                lineColor='darkgray',
                fillColor='white',

                opacity=None,
                depth=-2.0,
                interpolate=True
            )

            squares[size].append(square)
            
# ============================================================
# FUNÇÃO PARA CONFIGURAR OS QUADRADOS DE UMA MATRIZ
# ============================================================

def set_matrix(matrix, squares):
    """
    Configura as cores dos quadrados para representar uma matriz

    Parâmetros
    ----------
    matrix : lista de listas
        Matriz contendo 0 (branco) e 1 (preto).

    squares : dicionário
        Dicionário contendo os Rects das matrizes 4×4, 6×6 e 8×8.
    """

    # O número de linhas da matriz nos informa seu tamanho.
    #
    # Exemplos:
    #   matriz 4×4 → size = 4
    #   matriz 6×6 → size = 6
    #   matriz 8×8 → size = 8
    size = len(matrix)

    # Recuperamos os Rects correspondentes a esse tamanho
    current_squares = squares[size]

    # Contador que percorre os Rects
    square_index = 0

    # Percorremos a matriz linha por linha
    for row in matrix:

        # Percorremos cada célula da linha
        for value in row:

            # ------------------------------------------------
            # Definir a cor da célula
            # ------------------------------------------------

            if value == 0:
                current_squares[square_index].fillColor = 'white'
            else:
                current_squares[square_index].fillColor = 'black'

            # ------------------------------------------------
            # Próximo quadrado
            # ------------------------------------------------

            square_index += 1
matrix_1_text = visual.TextStim(win=win, name='matrix_1_text',
    text=None,
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=0.0, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI" ---
ISI_text = visual.TextStim(win=win, name='ISI_text',
    text=None,
    font='Arial',
    units='norm', pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=0.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "matrix_2" ---
matrix_2_text = visual.TextStim(win=win, name='matrix_2_text',
    text=None,
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=0.0, 
    languageStyle='LTR',
    depth=-1.0);
matrix_2_resp = keyboard.Keyboard()

# --- Initialize components for Routine "feedback" ---
feedback_msg = visual.TextStim(win=win, name='feedback_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
instructions = data.TrialHandler(nReps=999, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructions')
thisExp.addLoop(instructions)  # add the loop to the experiment
thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
if thisInstruction != None:
    for paramName in thisInstruction:
        exec('{} = thisInstruction[paramName]'.format(paramName))

for thisInstruction in instructions:
    currentLoop = instructions
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            exec('{} = thisInstruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    instr_msg.setText(instruction_list[current_instruction])
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
    elif current_instruction == len(instruction_list):
        current_instruction = 0 # zera contador de instruções
        instructions.finished = True # encerra o loop de teste do OSPAN
    
    # store data for instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=len(trials_list), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "new_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from new_trial_code
    idx = trials.thisN
    
    idx_msg = f"{idx + 1}/{len(trials_list)}"
    new_trial_prompt.setText('Pressione qualquer tecla para iniciar a próxima tentativa. ')
    new_trial_resp.keys = []
    new_trial_resp.rt = []
    _new_trial_resp_allKeys = []
    idx_count.setText(idx_msg)
    # keep track of which components have finished
    new_trialComponents = [new_trial_prompt, new_trial_resp, idx_count]
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
        if new_trial_prompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            new_trial_prompt.frameNStart = frameN  # exact frame index
            new_trial_prompt.tStart = t  # local t and not account for scr refresh
            new_trial_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_trial_prompt.started')
            new_trial_prompt.setAutoDraw(True)
        
        # *new_trial_resp* updates
        waitOnFlip = False
        if new_trial_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            new_trial_resp.frameNStart = frameN  # exact frame index
            new_trial_resp.tStart = t  # local t and not account for scr refresh
            new_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_trial_resp.started')
            new_trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(new_trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(new_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if new_trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = new_trial_resp.getKeys(keyList=None, waitRelease=False)
            _new_trial_resp_allKeys.extend(theseKeys)
            if len(_new_trial_resp_allKeys):
                new_trial_resp.keys = _new_trial_resp_allKeys[-1].name  # just the last key pressed
                new_trial_resp.rt = _new_trial_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *idx_count* updates
        if idx_count.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            idx_count.frameNStart = frameN  # exact frame index
            idx_count.tStart = t  # local t and not account for scr refresh
            idx_count.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(idx_count, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'idx_count.started')
            idx_count.setAutoDraw(True)
        
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
    # the Routine "new_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "pre_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    pre_trial_text.setText('+')
    # keep track of which components have finished
    pre_trialComponents = [pre_trial_text]
    for thisComponent in pre_trialComponents:
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
    
    # --- Run Routine "pre_trial" ---
    while continueRoutine and routineTimer.getTime() < 0.7:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_trial_text* updates
        if pre_trial_text.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            pre_trial_text.frameNStart = frameN  # exact frame index
            pre_trial_text.tStart = t  # local t and not account for scr refresh
            pre_trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_trial_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_trial_text.started')
            pre_trial_text.setAutoDraw(True)
        if pre_trial_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_trial_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                pre_trial_text.tStop = t  # not accounting for scr refresh
                pre_trial_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_trial_text.stopped')
                pre_trial_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pre_trial" ---
    for thisComponent in pre_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.700000)
    
    # --- Prepare to start Routine "matrix_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from matrix_1_code
    # Seleciona os dados correspondentes à repetição atual
    # do loop do Builder.
    current_trial = trials_list[trials.thisN]
    
    # Extrai as informações da tentativa atual.
    current_size = current_trial['size']
    current_isi = current_trial['isi']
    current_condition = current_trial['condition']
    corr_resp = current_trial['corr_resp']
    current_matrix1 = current_trial['matrix1']
    current_matrix2 = current_trial['matrix2']
    changed_cell = current_trial['changed_cell']
    
    # ============================================================
    # CONFIGURAR A PRIMEIRA MATRIZ
    # ============================================================
    
    # A função set_matrix() altera as cores dos Rects para que
    # eles representem a matriz 1 da tentativa atual.
    #
    # IMPORTANTE:
    # set_matrix() NÃO desenha os quadrados.
    # Ela apenas prepara os estímulos.
    set_matrix(current_matrix1, squares)
    
    # keep track of which components have finished
    matrix_1Components = [matrix_1_text]
    for thisComponent in matrix_1Components:
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
    
    # --- Run Routine "matrix_1" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from matrix_1_code
        # ============================================================
        # DESENHAR A PRIMEIRA MATRIZ
        # ============================================================
        
        # Selecionamos os Rects correspondentes ao tamanho da matriz
        # da tentativa atual.
        current_squares = squares[current_size]
        
        # Desenhamos cada quadrado.
        for square in current_squares:
            square.draw()
        
        # *matrix_1_text* updates
        if matrix_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_1_text.frameNStart = frameN  # exact frame index
            matrix_1_text.tStart = t  # local t and not account for scr refresh
            matrix_1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_1_text.started')
            matrix_1_text.setAutoDraw(True)
        if matrix_1_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > matrix_1_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                matrix_1_text.tStop = t  # not accounting for scr refresh
                matrix_1_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'matrix_1_text.stopped')
                matrix_1_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in matrix_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "matrix_1" ---
    for thisComponent in matrix_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISI_text]
    for thisComponent in ISIComponents:
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
    
    # --- Run Routine "ISI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_text* updates
        if ISI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_text.frameNStart = frameN  # exact frame index
            ISI_text.tStart = t  # local t and not account for scr refresh
            ISI_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI_text.started')
            ISI_text.setAutoDraw(True)
        if ISI_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_text.tStartRefresh + current_isi-frameTolerance:
                # keep track of stop time/frame for later
                ISI_text.tStop = t  # not accounting for scr refresh
                ISI_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI_text.stopped')
                ISI_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "matrix_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from matrix_2_code
    # ============================================================
    # CONFIGURAR A SEGUNDA MATRIZ
    # ============================================================
    set_matrix(current_matrix2, squares)
    matrix_2_resp.keys = []
    matrix_2_resp.rt = []
    _matrix_2_resp_allKeys = []
    # keep track of which components have finished
    matrix_2Components = [matrix_2_text, matrix_2_resp]
    for thisComponent in matrix_2Components:
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
    
    # --- Run Routine "matrix_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from matrix_2_code
        # ============================================================
        # DESENHAR A SEGUNDA MATRIZ
        # ============================================================
        # Desenhamos cada quadrado.
        for square in squares[current_size]:
            square.draw()
        
        # *matrix_2_text* updates
        if matrix_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_2_text.frameNStart = frameN  # exact frame index
            matrix_2_text.tStart = t  # local t and not account for scr refresh
            matrix_2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_2_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_2_text.started')
            matrix_2_text.setAutoDraw(True)
        
        # *matrix_2_resp* updates
        waitOnFlip = False
        if matrix_2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_2_resp.frameNStart = frameN  # exact frame index
            matrix_2_resp.tStart = t  # local t and not account for scr refresh
            matrix_2_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_2_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_2_resp.started')
            matrix_2_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(matrix_2_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(matrix_2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if matrix_2_resp.status == STARTED and not waitOnFlip:
            theseKeys = matrix_2_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _matrix_2_resp_allKeys.extend(theseKeys)
            if len(_matrix_2_resp_allKeys):
                matrix_2_resp.keys = _matrix_2_resp_allKeys[0].name  # just the first key pressed
                matrix_2_resp.rt = _matrix_2_resp_allKeys[0].rt
                # was this correct?
                if (matrix_2_resp.keys == str(corr_resp)) or (matrix_2_resp.keys == corr_resp):
                    matrix_2_resp.corr = 1
                else:
                    matrix_2_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in matrix_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "matrix_2" ---
    for thisComponent in matrix_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from matrix_2_code
    thisExp.addData('size', current_size)
    thisExp.addData('isi', current_isi)
    thisExp.addData('condition', current_condition)
    thisExp.addData('corr_resp', corr_resp)
    thisExp.addData('matrix1', current_matrix1)
    thisExp.addData('matrix2', current_matrix2)
    thisExp.addData('changed_cell', changed_cell)
    
    if matrix_2_resp.corr:
        fb_msg = "Correto!"
        fb_color = "darkgreen"
    else:
        fb_msg = "Incorreto!"
        fb_color = "red"
        
    # check responses
    if matrix_2_resp.keys in ['', [], None]:  # No response was made
        matrix_2_resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp).lower() == 'none':
           matrix_2_resp.corr = 1;  # correct non-response
        else:
           matrix_2_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('matrix_2_resp.keys',matrix_2_resp.keys)
    trials.addData('matrix_2_resp.corr', matrix_2_resp.corr)
    if matrix_2_resp.keys != None:  # we had a response
        trials.addData('matrix_2_resp.rt', matrix_2_resp.rt)
    # the Routine "matrix_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedback_msg.setColor(fb_color, colorSpace='rgb')
    feedback_msg.setText(fb_msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_msg]
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_msg* updates
        if feedback_msg.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feedback_msg.frameNStart = frameN  # exact frame index
            feedback_msg.tStart = t  # local t and not account for scr refresh
            feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_msg.started')
            feedback_msg.setAutoDraw(True)
        if feedback_msg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_msg.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                feedback_msg.tStop = t  # not accounting for scr refresh
                feedback_msg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_msg.stopped')
                feedback_msg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
# completed len(trials_list) repeats of 'trials'


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
