#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.2),
    on June 10, 2021, at 10:58
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
expName = 'quadrado_latino'  # from the Builder filename that created this script
expInfo = {'participante': '', 'ordem': ''}
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
    originPath='C:\\Users\\User\\Desktop\\PsychoPy\\Aulas\\Aula 019 – Quadrado Latino\\quadrado_latino_lastrun.py',
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
    size=[900,600], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "begin"
beginClock = core.Clock()
begin_msg = visual.TextStim(win=win, name='begin_msg',
    text='Pressione [BARRA DE ESPAÇO] para começar.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
spacebar = keyboard.Keyboard()

# Initialize components for Routine "stroop_task"
stroop_taskClock = core.Clock()
stroop_word = visual.TextStim(win=win, name='stroop_word',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stroop_resp = keyboard.Keyboard()
reminder_buttons = visual.ImageStim(
    win=win,
    name='reminder_buttons', units='norm', 
    image='reminder.jpg', mask=None,
    ori=0, pos=(0, -0.3), size=(0.4, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "eriksen_task"
eriksen_taskClock = core.Clock()
flanker_arrows = visual.TextStim(win=win, name='flanker_arrows',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
flanker_resp = keyboard.Keyboard()

# Initialize components for Routine "navon_task"
navon_taskClock = core.Clock()
navon_trial_type = visual.TextStim(win=win, name='navon_trial_type',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
navon_img = visual.ImageStim(
    win=win,
    name='navon_img', units='norm', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "odd_quadrant_task"
odd_quadrant_taskClock = core.Clock()
arrow_1 = visual.ImageStim(
    win=win,
    name='arrow_1', units='norm', 
    image='arrow.jpg', mask=None,
    ori=1.0, pos=(-0.5, 0.5), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
arrow_2 = visual.ImageStim(
    win=win,
    name='arrow_2', units='norm', 
    image='arrow.jpg', mask=None,
    ori=1.0, pos=(0.5, 0.5), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
arrow_3 = visual.ImageStim(
    win=win,
    name='arrow_3', units='norm', 
    image='arrow.jpg', mask=None,
    ori=1.0, pos=(-0.5, -0.5), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
arrow_4 = visual.ImageStim(
    win=win,
    name='arrow_4', units='norm', 
    image='sin', mask=None,
    ori=1.0, pos=(0.5, -0.5), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
odd_quadrant_resp = event.Mouse(win=win)
x, y = [None, None]
odd_quadrant_resp.mouseClock = core.Clock()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanks_msg = visual.TextStim(win=win, name='thanks_msg',
    text='Fim da tarefa!\n\nObrigado por sua participação.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "begin"-------
continueRoutine = True
# update component parameters for each repeat
spacebar.keys = []
spacebar.rt = []
_spacebar_allKeys = []
# keep track of which components have finished
beginComponents = [begin_msg, spacebar]
for thisComponent in beginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "begin"-------
while continueRoutine:
    # get current time
    t = beginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_msg* updates
    if begin_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_msg.frameNStart = frameN  # exact frame index
        begin_msg.tStart = t  # local t and not account for scr refresh
        begin_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_msg, 'tStartRefresh')  # time at next scr refresh
        begin_msg.setAutoDraw(True)
    
    # *spacebar* updates
    waitOnFlip = False
    if spacebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spacebar.frameNStart = frameN  # exact frame index
        spacebar.tStart = t  # local t and not account for scr refresh
        spacebar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spacebar, 'tStartRefresh')  # time at next scr refresh
        spacebar.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(spacebar.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(spacebar.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if spacebar.status == STARTED and not waitOnFlip:
        theseKeys = spacebar.getKeys(keyList=['space'], waitRelease=False)
        _spacebar_allKeys.extend(theseKeys)
        if len(_spacebar_allKeys):
            spacebar.keys = _spacebar_allKeys[-1].name  # just the last key pressed
            spacebar.rt = _spacebar_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin"-------
for thisComponent in beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('begin_msg.started', begin_msg.tStartRefresh)
thisExp.addData('begin_msg.stopped', begin_msg.tStopRefresh)
# the Routine "begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
latin_square = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(expInfo["ordem"] + ".xlsx"),
    seed=None, name='latin_square')
thisExp.addLoop(latin_square)  # add the loop to the experiment
thisLatin_square = latin_square.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLatin_square.rgb)
if thisLatin_square != None:
    for paramName in thisLatin_square:
        exec('{} = thisLatin_square[paramName]'.format(paramName))

for thisLatin_square in latin_square:
    currentLoop = latin_square
    # abbreviate parameter names if possible (e.g. rgb = thisLatin_square.rgb)
    if thisLatin_square != None:
        for paramName in thisLatin_square:
            exec('{} = thisLatin_square[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    stroop_trials = data.TrialHandler(nReps=stroop_reps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stroop_file.xlsx'),
        seed=None, name='stroop_trials')
    thisExp.addLoop(stroop_trials)  # add the loop to the experiment
    thisStroop_trial = stroop_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_trial.rgb)
    if thisStroop_trial != None:
        for paramName in thisStroop_trial:
            exec('{} = thisStroop_trial[paramName]'.format(paramName))
    
    for thisStroop_trial in stroop_trials:
        currentLoop = stroop_trials
        # abbreviate parameter names if possible (e.g. rgb = thisStroop_trial.rgb)
        if thisStroop_trial != None:
            for paramName in thisStroop_trial:
                exec('{} = thisStroop_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "stroop_task"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop_word.setColor(stroop_color, colorSpace='rgb')
        stroop_word.setText(stroop_stim)
        stroop_resp.keys = []
        stroop_resp.rt = []
        _stroop_resp_allKeys = []
        # keep track of which components have finished
        stroop_taskComponents = [stroop_word, stroop_resp, reminder_buttons]
        for thisComponent in stroop_taskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_task"-------
        while continueRoutine:
            # get current time
            t = stroop_taskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_taskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stroop_word* updates
            if stroop_word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop_word.frameNStart = frameN  # exact frame index
                stroop_word.tStart = t  # local t and not account for scr refresh
                stroop_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop_word, 'tStartRefresh')  # time at next scr refresh
                stroop_word.setAutoDraw(True)
            
            # *stroop_resp* updates
            waitOnFlip = False
            if stroop_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop_resp.frameNStart = frameN  # exact frame index
                stroop_resp.tStart = t  # local t and not account for scr refresh
                stroop_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop_resp, 'tStartRefresh')  # time at next scr refresh
                stroop_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(stroop_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(stroop_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if stroop_resp.status == STARTED and not waitOnFlip:
                theseKeys = stroop_resp.getKeys(keyList=['left', 'right', 'down'], waitRelease=False)
                _stroop_resp_allKeys.extend(theseKeys)
                if len(_stroop_resp_allKeys):
                    stroop_resp.keys = _stroop_resp_allKeys[0].name  # just the first key pressed
                    stroop_resp.rt = _stroop_resp_allKeys[0].rt
                    # was this correct?
                    if (stroop_resp.keys == str(resp_corr_stroop)) or (stroop_resp.keys == resp_corr_stroop):
                        stroop_resp.corr = 1
                    else:
                        stroop_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *reminder_buttons* updates
            if reminder_buttons.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                reminder_buttons.frameNStart = frameN  # exact frame index
                reminder_buttons.tStart = t  # local t and not account for scr refresh
                reminder_buttons.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reminder_buttons, 'tStartRefresh')  # time at next scr refresh
                reminder_buttons.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_taskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_task"-------
        for thisComponent in stroop_taskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stroop_trials.addData('stroop_word.started', stroop_word.tStartRefresh)
        stroop_trials.addData('stroop_word.stopped', stroop_word.tStopRefresh)
        # check responses
        if stroop_resp.keys in ['', [], None]:  # No response was made
            stroop_resp.keys = None
            # was no response the correct answer?!
            if str(resp_corr_stroop).lower() == 'none':
               stroop_resp.corr = 1;  # correct non-response
            else:
               stroop_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for stroop_trials (TrialHandler)
        stroop_trials.addData('stroop_resp.keys',stroop_resp.keys)
        stroop_trials.addData('stroop_resp.corr', stroop_resp.corr)
        if stroop_resp.keys != None:  # we had a response
            stroop_trials.addData('stroop_resp.rt', stroop_resp.rt)
        stroop_trials.addData('stroop_resp.started', stroop_resp.tStartRefresh)
        stroop_trials.addData('stroop_resp.stopped', stroop_resp.tStopRefresh)
        stroop_trials.addData('reminder_buttons.started', reminder_buttons.tStartRefresh)
        stroop_trials.addData('reminder_buttons.stopped', reminder_buttons.tStopRefresh)
        # the Routine "stroop_task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed stroop_reps repeats of 'stroop_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    flanker_trials = data.TrialHandler(nReps=eriksen_reps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('flanker_file.xlsx'),
        seed=None, name='flanker_trials')
    thisExp.addLoop(flanker_trials)  # add the loop to the experiment
    thisFlanker_trial = flanker_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFlanker_trial.rgb)
    if thisFlanker_trial != None:
        for paramName in thisFlanker_trial:
            exec('{} = thisFlanker_trial[paramName]'.format(paramName))
    
    for thisFlanker_trial in flanker_trials:
        currentLoop = flanker_trials
        # abbreviate parameter names if possible (e.g. rgb = thisFlanker_trial.rgb)
        if thisFlanker_trial != None:
            for paramName in thisFlanker_trial:
                exec('{} = thisFlanker_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "eriksen_task"-------
        continueRoutine = True
        # update component parameters for each repeat
        flanker_arrows.setText(flanker_stim)
        flanker_resp.keys = []
        flanker_resp.rt = []
        _flanker_resp_allKeys = []
        # keep track of which components have finished
        eriksen_taskComponents = [flanker_arrows, flanker_resp]
        for thisComponent in eriksen_taskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        eriksen_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "eriksen_task"-------
        while continueRoutine:
            # get current time
            t = eriksen_taskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=eriksen_taskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *flanker_arrows* updates
            if flanker_arrows.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
                # keep track of start time/frame for later
                flanker_arrows.frameNStart = frameN  # exact frame index
                flanker_arrows.tStart = t  # local t and not account for scr refresh
                flanker_arrows.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_arrows, 'tStartRefresh')  # time at next scr refresh
                flanker_arrows.setAutoDraw(True)
            
            # *flanker_resp* updates
            waitOnFlip = False
            if flanker_resp.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
                # keep track of start time/frame for later
                flanker_resp.frameNStart = frameN  # exact frame index
                flanker_resp.tStart = t  # local t and not account for scr refresh
                flanker_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_resp, 'tStartRefresh')  # time at next scr refresh
                flanker_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(flanker_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(flanker_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if flanker_resp.status == STARTED and not waitOnFlip:
                theseKeys = flanker_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _flanker_resp_allKeys.extend(theseKeys)
                if len(_flanker_resp_allKeys):
                    flanker_resp.keys = _flanker_resp_allKeys[0].name  # just the first key pressed
                    flanker_resp.rt = _flanker_resp_allKeys[0].rt
                    # was this correct?
                    if (flanker_resp.keys == str(corr_resp_flanker)) or (flanker_resp.keys == corr_resp_flanker):
                        flanker_resp.corr = 1
                    else:
                        flanker_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in eriksen_taskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "eriksen_task"-------
        for thisComponent in eriksen_taskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        flanker_trials.addData('flanker_arrows.started', flanker_arrows.tStartRefresh)
        flanker_trials.addData('flanker_arrows.stopped', flanker_arrows.tStopRefresh)
        # check responses
        if flanker_resp.keys in ['', [], None]:  # No response was made
            flanker_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp_flanker).lower() == 'none':
               flanker_resp.corr = 1;  # correct non-response
            else:
               flanker_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for flanker_trials (TrialHandler)
        flanker_trials.addData('flanker_resp.keys',flanker_resp.keys)
        flanker_trials.addData('flanker_resp.corr', flanker_resp.corr)
        if flanker_resp.keys != None:  # we had a response
            flanker_trials.addData('flanker_resp.rt', flanker_resp.rt)
        flanker_trials.addData('flanker_resp.started', flanker_resp.tStartRefresh)
        flanker_trials.addData('flanker_resp.stopped', flanker_resp.tStopRefresh)
        # the Routine "eriksen_task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed eriksen_reps repeats of 'flanker_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    navon_trials = data.TrialHandler(nReps=navon_reps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('navon_file.xlsx'),
        seed=None, name='navon_trials')
    thisExp.addLoop(navon_trials)  # add the loop to the experiment
    thisNavon_trial = navon_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNavon_trial.rgb)
    if thisNavon_trial != None:
        for paramName in thisNavon_trial:
            exec('{} = thisNavon_trial[paramName]'.format(paramName))
    
    for thisNavon_trial in navon_trials:
        currentLoop = navon_trials
        # abbreviate parameter names if possible (e.g. rgb = thisNavon_trial.rgb)
        if thisNavon_trial != None:
            for paramName in thisNavon_trial:
                exec('{} = thisNavon_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "navon_task"-------
        continueRoutine = True
        # update component parameters for each repeat
        navon_trial_type.setText('Característica: ' + trial_type)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        navon_img.setImage(navon_stim)
        # keep track of which components have finished
        navon_taskComponents = [navon_trial_type, key_resp, navon_img]
        for thisComponent in navon_taskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        navon_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "navon_task"-------
        while continueRoutine:
            # get current time
            t = navon_taskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=navon_taskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *navon_trial_type* updates
            if navon_trial_type.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                navon_trial_type.frameNStart = frameN  # exact frame index
                navon_trial_type.tStart = t  # local t and not account for scr refresh
                navon_trial_type.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(navon_trial_type, 'tStartRefresh')  # time at next scr refresh
                navon_trial_type.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['h', 's'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
                    # was this correct?
                    if (key_resp.keys == str(corr_resp_navon)) or (key_resp.keys == corr_resp_navon):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *navon_img* updates
            if navon_img.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                navon_img.frameNStart = frameN  # exact frame index
                navon_img.tStart = t  # local t and not account for scr refresh
                navon_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(navon_img, 'tStartRefresh')  # time at next scr refresh
                navon_img.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in navon_taskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "navon_task"-------
        for thisComponent in navon_taskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        navon_trials.addData('navon_trial_type.started', navon_trial_type.tStartRefresh)
        navon_trials.addData('navon_trial_type.stopped', navon_trial_type.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp_navon).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for navon_trials (TrialHandler)
        navon_trials.addData('key_resp.keys',key_resp.keys)
        navon_trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            navon_trials.addData('key_resp.rt', key_resp.rt)
        navon_trials.addData('key_resp.started', key_resp.tStartRefresh)
        navon_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        navon_trials.addData('navon_img.started', navon_img.tStartRefresh)
        navon_trials.addData('navon_img.stopped', navon_img.tStopRefresh)
        # the Routine "navon_task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed navon_reps repeats of 'navon_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    odd_quadrant_trials = data.TrialHandler(nReps=odd_reps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('odd_quadrant_file.xlsx'),
        seed=None, name='odd_quadrant_trials')
    thisExp.addLoop(odd_quadrant_trials)  # add the loop to the experiment
    thisOdd_quadrant_trial = odd_quadrant_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOdd_quadrant_trial.rgb)
    if thisOdd_quadrant_trial != None:
        for paramName in thisOdd_quadrant_trial:
            exec('{} = thisOdd_quadrant_trial[paramName]'.format(paramName))
    
    for thisOdd_quadrant_trial in odd_quadrant_trials:
        currentLoop = odd_quadrant_trials
        # abbreviate parameter names if possible (e.g. rgb = thisOdd_quadrant_trial.rgb)
        if thisOdd_quadrant_trial != None:
            for paramName in thisOdd_quadrant_trial:
                exec('{} = thisOdd_quadrant_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "odd_quadrant_task"-------
        continueRoutine = True
        # update component parameters for each repeat
        arrow_1.setOri(upper_left)
        arrow_2.setOri(upper_right)
        arrow_3.setOri(lower_left)
        arrow_4.setOri(lower_right)
        arrow_4.setImage('arrow.jpg')
        # setup some python lists for storing info about the odd_quadrant_resp
        odd_quadrant_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        odd_quadrant_taskComponents = [arrow_1, arrow_2, arrow_3, arrow_4, odd_quadrant_resp]
        for thisComponent in odd_quadrant_taskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_quadrant_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_quadrant_task"-------
        while continueRoutine:
            # get current time
            t = odd_quadrant_taskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_quadrant_taskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *arrow_1* updates
            if arrow_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                arrow_1.frameNStart = frameN  # exact frame index
                arrow_1.tStart = t  # local t and not account for scr refresh
                arrow_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_1, 'tStartRefresh')  # time at next scr refresh
                arrow_1.setAutoDraw(True)
            
            # *arrow_2* updates
            if arrow_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                arrow_2.frameNStart = frameN  # exact frame index
                arrow_2.tStart = t  # local t and not account for scr refresh
                arrow_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_2, 'tStartRefresh')  # time at next scr refresh
                arrow_2.setAutoDraw(True)
            
            # *arrow_3* updates
            if arrow_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                arrow_3.frameNStart = frameN  # exact frame index
                arrow_3.tStart = t  # local t and not account for scr refresh
                arrow_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_3, 'tStartRefresh')  # time at next scr refresh
                arrow_3.setAutoDraw(True)
            
            # *arrow_4* updates
            if arrow_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                arrow_4.frameNStart = frameN  # exact frame index
                arrow_4.tStart = t  # local t and not account for scr refresh
                arrow_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_4, 'tStartRefresh')  # time at next scr refresh
                arrow_4.setAutoDraw(True)
            # *odd_quadrant_resp* updates
            if odd_quadrant_resp.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                odd_quadrant_resp.frameNStart = frameN  # exact frame index
                odd_quadrant_resp.tStart = t  # local t and not account for scr refresh
                odd_quadrant_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_quadrant_resp, 'tStartRefresh')  # time at next scr refresh
                odd_quadrant_resp.status = STARTED
                odd_quadrant_resp.mouseClock.reset()
                prevButtonState = odd_quadrant_resp.getPressed()  # if button is down already this ISN'T a new click
            if odd_quadrant_resp.status == STARTED:  # only update if started and not finished!
                buttons = odd_quadrant_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [arrow_1, arrow_2, arrow_3, arrow_4]:
                            if obj.contains(odd_quadrant_resp):
                                gotValidClick = True
                                odd_quadrant_resp.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_quadrant_taskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_quadrant_task"-------
        for thisComponent in odd_quadrant_taskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd_quadrant_trials.addData('arrow_1.started', arrow_1.tStartRefresh)
        odd_quadrant_trials.addData('arrow_1.stopped', arrow_1.tStopRefresh)
        odd_quadrant_trials.addData('arrow_2.started', arrow_2.tStartRefresh)
        odd_quadrant_trials.addData('arrow_2.stopped', arrow_2.tStopRefresh)
        odd_quadrant_trials.addData('arrow_3.started', arrow_3.tStartRefresh)
        odd_quadrant_trials.addData('arrow_3.stopped', arrow_3.tStopRefresh)
        odd_quadrant_trials.addData('arrow_4.started', arrow_4.tStartRefresh)
        odd_quadrant_trials.addData('arrow_4.stopped', arrow_4.tStopRefresh)
        # store data for odd_quadrant_trials (TrialHandler)
        x, y = odd_quadrant_resp.getPos()
        buttons = odd_quadrant_resp.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [arrow_1, arrow_2, arrow_3, arrow_4]:
                if obj.contains(odd_quadrant_resp):
                    gotValidClick = True
                    odd_quadrant_resp.clicked_name.append(obj.name)
        odd_quadrant_trials.addData('odd_quadrant_resp.x', x)
        odd_quadrant_trials.addData('odd_quadrant_resp.y', y)
        odd_quadrant_trials.addData('odd_quadrant_resp.leftButton', buttons[0])
        odd_quadrant_trials.addData('odd_quadrant_resp.midButton', buttons[1])
        odd_quadrant_trials.addData('odd_quadrant_resp.rightButton', buttons[2])
        if len(odd_quadrant_resp.clicked_name):
            odd_quadrant_trials.addData('odd_quadrant_resp.clicked_name', odd_quadrant_resp.clicked_name[0])
        odd_quadrant_trials.addData('odd_quadrant_resp.started', odd_quadrant_resp.tStart)
        odd_quadrant_trials.addData('odd_quadrant_resp.stopped', odd_quadrant_resp.tStop)
        # the Routine "odd_quadrant_task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed odd_reps repeats of 'odd_quadrant_trials'
    
# completed 1 repeats of 'latin_square'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(10.000000)
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
        if tThisFlipGlobal > thanks_msg.tStartRefresh + 10-frameTolerance:
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
