#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on July 19, 2026, at 13:22
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
expName = 'threat-detection-paradigm'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Documentos\\Psychology\\8. YouTube\\psychopy-em-portugues\\Aula 080 – Paradigma de Detecção de Ameaças\\threat-detection-paradigm_lastrun.py',
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
Nesta tarefa, você verá uma grade com 9 imagens (3 × 3), contendo flores e cobras.

Em cada tentativa, haverá apenas UMA IMAGEM diferente das demais.
""",
"""
Antes das imagens aparecerem, será apresentada a palavra "Flor" ou "Cobra".

Essa palavra indica qual imagem você deverá encontrar.
""",
"""
Sua tarefa é clicar, com o mouse, na imagem correspondente à palavra apresentada.

Por exemplo:
    
• Se aparecer "Flor", clique na única flor entre as cobras.
• Se aparecer "Cobra", clique na única cobra entre as flores.
""",

"""
Responda o mais rápido e o mais corretamente possível.

Em seguida, iremos iniciar a tarefa. Caso tenha alguma dúvida, chame o experimentador.

Caso não tenha dúvidas, clique em [Avançar] para iniciar a tarefa.
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
stimuli = {"flowers": ["images/flower_01b.jpg", "images/flower_02s.jpg", "images/flower_03s.jpg",
                       "images/flower_04s.jpg", "images/flower_05s.jpg", "images/flower_06s.jpg",
                       "images/flower_07s.jpg", "images/flower_08s.jpg", "images/flower_09s.jpg",
                       "images/flower_10s.jpg", "images/flower_11s.jpg", "images/flower_12s.jpg",
                       "images/flower_13s.jpg", "images/flower_14s.jpg", "images/flower_15s.jpg",
                       "images/flower_16s.jpg", "images/flower_17s.jpg", "images/flower_18s.jpg",
                       "images/flower_19s.jpg"],
           "snakes": ["images/snake_01b.jpg", "images/snake_02s.jpg", "images/snake_03s.jpg",
                      "images/snake_04s.jpg", "images/snake_05s.jpg", "images/snake_06s.jpg",
                      "images/snake_07s.jpg", "images/snake_08s.jpg", "images/snake_09s.jpg",
                      "images/snake_10s.jpg", "images/snake_11s.jpg", "images/snake_12s.jpg",
                      "images/snake_13s.jpg", "images/snake_14s.jpg", "images/snake_15n.jpg",
                      "images/snake_16n.jpg"]
           }


new_trial_prompt = visual.TextStim(win=win, name='new_trial_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "target_detection_task_trial" ---
# Run 'Begin Experiment' code from trial_code
mapping = {
    "image_1": 0,
    "image_2": 1,
    "image_3": 2,
    "image_4": 3,
    "image_5": 4,
    "image_6": 5,
    "image_7": 6,
    "image_8": 7,
    "image_9": 8,
}
image_1 = visual.ImageStim(
    win=win,
    name='image_1', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.65, 0.65), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.65), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.65, 0.65), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.65, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.65, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image_7 = visual.ImageStim(
    win=win,
    name='image_7', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.65, -0.65), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_8 = visual.ImageStim(
    win=win,
    name='image_8', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.65), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.65, -0.65), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

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
target_detection_task_trials = data.TrialHandler(nReps=20.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='target_detection_task_trials')
thisExp.addLoop(target_detection_task_trials)  # add the loop to the experiment
thisTarget_detection_task_trial = target_detection_task_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTarget_detection_task_trial.rgb)
if thisTarget_detection_task_trial != None:
    for paramName in thisTarget_detection_task_trial:
        exec('{} = thisTarget_detection_task_trial[paramName]'.format(paramName))

for thisTarget_detection_task_trial in target_detection_task_trials:
    currentLoop = target_detection_task_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTarget_detection_task_trial.rgb)
    if thisTarget_detection_task_trial != None:
        for paramName in thisTarget_detection_task_trial:
            exec('{} = thisTarget_detection_task_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "new_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from new_trial_code
    # define se alvo é flor ou cobra
    if random.random() > .5:
        # alvo = flor
        target, lures, target_label = "flowers", "snakes", "Flor"
    else:
        # alvo = cobra
        target, lures, target_label = "snakes", "flowers", "Cobra"
    
    # aleatoriza imagens
    random.shuffle(stimuli[target])
    random.shuffle(stimuli[lures])
    target_image = stimuli[target][0] # define a imagem alvo
    stimulus_list = stimuli[lures][:8]
    stimulus_list.append(stimuli[target][0])
    random.shuffle(stimulus_list) # embaralha a lista de imagens
    
    # cria a lista final de estímulos de uma tentativa
    final_stimulus_list = []
    
    for i, stim in enumerate(stimulus_list):
        final_stimulus_list.append({
            "position": i + 1, # posição da imagem (1 a 9)
            "file": stim,      # nome da imagem (.jpg)
        })
    
    # print(final_stimulus_list)
    new_trial_prompt.setText(target_label)
    fixation.setText('+')
    # keep track of which components have finished
    new_trialComponents = [new_trial_prompt, fixation]
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
    while continueRoutine and routineTimer.getTime() < 3.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *new_trial_prompt* updates
        if new_trial_prompt.status == NOT_STARTED and tThisFlip >= 0.50-frameTolerance:
            # keep track of start time/frame for later
            new_trial_prompt.frameNStart = frameN  # exact frame index
            new_trial_prompt.tStart = t  # local t and not account for scr refresh
            new_trial_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_trial_prompt.started')
            new_trial_prompt.setAutoDraw(True)
        if new_trial_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > new_trial_prompt.tStartRefresh + 2.00-frameTolerance:
                # keep track of stop time/frame for later
                new_trial_prompt.tStop = t  # not accounting for scr refresh
                new_trial_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'new_trial_prompt.stopped')
                new_trial_prompt.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 2.50-frameTolerance:
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
            if tThisFlipGlobal > fixation.tStartRefresh + 1.00-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-3.500000)
    
    # --- Prepare to start Routine "target_detection_task_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trial_code
    
    
    
    image_1.setImage(final_stimulus_list[0]["file"])
    image_2.setImage(final_stimulus_list[1]["file"])
    image_3.setImage(final_stimulus_list[2]["file"])
    image_4.setImage(final_stimulus_list[3]["file"])
    image_5.setImage(final_stimulus_list[4]["file"])
    image_6.setSize((0.6, 0.6))
    image_6.setImage(final_stimulus_list[5]["file"])
    image_7.setImage(final_stimulus_list[6]["file"])
    image_8.setImage(final_stimulus_list[7]["file"])
    image_9.setImage(final_stimulus_list[8]["file"])
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    target_detection_task_trialComponents = [image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9, mouse]
    for thisComponent in target_detection_task_trialComponents:
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
    
    # --- Run Routine "target_detection_task_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_1* updates
        if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_1.frameNStart = frameN  # exact frame index
            image_1.tStart = t  # local t and not account for scr refresh
            image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1.started')
            image_1.setAutoDraw(True)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            image_2.setAutoDraw(True)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3.started')
            image_3.setAutoDraw(True)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4.started')
            image_4.setAutoDraw(True)
        
        # *image_5* updates
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_5.started')
            image_5.setAutoDraw(True)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_6.started')
            image_6.setAutoDraw(True)
        
        # *image_7* updates
        if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_7.frameNStart = frameN  # exact frame index
            image_7.tStart = t  # local t and not account for scr refresh
            image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_7.started')
            image_7.setAutoDraw(True)
        
        # *image_8* updates
        if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_8.frameNStart = frameN  # exact frame index
            image_8.tStart = t  # local t and not account for scr refresh
            image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_8.started')
            image_8.setAutoDraw(True)
        
        # *image_9* updates
        if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_9.started')
            image_9.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9])
                        clickableList = [image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9]
                    except:
                        clickableList = [[image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in target_detection_task_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "target_detection_task_trial" ---
    for thisComponent in target_detection_task_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from trial_code
    thisExp.addData("participant_code", participant_code)
    
    clicked = mouse.clicked_name[-1] # número da imagem clicada
    indice = mapping[clicked]        # índice da imagem clicada
    clicked_image = final_stimulus_list[indice]["file"] # nome da imagem
    correct = int(clicked_image == target_image) # acertou?
    
    # salva nome das iamgens (1 a 9)
    thisExp.addData("image_1", final_stimulus_list[0]["file"])
    thisExp.addData("image_2", final_stimulus_list[1]["file"])
    thisExp.addData("image_3", final_stimulus_list[2]["file"])
    thisExp.addData("image_4", final_stimulus_list[3]["file"])
    thisExp.addData("image_5", final_stimulus_list[4]["file"])
    thisExp.addData("image_6", final_stimulus_list[5]["file"])
    thisExp.addData("image_7", final_stimulus_list[6]["file"])
    thisExp.addData("image_8", final_stimulus_list[7]["file"])
    thisExp.addData("image_9", final_stimulus_list[8]["file"])
    
    thisExp.addData("target", target) 
    thisExp.addData("lures", lures)  
    
    # salva outras variáveis importantes
    thisExp.addData("target_image", target_image)    # alvo
    thisExp.addData("clicked_image", clicked_image)  # resposta
    thisExp.addData("correct", correct)              # acertou?
    thisExp.addData("RT", float(mouse.time[0]))
    
    print(float(mouse.time[0]))
    # store data for target_detection_task_trials (TrialHandler)
    target_detection_task_trials.addData('mouse.x', mouse.x)
    target_detection_task_trials.addData('mouse.y', mouse.y)
    target_detection_task_trials.addData('mouse.leftButton', mouse.leftButton)
    target_detection_task_trials.addData('mouse.midButton', mouse.midButton)
    target_detection_task_trials.addData('mouse.rightButton', mouse.rightButton)
    target_detection_task_trials.addData('mouse.time', mouse.time)
    target_detection_task_trials.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "target_detection_task_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'target_detection_task_trials'


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
