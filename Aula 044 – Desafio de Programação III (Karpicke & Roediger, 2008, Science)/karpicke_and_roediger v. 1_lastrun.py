﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on janeiro 21, 2023, at 19:44
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
    'participant': f"{randint(0, 999999):06.0f}",
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 044\\karpicke_and_roediger v. 1_lastrun.py',
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

# índices de instruções
current_instruction = 0

# lista de instruções
instruction_list = ["instrucoes_11a.jpg","instrucoes_12a.jpg","instrucoes_13a.jpg","instrucoes_14a.jpg","instrucoes_15a.jpg"]




instr_resp = keyboard.Keyboard()
instruction_images = visual.ImageStim(
    win=win,
    name='instruction_images', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

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
import random

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
    text='Pausa. \n\nRespire. Tome uma água. E pressione [BARRA DE ESPAÇO] para prosseguir.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prompt_resp = keyboard.Keyboard()

# --- Initialize components for Routine "test" ---
# Run 'Begin Experiment' code from code
resp_display = ""
cue_test = visual.TextStim(win=win, name='cue_test',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
target_test = visual.TextStim(win=win, name='target_test',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.2), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()
practice_line = visual.Rect(
    win=win, name='practice_line',units='norm', 
    width=(0.7, 0.01)[0], height=(0.7, 0.01)[1],
    ori=0, pos=(0, -0.3), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "thanks" ---
thanks_msg = visual.TextStim(win=win, name='thanks_msg',
    text='Fim da tarefa!\n\nRetorne daqui a 7 dias para a segunda sessão! ☻\n\nPressione [BARRA DE ESPAÇO] para fechar a janela.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
thanks_resp = keyboard.Keyboard()

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
    instr_resp.keys = []
    instr_resp.rt = []
    _instr_resp_allKeys = []
    instruction_images.setImage(instruction_list[current_instruction])
    # keep track of which components have finished
    instructionComponents = [instr_resp, instruction_images]
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
                instr_resp.keys = _instr_resp_allKeys[0].name  # just the first key pressed
                instr_resp.rt = _instr_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # *instruction_images* updates
        if instruction_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_images.frameNStart = frameN  # exact frame index
            instruction_images.tStart = t  # local t and not account for scr refresh
            instruction_images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_images, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_images.started')
            instruction_images.setAutoDraw(True)
        
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
    if instr_resp.keys == "left":
        current_instruction -= 1
    elif instr_resp.keys == "right":
        current_instruction += 1
    
    # Se a instrução atual for -1
    if current_instruction == -1:
        # Resete o valor para ser 0
        current_instruction = 0
    # Se a instrução atual é igual ao comprimento da lista de instruções
    elif current_instruction == len(instruction_list):
        current_instruction = 0 # zera contador de instruções
        instructions.finished = True # e encerra loop de estudo
    # check responses
    if instr_resp.keys in ['', [], None]:  # No response was made
        instr_resp.keys = None
    instructions.addData('instr_resp.keys',instr_resp.keys)
    if instr_resp.keys != None:  # we had a response
        instructions.addData('instr_resp.rt', instr_resp.rt)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'instructions'


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
        trialList=data.importConditions('cycle_1.csv'),
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
        trialList=data.importConditions('cycle_1.csv'),
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
        resp_display = ""
        max_digits = 12
        
        #key logger defaults
        last_len = 0
        key_list = []
        
        event.clearEvents('keyboard')
        
        
        
        cue_test.setText(English)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        testComponents = [cue_test, target_test, resp, practice_line]
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
        while continueRoutine and routineTimer.getTime() < 7.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            #if a new key has been pressed since last time
            if(len(resp.keys) > last_len):
                
                #increment the key logger length
                last_len = len(resp.keys)
                
                #grab the last key added to the keys list
                key_list.append(resp.keys.pop())
            
                #check for backspace
                if("backspace" in key_list):
                    key_list.remove("backspace")
            
                    #if we have at least 1 character, remove it
                    if(len(key_list) > 0):
                        key_list.pop()
            
                # if space is pressed then...
                elif("space" in key_list):
                    #remove the space key
                    key_list.pop()
                
                #if enter is pressed then...
                elif("return" in key_list):
                    #remove the enter key
                    key_list.pop()
            
            
                #now loop through and remove any extra characters that may exist
                while(len(key_list) > max_digits):
                    key_list.pop()
                    
                #create a variable to display
                resp_display = ''.join(key_list)
            
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
                if tThisFlipGlobal > cue_test.tStartRefresh + 7-frameTolerance:
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
                if tThisFlipGlobal > target_test.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    target_test.tStop = t  # not accounting for scr refresh
                    target_test.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_test.stopped')
                    target_test.setAutoDraw(False)
            if target_test.status == STARTED:  # only update if drawing
                target_test.setText(resp_display, log=False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp.stopped')
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'space', 'backspace', 'return'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = [key.name for key in _resp_allKeys]  # storing all keys
                    resp.rt = [key.rt for key in _resp_allKeys]
                    # was this correct?
                    if (resp.keys == str(Portuguese)) or (resp.keys == Portuguese):
                        resp.corr = 1
                    else:
                        resp.corr = 0
            
            # *practice_line* updates
            if practice_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_line.frameNStart = frameN  # exact frame index
                practice_line.tStart = t  # local t and not account for scr refresh
                practice_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_line, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_line.started')
                practice_line.setAutoDraw(True)
            if practice_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_line.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_line.tStop = t  # not accounting for scr refresh
                    practice_line.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_line.stopped')
                    practice_line.setAutoDraw(False)
            
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
        thisExp.addData('response', resp_display)
        
        if resp_display == Portuguese:
            response_corr = 1
        else:
            response_corr = 0
            
        thisExp.addData("response_corr", response_corr)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(Portuguese).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for test_period (TrialHandler)
        test_period.addData('resp.keys',resp.keys)
        test_period.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            test_period.addData('resp.rt', resp.rt)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-7.000000)
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
