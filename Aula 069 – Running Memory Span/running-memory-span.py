#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on August 23, 2025, at 12:31
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
expName = 'running-memory-span'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 069 – Running Memory Span\\running-memory-span.py',
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
 
instruction_list = [
"""
Neste estudo, você verá sequências de letras na tela. 

Sua tarefa será memorizar e relatar as últimas N letras de cada sequência, na ordem em que elas aparecerem.
""",
"""
Antes de cada sequência, você será informado sobre quantos itens (N) deverá relatar ao final.

Por exemplo: se N = 3 e a sequência for ABCDE, a resposta correta será CDE.
""",
"""
As letras aparecerão uma de cada vez no centro da tela. 

Concentre-se em lembrar apenas as últimas N letras, na ordem em que elas aparecerem.
""",
"""
Em algumas tentativas, o número de letras a lembrar será igual ao número apresentado. 

Em outras, você verá mais letras do que precisará efetivamente se lembrar depois. 

Nos dois casos, relate apenas as últimas N letras vistas.
""",
"""
Depois da sequência, você verá uma grade com 12 letras e botões de resposta.

- Clique nas letras para selecioná-las.
- As letras escolhidas aparecerão em uma barra na parte inferior da tela.
""",
"""
Use os botões para ajudar na resposta:

- [Enviar]: quando terminar de selecionar todas as N letras, na ordem correta.
- [Limpar]: apaga sua resposta e permite começar novamente.
- [Branco]: marca a posição de uma letra esquecida.
""",
"""
Lembre-se: a ordem das letras é muito importante. 

Se você se esquecer de uma letra, use [Branco] para marcar a posição da letra esquecida com um traço (–).

Por exemplo, se N = 3 e a sequência for ABCDE, mas você esqueceu a penúltima letra, responda C–E. Você ganhará 2 pontos, pois C e E estão corretos em suas respectivas posições.
""",
"""
Por outro lado, se N = 3 e a sequência for ABCDE, mas você responder CE, você ganhará apenas um ponto.

Isso acontecerá porque apenas a letra E está na posição serial correta. A letra C não foi a penúltima vista, mas, sim, a antepenúltima.
""",
"""
Em seguida, daremos início à tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
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
    text='Na próxima sequência, você deverá recordar as   últimas letras.\n\nClique em [Avançar] para iniciar a próxima tentativa',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
new_trial_prompt_letters = visual.TextStim(win=win, name='new_trial_prompt_letters',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.44, 0.12), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='darkblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
new_trial_next = visual.ImageStim(
    win=win,
    name='new_trial_next', units='norm', 
    image='images/next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
new_trial_resp = event.Mouse(win=win)
x, y = [None, None]
new_trial_resp.mouseClock = core.Clock()

# --- Initialize components for Routine "letter" ---
# Run 'Begin Experiment' code from letters_code
fixed_letters = list("FHJKLNPQRSTY")
letters = list("FHJKLNPQRSTY")

letter_list = list()


to_be_remembered = visual.TextStim(win=win, name='to_be_remembered',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.5, wrapWidth=1.8, ori=0.0, 
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


response_recall = visual.TextStim(win=win, name='response_recall',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.6), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='darkblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prompt_recall = visual.TextStim(win=win, name='prompt_recall',
    text='Selecione as últimas     letras na mesma ordem em que foram apresentadas.\nUse o botão [Branco] para indicar a posição das letras que esqueceu.',
    font='Times New Roman',
    units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prompt_recall_letter = visual.TextStim(win=win, name='prompt_recall_letter',
    text='',
    font='Times New Roman',
    units='norm', pos=(-0.33, 0.9), height=0.09, wrapWidth=1.8, ori=0.0, 
    color='darkblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
F = visual.ImageStim(
    win=win,
    name='F', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
H = visual.ImageStim(
    win=win,
    name='H', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
J = visual.ImageStim(
    win=win,
    name='J', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.55), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
K = visual.ImageStim(
    win=win,
    name='K', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
L = visual.ImageStim(
    win=win,
    name='L', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
N = visual.ImageStim(
    win=win,
    name='N', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.25), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P = visual.ImageStim(
    win=win,
    name='P', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
Q = visual.ImageStim(
    win=win,
    name='Q', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
R = visual.ImageStim(
    win=win,
    name='R', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.05), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
S = visual.ImageStim(
    win=win,
    name='S', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
T = visual.ImageStim(
    win=win,
    name='T', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
Y = visual.ImageStim(
    win=win,
    name='Y', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.35), size=(0.18, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
clear_ = visual.ImageStim(
    win=win,
    name='clear_', units='norm', 
    image='images/clear_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
blank = visual.ImageStim(
    win=win,
    name='blank', units='norm', 
    image='images/blank_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
send = visual.ImageStim(
    win=win,
    name='send', units='norm', 
    image='images/send_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
recall_response = event.Mouse(win=win)
x, y = [None, None]
recall_response.mouseClock = core.Clock()

# --- Initialize components for Routine "recall_feedback" ---
recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
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
running_memory_span_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('span.xlsx'),
    seed=None, name='running_memory_span_trials')
thisExp.addLoop(running_memory_span_trials)  # add the loop to the experiment
thisRunning_memory_span_trial = running_memory_span_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRunning_memory_span_trial.rgb)
if thisRunning_memory_span_trial != None:
    for paramName in thisRunning_memory_span_trial:
        exec('{} = thisRunning_memory_span_trial[paramName]'.format(paramName))

for thisRunning_memory_span_trial in running_memory_span_trials:
    currentLoop = running_memory_span_trials
    # abbreviate parameter names if possible (e.g. rgb = thisRunning_memory_span_trial.rgb)
    if thisRunning_memory_span_trial != None:
        for paramName in thisRunning_memory_span_trial:
            exec('{} = thisRunning_memory_span_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    distractor_length = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('distractor.xlsx'),
        seed=None, name='distractor_length')
    thisExp.addLoop(distractor_length)  # add the loop to the experiment
    thisDistractor_length = distractor_length.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDistractor_length.rgb)
    if thisDistractor_length != None:
        for paramName in thisDistractor_length:
            exec('{} = thisDistractor_length[paramName]'.format(paramName))
    
    for thisDistractor_length in distractor_length:
        currentLoop = distractor_length
        # abbreviate parameter names if possible (e.g. rgb = thisDistractor_length.rgb)
        if thisDistractor_length != None:
            for paramName in thisDistractor_length:
                exec('{} = thisDistractor_length[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "new_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from new_trial_code
        # m = current_distractor; n = current_span
        current_length = current_span + current_distractor
        new_trial_prompt_letters.setText(current_span)
        # setup some python lists for storing info about the new_trial_resp
        new_trial_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        new_trialComponents = [new_trial_prompt, new_trial_prompt_letters, new_trial_next, new_trial_resp]
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
            
            # *new_trial_prompt_letters* updates
            if new_trial_prompt_letters.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                new_trial_prompt_letters.frameNStart = frameN  # exact frame index
                new_trial_prompt_letters.tStart = t  # local t and not account for scr refresh
                new_trial_prompt_letters.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(new_trial_prompt_letters, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'new_trial_prompt_letters.started')
                new_trial_prompt_letters.setAutoDraw(True)
            
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
        thisExp.addData('current_length', current_length)
        thisExp.addData('current_span', current_span)
        thisExp.addData('current_distractor', current_distractor)
        # store data for distractor_length (TrialHandler)
        # the Routine "new_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        running_memory_span_trial = data.TrialHandler(nReps=current_length, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='running_memory_span_trial')
        thisExp.addLoop(running_memory_span_trial)  # add the loop to the experiment
        thisRunning_memory_span_trial = running_memory_span_trial.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRunning_memory_span_trial.rgb)
        if thisRunning_memory_span_trial != None:
            for paramName in thisRunning_memory_span_trial:
                exec('{} = thisRunning_memory_span_trial[paramName]'.format(paramName))
        
        for thisRunning_memory_span_trial in running_memory_span_trial:
            currentLoop = running_memory_span_trial
            # abbreviate parameter names if possible (e.g. rgb = thisRunning_memory_span_trial.rgb)
            if thisRunning_memory_span_trial != None:
                for paramName in thisRunning_memory_span_trial:
                    exec('{} = thisRunning_memory_span_trial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "letter" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from letters_code
            # tenta atribuir o valor da repetição do loop atual à variável index
            # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
            try:
                index = running_memory_span_trial.thisN
            except:
                pass
            
            # tenta embaralhar as letras sempre que estivermos em uma nova tentativa
            try:
                # se é a primeira execução do loop...
                if running_memory_span_trial.thisN == 0:
                    # embaralha letras usada na tarefa de armazenamento
                    np.random.shuffle(letters) 
                    # seleciona a sequência que será mostrada na rodada
                    current_sequence = "".join(letters[:current_length])
                    # e seleciona as n últimas letras que serão o alvo da tentativa
                    correct_response = current_sequence[-current_span:] 
                   
            except:
                pass
            
            # cria uma lista de imagens (que está na subpasta "images")
            for letter in fixed_letters:
                letter_list.append(f"images/{letter}_gray.jpg")
            
            
            to_be_remembered.setText(current_sequence[index])
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
            # Run 'End Routine' code from letters_code
            thisExp.addData('current_length', current_length)
            thisExp.addData('current_span', current_span)
            thisExp.addData('current_distractor', current_distractor)
            # using non-slip timing so subtract the expected duration of this Routine
            routineTimer.addTime(-0.800000)
            thisExp.nextEntry()
            
        # completed current_length repeats of 'running_memory_span_trial'
        
        
        # --- Prepare to start Routine "recall" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_recall
        clicked_things = []
        clickables = [F, H, J, K, L, N, P, Q, R, S, T, Y, send, clear_, blank]
        allowed_send = False
        allowed_blank = True
        
        my_response = "Minha resposta: "
        prompt_recall_letter.setText(current_span)
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
        recallComponents = [response_recall, prompt_recall, prompt_recall_letter, F, H, J, K, L, N, P, Q, R, S, T, Y, clear_, blank, send, recall_response]
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
            
            # *prompt_recall_letter* updates
            if prompt_recall_letter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_recall_letter.frameNStart = frameN  # exact frame index
                prompt_recall_letter.tStart = t  # local t and not account for scr refresh
                prompt_recall_letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_recall_letter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_recall_letter.started')
                prompt_recall_letter.setAutoDraw(True)
            
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
        
        # créditos completo parcial e edit distance, somatório da sessão (máx. 99)
        try:
            if running_memory_span_trials.thisN >= 0:
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
         
        # salva respostas
        thisExp.addData('current_length', current_length)
        thisExp.addData('current_span', current_span)
        thisExp.addData('current_distractor', current_distractor)
        thisExp.addData("participant_response", participant_response)
        thisExp.addData("full_credit_score", full_credit_score)
        thisExp.addData("partial_credit_score", partial_credit_score)
        thisExp.addData("edit_distance_score", edit_distance_score)
        
        print(f"Sequência: {current_sequence}; gabarito: {correct_response}; resposta: {participant_response}")
        # store data for distractor_length (TrialHandler)
        distractor_length.addData('recall_response.x', recall_response.x)
        distractor_length.addData('recall_response.y', recall_response.y)
        distractor_length.addData('recall_response.leftButton', recall_response.leftButton)
        distractor_length.addData('recall_response.midButton', recall_response.midButton)
        distractor_length.addData('recall_response.rightButton', recall_response.rightButton)
        distractor_length.addData('recall_response.time', recall_response.time)
        distractor_length.addData('recall_response.clicked_name', recall_response.clicked_name)
        # the Routine "recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "recall_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        recall_feedback_prompt.setText(recall_feedback_msg)
        # keep track of which components have finished
        recall_feedbackComponents = [recall_feedback_prompt]
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
        
    # completed 1.0 repeats of 'distractor_length'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'running_memory_span_trials'


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
