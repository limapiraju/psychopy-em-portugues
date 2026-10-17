#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on October 15, 2026, at 18:43
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
expName = 'counting-span-task'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 084 – Counting Span Task\\counting-span-task_lastrun.py',
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
 
# Cada string corresponde a uma tela de instruções
instruction_list = [
"""
Neste estudo, você verá telas com círculos e quadrados de diferentes cores.

Sua tarefa será contar apenas os CÍRCULOS AZUL-ESCUROS.
""",
"""
Em cada tela, aparecerão vários estímulos distribuídos pela tela.

Ignore os quadrados azul-escuros e os quadrados azul-claros. Conte somente os CÍRCULOS AZUL-ESCUROS.
""",
"""
Conte os CÍRCULOS AZUL-ESCUROS em voz alta e, ao final, repita o número final identificado.

Por exemplo, se houver 3 círculos azul-escuros, conte em voz alta, "Um, dois, três, TRÊS", repetindo o número final.

Em seguida, clique em [Continuar] para avançar para a próxima tela.
""",
"""
Após observar cada tela, avance para a próxima.

Conte os CÍRCULOS AZUL-ESCUROS com atenção, pois você precisará memorizar a quantidade apresentada em cada tela.
""",
"""
Ao final de uma sequência de telas, aparecerá a palavra RECORDAR e um campo para você digitar sua resposta.

Digite, na ordem em que apareceram, as quantidades de CÍRCULOS AZUL-ESCUROS de cada tela, sem espaços ou separadores.
""",
"""
Por exemplo, se você observar 3 CÍRCULOS AZUL-ESCUROS na primeira tela, 5 na segunda, 2 na terceira e 4 na quarta, sua resposta deverá ser:

3524
""",
"""
O número de telas de cada sequência poderá variar.

Concentre-se tanto em contar corretamente os CÍRCULOS AZUL-ESCUROS quanto em memorizar a ordem das contagens.
""",
"""
Tente manter a maior quantidade possível de informações na memória.

Ignore os círculos azul-claros e os quadrados azul-escuros. Seu foco será nos CÍRCULOS AZUL-ESCUROS.
""",
"""
Não digite sua resposta durante a apresentação das telas. Aguarde até que a tela de recordação apareça.
""",
"""
Quando estiver pronto(a), avance para iniciar a tarefa.
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

# --- Initialize components for Routine "sequence_control" ---
# Run 'Begin Experiment' code from sequence_code
# Armazena as contagens de alvos de cada tentativa
target_counts = []

# Número de telas na tentativa atual
n_screens = 0

# Cria 3 repetições de cada comprimento, de 2 a 8 telas
screen_counts = list(range(2, 9)) * 3

# Embaralha a ordem dos 21 trials
random.shuffle(screen_counts)

# Armazena os resultados de cada trial para calcular o desempenho global
all_correct = []
all_proportional = []
all_unordered = []
pre_trial_prompt = visual.TextStim(win=win, name='pre_trial_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
pre_trial_resp = keyboard.Keyboard()

# --- Initialize components for Routine "counting_display" ---
# Run 'Begin Experiment' code from generate_stimuli
import random  # Sorteio das quantidades e posições
import math    # Cálculos geométricos


mouse_continue = event.Mouse(win=win)
x, y = [None, None]
mouse_continue.mouseClock = core.Clock()
continue_button = visual.ImageStim(
    win=win,
    name='continue_button', units='norm', 
    image='images/continue_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "recall" ---
# Run 'Begin Experiment' code from recall_code
from collections import Counter


recall_title = visual.TextStim(win=win, name='recall_title',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.7), height=0.25, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
recall_prompt = visual.TextStim(win=win, name='recall_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.30), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
recall_msg = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.30),units='norm',     letterHeight=0.2,
     size=(1, 0.25), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=[0.0000, 0.0000, 0.0000], borderColor=[1.0000, 1.0000, 1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='recall_msg',
     autoLog=True,
)
recall_finish = event.Mouse(win=win)
x, y = [None, None]
recall_finish.mouseClock = core.Clock()
recall_button = visual.ImageStim(
    win=win,
    name='recall_button', units='norm', 
    image='images/continue_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

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
trials = data.TrialHandler(nReps=len(screen_counts), method='random', 
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
    
    # --- Prepare to start Routine "sequence_control" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sequence_code
    # Retira o próximo comprimento da lista
    n_screens = screen_counts.pop()
    
    # Reinicia a sequência de contagens deste trial
    target_counts = []
    pre_trial_prompt.setText('Pressione [Barra de Espaço] para iniciar a próxima tentativa. ')
    pre_trial_resp.keys = []
    pre_trial_resp.rt = []
    _pre_trial_resp_allKeys = []
    # keep track of which components have finished
    sequence_controlComponents = [pre_trial_prompt, pre_trial_resp]
    for thisComponent in sequence_controlComponents:
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
    
    # --- Run Routine "sequence_control" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_trial_prompt* updates
        if pre_trial_prompt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pre_trial_prompt.frameNStart = frameN  # exact frame index
            pre_trial_prompt.tStart = t  # local t and not account for scr refresh
            pre_trial_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_trial_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_trial_prompt.started')
            pre_trial_prompt.setAutoDraw(True)
        
        # *pre_trial_resp* updates
        waitOnFlip = False
        if pre_trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pre_trial_resp.frameNStart = frameN  # exact frame index
            pre_trial_resp.tStart = t  # local t and not account for scr refresh
            pre_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_trial_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_trial_resp.started')
            pre_trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pre_trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pre_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pre_trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = pre_trial_resp.getKeys(keyList=['space'], waitRelease=False)
            _pre_trial_resp_allKeys.extend(theseKeys)
            if len(_pre_trial_resp_allKeys):
                pre_trial_resp.keys = _pre_trial_resp_allKeys[-1].name  # just the last key pressed
                pre_trial_resp.rt = _pre_trial_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sequence_controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sequence_control" ---
    for thisComponent in sequence_controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "sequence_control" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    screen_loop = data.TrialHandler(nReps=n_screens, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='screen_loop')
    thisExp.addLoop(screen_loop)  # add the loop to the experiment
    thisScreen_loop = screen_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisScreen_loop.rgb)
    if thisScreen_loop != None:
        for paramName in thisScreen_loop:
            exec('{} = thisScreen_loop[paramName]'.format(paramName))
    
    for thisScreen_loop in screen_loop:
        currentLoop = screen_loop
        # abbreviate parameter names if possible (e.g. rgb = thisScreen_loop.rgb)
        if thisScreen_loop != None:
            for paramName in thisScreen_loop:
                exec('{} = thisScreen_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "counting_display" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from generate_stimuli
        # Quantidade de estímulos de cada tipo nesta tela
        n_targets = random.randint(3, 9)       # Círculos azul-escuros
        n_color_dist = random.randint(1, 9)    # Quadrados azul-escuros
        n_shape_dist = random.randint(1, 5)    # Quadrados azul-claros
        
        # Calcula o total de estímulos desta tela
        n_stimuli = n_targets + n_color_dist + n_shape_dist
        
        # Diagnóstico: imprime as quantidades no console
        print(
            f"Alvos: {n_targets}; "
            f"Distratores de cor: {n_color_dist}; "
            f"Distratores de forma: {n_shape_dist}; "
            f"Total: {n_stimuli}"
        )
        
        # Tamanho dos estímulos em unidades norm
        stim_size = 0.10
        
        # Área disponível em unidades height
        # Ajuste a largura disponível à proporção da tela
        aspect_ratio = win.size[0] / win.size[1]
        
        x_min = -aspect_ratio * 0.45
        x_max =  aspect_ratio * 0.45
        
        # Mantém a região inferior livre
        y_min, y_max = -0.20, 0.40
        
        # Lista que armazenará as posições dos estímulos
        positions = []
        
        # Total de estímulos nesta tela
        n_stimuli = n_targets + n_color_dist + n_shape_dist
        
        # Raio de segurança: metade do tamanho mais uma pequena margem
        min_dist = stim_size * math.sqrt(2) + 0.005
        
        # Posiciona cada estímulo
        for i in range(n_stimuli):
        
            for attempt in range(1000):
        
                # Sorteia a posição dentro da área permitida
                x = random.uniform(x_min, x_max)
                y = random.uniform(y_min, y_max)
        
                # Verifica a distância de todos os estímulos anteriores
                valid = all(
                    math.hypot(x - px, y - py) >= min_dist
                    for px, py in positions
                )
        
                if valid:
                    positions.append((x, y))
                    break
        
            else:
                raise RuntimeError(
                    "Não foi possível posicionar todos os estímulos."
                )
                
        # Define as categorias de estímulos
        stim_types = (
            ["target"] * n_targets
            + ["color_dist"] * n_color_dist
            + ["shape_dist"] * n_shape_dist
        )
        
        # Embaralha a ordem para distribuir os tipos aleatoriamente
        random.shuffle(stim_types)
        
        # Lista que guardará os objetos visuais
        stimuli = []
        
        for stim_type, (x, y) in zip(stim_types, positions):
        
            # Círculos azul-escuros: alvos
            if stim_type == "target":
                stim = visual.Circle(
                    win, radius=stim_size / 2,
                    pos=(x, y), fillColor = "darkblue",
                    lineColor = "darkblue", units = "height"
                )
        
            # Quadrados azul-escuros: distratores de cor
            elif stim_type == "color_dist":
                stim = visual.Rect(
                    win, width = stim_size, height = stim_size,
                    pos=(x, y), fillColor = "darkblue",
                    lineColor = "darkblue", units = "height"
                )
        
            # Quadrados azul-claros: distratores de forma
            else:
                stim = visual.Rect(
                    win, width = stim_size, height = stim_size,
                    pos=(x, y), fillColor = "lightblue",
                    lineColor = "lightblue", units = "height"
                )
        
            stimuli.append(stim)
        
        # Registra a quantidade de círculos azul-escuros desta tela
        target_counts.append(n_targets)
        # setup some python lists for storing info about the mouse_continue
        mouse_continue.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        counting_displayComponents = [mouse_continue, continue_button]
        for thisComponent in counting_displayComponents:
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
        
        # --- Run Routine "counting_display" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from generate_stimuli
            # Desenha todos os estímulos em cada quadro
            for stim in stimuli:
                stim.draw()
            # *mouse_continue* updates
            if mouse_continue.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_continue.frameNStart = frameN  # exact frame index
                mouse_continue.tStart = t  # local t and not account for scr refresh
                mouse_continue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_continue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_continue.started', t)
                mouse_continue.status = STARTED
                mouse_continue.mouseClock.reset()
                prevButtonState = mouse_continue.getPressed()  # if button is down already this ISN'T a new click
            if mouse_continue.status == STARTED:  # only update if started and not finished!
                buttons = mouse_continue.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([continue_button,])
                            clickableList = [continue_button,]
                        except:
                            clickableList = [[continue_button,]]
                        for obj in clickableList:
                            if obj.contains(mouse_continue):
                                gotValidClick = True
                                mouse_continue.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *continue_button* updates
            if continue_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_button.frameNStart = frameN  # exact frame index
                continue_button.tStart = t  # local t and not account for scr refresh
                continue_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button.started')
                continue_button.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in counting_displayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "counting_display" ---
        for thisComponent in counting_displayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for screen_loop (TrialHandler)
        # the Routine "counting_display" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed n_screens repeats of 'screen_loop'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from recall_code
    # Converte as contagens em uma sequência sem separadores
    correct_response = "".join(str(n) for n in target_counts)
    
    # Inicializa a resposta do participante
    participant_response = ""
    
    # Tamanhos mínimo e máximo da resposta
    max_length = 9
    recall_title.setText('Recordação')
    recall_prompt.setText('Digite TODOS os números de círculos azuis escuros na ordem apresentada e clique em [Continuar] para enviar sua resposta.')
    recall_msg.reset()
    # setup some python lists for storing info about the recall_finish
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    recallComponents = [recall_title, recall_prompt, recall_msg, recall_finish, recall_button]
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
        # Run 'Each Frame' code from recall_code
        # Remove espaços no início e no fim da resposta
        recall_msg.text = recall_msg.text.strip()
        
        # Limita o comprimento da resposta
        if len(recall_msg.text) > max_length:
            recall_msg.text = recall_msg.text[:max_length]
        
        # *recall_title* updates
        if recall_title.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_title.frameNStart = frameN  # exact frame index
            recall_title.tStart = t  # local t and not account for scr refresh
            recall_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_title, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_title.started')
            recall_title.setAutoDraw(True)
        
        # *recall_prompt* updates
        if recall_prompt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_prompt.frameNStart = frameN  # exact frame index
            recall_prompt.tStart = t  # local t and not account for scr refresh
            recall_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_prompt.started')
            recall_prompt.setAutoDraw(True)
        
        # *recall_msg* updates
        if recall_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_msg.frameNStart = frameN  # exact frame index
            recall_msg.tStart = t  # local t and not account for scr refresh
            recall_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_msg.started')
            recall_msg.setAutoDraw(True)
        # *recall_finish* updates
        if recall_finish.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_finish.frameNStart = frameN  # exact frame index
            recall_finish.tStart = t  # local t and not account for scr refresh
            recall_finish.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_finish, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('recall_finish.started', t)
            recall_finish.status = STARTED
            recall_finish.mouseClock.reset()
            prevButtonState = recall_finish.getPressed()  # if button is down already this ISN'T a new click
        if recall_finish.status == STARTED:  # only update if started and not finished!
            buttons = recall_finish.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # abort routine on response        
        # *recall_button* updates
        if recall_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_button.frameNStart = frameN  # exact frame index
            recall_button.tStart = t  # local t and not account for scr refresh
            recall_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_button.started')
            recall_button.setAutoDraw(True)
        
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
    # Run 'End Routine' code from recall_code
    participant_response = recall_msg.text.strip()
    
    # Nota: o denominador considera o comprimento da maior sequência, penalizando 
    # omissões e dígitos extras. O crédito não proporcional considera quantas vezes
    # cada contagem aparece, sem exigir a posição correta
    
    # Gabarito: sequência de contagens apresentadas
    correct_response = "".join(str(n) for n in target_counts)
    
    if recall_msg.text.strip() == correct_response:
        response_corr = 1
    else:
        response_corr = 0
        
    # Crédito proporcional: dígitos corretos nas mesmas posições
    n_positions = max(len(correct_response), len(participant_response), 1)
    
    n_positional = sum(
        a == b
        for a, b in zip(correct_response, participant_response)
    )
    
    proportional_score = n_positional / n_positions
    
    # Crédito não proporcional: contagens corretas, ignorando a ordem
    overlap = Counter(correct_response) & Counter(participant_response)
    n_unordered = sum(overlap.values())
    
    unordered_score = n_unordered / n_positions
    
    # Guarda os escores desta tentativa para o cálculo global
    all_correct.append(response_corr)
    all_proportional.append(proportional_score)
    all_unordered.append(unordered_score)
    
    # Registra as medidas desta tentativa
    thisExp.addData("memory_load", n_screens)
    thisExp.addData("target_counts", correct_response)
    thisExp.addData("participant_response", participant_response)
    thisExp.addData("response_corr", response_corr)
    thisExp.addData("n_positional", n_positional)
    thisExp.addData("proportional_score", proportional_score)
    thisExp.addData("n_unordered", n_unordered)
    thisExp.addData("unordered_score", unordered_score)
    trials.addData('recall_msg.text',recall_msg.text)
    # store data for trials (TrialHandler)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed len(screen_counts) repeats of 'trials'


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

# Run 'End Experiment' code from recall_code
# Calcula o desempenho global ao final dos 21 trials
global_accuracy = sum(all_correct) / len(all_correct)
global_proportional = sum(all_proportional) / len(all_proportional)
global_unordered = sum(all_unordered) / len(all_unordered)

thisExp.addData("global_accuracy", global_accuracy)
thisExp.addData("global_proportional", global_proportional)
thisExp.addData("global_unordered", global_unordered)

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
