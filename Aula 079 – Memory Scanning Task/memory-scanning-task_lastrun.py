#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on December 30, 2025, at 12:11
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
expName = 'memory-scanning-task'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 079 – Sternberg\\memory-scanning-task_lastrun.py',
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
Neste estudo, você verá sequências de dígitos.

Os dígitos aparecerão um de cada vez.
""",
"""
Depois de ver uma sequência completa de dígitos, você verá um dígito de teste (na cor laranja).

Sua tarefa será julgar se o dígito de teste apareceu ou não na sequência anterior.
""",
"""
Por exemplo, suponha que você viu a sequência 1 – 5 – 9. Se o dígito de teste for 5, você deverá responder [←], pois sim, ele apareceu na sequência anterior.

Em contrapartida, se o dígito de teste for 8, você deverá responder [→], pois não, ele não apareceu na sequência anterior. 

Após dar sua resposta, você receberá um feedback indicando se acertou ou errou. Tente responder da maneira mais rápida e acurada possível.
""",
"""
O tamanho de cada sequência irá variar a cada tentativa. 

Além disso, você realizará várias tentativas, e pode descansar entre as tentativas, se julgar necessário.
""",
"""
Lembre-se: sua tarefa será julgar se o dígito de teste, na cor laranja, apareceu na sequência anterior:

    • Se sim, pressione [←]
    • Se não, pressione [→] 
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
# Run 'Begin Experiment' code from new_trial_code
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

# criando tentativas
testing = sternberg_trials()

new_trial_prompt = visual.TextStim(win=win, name='new_trial_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
new_trial_resp = keyboard.Keyboard()

# --- Initialize components for Routine "digit_trial" ---
to_be_remembered = visual.TextStim(win=win, name='to_be_remembered',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.6, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "recall" ---
# Run 'Begin Experiment' code from code_recall
feedback_next_msg = "Pressione [Barra de Espaço] para iniciar a próxima tentativa"
prompt_task = visual.TextStim(win=win, name='prompt_task',
    text='Em breve, você verá um dígito. Você viu ele antes?',
    font='Times New Roman',
    units='norm', pos=(0, 0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prompt_recall = visual.TextStim(win=win, name='prompt_recall',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.6, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()
positive_button = visual.ImageStim(
    win=win,
    name='positive_button', units='norm', 
    image='images/left_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.6), size=(0.25, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
negative_button = visual.ImageStim(
    win=win,
    name='negative_button', units='norm', 
    image='images/right_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.25, -0.6), size=(0.25, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
positive = visual.TextStim(win=win, name='positive',
    text='Sim',
    font='Times New Roman',
    units='norm', pos=(-0.25, -0.87), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
negative = visual.TextStim(win=win, name='negative',
    text='Não',
    font='Times New Roman',
    units='norm', pos=(0.25, -0.87), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "feedback" ---
prompt_task_2 = visual.TextStim(win=win, name='prompt_task_2',
    text='Em breve, você verá um dígito. Você viu ele antes?',
    font='Times New Roman',
    units='norm', pos=(0, 0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prompt_feedback = visual.TextStim(win=win, name='prompt_feedback',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
positive_button_2 = visual.ImageStim(
    win=win,
    name='positive_button_2', units='norm', 
    image='images/left_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.6), size=(0.25, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
negative_button_2 = visual.ImageStim(
    win=win,
    name='negative_button_2', units='norm', 
    image='images/right_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.25, -0.6), size=(0.25, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
positive_2 = visual.TextStim(win=win, name='positive_2',
    text='Sim',
    font='Times New Roman',
    units='norm', pos=(-0.25, -0.87), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
negative_2 = visual.TextStim(win=win, name='negative_2',
    text='Não',
    font='Times New Roman',
    units='norm', pos=(0.25, -0.87), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
feedback_next = visual.TextStim(win=win, name='feedback_next',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.2), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
feedback_next_resp = keyboard.Keyboard()

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


# --- Prepare to start Routine "new_trial" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from new_trial_code
new_trial_msg = f"""
Pressione [Barra de Espaço] para iniciar a primeira tentativa
"""
new_trial_prompt.setText(new_trial_msg)
new_trial_resp.keys = []
new_trial_resp.rt = []
_new_trial_resp_allKeys = []
# keep track of which components have finished
new_trialComponents = [new_trial_prompt, new_trial_resp]
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
    
    # *new_trial_resp* updates
    waitOnFlip = False
    if new_trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        theseKeys = new_trial_resp.getKeys(keyList=['space'], waitRelease=False)
        _new_trial_resp_allKeys.extend(theseKeys)
        if len(_new_trial_resp_allKeys):
            new_trial_resp.keys = _new_trial_resp_allKeys[-1].name  # just the last key pressed
            new_trial_resp.rt = _new_trial_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
thisExp.addData("participant_code", participant_code)
# the Routine "new_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
memory_scanning_task_trials = data.TrialHandler(nReps=len(testing), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='memory_scanning_task_trials')
thisExp.addLoop(memory_scanning_task_trials)  # add the loop to the experiment
thisMemory_scanning_task_trial = memory_scanning_task_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMemory_scanning_task_trial.rgb)
if thisMemory_scanning_task_trial != None:
    for paramName in thisMemory_scanning_task_trial:
        exec('{} = thisMemory_scanning_task_trial[paramName]'.format(paramName))

for thisMemory_scanning_task_trial in memory_scanning_task_trials:
    currentLoop = memory_scanning_task_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMemory_scanning_task_trial.rgb)
    if thisMemory_scanning_task_trial != None:
        for paramName in thisMemory_scanning_task_trial:
            exec('{} = thisMemory_scanning_task_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    memory_scanning_task_digit = data.TrialHandler(nReps=testing[memory_scanning_task_trials.thisN]['load'], method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='memory_scanning_task_digit')
    thisExp.addLoop(memory_scanning_task_digit)  # add the loop to the experiment
    thisMemory_scanning_task_digit = memory_scanning_task_digit.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMemory_scanning_task_digit.rgb)
    if thisMemory_scanning_task_digit != None:
        for paramName in thisMemory_scanning_task_digit:
            exec('{} = thisMemory_scanning_task_digit[paramName]'.format(paramName))
    
    for thisMemory_scanning_task_digit in memory_scanning_task_digit:
        currentLoop = memory_scanning_task_digit
        # abbreviate parameter names if possible (e.g. rgb = thisMemory_scanning_task_digit.rgb)
        if thisMemory_scanning_task_digit != None:
            for paramName in thisMemory_scanning_task_digit:
                exec('{} = thisMemory_scanning_task_digit[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "digit_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from digit_trial_code
        my_digit = testing[memory_scanning_task_trials.thisN]['sequence'][memory_scanning_task_digit.thisN]
        load = testing[memory_scanning_task_trials.thisN]['load']
        trial_type = testing[memory_scanning_task_trials.thisN]['trial_type']
        probe = testing[memory_scanning_task_trials.thisN]['probe']
        sequence = testing[memory_scanning_task_trials.thisN]['sequence']
        position = testing[memory_scanning_task_trials.thisN]['position']
        
        if trial_type == "positive":
            corr_resp = "left"
        elif trial_type == "negative":
            corr_resp = "right"
        
        to_be_remembered.setText(my_digit)
        # keep track of which components have finished
        digit_trialComponents = [to_be_remembered]
        for thisComponent in digit_trialComponents:
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
        
        # --- Run Routine "digit_trial" ---
        while continueRoutine and routineTimer.getTime() < 1.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *to_be_remembered* updates
            if to_be_remembered.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
                if tThisFlipGlobal > to_be_remembered.tStartRefresh + 1.2-frameTolerance:
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
            for thisComponent in digit_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "digit_trial" ---
        for thisComponent in digit_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-1.200000)
    # completed testing[memory_scanning_task_trials.thisN]['load'] repeats of 'memory_scanning_task_digit'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_recall
    event.clearEvents('keyboard')
    
    prompt_recall.setText(probe)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    recallComponents = [prompt_task, prompt_recall, resp, positive_button, negative_button, positive, negative]
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
        
        
        
        # *prompt_task* updates
        if prompt_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_task.frameNStart = frameN  # exact frame index
            prompt_task.tStart = t  # local t and not account for scr refresh
            prompt_task.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_task, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_task.started')
            prompt_task.setAutoDraw(True)
        
        # *prompt_recall* updates
        if prompt_recall.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            prompt_recall.frameNStart = frameN  # exact frame index
            prompt_recall.tStart = t  # local t and not account for scr refresh
            prompt_recall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_recall, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_recall.started')
            prompt_recall.setAutoDraw(True)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
            theseKeys = resp.getKeys(keyList=['left','right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[0].name  # just the first key pressed
                resp.rt = _resp_allKeys[0].rt
                # was this correct?
                if (resp.keys == str(corr_resp)) or (resp.keys == corr_resp):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *positive_button* updates
        if positive_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            positive_button.frameNStart = frameN  # exact frame index
            positive_button.tStart = t  # local t and not account for scr refresh
            positive_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(positive_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'positive_button.started')
            positive_button.setAutoDraw(True)
        
        # *negative_button* updates
        if negative_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            negative_button.frameNStart = frameN  # exact frame index
            negative_button.tStart = t  # local t and not account for scr refresh
            negative_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negative_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'negative_button.started')
            negative_button.setAutoDraw(True)
        
        # *positive* updates
        if positive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            positive.frameNStart = frameN  # exact frame index
            positive.tStart = t  # local t and not account for scr refresh
            positive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(positive, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'positive.started')
            positive.setAutoDraw(True)
        
        # *negative* updates
        if negative.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            negative.frameNStart = frameN  # exact frame index
            negative.tStart = t  # local t and not account for scr refresh
            negative.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negative, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'negative.started')
            negative.setAutoDraw(True)
        
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
    memory_scanning_task_trials.addData('participant_code', participant_code)
    memory_scanning_task_trials.addData('my_digit', my_digit)
    memory_scanning_task_trials.addData('load', load)
    memory_scanning_task_trials.addData('trial_type', trial_type)
    memory_scanning_task_trials.addData('probe', probe)
    memory_scanning_task_trials.addData('sequence', sequence)
    memory_scanning_task_trials.addData('position', position)
    memory_scanning_task_trials.addData('corr_resp', corr_resp)
    
    if resp.corr == 1:
        feedback_msg = "Correto!"
        feedback_color = "green"
    elif resp.corr == 0:
        feedback_msg = "Incorreto!"
        feedback_color = "red"
    
    if memory_scanning_task_trials.thisN == (len(testing) - 1):
        feedback_next_msg = "Pressione [Barra de Espaço] para finalizar a tarefa"
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for memory_scanning_task_trials (TrialHandler)
    memory_scanning_task_trials.addData('resp.keys',resp.keys)
    memory_scanning_task_trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        memory_scanning_task_trials.addData('resp.rt', resp.rt)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    prompt_feedback.setColor(feedback_color, colorSpace='rgb')
    prompt_feedback.setText(feedback_msg)
    feedback_next.setText(feedback_next_msg)
    feedback_next_resp.keys = []
    feedback_next_resp.rt = []
    _feedback_next_resp_allKeys = []
    # keep track of which components have finished
    feedbackComponents = [prompt_task_2, prompt_feedback, positive_button_2, negative_button_2, positive_2, negative_2, feedback_next, feedback_next_resp]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt_task_2* updates
        if prompt_task_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_task_2.frameNStart = frameN  # exact frame index
            prompt_task_2.tStart = t  # local t and not account for scr refresh
            prompt_task_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_task_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_task_2.started')
            prompt_task_2.setAutoDraw(True)
        
        # *prompt_feedback* updates
        if prompt_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prompt_feedback.frameNStart = frameN  # exact frame index
            prompt_feedback.tStart = t  # local t and not account for scr refresh
            prompt_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_feedback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_feedback.started')
            prompt_feedback.setAutoDraw(True)
        
        # *positive_button_2* updates
        if positive_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            positive_button_2.frameNStart = frameN  # exact frame index
            positive_button_2.tStart = t  # local t and not account for scr refresh
            positive_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(positive_button_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'positive_button_2.started')
            positive_button_2.setAutoDraw(True)
        
        # *negative_button_2* updates
        if negative_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            negative_button_2.frameNStart = frameN  # exact frame index
            negative_button_2.tStart = t  # local t and not account for scr refresh
            negative_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negative_button_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'negative_button_2.started')
            negative_button_2.setAutoDraw(True)
        
        # *positive_2* updates
        if positive_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            positive_2.frameNStart = frameN  # exact frame index
            positive_2.tStart = t  # local t and not account for scr refresh
            positive_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(positive_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'positive_2.started')
            positive_2.setAutoDraw(True)
        
        # *negative_2* updates
        if negative_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            negative_2.frameNStart = frameN  # exact frame index
            negative_2.tStart = t  # local t and not account for scr refresh
            negative_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(negative_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'negative_2.started')
            negative_2.setAutoDraw(True)
        
        # *feedback_next* updates
        if feedback_next.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            feedback_next.frameNStart = frameN  # exact frame index
            feedback_next.tStart = t  # local t and not account for scr refresh
            feedback_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_next.started')
            feedback_next.setAutoDraw(True)
        
        # *feedback_next_resp* updates
        waitOnFlip = False
        if feedback_next_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            feedback_next_resp.frameNStart = frameN  # exact frame index
            feedback_next_resp.tStart = t  # local t and not account for scr refresh
            feedback_next_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_next_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_next_resp.started')
            feedback_next_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(feedback_next_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(feedback_next_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if feedback_next_resp.status == STARTED and not waitOnFlip:
            theseKeys = feedback_next_resp.getKeys(keyList=['space'], waitRelease=False)
            _feedback_next_resp_allKeys.extend(theseKeys)
            if len(_feedback_next_resp_allKeys):
                feedback_next_resp.keys = _feedback_next_resp_allKeys[-1].name  # just the last key pressed
                feedback_next_resp.rt = _feedback_next_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed len(testing) repeats of 'memory_scanning_task_trials'


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
