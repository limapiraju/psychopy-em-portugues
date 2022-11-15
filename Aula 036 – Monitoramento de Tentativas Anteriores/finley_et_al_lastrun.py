#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on julho 22, 2022, at 11:39
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

# Run 'Before Experiment' code from random_seed
import random

my_seed = random.randint(0, 1000000)
# Run 'Before Experiment' code from practice_code
# cria uma lista com números das linhas
rows = list(range(0, 12))

# embaralha essa lista
random.shuffle(rows)

# fatia a lista anterior em duas metades
all_rows = list()
all_rows.append(rows[:6])
all_rows.append(rows[6:])

# cria lista de condições 
conditions = list()

for condition in ["somente estudo", "acumulação", "diminuição"]:
    for i in range(2):
        conditions.append(condition)
        
all_conditions = list()

for i in range(2):
    random.shuffle(conditions)
    all_conditions.append(conditions[:])

# cria dicionário que mantém memória do experimento
Inupiaq_dict = dict()



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'finley_et_al'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Python para Psicólogos\\psychopy-em-portugues\\Aula 036 – Monitoramento de Tentativas Anteriores\\finley_et_al_lastrun.py',
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
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
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

# --- Initialize components for Routine "instructions" ---
instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='Pressione\n[BARRA DE ESPAÇO]\npara iniciar a tarefa.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "initial_presentation" ---

# --- Initialize components for Routine "distractor" ---

# --- Initialize components for Routine "practice_phase" ---
cue_practice = visual.TextStim(win=win, name='cue_practice',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.3), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
target_practice = visual.TextStim(win=win, name='target_practice',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.3), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_practice = keyboard.Keyboard()
condition_name = visual.TextStim(win=win, name='condition_name',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.7), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "distractor" ---

# --- Initialize components for Routine "final_test" ---
cue_final = visual.TextStim(win=win, name='cue_final',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.3), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
target_final = visual.TextStim(win=win, name='target_final',
    text='_ _ _ _ _',
    font='Times New Roman',
    units='norm', pos=(0, -0.3), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_final = keyboard.Keyboard()

# --- Initialize components for Routine "thanks" ---
thanks_msg = visual.TextStim(win=win, name='thanks_msg',
    text='Tarefa concluída.\n\nObrigado por sua participação!',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions" ---
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
frameN = -1

# --- Run Routine "instructions" ---
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

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_resp.keys in ['', [], None]:  # No response was made
    instr_resp.keys = None
thisExp.addData('instr_resp.keys',instr_resp.keys)
if instr_resp.keys != None:  # we had a response
    thisExp.addData('instr_resp.rt', instr_resp.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
initial_presentation_cycles = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='initial_presentation_cycles')
thisExp.addLoop(initial_presentation_cycles)  # add the loop to the experiment
thisInitial_presentation_cycle = initial_presentation_cycles.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInitial_presentation_cycle.rgb)
if thisInitial_presentation_cycle != None:
    for paramName in thisInitial_presentation_cycle:
        exec('{} = thisInitial_presentation_cycle[paramName]'.format(paramName))

for thisInitial_presentation_cycle in initial_presentation_cycles:
    currentLoop = initial_presentation_cycles
    # abbreviate parameter names if possible (e.g. rgb = thisInitial_presentation_cycle.rgb)
    if thisInitial_presentation_cycle != None:
        for paramName in thisInitial_presentation_cycle:
            exec('{} = thisInitial_presentation_cycle[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    initial_presentation_trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('word_pairs.xlsx'),
        seed=my_seed, name='initial_presentation_trials')
    thisExp.addLoop(initial_presentation_trials)  # add the loop to the experiment
    thisInitial_presentation_trial = initial_presentation_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInitial_presentation_trial.rgb)
    if thisInitial_presentation_trial != None:
        for paramName in thisInitial_presentation_trial:
            exec('{} = thisInitial_presentation_trial[paramName]'.format(paramName))
    
    for thisInitial_presentation_trial in initial_presentation_trials:
        currentLoop = initial_presentation_trials
        # abbreviate parameter names if possible (e.g. rgb = thisInitial_presentation_trial.rgb)
        if thisInitial_presentation_trial != None:
            for paramName in thisInitial_presentation_trial:
                exec('{} = thisInitial_presentation_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "initial_presentation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        initial_presentationComponents = []
        for thisComponent in initial_presentationComponents:
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
        
        # --- Run Routine "initial_presentation" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            for thisComponent in initial_presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "initial_presentation" ---
        for thisComponent in initial_presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "initial_presentation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'initial_presentation_trials'
    
# completed 3.0 repeats of 'initial_presentation_cycles'


# --- Prepare to start Routine "distractor" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from distractor_code
# tarefa distratora inicial = 1,5 min
# tarefa distratora final = 10 min
clock = core.CountdownTimer(start = 10)
# keep track of which components have finished
distractorComponents = []
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
    # Run 'Each Frame' code from distractor_code
    timer = int(clock.getTime())
    
    if int(clock.getTime()) <= 0:
        continueRoutine = False
    
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
# the Routine "distractor" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_phase_blocks = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_phase_blocks')
thisExp.addLoop(practice_phase_blocks)  # add the loop to the experiment
thisPractice_phase_block = practice_phase_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_phase_block.rgb)
if thisPractice_phase_block != None:
    for paramName in thisPractice_phase_block:
        exec('{} = thisPractice_phase_block[paramName]'.format(paramName))

for thisPractice_phase_block in practice_phase_blocks:
    currentLoop = practice_phase_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_phase_block.rgb)
    if thisPractice_phase_block != None:
        for paramName in thisPractice_phase_block:
            exec('{} = thisPractice_phase_block[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    practice_phase_cycles = data.TrialHandler(nReps=6.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practice_phase_cycles')
    thisExp.addLoop(practice_phase_cycles)  # add the loop to the experiment
    thisPractice_phase_cycle = practice_phase_cycles.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_phase_cycle.rgb)
    if thisPractice_phase_cycle != None:
        for paramName in thisPractice_phase_cycle:
            exec('{} = thisPractice_phase_cycle[paramName]'.format(paramName))
    
    for thisPractice_phase_cycle in practice_phase_cycles:
        currentLoop = practice_phase_cycles
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_phase_cycle.rgb)
        if thisPractice_phase_cycle != None:
            for paramName in thisPractice_phase_cycle:
                exec('{} = thisPractice_phase_cycle[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        practice_phase_trials = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('word_pairs.xlsx', selection=all_rows[practice_phase_blocks.thisN]),
            seed=my_seed, name='practice_phase_trials')
        thisExp.addLoop(practice_phase_trials)  # add the loop to the experiment
        thisPractice_phase_trial = practice_phase_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_phase_trial.rgb)
        if thisPractice_phase_trial != None:
            for paramName in thisPractice_phase_trial:
                exec('{} = thisPractice_phase_trial[paramName]'.format(paramName))
        
        for thisPractice_phase_trial in practice_phase_trials:
            currentLoop = practice_phase_trials
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_phase_trial.rgb)
            if thisPractice_phase_trial != None:
                for paramName in thisPractice_phase_trial:
                    exec('{} = thisPractice_phase_trial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "practice_phase" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from practice_code
            # ACRESCENTA NOVAS PALAVRAS AO DICIONÁRIO NO CICLO 1
            if practice_phase_cycles.thisN == 0:
                Inupiaq_dict[Inupiaq] = Inupiaq
            
            # pista a ser apresentada ao participante
            Inupiaq_cue = ""
            
            # monitora condição tentativa a tentativa
            current_condition = all_conditions[practice_phase_blocks.thisN][practice_phase_trials.thisN] # [0, 1, 2, 3, 4, 5]
            
            if current_condition == "acumulação":
                # define underscores no ciclo 1
                if practice_phase_cycles.thisN == 0:
                    Inupiaq_cue = "_____"
                
                # acrescenta uma letra por ciclo
                else:
                    while True:
                        auxiliar = random.randint(0, 4)
                        if Inupiaq_dict[Inupiaq][auxiliar] == "_":
                            break
            
                    for position, letter in enumerate(Inupiaq):
                        
                        if Inupiaq[position] == Inupiaq_dict[Inupiaq][position]:
                            Inupiaq_cue += Inupiaq[position]
                            
                        elif auxiliar == position:
                            Inupiaq_cue += Inupiaq[position]
                            
                        else:
                            Inupiaq_cue += "_"
            
                # atualiza valor da chave do dicionário
                Inupiaq_dict[Inupiaq] = Inupiaq_cue
            
            elif current_condition == "diminuição":
                # define todas as letras no ciclo 1
                if practice_phase_cycles.thisN == 0:
                    Inupiaq_cue = Inupiaq
                
                # diminui uma letra por ciclo
                else:
                    while True:
                        auxiliar = random.randint(0, 4)
                        if Inupiaq_dict[Inupiaq][auxiliar] != "_":
                            break
            
                    for position, letter in enumerate(Inupiaq):
                        
                        if Inupiaq_dict[Inupiaq][position] == "_":
                            Inupiaq_cue += "_"
                            
                        elif auxiliar == position:
                            Inupiaq_cue += "_"
                            
                        else:
                            Inupiaq_cue += Inupiaq[position]
            
            
                Inupiaq_dict[Inupiaq] = Inupiaq_cue
            
            
            else:
                Inupiaq_cue = Inupiaq
                
            Inupiaq_cue = " ".join(Inupiaq_cue)
                
            
            cue_practice.setText(Portuguese)
            target_practice.setText(Inupiaq_cue)
            key_practice.keys = []
            key_practice.rt = []
            _key_practice_allKeys = []
            condition_name.setText(current_condition)
            # keep track of which components have finished
            practice_phaseComponents = [cue_practice, target_practice, key_practice, condition_name]
            for thisComponent in practice_phaseComponents:
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
            
            # --- Run Routine "practice_phase" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cue_practice* updates
                if cue_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cue_practice.frameNStart = frameN  # exact frame index
                    cue_practice.tStart = t  # local t and not account for scr refresh
                    cue_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cue_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cue_practice.started')
                    cue_practice.setAutoDraw(True)
                
                # *target_practice* updates
                if target_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_practice.frameNStart = frameN  # exact frame index
                    target_practice.tStart = t  # local t and not account for scr refresh
                    target_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_practice.started')
                    target_practice.setAutoDraw(True)
                
                # *key_practice* updates
                waitOnFlip = False
                if key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_practice.frameNStart = frameN  # exact frame index
                    key_practice.tStart = t  # local t and not account for scr refresh
                    key_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_practice.started')
                    key_practice.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_practice.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_practice.status == STARTED and not waitOnFlip:
                    theseKeys = key_practice.getKeys(keyList=['space'], waitRelease=False)
                    _key_practice_allKeys.extend(theseKeys)
                    if len(_key_practice_allKeys):
                        key_practice.keys = _key_practice_allKeys[-1].name  # just the last key pressed
                        key_practice.rt = _key_practice_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *condition_name* updates
                if condition_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    condition_name.frameNStart = frameN  # exact frame index
                    condition_name.tStart = t  # local t and not account for scr refresh
                    condition_name.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(condition_name, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'condition_name.started')
                    condition_name.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practice_phaseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practice_phase" ---
            for thisComponent in practice_phaseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_practice.keys in ['', [], None]:  # No response was made
                key_practice.keys = None
            practice_phase_trials.addData('key_practice.keys',key_practice.keys)
            if key_practice.keys != None:  # we had a response
                practice_phase_trials.addData('key_practice.rt', key_practice.rt)
            # the Routine "practice_phase" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'practice_phase_trials'
        
    # completed 6.0 repeats of 'practice_phase_cycles'
    
# completed 2.0 repeats of 'practice_phase_blocks'


# --- Prepare to start Routine "distractor" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from distractor_code
# tarefa distratora inicial = 1,5 min
# tarefa distratora final = 10 min
clock = core.CountdownTimer(start = 10)
# keep track of which components have finished
distractorComponents = []
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
    # Run 'Each Frame' code from distractor_code
    timer = int(clock.getTime())
    
    if int(clock.getTime()) <= 0:
        continueRoutine = False
    
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
# the Routine "distractor" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
final_test_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('word_pairs.xlsx'),
    seed=None, name='final_test_trials')
thisExp.addLoop(final_test_trials)  # add the loop to the experiment
thisFinal_test_trial = final_test_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFinal_test_trial.rgb)
if thisFinal_test_trial != None:
    for paramName in thisFinal_test_trial:
        exec('{} = thisFinal_test_trial[paramName]'.format(paramName))

for thisFinal_test_trial in final_test_trials:
    currentLoop = final_test_trials
    # abbreviate parameter names if possible (e.g. rgb = thisFinal_test_trial.rgb)
    if thisFinal_test_trial != None:
        for paramName in thisFinal_test_trial:
            exec('{} = thisFinal_test_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "final_test" ---
    continueRoutine = True
    # update component parameters for each repeat
    cue_final.setText(Portuguese)
    key_final.keys = []
    key_final.rt = []
    _key_final_allKeys = []
    # keep track of which components have finished
    final_testComponents = [cue_final, target_final, key_final]
    for thisComponent in final_testComponents:
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
    
    # --- Run Routine "final_test" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_final* updates
        if cue_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_final.frameNStart = frameN  # exact frame index
            cue_final.tStart = t  # local t and not account for scr refresh
            cue_final.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_final, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_final.started')
            cue_final.setAutoDraw(True)
        
        # *target_final* updates
        if target_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_final.frameNStart = frameN  # exact frame index
            target_final.tStart = t  # local t and not account for scr refresh
            target_final.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_final, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_final.started')
            target_final.setAutoDraw(True)
        
        # *key_final* updates
        waitOnFlip = False
        if key_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_final.frameNStart = frameN  # exact frame index
            key_final.tStart = t  # local t and not account for scr refresh
            key_final.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_final, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_final.started')
            key_final.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_final.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_final.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_final.status == STARTED and not waitOnFlip:
            theseKeys = key_final.getKeys(keyList=['space'], waitRelease=False)
            _key_final_allKeys.extend(theseKeys)
            if len(_key_final_allKeys):
                key_final.keys = _key_final_allKeys[-1].name  # just the last key pressed
                key_final.rt = _key_final_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in final_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "final_test" ---
    for thisComponent in final_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_final.keys in ['', [], None]:  # No response was made
        key_final.keys = None
    final_test_trials.addData('key_final.keys',key_final.keys)
    if key_final.keys != None:  # we had a response
        final_test_trials.addData('key_final.rt', key_final.rt)
    # the Routine "final_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'final_test_trials'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
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
frameN = -1

# --- Run Routine "thanks" ---
while continueRoutine and routineTimer.getTime() < 5.0:
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
    if thanks_msg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks_msg.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            thanks_msg.tStop = t  # not accounting for scr refresh
            thanks_msg.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks_msg.stopped')
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

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine
routineTimer.addTime(-5.000000)
# Run 'End Experiment' code from xxx
'''
resp_display = ""
max_digits = 10

#key logger defaults
last_len = 0
key_list = []

event.clearEvents('keyboard')



current_condition = conditions_part1[practice_trials_part1.thisN]

Inupiaq_cue = ""

if current_condition == "AC": 
    # letras a serem mostradas = 1
    # letras a serem representadas por underscore = 0
    letters = [0] * (5 - practice_cycles_part1.thisN) + [1] * practice_cycles_part1.thisN
    random.shuffle(letters)
          
    for i, letter in enumerate(letters):
        if letter == 0:
            Inupiaq_cue += "_"
        else:
            Inupiaq_cue += Inupiaq[i]

elif current_condition == "DC": 
    # letras a serem mostradas = 1
    # letras a serem representadas por underscore = 0
    letters = [0] * (practice_cycles_part1.thisN) + [1] * (5 - practice_cycles_part1.thisN)
    random.shuffle(letters)
          
    for i, letter in enumerate(letters):
        if letter == 0:
            Inupiaq_cue += "_"
        else:
            Inupiaq_cue += Inupiaq[i]

else:
    Inupiaq_cue = Inupiaq
    
Inupiaq_cue = " ".join(Inupiaq_cue)
        
    
'''

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
