#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on janeiro 07, 2023, at 20:53
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
expName = 'aula042'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 042\\aula 042_lastrun.py',
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

# --- Initialize components for Routine "test" ---
# Run 'Begin Experiment' code from code
# variável armazenará string que participante digitou
# e que aparecerá na tela
resp_display = ""


# cria 30 strings inicialmente vazias
# esses valores serão gradativamente substituídos pelas respostas
# dos participantes
responses = [" " * 15 for j in range(6) for i in range (5)]

# define função que passa respostas dos participantes a uma lista
# contendo numeração + respostas
def response_box(responses):

    # criando uma lista vazia de respostas
    word_list = list()
    
    # cada iteração desse loop cria uma coluna de respostas
    # contendo 6 respostas cada
    for i in range(5):
        temp_string = f"""
    {(i * 6) + 1}. {responses[(i * 6) + 0]}
    {(i * 6) + 2}. {responses[(i * 6) + 1]}
    {(i * 6) + 3}. {responses[(i * 6) + 2]}
    {(i * 6) + 4}. {responses[(i * 6) + 3]}
    {(i * 6) + 5}. {responses[(i * 6) + 4]}
    {(i * 6) + 6}. {responses[(i * 6) + 5]}
    """
        word_list.append(temp_string)

    return word_list

# cria combinação numeração + respostas (inicialmente vazias)
word_list = response_box(responses)

# gera prompt da tarefa de recordação livre
test_prompt = "Digite todas as palavras que você se lembra de ter estudado anteriormente. Pressione [BARRA DE ESPAÇO] para confirmar cada resposta"

# inicializa uma variável que será atualizada só quando estivermos na última tentativa
# e ENTER tiver sido pressionado
last_word = False
prompt_resp = visual.TextStim(win=win, name='prompt_resp',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.7), height=0.1, wrapWidth=1.8, ori=0, 
    color='orange', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
target_resp = visual.TextStim(win=win, name='target_resp',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()
response_rect = visual.Rect(
    win=win, name='response_rect',units='norm', 
    width=(1.95, 0.7)[0], height=(1.95, 0.7)[1],
    ori=0.0, pos=(0, -0.60), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
practice_line = visual.Rect(
    win=win, name='practice_line',units='norm', 
    width=(0.9, 0.01)[0], height=(0.9, 0.01)[1],
    ori=0, pos=(0, -0.15), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-5.0, interpolate=True)
column_1 = visual.TextStim(win=win, name='column_1',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.6), height=0.08, wrapWidth=2.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
column_2 = visual.TextStim(win=win, name='column_2',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.375, -0.6), height=0.08, wrapWidth=2.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
column_3 = visual.TextStim(win=win, name='column_3',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.75, -0.6), height=0.08, wrapWidth=2.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
column_4 = visual.TextStim(win=win, name='column_4',
    text='',
    font='Times New Roman',
    units='norm', pos=(1.125, -0.6), height=0.08, wrapWidth=2.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
column_5 = visual.TextStim(win=win, name='column_5',
    text='',
    font='Times New Roman',
    units='norm', pos=(1.5, -0.6), height=0.08, wrapWidth=2.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
debug = visual.TextStim(win=win, name='debug',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.9, 0.9), height=0.08, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

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
    trialList=data.importConditions('palavras.xlsx'),
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
test_phase = data.TrialHandler(nReps=30.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # --- Prepare to start Routine "test" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    # se estamos na primeira palavra
    if test_phase.thisN == 0:
        # inicializa um relógio que controla duração da tarefa
        my_clock = core.Clock()
    
    # definindo alinhamento dos textos à esquerda
    column_1.alignText = 'left'
    column_2.alignText = 'left'
    column_3.alignText = 'left'
    column_4.alignText = 'left'
    column_5.alignText = 'left'
    
    # inicializa variáveis importantes para a rotina
    resp_display = ""
    max_digits = 11
    min_digits = 3
    
    # valores default das teclas pressionadas
    # e comprimento da lista
    last_len = 0
    key_list = []
    
    event.clearEvents('keyboard')
    
    
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    testComponents = [prompt_resp, target_resp, resp, response_rect, practice_line, column_1, column_2, column_3, column_4, column_5, debug]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code
        # se tempo da tarefa s esgotou...
        if my_clock.getTime() >= 60:
            # finaliza loop e rotina
            test_phase.finished = True
            continueRoutine = False
            
        # se uma nova tecla foi pressionada...
        if(len(resp.keys) > last_len):
            
            # incrementa o valor de last_len
            last_len = len(resp.keys)
            
            # e joga o valor mais recente de resp.keys para key_list
            key_list.append(resp.keys.pop())
            
            # se a teclada pressionada foi "5"...
            if("5" in key_list):
                # remove o 5 da lista...
                key_list.remove("5")
                # e, caso estejamos na última tentativa...
                if test_phase.thisN == 29:
                    # finaliza a tarefa por critério de conclusão
                    continueRoutine = False
            
            # se a teclada pressionada foi "5"...
            if("num_5" in key_list):
                # remove o 5 da lista...
                key_list.remove("num_5")
                # e, caso estejamos na última tentativa...
                if test_phase.thisN == 29:
                    # finaliza a tarefa por critério de conclusão
                    continueRoutine = False
        
        
            # se a tecla [<-] foi pressionada...
            if("backspace" in key_list):
                # removemos ela da lista
                key_list.remove("backspace")
        
                # se a resposta atual tinha ao menos um caractere,
                # apagamos o último digitado
                if(len(key_list) > 0):
                    key_list.pop()
        
            # se a tecla [BARRA DE ESPAÇO] foi pressionada...
            elif("space" in key_list):
                # removemos ela da lista...
                key_list.pop()
                # e adicionamos um espaço vazio ao final da string
                key_list.append(" ")
            
            # se a tecla pressionada foi [ENTER]...
            elif("return" in key_list):
                # removemos essa tecla da lista...
                key_list.pop()
                # e atualizamos a lista de palavras que deve aparecer na tela
                responses[test_phase.thisN] = resp_display
                # se ainda não estamos na última tentativa...
                if (test_phase.thisN < 29):
                    # e se nossa resposta é maior ou igual que
                    # o valor mínimo de caracteres aceito como resposta...
                    if (len(key_list) >= min_digits):
                        # finalizamos a rotina
                        continueRoutine = False
                # se estamos na última tentativa...
                else:
                    # invocamos response_box para atualizar
                    # valor da 30a. posição das palavras
                    word_list = response_box(responses)
                    # e mudamos o prompt para o participante
                    test_prompt = "Pressione [ 5 ] para finalizar o teste"
                    # copiamos a lista de teclas pressionadas
                    new_key_list = key_list[:]
                    # e atualizamos o valor de last_word
                    last_word = True
            
            # o que fará com que o participante caia aqui dentro
            if last_word:
                # e que key_list não se modifique mais
                key_list = new_key_list[:]
        
            # se o número de teclas pressionadas é maior que o máximo permitido...
            while(len(key_list) > max_digits):
                # vamos removendo os valores mais recentes
                key_list.pop()
                
            # e, finalmente, criamos a variável que apresentará a resposta
            # momento a momento na tela
            resp_display = ''.join(key_list)
        
        # *prompt_resp* updates
        if prompt_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_resp.frameNStart = frameN  # exact frame index
            prompt_resp.tStart = t  # local t and not account for scr refresh
            prompt_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prompt_resp.started')
            prompt_resp.setAutoDraw(True)
        if prompt_resp.status == STARTED:  # only update if drawing
            prompt_resp.setText(test_prompt, log=False)
        
        # *target_resp* updates
        if target_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_resp.frameNStart = frameN  # exact frame index
            target_resp.tStart = t  # local t and not account for scr refresh
            target_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_resp.started')
            target_resp.setAutoDraw(True)
        if target_resp.status == STARTED:  # only update if drawing
            target_resp.setText(resp_display, log=False)
        
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
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'space', 'backspace', 'return', '5', 'num_5'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = [key.name for key in _resp_allKeys]  # storing all keys
                resp.rt = [key.rt for key in _resp_allKeys]
        
        # *response_rect* updates
        if response_rect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_rect.frameNStart = frameN  # exact frame index
            response_rect.tStart = t  # local t and not account for scr refresh
            response_rect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_rect, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_rect.started')
            response_rect.setAutoDraw(True)
        
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
        
        # *column_1* updates
        if column_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            column_1.frameNStart = frameN  # exact frame index
            column_1.tStart = t  # local t and not account for scr refresh
            column_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(column_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'column_1.started')
            column_1.setAutoDraw(True)
        if column_1.status == STARTED:  # only update if drawing
            column_1.setText(word_list[0], log=False)
        
        # *column_2* updates
        if column_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            column_2.frameNStart = frameN  # exact frame index
            column_2.tStart = t  # local t and not account for scr refresh
            column_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(column_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'column_2.started')
            column_2.setAutoDraw(True)
        if column_2.status == STARTED:  # only update if drawing
            column_2.setText(word_list[1], log=False)
        
        # *column_3* updates
        if column_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            column_3.frameNStart = frameN  # exact frame index
            column_3.tStart = t  # local t and not account for scr refresh
            column_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(column_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'column_3.started')
            column_3.setAutoDraw(True)
        if column_3.status == STARTED:  # only update if drawing
            column_3.setText(word_list[2], log=False)
        
        # *column_4* updates
        if column_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            column_4.frameNStart = frameN  # exact frame index
            column_4.tStart = t  # local t and not account for scr refresh
            column_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(column_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'column_4.started')
            column_4.setAutoDraw(True)
        if column_4.status == STARTED:  # only update if drawing
            column_4.setText(word_list[3], log=False)
        
        # *column_5* updates
        if column_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            column_5.frameNStart = frameN  # exact frame index
            column_5.tStart = t  # local t and not account for scr refresh
            column_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(column_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'column_5.started')
            column_5.setAutoDraw(True)
        if column_5.status == STARTED:  # only update if drawing
            column_5.setText(word_list[4], log=False)
        
        # *debug* updates
        if debug.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debug.frameNStart = frameN  # exact frame index
            debug.tStart = t  # local t and not account for scr refresh
            debug.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debug, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debug.started')
            debug.setAutoDraw(True)
        if debug.status == STARTED:  # only update if drawing
            debug.setText(int(my_clock.getTime()), log=False)
        
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
    # salva a resposta no arquivo .csv
    thisExp.addData('response', resp_display)
    
    # e atualiza word_list para a próxima tentativa
    word_list = response_box(responses)
    
    # print(responses)
    # print(word_list)
    
    
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
    test_phase.addData('resp.keys',resp.keys)
    if resp.keys != None:  # we had a response
        test_phase.addData('resp.rt', resp.rt)
    # the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 30.0 repeats of 'test_phase'

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
