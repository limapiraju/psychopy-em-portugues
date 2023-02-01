#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on janeiro 07, 2023, at 20:26
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
expName = 'session1'  # from the Builder filename that created this script
expInfo = {
    'participante': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participante'], expInfo['date'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 043\\aula 043_lastrun.py',
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

# --- Initialize components for Routine "welcome" ---
welcome_msg = visual.TextStim(win=win, name='welcome_msg',
    text='Seja bem-vindo(a)!\n\n<Inserir instruções aqui>\n\nPressione [BARRA DE ESPAÇO] para iniciar a tarefa.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_resp = keyboard.Keyboard()

# --- Initialize components for Routine "study" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
study_item = visual.TextStim(win=win, name='study_item',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "pause" ---
pause_msg = visual.TextStim(win=win, name='pause_msg',
    text='<Inserir instruções da fase de teste aqui>\n\nPressione [BARRA DE ESPAÇO] para iniciar o teste.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pause_resp = keyboard.Keyboard()

# --- Initialize components for Routine "recognition" ---
recog_prompt = visual.TextStim(win=win, name='recog_prompt',
    text='Você viu a palavra abaixo na etapa anterior?',
    font='Times New Roman',
    units='norm', pos=(0, 0.75), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
recog_item = visual.TextStim(win=win, name='recog_item',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
recog_resp = keyboard.Keyboard()
recog_buttons = visual.ImageStim(
    win=win,
    name='recog_buttons', units='norm', 
    image='buttons.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.6), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "remember_know" ---
r_k_prompt = visual.TextStim(win=win, name='r_k_prompt',
    text='Você LEMBRA de ter visto a palavra ou você SABE que a viu?',
    font='Times New Roman',
    units='norm', pos=(0, 0.75), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
r_k_item = visual.TextStim(win=win, name='r_k_item',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
r_k_resp = keyboard.Keyboard()
r_k_buttons = visual.ImageStim(
    win=win,
    name='r_k_buttons', units='norm', 
    image='r_k_buttons.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.6), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "thanks" ---
thanks_prompt = visual.TextStim(win=win, name='thanks_prompt',
    text='Fim do experimento!\n\nPressione [BARRA DE ESPAÇO] para fechar a janela.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
thanks_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
# update component parameters for each repeat
welcome_resp.keys = []
welcome_resp.rt = []
_welcome_resp_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_msg, welcome_resp]
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
    
    # *welcome_resp* updates
    waitOnFlip = False
    if welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_resp.started')
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_resp.getKeys(keyList=['space'], waitRelease=False)
        _welcome_resp_allKeys.extend(theseKeys)
        if len(_welcome_resp_allKeys):
            welcome_resp.keys = _welcome_resp_allKeys[-1].name  # just the last key pressed
            welcome_resp.rt = _welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
study_phase = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('palavras.xlsx', selection='0:15'),
    seed=None, name='study_phase')
thisExp.addLoop(study_phase)  # add the loop to the experiment
thisStudy_phase = study_phase.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy_phase.rgb)
if thisStudy_phase != None:
    for paramName in thisStudy_phase:
        exec('{} = thisStudy_phase[paramName]'.format(paramName))

for thisStudy_phase in study_phase:
    currentLoop = study_phase
    # abbreviate parameter names if possible (e.g. rgb = thisStudy_phase.rgb)
    if thisStudy_phase != None:
        for paramName in thisStudy_phase:
            exec('{} = thisStudy_phase[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "study" ---
    continueRoutine = True
    # update component parameters for each repeat
    study_item.setText(Palavra.lower())
    # keep track of which components have finished
    studyComponents = [fixation, study_item]
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
    while continueRoutine and routineTimer.getTime() < 0.2:
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
            if tThisFlipGlobal > fixation.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        
        # *study_item* updates
        if study_item.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            study_item.frameNStart = frameN  # exact frame index
            study_item.tStart = t  # local t and not account for scr refresh
            study_item.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(study_item, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'study_item.started')
            study_item.setAutoDraw(True)
        if study_item.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > study_item.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                study_item.tStop = t  # not accounting for scr refresh
                study_item.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'study_item.stopped')
                study_item.setAutoDraw(False)
        
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
    routineTimer.addTime(-0.200000)
    thisExp.nextEntry()
    
# completed 1 repeats of 'study_phase'

# get names of stimulus parameters
if study_phase.trialList in ([], [None], None):
    params = []
else:
    params = study_phase.trialList[0].keys()
# save data for this loop
study_phase.saveAsExcel(filename + '.xlsx', sheetName='study_phase',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
study_phase.saveAsText(filename + 'study_phase.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "pause" ---
continueRoutine = True
# update component parameters for each repeat
pause_resp.keys = []
pause_resp.rt = []
_pause_resp_allKeys = []
# keep track of which components have finished
pauseComponents = [pause_msg, pause_resp]
for thisComponent in pauseComponents:
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

# --- Run Routine "pause" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pause_msg* updates
    if pause_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pause_msg.frameNStart = frameN  # exact frame index
        pause_msg.tStart = t  # local t and not account for scr refresh
        pause_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pause_msg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pause_msg.started')
        pause_msg.setAutoDraw(True)
    
    # *pause_resp* updates
    waitOnFlip = False
    if pause_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pause_resp.frameNStart = frameN  # exact frame index
        pause_resp.tStart = t  # local t and not account for scr refresh
        pause_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pause_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pause_resp.started')
        pause_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(pause_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(pause_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if pause_resp.status == STARTED and not waitOnFlip:
        theseKeys = pause_resp.getKeys(keyList=['space'], waitRelease=False)
        _pause_resp_allKeys.extend(theseKeys)
        if len(_pause_resp_allKeys):
            pause_resp.keys = _pause_resp_allKeys[-1].name  # just the last key pressed
            pause_resp.rt = _pause_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pause" ---
for thisComponent in pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_phase = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('palavras.xlsx'),
    seed=None, name='test_phase')
thisExp.addLoop(test_phase)  # add the loop to the experiment
thisTest_phase = test_phase.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest_phase.rgb)
if thisTest_phase != None:
    for paramName in thisTest_phase:
        exec('{} = thisTest_phase[paramName]'.format(paramName))

for thisTest_phase in test_phase:
    currentLoop = test_phase
    # abbreviate parameter names if possible (e.g. rgb = thisTest_phase.rgb)
    if thisTest_phase != None:
        for paramName in thisTest_phase:
            exec('{} = thisTest_phase[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "recognition" ---
    continueRoutine = True
    # update component parameters for each repeat
    recog_item.setText(Palavra.lower())
    recog_resp.keys = []
    recog_resp.rt = []
    _recog_resp_allKeys = []
    # keep track of which components have finished
    recognitionComponents = [recog_prompt, recog_item, recog_resp, recog_buttons]
    for thisComponent in recognitionComponents:
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
    
    # --- Run Routine "recognition" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recog_prompt* updates
        if recog_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recog_prompt.frameNStart = frameN  # exact frame index
            recog_prompt.tStart = t  # local t and not account for scr refresh
            recog_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recog_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recog_prompt.started')
            recog_prompt.setAutoDraw(True)
        
        # *recog_item* updates
        if recog_item.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            recog_item.frameNStart = frameN  # exact frame index
            recog_item.tStart = t  # local t and not account for scr refresh
            recog_item.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recog_item, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recog_item.started')
            recog_item.setAutoDraw(True)
        
        # *recog_resp* updates
        waitOnFlip = False
        if recog_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            recog_resp.frameNStart = frameN  # exact frame index
            recog_resp.tStart = t  # local t and not account for scr refresh
            recog_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recog_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recog_resp.started')
            recog_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(recog_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(recog_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if recog_resp.status == STARTED and not waitOnFlip:
            theseKeys = recog_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _recog_resp_allKeys.extend(theseKeys)
            if len(_recog_resp_allKeys):
                recog_resp.keys = _recog_resp_allKeys[0].name  # just the first key pressed
                recog_resp.rt = _recog_resp_allKeys[0].rt
                # was this correct?
                if (recog_resp.keys == str(Resp)) or (recog_resp.keys == Resp):
                    recog_resp.corr = 1
                else:
                    recog_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *recog_buttons* updates
        if recog_buttons.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            recog_buttons.frameNStart = frameN  # exact frame index
            recog_buttons.tStart = t  # local t and not account for scr refresh
            recog_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recog_buttons, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recog_buttons.started')
            recog_buttons.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recognitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recognition" ---
    for thisComponent in recognitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if recog_resp.keys in ['', [], None]:  # No response was made
        recog_resp.keys = None
        # was no response the correct answer?!
        if str(Resp).lower() == 'none':
           recog_resp.corr = 1;  # correct non-response
        else:
           recog_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for test_phase (TrialHandler)
    test_phase.addData('recog_resp.keys',recog_resp.keys)
    test_phase.addData('recog_resp.corr', recog_resp.corr)
    if recog_resp.keys != None:  # we had a response
        test_phase.addData('recog_resp.rt', recog_resp.rt)
    # the Routine "recognition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "remember_know" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from r_k_code
    if recog_resp.keys == "right":
        continueRoutine = False
    r_k_item.setText(Palavra.lower())
    r_k_resp.keys = []
    r_k_resp.rt = []
    _r_k_resp_allKeys = []
    # keep track of which components have finished
    remember_knowComponents = [r_k_prompt, r_k_item, r_k_resp, r_k_buttons]
    for thisComponent in remember_knowComponents:
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
    
    # --- Run Routine "remember_know" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *r_k_prompt* updates
        if r_k_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            r_k_prompt.frameNStart = frameN  # exact frame index
            r_k_prompt.tStart = t  # local t and not account for scr refresh
            r_k_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(r_k_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'r_k_prompt.started')
            r_k_prompt.setAutoDraw(True)
        
        # *r_k_item* updates
        if r_k_item.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            r_k_item.frameNStart = frameN  # exact frame index
            r_k_item.tStart = t  # local t and not account for scr refresh
            r_k_item.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(r_k_item, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'r_k_item.started')
            r_k_item.setAutoDraw(True)
        
        # *r_k_resp* updates
        waitOnFlip = False
        if r_k_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            r_k_resp.frameNStart = frameN  # exact frame index
            r_k_resp.tStart = t  # local t and not account for scr refresh
            r_k_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(r_k_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'r_k_resp.started')
            r_k_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(r_k_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(r_k_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if r_k_resp.status == STARTED and not waitOnFlip:
            theseKeys = r_k_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _r_k_resp_allKeys.extend(theseKeys)
            if len(_r_k_resp_allKeys):
                r_k_resp.keys = _r_k_resp_allKeys[0].name  # just the first key pressed
                r_k_resp.rt = _r_k_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # *r_k_buttons* updates
        if r_k_buttons.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            r_k_buttons.frameNStart = frameN  # exact frame index
            r_k_buttons.tStart = t  # local t and not account for scr refresh
            r_k_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(r_k_buttons, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'r_k_buttons.started')
            r_k_buttons.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in remember_knowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "remember_know" ---
    for thisComponent in remember_knowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if r_k_resp.keys in ['', [], None]:  # No response was made
        r_k_resp.keys = None
    test_phase.addData('r_k_resp.keys',r_k_resp.keys)
    if r_k_resp.keys != None:  # we had a response
        test_phase.addData('r_k_resp.rt', r_k_resp.rt)
    # the Routine "remember_know" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'test_phase'

# get names of stimulus parameters
if test_phase.trialList in ([], [None], None):
    params = []
else:
    params = test_phase.trialList[0].keys()
# save data for this loop
test_phase.saveAsExcel(filename + '.xlsx', sheetName='test_phase',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
test_phase.saveAsText(filename + 'test_phase.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "thanks" ---
continueRoutine = True
# update component parameters for each repeat
thanks_resp.keys = []
thanks_resp.rt = []
_thanks_resp_allKeys = []
# keep track of which components have finished
thanksComponents = [thanks_prompt, thanks_resp]
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
