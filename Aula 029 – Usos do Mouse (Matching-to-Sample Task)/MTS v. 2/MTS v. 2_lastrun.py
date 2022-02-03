#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.2),
    on August 18, 2021, at 17:12
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.2'
expName = 'MTS v. 1'  # from the Builder filename that created this script
expInfo = {'participante': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participante'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\User\\Desktop\\PsychoPy\\Aulas\\Editar e gravar\\Aula 029 – Usos do Mouse (Matching-to-Sample Task)\\MTS v. 2\\MTS v. 2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[900, 600], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='Pressione [BARRA DE ESPAÇO] para continuar',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
# define uma lista de tuplas com as posições; 
# a lista será embaralhada a cada tentativa;
# isso permitirá atribuir diferentes posições a diferentes estímulos de comparação;
# comparison1 sempre será o gabarito!
positions = [(-0.60, -0.50), # esquerda (x, y)
            (0.00, -0.50), # centro (x, y)
            (0.60, -0.50)] # direita (x, y)

sample = visual.TextStim(win=win, name='sample',
    text='default text',
    font='Times New Roman',
    units='norm', pos=(0, 0.25), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
comparison1 = visual.ImageStim(
    win=win,
    name='comparison1', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
comparison2 = visual.ImageStim(
    win=win,
    name='comparison2', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
comparison3 = visual.ImageStim(
    win=win,
    name='comparison3', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
resp = event.Mouse(win=win)
x, y = [None, None]
resp.mouseClock = core.Clock()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
sample_2 = visual.TextStim(win=win, name='sample_2',
    text='default text',
    font='Times New Roman',
    units='norm', pos=(0, 0.25), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
comparison1_2 = visual.ImageStim(
    win=win,
    name='comparison1_2', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
comparison2_2 = visual.ImageStim(
    win=win,
    name='comparison2_2', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
comparison3_2 = visual.ImageStim(
    win=win,
    name='comparison3_2', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
feedback_stim = visual.Rect(
    win=win, name='feedback_stim',units='norm', 
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0],
    lineWidth=7, lineColor=1.0, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
feedback_msg = visual.TextStim(win=win, name='feedback_msg',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanks_msg = visual.TextStim(win=win, name='thanks_msg',
    text='Tarefa encerrada!\n\nObrigado por sua participação!',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instr_resp.keys = []
instr_resp.rt = []
_instr_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instr_msg, instr_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
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
        instr_msg.setAutoDraw(True)
    
    # *instr_resp* updates
    waitOnFlip = False
    if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp.frameNStart = frameN  # exact frame index
        instr_resp.tStart = t  # local t and not account for scr refresh
        instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
        instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp.getKeys(keyList=['space'], waitRelease=False)
        _instr_resp_allKeys.extend(theseKeys)
        if len(_instr_resp_allKeys):
            instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
            instr_resp.rt = _instr_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_msg.started', instr_msg.tStartRefresh)
thisExp.addData('instr_msg.stopped', instr_msg.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim.xlsx'),
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
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # embaralha as posições
    shuffle(positions)
    
    # e embaralha a lista contendo as diferentes alternativas incorretas candidatas
    shuffle(incorrect_responses)
    
    comparison1_img = comparison2_img = comparison3_img = "interrogation.jpg"
    
    sample.setText(sample_stim)
    comparison1.setPos(positions[0])
    comparison2.setPos(positions[1])
    comparison3.setPos(positions[2])
    # setup some python lists for storing info about the resp
    resp.x = []
    resp.y = []
    resp.leftButton = []
    resp.midButton = []
    resp.rightButton = []
    resp.time = []
    resp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [sample, comparison1, comparison2, comparison3, resp]
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
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # se a imagem comparison1 contém em si o mouse
        # ou, em outras palavras
        # se o mouse está em cima da imagem comparison1
        if comparison1.contains(resp):
            comparison1_img = correct_response
        else:
            comparison1_img = "interrogation.jpg"
        
        # se a imagem comparison2 contém em si o mouse
        # ou, em outras palavras
        # se o mouse está em cima da imagem comparison2
        if comparison2.contains(resp):
            comparison2_img = incorrect_responses[0]
        else:
            comparison2_img = "interrogation.jpg"
        
        # se a imagem comparison3 contém em si o mouse
        # ou, em outras palavras
        # se o mouse está em cima da imagem comparison3
        if comparison3.contains(resp):
            comparison3_img = incorrect_responses[1]
        else:
            comparison3_img = "interrogation.jpg"
        
        # *sample* updates
        if sample.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            sample.frameNStart = frameN  # exact frame index
            sample.tStart = t  # local t and not account for scr refresh
            sample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample, 'tStartRefresh')  # time at next scr refresh
            sample.setAutoDraw(True)
        
        # *comparison1* updates
        if comparison1.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            comparison1.frameNStart = frameN  # exact frame index
            comparison1.tStart = t  # local t and not account for scr refresh
            comparison1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comparison1, 'tStartRefresh')  # time at next scr refresh
            comparison1.setAutoDraw(True)
        if comparison1.status == STARTED:  # only update if drawing
            comparison1.setImage(comparison1_img, log=False)
        
        # *comparison2* updates
        if comparison2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            comparison2.frameNStart = frameN  # exact frame index
            comparison2.tStart = t  # local t and not account for scr refresh
            comparison2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comparison2, 'tStartRefresh')  # time at next scr refresh
            comparison2.setAutoDraw(True)
        if comparison2.status == STARTED:  # only update if drawing
            comparison2.setImage(comparison2_img, log=False)
        
        # *comparison3* updates
        if comparison3.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            comparison3.frameNStart = frameN  # exact frame index
            comparison3.tStart = t  # local t and not account for scr refresh
            comparison3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comparison3, 'tStartRefresh')  # time at next scr refresh
            comparison3.setAutoDraw(True)
        if comparison3.status == STARTED:  # only update if drawing
            comparison3.setImage(comparison3_img, log=False)
        # *resp* updates
        if resp.status == NOT_STARTED and t >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            resp.mouseClock.reset()
            prevButtonState = resp.getPressed()  # if button is down already this ISN'T a new click
        if resp.status == STARTED:  # only update if started and not finished!
            buttons = resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [comparison1, comparison2, comparison3]:
                        if obj.contains(resp):
                            gotValidClick = True
                            resp.clicked_name.append(obj.name)
                    x, y = resp.getPos()
                    resp.x.append(x)
                    resp.y.append(y)
                    buttons = resp.getPressed()
                    resp.leftButton.append(buttons[0])
                    resp.midButton.append(buttons[1])
                    resp.rightButton.append(buttons[2])
                    resp.time.append(resp.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('sample.started', sample.tStartRefresh)
    trials.addData('sample.stopped', sample.tStopRefresh)
    trials.addData('comparison1.started', comparison1.tStartRefresh)
    trials.addData('comparison1.stopped', comparison1.tStopRefresh)
    trials.addData('comparison2.started', comparison2.tStartRefresh)
    trials.addData('comparison2.stopped', comparison2.tStopRefresh)
    trials.addData('comparison3.started', comparison3.tStartRefresh)
    trials.addData('comparison3.stopped', comparison3.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(resp.x): trials.addData('resp.x', resp.x[0])
    if len(resp.y): trials.addData('resp.y', resp.y[0])
    if len(resp.leftButton): trials.addData('resp.leftButton', resp.leftButton[0])
    if len(resp.midButton): trials.addData('resp.midButton', resp.midButton[0])
    if len(resp.rightButton): trials.addData('resp.rightButton', resp.rightButton[0])
    if len(resp.time): trials.addData('resp.time', resp.time[0])
    if len(resp.clicked_name): trials.addData('resp.clicked_name', resp.clicked_name[0])
    trials.addData('resp.started', resp.tStart)
    trials.addData('resp.stopped', resp.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # se o participante acertou a resposta
    if resp.isPressedIn(comparison1):
        color = "green"
        msg = "Correto!"
        corr = 1
    # se o participante errou a resposta
    else:
        color = "red"
        msg = "Incorreto!"
        corr = 0
        
    sample_2.setText(sample_stim)
    comparison1_2.setPos(positions[0])
    comparison1_2.setImage(correct_response)
    comparison2_2.setPos(positions[1])
    comparison2_2.setImage(incorrect_responses[0])
    comparison3_2.setPos(positions[2])
    comparison3_2.setImage(incorrect_responses[1])
    feedback_stim.setPos(positions[0])
    feedback_stim.setLineColor(color)
    feedback_msg.setColor(color, colorSpace='rgb')
    feedback_msg.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [sample_2, comparison1_2, comparison2_2, comparison3_2, feedback_stim, feedback_msg]
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
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sample_2* updates
        if sample_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sample_2.frameNStart = frameN  # exact frame index
            sample_2.tStart = t  # local t and not account for scr refresh
            sample_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample_2, 'tStartRefresh')  # time at next scr refresh
            sample_2.setAutoDraw(True)
        if sample_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                sample_2.tStop = t  # not accounting for scr refresh
                sample_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sample_2, 'tStopRefresh')  # time at next scr refresh
                sample_2.setAutoDraw(False)
        
        # *comparison1_2* updates
        if comparison1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            comparison1_2.frameNStart = frameN  # exact frame index
            comparison1_2.tStart = t  # local t and not account for scr refresh
            comparison1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comparison1_2, 'tStartRefresh')  # time at next scr refresh
            comparison1_2.setAutoDraw(True)
        if comparison1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > comparison1_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                comparison1_2.tStop = t  # not accounting for scr refresh
                comparison1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(comparison1_2, 'tStopRefresh')  # time at next scr refresh
                comparison1_2.setAutoDraw(False)
        
        # *comparison2_2* updates
        if comparison2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            comparison2_2.frameNStart = frameN  # exact frame index
            comparison2_2.tStart = t  # local t and not account for scr refresh
            comparison2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comparison2_2, 'tStartRefresh')  # time at next scr refresh
            comparison2_2.setAutoDraw(True)
        if comparison2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > comparison2_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                comparison2_2.tStop = t  # not accounting for scr refresh
                comparison2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(comparison2_2, 'tStopRefresh')  # time at next scr refresh
                comparison2_2.setAutoDraw(False)
        
        # *comparison3_2* updates
        if comparison3_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            comparison3_2.frameNStart = frameN  # exact frame index
            comparison3_2.tStart = t  # local t and not account for scr refresh
            comparison3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comparison3_2, 'tStartRefresh')  # time at next scr refresh
            comparison3_2.setAutoDraw(True)
        if comparison3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > comparison3_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                comparison3_2.tStop = t  # not accounting for scr refresh
                comparison3_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(comparison3_2, 'tStopRefresh')  # time at next scr refresh
                comparison3_2.setAutoDraw(False)
        
        # *feedback_stim* updates
        if feedback_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_stim.frameNStart = frameN  # exact frame index
            feedback_stim.tStart = t  # local t and not account for scr refresh
            feedback_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_stim, 'tStartRefresh')  # time at next scr refresh
            feedback_stim.setAutoDraw(True)
        if feedback_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_stim.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                feedback_stim.tStop = t  # not accounting for scr refresh
                feedback_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_stim, 'tStopRefresh')  # time at next scr refresh
                feedback_stim.setAutoDraw(False)
        
        # *feedback_msg* updates
        if feedback_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_msg.frameNStart = frameN  # exact frame index
            feedback_msg.tStart = t  # local t and not account for scr refresh
            feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_msg, 'tStartRefresh')  # time at next scr refresh
            feedback_msg.setAutoDraw(True)
        if feedback_msg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_msg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                feedback_msg.tStop = t  # not accounting for scr refresh
                feedback_msg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_msg, 'tStopRefresh')  # time at next scr refresh
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
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("resp.corr", corr)
    trials.addData('sample_2.started', sample_2.tStartRefresh)
    trials.addData('sample_2.stopped', sample_2.tStopRefresh)
    trials.addData('comparison1_2.started', comparison1_2.tStartRefresh)
    trials.addData('comparison1_2.stopped', comparison1_2.tStopRefresh)
    trials.addData('comparison2_2.started', comparison2_2.tStartRefresh)
    trials.addData('comparison2_2.stopped', comparison2_2.tStopRefresh)
    trials.addData('comparison3_2.started', comparison3_2.tStartRefresh)
    trials.addData('comparison3_2.stopped', comparison3_2.tStopRefresh)
    trials.addData('feedback_stim.started', feedback_stim.tStartRefresh)
    trials.addData('feedback_stim.stopped', feedback_stim.tStopRefresh)
    trials.addData('feedback_msg.started', feedback_msg.tStartRefresh)
    trials.addData('feedback_msg.stopped', feedback_msg.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanks_msg]
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
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
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
        thanks_msg.setAutoDraw(True)
    if thanks_msg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks_msg.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            thanks_msg.tStop = t  # not accounting for scr refresh
            thanks_msg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks_msg, 'tStopRefresh')  # time at next scr refresh
            thanks_msg.setAutoDraw(False)
    
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

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks_msg.started', thanks_msg.tStartRefresh)
thisExp.addData('thanks_msg.stopped', thanks_msg.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
