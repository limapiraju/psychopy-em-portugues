#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.2),
    on March 18, 2022, at 09:15
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
expName = 'pm_ga'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Python_files\\PsychoPy\\YouTube\\Aulas\\Aula 030 – Relógios\\temp_lastrun.py',
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
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start"
startClock = core.Clock()
import random
import math

random.seed()
puttarget = 25
wordlist = []
answerlist = []
targetlist = []
word_num = 0
nonword_num = 0
tar_num = 0
trialnum = 1
NTargets = 8
NTrials = 200
targetgap = 25
mins = 0
secs = 0
showtime = 0
showclock = 0
now_clock = 0
text = visual.TextStim(win=win, name='text',
    text="Please categorise items into words and non-words by pressing 'w' or 'n' on the keyboard.\nDuring this phase please press the 's' key if you see item that starts with an s before categorising it.\n\nPlease also press '\\' every minute. You can press the space bar to view a clock.\n\nProceed as quickly and accurately as possible.\n\nPlease indicate to the researcher if you have understood these instructions\n\nPress the space bar to start",
    font='Arial',
    pos=[0, 0], height=30, wrapWidth=800, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "loadwords"
loadwordsClock = core.Clock()

# Initialize components for Routine "loadtargets"
loadtargetsClock = core.Clock()

# Initialize components for Routine "pretrial"
pretrialClock = core.Clock()
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=120, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
response = keyboard.Keyboard()
text_item = visual.TextStim(win=win, name='text_item',
    text='default text',
    font='Arial',
    pos=(0, 0), height=60, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
clock_time = visual.TextStim(win=win, name='clock_time',
    text='default text',
    font='Arial',
    pos=(450, 300), height=60, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Block_pause"
Block_pauseClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Please take a break\n\nPress space when you are ready to continue',
    font='Arial',
    pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank you very much for taking part',
    font='Arial',
    pos=[0, 0], height=30, wrapWidth=800, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
startComponents = [text, key_resp_2]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
word_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('WordLists.xlsx'),
    seed=None, name='word_loop')
thisExp.addLoop(word_loop)  # add the loop to the experiment
thisWord_loop = word_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWord_loop.rgb)
if thisWord_loop != None:
    for paramName in thisWord_loop:
        exec('{} = thisWord_loop[paramName]'.format(paramName))

for thisWord_loop in word_loop:
    currentLoop = word_loop
    # abbreviate parameter names if possible (e.g. rgb = thisWord_loop.rgb)
    if thisWord_loop != None:
        for paramName in thisWord_loop:
            exec('{} = thisWord_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "loadwords"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    loadwordsComponents = []
    for thisComponent in loadwordsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    loadwordsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "loadwords"-------
    while continueRoutine:
        # get current time
        t = loadwordsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=loadwordsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loadwordsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loadwords"-------
    for thisComponent in loadwordsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wordlist.append(Words)
    answerlist.append(Answer)
    # the Routine "loadwords" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'word_loop'


# set up handler to look after randomisation of conditions etc
targets = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('WordLists.xlsx', selection=slice(1,8)),
    seed=None, name='targets')
thisExp.addLoop(targets)  # add the loop to the experiment
thisTarget = targets.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTarget.rgb)
if thisTarget != None:
    for paramName in thisTarget:
        exec('{} = thisTarget[paramName]'.format(paramName))

for thisTarget in targets:
    currentLoop = targets
    # abbreviate parameter names if possible (e.g. rgb = thisTarget.rgb)
    if thisTarget != None:
        for paramName in thisTarget:
            exec('{} = thisTarget[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "loadtargets"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    loadtargetsComponents = []
    for thisComponent in loadtargetsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    loadtargetsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "loadtargets"-------
    while continueRoutine:
        # get current time
        t = loadtargetsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=loadtargetsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loadtargetsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loadtargets"-------
    for thisComponent in loadtargetsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    targetlist.append(Targets)
    # the Routine "loadtargets" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'targets'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1000, method='random', 
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
    
    # ------Prepare to start Routine "pretrial"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if tar_num > NTargets:
        thisitem = wordlist[trialnum-tarnum]
        thisanswer = wordlist[trialnum-tarnum]
        thistarget = 0
    elif trials.thisN == puttarget:
        puttarget = puttarget + targetgap
        thisitem = targetlist[tar_num]
        thisanswer = 'w'
        tar_num = tar_num + 1
        thistarget = 1
        trialnum = 0
    else:
        thisitem = wordlist[trialnum-tar_num]
        thisanswer = wordlist[trialnum-tar_num]
        thistarget = 0
    
    target_flag = 0
    time_flag = 0
    trialnum = trialnum + 1
    
    if trialnum == 104:
        pauseblock = 1
    else:
        pauseblock = 0
    
    if trials.thisN == 0:
        pm_clock=core.Clock()
    # keep track of which components have finished
    pretrialComponents = [ISI_2, fixation]
    for thisComponent in pretrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pretrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pretrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pretrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pretrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        # *ISI_2* period
        if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.tStart = t  # local t and not account for scr refresh
            ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
            ISI_2.start(0.5)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
            ISI_2.tStop = ISI_2.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pretrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pretrial"-------
    for thisComponent in pretrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('ISI_2.started', ISI_2.tStart)
    trials.addData('ISI_2.stopped', ISI_2.tStop)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    response.keys = []
    response.rt = []
    _response_allKeys = []
    clock_flag = 0
    text_item.setText(thisitem)
    # keep track of which components have finished
    trialComponents = [response, text_item, clock_time]
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
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['t', 'backslash', 's', 'w', 'n', 'space'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # was this correct?
                if (response.keys == str(thisanswer)) or (response.keys == thisanswer):
                    response.corr = 1
                else:
                    response.corr = 0
        mins = math.floor(pm_clock.getTime()/60)
        secs = round(pm_clock.getTime()-mins*60,0)
        
        if showclock == 1:
            now_clock = now_clock +1
            if now_clock > 100:
                showclock = 0
                now_clock = 0
        
        
        if "space" in response.keys:
            continueRoutine = True
            if showclock < 1:
                if clock_flag < 1:
                    thisExp.addData('Time_View', round(pm_clock.getTime(),0))
                    showclock = 1
                    clock_flag = 1
                    now_clock=0
        elif "s" in response.keys:
            continueRoutine = True
            if target_flag < 1:
                thisExp.addData('Target_RT', round(response.rt,3))
                target_flag = 1
        elif "t" in response.keys:
            continueRoutine = True
            if time_flag < 1:
                thisExp.addData('Time_Response', round(pm_clock.getTime(),0))
                if secs < 6:
                    timescore = 1
                elif secs > 54:
                    timescore = 1
                else:
                    timescore = 0
                thisExp.addData('Time_Score', timescore)
                time_flag = 1
        elif "backslash" in response.keys:
            continueRoutine = True
            if time_flag < 1:
                thisExp.addData('Time_Response', round(pm_clock.getTime(),0))
                if secs < 6:
                    timescore = 1
                elif secs > 54:
                    timescore = 1
                else:
                    timescore = 0
                thisExp.addData('Time_Score', timescore)
                time_flag = 1
        elif len(response.keys) > 0:
            continueRoutine = False
        
        # *text_item* updates
        if text_item.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_item.frameNStart = frameN  # exact frame index
            text_item.tStart = t  # local t and not account for scr refresh
            text_item.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_item, 'tStartRefresh')  # time at next scr refresh
            text_item.setAutoDraw(True)
        
        # *clock_time* updates
        if clock_time.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clock_time.frameNStart = frameN  # exact frame index
            clock_time.tStart = t  # local t and not account for scr refresh
            clock_time.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clock_time, 'tStartRefresh')  # time at next scr refresh
            clock_time.setAutoDraw(True)
        if clock_time.status == STARTED:  # only update if drawing
            clock_time.setOpacity(showclock, log=False)
            clock_time.setText(str(int(mins)).zfill(2) + ':' + str(int(secs)).zfill(2), log=False)
        
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
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(thisanswer).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    trials.addData('response.started', response.tStartRefresh)
    trials.addData('response.stopped', response.tStopRefresh)
    thisExp.addData('Item', thisitem)
    thisExp.addData('Answer', thisanswer)
    thisExp.addData('Target', thistarget)
    
    if (trials.thisN) == NTrials-1:
        trials.finished = True
    
    
    trials.addData('text_item.started', text_item.tStartRefresh)
    trials.addData('text_item.stopped', text_item.tStopRefresh)
    trials.addData('clock_time.started', clock_time.tStartRefresh)
    trials.addData('clock_time.stopped', clock_time.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=pauseblock, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Block_pause"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        Block_pauseComponents = [text_3, key_resp_4]
        for thisComponent in Block_pauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block_pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block_pause"-------
        while continueRoutine:
            # get current time
            t = Block_pauseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block_pauseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block_pauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block_pause"-------
        for thisComponent in Block_pauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('text_3.started', text_3.tStartRefresh)
        trials_2.addData('text_3.stopped', text_3.tStopRefresh)
        # the Routine "Block_pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed pauseblock repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1000 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
endComponents = [text_2, key_resp_3]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
