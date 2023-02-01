#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on janeiro 22, 2023, at 10:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from instr_code




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'karpicke_and_roediger'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 044\\aula 044.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[900, 600], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
# define condição experimental
study_drop = randchoice([0, 1]) # 1 = drop study
test_drop = randchoice([0, 1]) # 1 = drop test
total_items = 10

# índices de instruções
current_instruction = 0

instruction_text_list = ["instrucao_11.jpg", "instrucao_12.jpg", "instrucao_13.jpg", "instrucao_14.jpg", "instrucao_15.jpg"]
instruction_img_list = ["imagem_11.jpg", "imagem_12.jpg", "imagem_13.jpg", "imagem_14.jpg", "imagem_15.jpg"]

instruction_text = visual.ImageStim(
    win=win,
    name='instruction_text', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0.4), size=(2, 1.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instruction_image = visual.ImageStim(
    win=win,
    name='instruction_image', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.35, -.6), size=(.75, .65),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
back_button = visual.ButtonStim(win, 
    text='<<< Anterior', font='Times New Roman',
    pos=(0.3, -.8),units='norm',
    letterHeight=0.085,
    size=(.4, .2), borderWidth=1.0,
    fillColor=[-1.0000, -1.0000, 1.0000], borderColor=[1.0000, 1.0000, 1.0000],
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='back_button'
)
back_button.buttonClock = core.Clock()
next_button = visual.ButtonStim(win, 
    text='Próximo >>>', font='Times New Roman',
    pos=(.75, -.8),units='norm',
    letterHeight=0.085,
    size=(.4, .2), borderWidth=1.0,
    fillColor=[-1.0000, -1.0000, 1.0000], borderColor=[1.0000, 1.0000, 1.0000],
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='next_button'
)
next_button.buttonClock = core.Clock()

# --- Initialize components for Routine "study" ---
# Run 'Begin Experiment' code from code_study
# mede comprimento do arquivo do atual loop de ciclos
arquivo = open("cycle_1.csv", "r").readlines()
numero_de_itens = len(arquivo[1:]) # conta número de pares, ignora cabeçalho

cue_study = visual.TextStim(win=win, name='cue_study',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
target_study = visual.TextStim(win=win, name='target_study',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.2), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "distractor" ---
# Run 'Begin Experiment' code from math_code
# contador de número de tentativas na tarefa distratora
my_count = 0

# contador de qual tarefa distratora estamos
distractor_index = 0


math_problem = visual.TextStim(win=win, name='math_problem',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.15), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
math_resp = visual.TextStim(win=win, name='math_resp',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.15), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
math_line = visual.Rect(
    win=win, name='math_line',units='norm', 
    width=(0.3, 0.01)[0], height=(0.3, 0.01)[1],
    ori=0, pos=(0, -0.25), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-3.0, interpolate=True)
debug1 = visual.TextStim(win=win, name='debug1',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.8), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
math_prompt = visual.TextStim(win=win, name='math_prompt',
    text='Digite sua resposta e tecle [ENTER].',
    font='Times New Roman',
    units='norm', pos=(0, 0.70), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "prompt" ---
prompt_msg = visual.TextStim(win=win, name='prompt_msg',
    text='Pausa. \n\nRespire. Tome uma água.\nE pressione [BARRA DE ESPAÇO] para prosseguir.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.15, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prompt_resp = keyboard.Keyboard()

# --- Initialize components for Routine "test" ---
# Run 'Begin Experiment' code from file_manager
import random, shutil, os
from os.path import exists

my_directory = f"{expInfo['participant']}"
if not exists(my_directory):
    os.mkdir(my_directory)
    print(os.mkdir)

# Source path
study_file = test_file = "cycle_1.csv"
 
# Destination path
destination = f"{expInfo['participant']}/{study_file}"
 
# Copy the content of
# source to destination
dest = shutil.copyfile(study_file, destination)
 


cue_test = visual.TextStim(win=win, name='cue_test',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
target_test = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.2),units='norm',     letterHeight=0.2,
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
     name='target_test',
     autoLog=True,
)

# --- Initialize components for Routine "thanks" ---
thanks_msg = visual.TextStim(win=win, name='thanks_msg',
    text='Fim da tarefa!\n\nRetorne daqui a 7 dias para a segunda sessão! ☻\n\nPressione [BARRA DE ESPAÇO] para fechar a janela.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
thanks_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=9999.0, method='sequential', 
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
    # Run 'Begin Routine' code from instr_code
    button_pressed = ""
    instruction_text.setImage(instruction_text_list[current_instruction])
    instruction_image.setImage(instruction_img_list[current_instruction])
    # keep track of which components have finished
    instructionComponents = [instruction_text, instruction_image, back_button, next_button]
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
        
        # *instruction_text* updates
        if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_text.frameNStart = frameN  # exact frame index
            instruction_text.tStart = t  # local t and not account for scr refresh
            instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_text.started')
            instruction_text.setAutoDraw(True)
        
        # *instruction_image* updates
        if instruction_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_image.frameNStart = frameN  # exact frame index
            instruction_image.tStart = t  # local t and not account for scr refresh
            instruction_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_image.started')
            instruction_image.setAutoDraw(True)
        
        # *back_button* updates
        if back_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            back_button.frameNStart = frameN  # exact frame index
            back_button.tStart = t  # local t and not account for scr refresh
            back_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'back_button.started')
            back_button.setAutoDraw(True)
        if back_button.status == STARTED:
            # check whether back_button has been pressed
            if back_button.isClicked:
                if not back_button.wasClicked:
                    back_button.timesOn.append(back_button.buttonClock.getTime()) # store time of first click
                    back_button.timesOff.append(back_button.buttonClock.getTime()) # store time clicked until
                else:
                    back_button.timesOff[-1] = back_button.buttonClock.getTime() # update time clicked until
                if not back_button.wasClicked:
                    continueRoutine = False  # end routine when back_button is clicked
                    current_instruction -= 1
                back_button.wasClicked = True  # if back_button is still clicked next frame, it is not a new click
            else:
                back_button.wasClicked = False  # if back_button is clicked next frame, it is a new click
        else:
            back_button.wasClicked = False  # if back_button is clicked next frame, it is a new click
        
        # *next_button* updates
        if next_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            next_button.frameNStart = frameN  # exact frame index
            next_button.tStart = t  # local t and not account for scr refresh
            next_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next_button.started')
            next_button.setAutoDraw(True)
        if next_button.status == STARTED:
            # check whether next_button has been pressed
            if next_button.isClicked:
                if not next_button.wasClicked:
                    next_button.timesOn.append(next_button.buttonClock.getTime()) # store time of first click
                    next_button.timesOff.append(next_button.buttonClock.getTime()) # store time clicked until
                else:
                    next_button.timesOff[-1] = next_button.buttonClock.getTime() # update time clicked until
                if not next_button.wasClicked:
                    continueRoutine = False  # end routine when next_button is clicked
                    current_instruction += 1
                next_button.wasClicked = True  # if next_button is still clicked next frame, it is not a new click
            else:
                next_button.wasClicked = False  # if next_button is clicked next frame, it is a new click
        else:
            next_button.wasClicked = False  # if next_button is clicked next frame, it is a new click
        
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
    # Se a instrução atual for -1
    if current_instruction == -1:
        # Resete o valor para ser 0
        current_instruction = 0
    # Se a instrução atual é igual ao comprimento da lista de instruções
    elif current_instruction == len(instruction_text_list):
        current_instruction = 0 # zera contador de instruções
        instructions.finished = True # e encerra loop de estudo
    instructions.addData('back_button.numClicks', back_button.numClicks)
    if back_button.numClicks:
       instructions.addData('back_button.timesOn', back_button.timesOn)
       instructions.addData('back_button.timesOff', back_button.timesOff)
    else:
       instructions.addData('back_button.timesOn', "")
       instructions.addData('back_button.timesOff', "")
    instructions.addData('next_button.numClicks', next_button.numClicks)
    if next_button.numClicks:
       instructions.addData('next_button.timesOn', next_button.timesOn)
       instructions.addData('next_button.timesOff', next_button.timesOff)
    else:
       instructions.addData('next_button.timesOn', "")
       instructions.addData('next_button.timesOff', "")
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 9999.0 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
cycle = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='cycle')
thisExp.addLoop(cycle)  # add the loop to the experiment
thisCycle = cycle.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCycle.rgb)
if thisCycle != None:
    for paramName in thisCycle:
        exec('{} = thisCycle[paramName]'.format(paramName))

for thisCycle in cycle:
    currentLoop = cycle
    # abbreviate parameter names if possible (e.g. rgb = thisCycle.rgb)
    if thisCycle != None:
        for paramName in thisCycle:
            exec('{} = thisCycle[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    study_period = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(study_file),
        seed=None, name='study_period')
    thisExp.addLoop(study_period)  # add the loop to the experiment
    thisStudy_period = study_period.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStudy_period.rgb)
    if thisStudy_period != None:
        for paramName in thisStudy_period:
            exec('{} = thisStudy_period[paramName]'.format(paramName))
    
    for thisStudy_period in study_period:
        currentLoop = study_period
        # abbreviate parameter names if possible (e.g. rgb = thisStudy_period.rgb)
        if thisStudy_period != None:
            for paramName in thisStudy_period:
                exec('{} = thisStudy_period[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "study" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_study
        # encerra loop se for condição Sn e não houver novos itens na planilha
        if (study_drop == True) and numero_de_itens == 0:
            continueRoutine = False
            study_period.finished = True
        cue_study.setText(English)
        target_study.setText(Portuguese)
        # keep track of which components have finished
        studyComponents = [cue_study, target_study]
        for thisComponent in studyComponents:
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
        
        # --- Run Routine "study" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cue_study* updates
            if cue_study.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cue_study.frameNStart = frameN  # exact frame index
                cue_study.tStart = t  # local t and not account for scr refresh
                cue_study.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue_study, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_study.started')
                cue_study.setAutoDraw(True)
            if cue_study.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue_study.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    cue_study.tStop = t  # not accounting for scr refresh
                    cue_study.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cue_study.stopped')
                    cue_study.setAutoDraw(False)
            
            # *target_study* updates
            if target_study.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target_study.frameNStart = frameN  # exact frame index
                target_study.tStart = t  # local t and not account for scr refresh
                target_study.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_study, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_study.started')
                target_study.setAutoDraw(True)
            if target_study.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target_study.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    target_study.tStop = t  # not accounting for scr refresh
                    target_study.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_study.stopped')
                    target_study.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in studyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "study" ---
        for thisComponent in studyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'study_period'
    
    
    # set up handler to look after randomisation of conditions etc
    distractor_period = data.TrialHandler(nReps=999.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='distractor_period')
    thisExp.addLoop(distractor_period)  # add the loop to the experiment
    thisDistractor_period = distractor_period.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDistractor_period.rgb)
    if thisDistractor_period != None:
        for paramName in thisDistractor_period:
            exec('{} = thisDistractor_period[paramName]'.format(paramName))
    
    for thisDistractor_period in distractor_period:
        currentLoop = distractor_period
        # abbreviate parameter names if possible (e.g. rgb = thisDistractor_period.rgb)
        if thisDistractor_period != None:
            for paramName in thisDistractor_period:
                exec('{} = thisDistractor_period[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "distractor" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from math_code
        # se estamos na primeira tentativa da tarefa distratora...
        if my_count == 0:
            my_clock = core.Clock()
        
        # variáveis do problema matemático
        factor1, factor2 = random.randint(2, 10), random.randint(2, 20) 
        if random.random() > 0.5:
            factor1, factor2 = factor2, factor1
        product = factor1 * factor2
        problem = f"Quanto é {factor1} × {factor2}?"
        
        # variáveis para digitação da resposta
        distractor_msg = ""
        allowed_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'num_0', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9']
        max_len = 3
        
        # monitorando teclas pressionadas e tempo
        distractor_clock = core.Clock() # relógio da rotina que monitora tempo
        pressed_keys = list() # lista de teclas pressionadas
        pressed_keys_time = list() # lista de tempo de pressão de cada tecla
        math_problem.setText(problem)
        # keep track of which components have finished
        distractorComponents = [math_problem, math_resp, math_line, debug1, math_prompt]
        for thisComponent in distractorComponents:
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
        
        # --- Run Routine "distractor" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from math_code
            keys = event.getKeys() # atribui as entradas do participante no teclado à variável keys
            
            if len(keys): # se keys > 0; i.e., se houver algum valor em keys
                pressed_keys_time.append(clock.getTime())
                pressed_keys.append(keys[0])
                if 'backspace' in keys:
                    # se a tecla pressionada é [← BACKSPACE] (apagar)
                    distractor_msg = distractor_msg[:-1] # exclua o último caractere
                elif 'return' in keys:
                    if len(distractor_msg) > 0:
                        # se a tecla pressionada é [ENTER] é há pelo menos um caractere em msg
                        continueRoutine = False # encerre a rotina atual
                elif keys[0] in allowed_keys and len(distractor_msg) < max_len:
                    # se a tecla pressionada estiver na lista buttons...
                    # e o tamanho atual da msg for menor que o comprimento máximo que ela pode assumir
                    distractor_msg += keys[0][-1] # concatene o último caractere da tecla pressionada com o valor atual de msg
             
            
            # monitora valor do relógio para que tarefa dure 60 s
            if my_clock.getTime() >= 5:
                my_count = 0
                continueRoutine = False
                distractor_period.finished = True # encerra loop
                
            
            # *math_problem* updates
            if math_problem.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                math_problem.frameNStart = frameN  # exact frame index
                math_problem.tStart = t  # local t and not account for scr refresh
                math_problem.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_problem, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_problem.started')
                math_problem.setAutoDraw(True)
            
            # *math_resp* updates
            if math_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                math_resp.frameNStart = frameN  # exact frame index
                math_resp.tStart = t  # local t and not account for scr refresh
                math_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_resp.started')
                math_resp.setAutoDraw(True)
            if math_resp.status == STARTED:  # only update if drawing
                math_resp.setText(distractor_msg, log=False)
            
            # *math_line* updates
            if math_line.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                math_line.frameNStart = frameN  # exact frame index
                math_line.tStart = t  # local t and not account for scr refresh
                math_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(math_line, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'math_line.started')
                math_line.setAutoDraw(True)
            
            # *debug1* updates
            if debug1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                debug1.frameNStart = frameN  # exact frame index
                debug1.tStart = t  # local t and not account for scr refresh
                debug1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debug1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debug1.started')
                debug1.setAutoDraw(True)
            if debug1.status == STARTED:  # only update if drawing
                debug1.setText(my_clock.getTime(), log=False)
            
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
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in distractorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "distractor" ---
        for thisComponent in distractorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from math_code
        my_count += 1 # incrementa contador de tentativas
        
        # variáveis do problema matemático
        thisExp.addData("factor1", factor1)
        thisExp.addData("factor2", factor2)
        thisExp.addData("product", product)
        
        # resposta do participante
        thisExp.addData("distractor_response", distractor_msg)
        
        # salva variáveis relacionadas ao tempo
        thisExp.addData("teclas_pressionadas", pressed_keys)
        thisExp.addData("teclas_pressionadas_tempo", pressed_keys_time)
        
        # avalia se resposta foi um acerto (corr = 1) ou um erro (corr = 0)
        if (distractor_msg == str(product)):
            distractor_corr = 1
        else:
            distractor_corr = 0
        
        # salva acerto ou erro no arquivo de saídas
        thisExp.addData("distractor_resp_corr", distractor_corr)
        
        
        # the Routine "distractor" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 999.0 repeats of 'distractor_period'
    
    
    # --- Prepare to start Routine "prompt" ---
    continueRoutine = True
    # update component parameters for each repeat
    prompt_resp.keys = []
    prompt_resp.rt = []
    _prompt_resp_allKeys = []
    # keep track of which components have finished
    promptComponents = [prompt_msg, prompt_resp]
    for thisComponent in promptComponents:
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
    
    # --- Run Routine "prompt" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt_msg* updates
        if prompt_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_msg.frameNStart = frameN  # exact frame index
            prompt_msg.tStart = t  # local t and not account for scr refresh
            prompt_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_msg.started')
            prompt_msg.setAutoDraw(True)
        
        # *prompt_resp* updates
        waitOnFlip = False
        if prompt_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_resp.frameNStart = frameN  # exact frame index
            prompt_resp.tStart = t  # local t and not account for scr refresh
            prompt_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_resp.started')
            prompt_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prompt_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prompt_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prompt_resp.status == STARTED and not waitOnFlip:
            theseKeys = prompt_resp.getKeys(keyList=['space'], waitRelease=False)
            _prompt_resp_allKeys.extend(theseKeys)
            if len(_prompt_resp_allKeys):
                prompt_resp.keys = _prompt_resp_allKeys[-1].name  # just the last key pressed
                prompt_resp.rt = _prompt_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in promptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prompt" ---
    for thisComponent in promptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    test_period = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(test_file),
        seed=None, name='test_period')
    thisExp.addLoop(test_period)  # add the loop to the experiment
    thisTest_period = test_period.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest_period.rgb)
    if thisTest_period != None:
        for paramName in thisTest_period:
            exec('{} = thisTest_period[paramName]'.format(paramName))
    
    for thisTest_period in test_period:
        currentLoop = test_period
        # abbreviate parameter names if possible (e.g. rgb = thisTest_period.rgb)
        if thisTest_period != None:
            for paramName in thisTest_period:
                exec('{} = thisTest_period[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "test" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        max_length = 12
        
        
        
        # Run 'Begin Routine' code from file_manager
        max_cycles = 4 # número máximo de ciclos no experimento
        
        # criando arquivos
        if (test_period.thisN == 0) and (cycle.thisN < max_cycles):
            if not exists(f"{expInfo['participant']}/cycle_{cycle.thisN + 2}.csv"):
                novo_arquivo = open(f"{expInfo['participant']}/cycle_{cycle.thisN + 2}.csv", "w")
                # cria cabeçalho do arquivo
                novo_arquivo.write("English,Portuguese\n")
                
                print(f"{expInfo['participant']}/cycle_{cycle.thisN + 2}.csv criado com sucesso!")
                
                # mede comprimento do arquivo do atual loop de ciclos
                arquivo = open(f"{expInfo['participant']}/cycle_{cycle.thisN + 1}.csv", "r").readlines()
                if test_drop:
                    numero_de_itens = len(arquivo[1:]) # conta número de pares, ignora cabeçalho
                else:
                    numero_de_itens = total_items
                # para debuggar
                print(f"Ciclo {cycle.thisN + 1}: {numero_de_itens}")
                
        # encerra loop se for condição Tn e não houver novos itens na planilha
        if (test_drop == True) and numero_de_itens == 0:
            continueRoutine = False
            test_period.finished = True
        cue_test.setText(English)
        target_test.reset()
        # keep track of which components have finished
        testComponents = [cue_test, target_test]
        for thisComponent in testComponents:
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
        
        # --- Run Routine "test" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            target_test.text = target_test.text.strip()
            if len(target_test.text) > max_length:
                target_test.text = target_test.text.strip()[:max_length]
            
            # *cue_test* updates
            if cue_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cue_test.frameNStart = frameN  # exact frame index
                cue_test.tStart = t  # local t and not account for scr refresh
                cue_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue_test, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_test.started')
                cue_test.setAutoDraw(True)
            if cue_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue_test.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    cue_test.tStop = t  # not accounting for scr refresh
                    cue_test.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cue_test.stopped')
                    cue_test.setAutoDraw(False)
            
            # *target_test* updates
            if target_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target_test.frameNStart = frameN  # exact frame index
                target_test.tStart = t  # local t and not account for scr refresh
                target_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_test, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_test.started')
                target_test.setAutoDraw(True)
            if target_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target_test.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    target_test.tStop = t  # not accounting for scr refresh
                    target_test.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_test.stopped')
                    target_test.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test" ---
        for thisComponent in testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        if target_test.text.strip() == Portuguese:
            response_corr = 1
        else:
            response_corr = 0
            
        thisExp.addData("response_corr", response_corr)
        
        if (study_drop == 1) and (test_drop == 1):
            thisExp.addData("condition", "SnTn")
        elif (study_drop == 1) and (test_drop == 0):
            thisExp.addData("condition", "SnT")
        elif (study_drop == 0) and (test_drop == 1):
            thisExp.addData("condition", "STn")
        elif (study_drop == 0) and (test_drop == 0):
            thisExp.addData("condition", "ST")
        
        
        # Run 'End Routine' code from file_manager
        print(English)
        print(arquivo)
        auxiliar = f"{English},{Portuguese}\n"
        
        # alimenta arquivo para o dropout
        if (response_corr == 0) and (auxiliar in arquivo):
            novo_arquivo.write(f"{English},{Portuguese}\n")
            print(f"Salvei o par {English}-{Portuguese}!")
        
        # se estamos na primeira iteração da rotina
        if test_period.thisN == (numero_de_itens - 1):
            novo_arquivo.close()
            # dropout em estudo
            if study_drop:
                study_file = f"{expInfo['participant']}/cycle_{cycle.thisN + 2}.csv"
            # dropout em teste
            if test_drop:
                test_file = f"{expInfo['participant']}/cycle_{cycle.thisN + 2}.csv"
            
           
        
        test_period.addData('target_test.text',target_test.text)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'test_period'
    
# completed 4.0 repeats of 'cycle'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
# update component parameters for each repeat
thanks_resp.keys = []
thanks_resp.rt = []
_thanks_resp_allKeys = []
# keep track of which components have finished
thanksComponents = [thanks_msg, thanks_resp]
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
    
    # *thanks_msg* updates
    if thanks_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_msg.frameNStart = frameN  # exact frame index
        thanks_msg.tStart = t  # local t and not account for scr refresh
        thanks_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_msg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thanks_msg.started')
        thanks_msg.setAutoDraw(True)
    
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
# Run 'End Experiment' code from instr_code
# salvando duração da sessão...
thisExp.addData("session_duration", globalClock.getTime())


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
