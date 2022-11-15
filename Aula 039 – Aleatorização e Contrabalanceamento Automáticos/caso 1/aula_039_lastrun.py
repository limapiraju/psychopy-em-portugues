#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on novembro 12, 2022, at 17:03
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

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'aula_039'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 039\\caso 1\\aula_039_lastrun.py',
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
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
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
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
import random

# em qual tela de instrução estamos?
current_instruction = 0

if expInfo["participant"] == "":
    expInfo["participant"] = "participante"

# textos de instruções (um por tela)
instructions_list = [f"""Olá, {expInfo["participant"]}! Começaremos agora a primeira sessão desta pesquisa.""", "Segunda tela de instruções", "Terceira tela de instruções", "Quarta tela de instruções", "Quinta tela de instruções"] 

current_button = "buttons1.jpg"

# texto de agradecimento
thanks_msg = f"""{expInfo["participant"].title()}, as tarefas de  hoje terminaram!

Obrigado por sua participação!"""

# lista contém as possíveis condições experimentais
colors = ["red", "green", "blue"]

# embaralha lista de cores
random.shuffle(colors)

# seleciona a primeira como a condição experimental
color = colors[0]

# maneira alternativa
"""
color = random.choice(["red", "green", "blue"])
"""

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_resp = keyboard.Keyboard()
instr_button = visual.ImageStim(
    win=win,
    name='instr_button', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.7), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "trial" ---
word = visual.TextStim(win=win, name='word',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.25, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "thanks" ---
thansk_msg = visual.TextStim(win=win, name='thansk_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=999.0, method='sequential', 
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
    instr_msg.setText(instructions_list[current_instruction])
    instr_resp.keys = []
    instr_resp.rt = []
    _instr_resp_allKeys = []
    instr_button.setImage(current_button)
    # keep track of which components have finished
    instructionComponents = [instr_msg, instr_resp, instr_button]
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
        
        # *instr_resp* updates
        waitOnFlip = False
        if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_resp.started')
            instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _instr_resp_allKeys.extend(theseKeys)
            if len(_instr_resp_allKeys):
                instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
                instr_resp.rt = _instr_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *instr_button* updates
        if instr_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_button.frameNStart = frameN  # exact frame index
            instr_button.tStart = t  # local t and not account for scr refresh
            instr_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_button.started')
            instr_button.setAutoDraw(True)
        
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
    # se participante apertou esquerda...
    if instr_resp.keys == "left":
        # diminui em uma unidade o índice da lista de instruções
        current_instruction -= 1
    # se o participante apertou direita...
    elif instr_resp.keys == "right":
        # aumenta em uma unidade o índice da lista de instruções
        current_instruction += 1
    
    # se o índice da lista de instruções ficou negativo...
    if current_instruction < 0:
        current_instruction = 0
    elif current_instruction == len(instructions_list):
        current_instruction = 0
        instructions.finished = True
    
    # atualiza qual botão vai aparecer na tela
    if current_instruction == 0:
        current_button = "buttons1.jpg"
    else:
        current_button = "buttons2.jpg"
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('words.xlsx'),
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
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    word.setColor(color, colorSpace='rgb')
    word.setText(portuguese)
    # keep track of which components have finished
    trialComponents = [word]
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
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word* updates
        if word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word.frameNStart = frameN  # exact frame index
            word.tStart = t  # local t and not account for scr refresh
            word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'word.started')
            word.setAutoDraw(True)
        if word.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                word.tStop = t  # not accounting for scr refresh
                word.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'word.stopped')
                word.setAutoDraw(False)
        
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
    # Run 'End Routine' code from trial_code
    thisExp.addData("condição experimental", color)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
# update component parameters for each repeat
thansk_msg.setText(thanks_msg)
# keep track of which components have finished
thanksComponents = [thansk_msg]
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
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thansk_msg* updates
    if thansk_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thansk_msg.frameNStart = frameN  # exact frame index
        thansk_msg.tStart = t  # local t and not account for scr refresh
        thansk_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thansk_msg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thansk_msg.started')
        thansk_msg.setAutoDraw(True)
    if thansk_msg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thansk_msg.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            thansk_msg.tStop = t  # not accounting for scr refresh
            thansk_msg.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thansk_msg.stopped')
            thansk_msg.setAutoDraw(False)
    
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
# using non-slip timing so subtract the expected duration of this Routine
routineTimer.addTime(-5.000000)
# Run 'End Experiment' code from instr_code
thisExp.addData("condição experimental", color)

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
