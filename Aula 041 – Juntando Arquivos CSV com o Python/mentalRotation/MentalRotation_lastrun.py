#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on dezembro 31, 2022, at 09:36
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'MentalRot'  # from the Builder filename that created this script
expInfo = {
    'session': '001',
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\mentalRotation\\MentalRotation_lastrun.py',
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
    size=[1100, 750], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
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

# --- Initialize components for Routine "Intructions_1" ---
instr_txt_1 = visual.TextStim(win=win, name='instr_txt_1',
    text="Welcome. You will see two letters on the screen that have been rotated. For each pair of letters, indicate if they are mirror images of each other when they two letters are in their normal upright position. (Ignore the rotations.) \n \nPress 'm' if they are mirror images of each other.\nPress 'n' if they are not the same (not mirror images).   \n \nPress the 'm' to continue.",
    font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=.8, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_key_1 = keyboard.Keyboard()

# --- Initialize components for Routine "Intructions_2" ---
image_L_3 = visual.ImageStim(
    win=win,
    name='image_L_3', 
    image='sin', mask='raisedCos', anchor='center',
    ori=1.0, pos=[-.25, .2], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_R_3 = visual.ImageStim(
    win=win,
    name='image_R_3', 
    image='sin', mask='raisedCos', anchor='center',
    ori=1.0, pos=[0.25, .2], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instr_txt_2 = visual.TextStim(win=win, name='instr_txt_2',
    text="Here, the letter on the right is a mirror image of the letter on the left. They would still be different after mentally rotating them to line up. So press 'n' (different). If they are the same, you would press 'm'. \n \nTry to respond as accurately as you can. Also try to be fast, but emphasize being accurate. Press 'n' to start.",
    font='Arial',
    pos=[0, -.3], height=0.04, wrapWidth=1.2, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_key_2 = keyboard.Keyboard()

# --- Initialize components for Routine "pause_start" ---
mini_pause_2 = visual.TextStim(win=win, name='mini_pause_2',
    text=' +',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial" ---
image_L = visual.ImageStim(
    win=win,
    name='image_L', 
    image='sin', mask='raisedCos', anchor='center',
    ori=1.0, pos=[-.25, 0], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_R = visual.ImageStim(
    win=win,
    name='image_R', 
    image='sin', mask='raisedCos', anchor='center',
    ori=1.0, pos=[0.25, 0], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response = keyboard.Keyboard()
main_instr = visual.TextStim(win=win, name='main_instr',
    text='\'n\' for "non mirrored"/"different"\n\'m\' for "mirrored"/"same"',
    font='Arial',
    pos=[0, -.3], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
# Run 'Begin Experiment' code from add_data
data_string = 'angle,rt,corr\n'
trial_count = visual.TextStim(win=win, name='trial_count',
    text='',
    font='Arial',
    pos=[.4, -.4], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "pause" ---
mini_pause = visual.TextStim(win=win, name='mini_pause',
    text=' ',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "the_end" ---
end_txt = visual.TextStim(win=win, name='end_txt',
    text='The end. \n \nPress space to see your data.',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Intructions_1" ---
continueRoutine = True
# update component parameters for each repeat
instr_key_1.keys = []
instr_key_1.rt = []
_instr_key_1_allKeys = []
# keep track of which components have finished
Intructions_1Components = [instr_txt_1, instr_key_1]
for thisComponent in Intructions_1Components:
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

# --- Run Routine "Intructions_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_txt_1* updates
    if instr_txt_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_txt_1.frameNStart = frameN  # exact frame index
        instr_txt_1.tStart = t  # local t and not account for scr refresh
        instr_txt_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_txt_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_txt_1.started')
        instr_txt_1.setAutoDraw(True)
    
    # *instr_key_1* updates
    waitOnFlip = False
    if instr_key_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_key_1.frameNStart = frameN  # exact frame index
        instr_key_1.tStart = t  # local t and not account for scr refresh
        instr_key_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_key_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_key_1.started')
        instr_key_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_key_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_key_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_key_1.status == STARTED and not waitOnFlip:
        theseKeys = instr_key_1.getKeys(keyList=['m'], waitRelease=False)
        _instr_key_1_allKeys.extend(theseKeys)
        if len(_instr_key_1_allKeys):
            instr_key_1.keys = _instr_key_1_allKeys[-1].name  # just the last key pressed
            instr_key_1.rt = _instr_key_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Intructions_1" ---
for thisComponent in Intructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_key_1.keys in ['', [], None]:  # No response was made
    instr_key_1.keys = None
thisExp.addData('instr_key_1.keys',instr_key_1.keys)
if instr_key_1.keys != None:  # we had a response
    thisExp.addData('instr_key_1.rt', instr_key_1.rt)
thisExp.nextEntry()
# the Routine "Intructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Intructions_2" ---
continueRoutine = True
# update component parameters for each repeat
image_L_3.setOri(0)
image_L_3.setImage('FR.png')
image_R_3.setOri(-90)
image_R_3.setImage('F.png')
instr_key_2.keys = []
instr_key_2.rt = []
_instr_key_2_allKeys = []
# keep track of which components have finished
Intructions_2Components = [image_L_3, image_R_3, instr_txt_2, instr_key_2]
for thisComponent in Intructions_2Components:
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

# --- Run Routine "Intructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_L_3* updates
    if image_L_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_L_3.frameNStart = frameN  # exact frame index
        image_L_3.tStart = t  # local t and not account for scr refresh
        image_L_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_L_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_L_3.started')
        image_L_3.setAutoDraw(True)
    
    # *image_R_3* updates
    if image_R_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_R_3.frameNStart = frameN  # exact frame index
        image_R_3.tStart = t  # local t and not account for scr refresh
        image_R_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_R_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_R_3.started')
        image_R_3.setAutoDraw(True)
    
    # *instr_txt_2* updates
    if instr_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_txt_2.frameNStart = frameN  # exact frame index
        instr_txt_2.tStart = t  # local t and not account for scr refresh
        instr_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_txt_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_txt_2.started')
        instr_txt_2.setAutoDraw(True)
    
    # *instr_key_2* updates
    waitOnFlip = False
    if instr_key_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_key_2.frameNStart = frameN  # exact frame index
        instr_key_2.tStart = t  # local t and not account for scr refresh
        instr_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_key_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_key_2.started')
        instr_key_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_key_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_key_2.status == STARTED and not waitOnFlip:
        theseKeys = instr_key_2.getKeys(keyList=['n'], waitRelease=False)
        _instr_key_2_allKeys.extend(theseKeys)
        if len(_instr_key_2_allKeys):
            instr_key_2.keys = _instr_key_2_allKeys[-1].name  # just the last key pressed
            instr_key_2.rt = _instr_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Intructions_2" ---
for thisComponent in Intructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Intructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pause_start" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
pause_startComponents = [mini_pause_2]
for thisComponent in pause_startComponents:
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

# --- Run Routine "pause_start" ---
while continueRoutine and routineTimer.getTime() < 1.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mini_pause_2* updates
    if mini_pause_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mini_pause_2.frameNStart = frameN  # exact frame index
        mini_pause_2.tStart = t  # local t and not account for scr refresh
        mini_pause_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mini_pause_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'mini_pause_2.started')
        mini_pause_2.setAutoDraw(True)
    if mini_pause_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mini_pause_2.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            mini_pause_2.tStop = t  # not accounting for scr refresh
            mini_pause_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mini_pause_2.stopped')
            mini_pause_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pause_startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pause_start" ---
for thisComponent in pause_startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine
routineTimer.addTime(-1.500000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MentalRot.csv'),
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
    # Run 'Begin Routine' code from set_images
    # randomly position the limage or rimage on the left or right hand side of the screen
    if same == 'n':
        limage = 'F.png'
        rimage = 'FR.png'
        if random() > .5:
           rimage, limage = limage, rimage
    else:
        limage = rimage = 'F.png'
        if random() > .5:
            limage = rimage = 'FR.png'
    image_L.setOri(leftori)
    image_L.setImage(limage)
    image_R.setOri(rightori)
    image_R.setImage(rimage)
    response.keys = []
    response.rt = []
    _response_allKeys = []
    trial_count.setText(trials.thisN)
    # keep track of which components have finished
    trialComponents = [image_L, image_R, response, main_instr, trial_count]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_L* updates
        if image_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_L.frameNStart = frameN  # exact frame index
            image_L.tStart = t  # local t and not account for scr refresh
            image_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_L.started')
            image_L.setAutoDraw(True)
        
        # *image_R* updates
        if image_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_R.frameNStart = frameN  # exact frame index
            image_R.tStart = t  # local t and not account for scr refresh
            image_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_R.started')
            image_R.setAutoDraw(True)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response.started')
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['n','m'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # was this correct?
                if (response.keys == str(corrAns)) or (response.keys == corrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *main_instr* updates
        if main_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_instr.frameNStart = frameN  # exact frame index
            main_instr.tStart = t  # local t and not account for scr refresh
            main_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_instr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_instr.started')
            main_instr.setAutoDraw(True)
        
        # *trial_count* updates
        if trial_count.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_count.frameNStart = frameN  # exact frame index
            trial_count.tStart = t  # local t and not account for scr refresh
            trial_count.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_count, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_count.started')
            trial_count.setAutoDraw(True)
        
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
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    # Run 'End Routine' code from add_data
    '''
    used only to demonstrate how to write/analyse a custom data format 
    as you go in your experiment. if you simply want to save custom variables on the fly to your data file 
    you can use:
        
        thisExp.addData('name of column header', variableName)
    
    e.g. to store which image was presented on the left or right you could use:
        
        thisExp.addData('left_image', image_L.image)
        thisExp.addData('right_image', image_R.image)
    '''
    data_string += '%d,%.3f,%d\n' % (abs(angle), response.rt, response.corr)
    # print(data_string)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from check_end
    # this allows us to end the current task on the nth trial if the participant name was pilot
    if trials.thisN == 4 and expInfo['participant'] == 'pilot':
        trials.finished = True
    # keep track of which components have finished
    pauseComponents = [mini_pause]
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
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mini_pause* updates
        if mini_pause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mini_pause.frameNStart = frameN  # exact frame index
            mini_pause.tStart = t  # local t and not account for scr refresh
            mini_pause.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mini_pause, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mini_pause.started')
            mini_pause.setAutoDraw(True)
        if mini_pause.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mini_pause.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                mini_pause.tStop = t  # not accounting for scr refresh
                mini_pause.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mini_pause.stopped')
                mini_pause.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 10 repeats of 'trials'


# --- Prepare to start Routine "the_end" ---
continueRoutine = True
# update component parameters for each repeat
end_key.keys = []
end_key.rt = []
_end_key_allKeys = []
# keep track of which components have finished
the_endComponents = [end_txt, end_key]
for thisComponent in the_endComponents:
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

# --- Run Routine "the_end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_txt* updates
    if end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_txt.frameNStart = frameN  # exact frame index
        end_txt.tStart = t  # local t and not account for scr refresh
        end_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_txt.started')
        end_txt.setAutoDraw(True)
    
    # *end_key* updates
    waitOnFlip = False
    if end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key.frameNStart = frameN  # exact frame index
        end_key.tStart = t  # local t and not account for scr refresh
        end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_key.started')
        end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key.status == STARTED and not waitOnFlip:
        theseKeys = end_key.getKeys(keyList=['space'], waitRelease=False)
        _end_key_allKeys.extend(theseKeys)
        if len(_end_key_allKeys):
            end_key.keys = _end_key_allKeys[-1].name  # just the last key pressed
            end_key.rt = _end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in the_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "the_end" ---
for thisComponent in the_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "the_end" was not non-slip safe, so reset the non-slip timer
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
