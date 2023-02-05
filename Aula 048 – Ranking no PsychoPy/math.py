#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on fevereiro 05, 2023, at 08:21
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
expName = 'math'  # from the Builder filename that created this script
expInfo = {
    'nome': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['date'], expInfo['nome'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\ranking\\math.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
win.mouseVisible = False
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
# Run 'Begin Experiment' code from welcome_code
import random
from os.path import exists
import time
import copy

if expInfo["nome"] == "":
    expInfo["nome"] = f"random{np.random.randint(low = 1000, high = 10000)}"

# abre arquivo contendo ranking
ranking = open("ranking.csv", "r").readlines()[1:]

# cria listas que armazenará top 5
nicknames = list()
scores = list()

# guarda textos que conterão ranking
nicknames_mytext = """
"""
scores_mytext = """
"""

# separando nicknames e pontuações
for i, position in enumerate(ranking):
    ranking[i] = position.split(",")
    nicknames.append(ranking[i][1])
    scores.append(ranking[i][2])
    
    nicknames_mytext = f"{ranking[i][1]}"
    scores_mytext = f"{ranking[i][2]}"

    if i < len(ranking):
        nicknames_mytext += """
        """
        scores_mytext += """
        """

is_my_score_saved = False

def ranking_update(ranking_name = ranking, nickname = my_nickname, score = my_score):
    new_ranking = list()

    ranking_auxiliar = copy.deepcopy(ranking)

    for i, position in enumerate(ranking_auxiliar):
        
        # se minha pontuação foi maior que a pontuação na posição i   
        if (my_score > int(scores[i])) and (is_my_score_saved == False):
            new_ranking.append(f"{i + 1},{my_nickname},{my_score}\n")
            ranking.pop()
            is_my_score_saved = True

        elif is_my_score_saved:
            new_ranking.append(f"{i + 1},{nicknames[i - 1]},{scores[i - 1]}")

        else:
            new_ranking.append(f"{i + 1},{nicknames[i]},{scores[i]}")

    updated_ranking = open("ranking.csv", "w")
    updated_ranking.write("position,nickname,score\n")

    for position in new_ranking:
        updated_ranking.write(position)

    updated_ranking.close()

welcome_msg = visual.TextStim(win=win, name='welcome_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
welcome_resp = keyboard.Keyboard()

# --- Initialize components for Routine "show_ranking" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.8), height=0.12, wrapWidth=1.8, ori=0, 
    color='orange', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
nicknames_msg = visual.TextStim(win=win, name='nicknames_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(-0.3, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
scores_text = visual.TextStim(win=win, name='scores_text',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.3, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
show_ranking_spacebar = visual.TextStim(win=win, name='show_ranking_spacebar',
    text='Pressione [BARRA DE ESPAÇO] para avançar.',
    font='Times New Roman',
    units='norm', pos=(0, -0.8), height=0.07, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
show_ranking_resp = keyboard.Keyboard()

# --- Initialize components for Routine "distractor" ---
# Run 'Begin Experiment' code from math_code
# contador de número de tentativas na tarefa distratora
my_count = 0

# contador de qual tarefa distratora estamos
distractor_index = 0

# contador de pontos
my_score = 0

math_problem = visual.TextStim(win=win, name='math_problem',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.15), height=0.2, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
math_prompt = visual.TextStim(win=win, name='math_prompt',
    text='Digite sua resposta e tecle [ENTER].',
    font='Times New Roman',
    units='norm', pos=(0, 0.70), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
math_resp = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, 0),units='norm',     letterHeight=0.2,
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
     name='math_resp',
     autoLog=True,
)

# --- Initialize components for Routine "show_ranking" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.8), height=0.12, wrapWidth=1.8, ori=0, 
    color='orange', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
nicknames_msg = visual.TextStim(win=win, name='nicknames_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(-0.3, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
scores_text = visual.TextStim(win=win, name='scores_text',
    text='',
    font='Times New Roman',
    units='norm', pos=(0.3, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
show_ranking_spacebar = visual.TextStim(win=win, name='show_ranking_spacebar',
    text='Pressione [BARRA DE ESPAÇO] para avançar.',
    font='Times New Roman',
    units='norm', pos=(0, -0.8), height=0.07, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
show_ranking_resp = keyboard.Keyboard()

# --- Initialize components for Routine "thanks" ---
thanks_prompt = visual.TextStim(win=win, name='thanks_prompt',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
thanks_spacebar = visual.TextStim(win=win, name='thanks_spacebar',
    text='Pressione [BARRA DE ESPAÇO] para fechar a janela.',
    font='Times New Roman',
    units='norm', pos=(0, -0.8), height=0.07, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
thanks_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
# update component parameters for each repeat
welcome_msg.setText(welcome_txt)
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
# Run 'End Routine' code from welcome_code
thisExp.addData('Código', participant_code)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "show_ranking" ---
continueRoutine = True
# update component parameters for each repeat
feedback_text.setText(feedback)
nicknames_msg.setText(nicknames_text)
scores_text.setText(nicknames_text)
show_ranking_resp.keys = []
show_ranking_resp.rt = []
_show_ranking_resp_allKeys = []
# keep track of which components have finished
show_rankingComponents = [feedback_text, nicknames_msg, scores_text, show_ranking_spacebar, show_ranking_resp]
for thisComponent in show_rankingComponents:
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

# --- Run Routine "show_ranking" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedback_text* updates
    if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_text.frameNStart = frameN  # exact frame index
        feedback_text.tStart = t  # local t and not account for scr refresh
        feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_text.started')
        feedback_text.setAutoDraw(True)
    
    # *nicknames_msg* updates
    if nicknames_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nicknames_msg.frameNStart = frameN  # exact frame index
        nicknames_msg.tStart = t  # local t and not account for scr refresh
        nicknames_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nicknames_msg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'nicknames_msg.started')
        nicknames_msg.setAutoDraw(True)
    
    # *scores_text* updates
    if scores_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scores_text.frameNStart = frameN  # exact frame index
        scores_text.tStart = t  # local t and not account for scr refresh
        scores_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scores_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'scores_text.started')
        scores_text.setAutoDraw(True)
    
    # *show_ranking_spacebar* updates
    if show_ranking_spacebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        show_ranking_spacebar.frameNStart = frameN  # exact frame index
        show_ranking_spacebar.tStart = t  # local t and not account for scr refresh
        show_ranking_spacebar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(show_ranking_spacebar, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'show_ranking_spacebar.started')
        show_ranking_spacebar.setAutoDraw(True)
    
    # *show_ranking_resp* updates
    waitOnFlip = False
    if show_ranking_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        show_ranking_resp.frameNStart = frameN  # exact frame index
        show_ranking_resp.tStart = t  # local t and not account for scr refresh
        show_ranking_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(show_ranking_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'show_ranking_resp.started')
        show_ranking_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(show_ranking_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(show_ranking_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if show_ranking_resp.status == STARTED and not waitOnFlip:
        theseKeys = show_ranking_resp.getKeys(keyList=['space'], waitRelease=False)
        _show_ranking_resp_allKeys.extend(theseKeys)
        if len(_show_ranking_resp_allKeys):
            show_ranking_resp.keys = _show_ranking_resp_allKeys[-1].name  # just the last key pressed
            show_ranking_resp.rt = _show_ranking_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in show_rankingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "show_ranking" ---
for thisComponent in show_rankingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "show_ranking" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
distractor_period = data.TrialHandler(nReps=999, method='random', 
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
    factor1, factor2 = np.random.randint(2, 10), np.random.randint(2, 20) 
    if np.random.random() > 0.5:
        factor1, factor2 = factor2, factor1
    product = factor1 * factor2
    problem = f"Quanto é {factor1} × {factor2}?"
    
    # tamanho máximo da resposta
    max_length = 3
    
    # monitorando teclas pressionadas e tempo
    distractor_clock = core.Clock() # relógio da rotina que monitora tempo
    pressed_keys = list() # lista de teclas pressionadas
    pressed_keys_time = list() # lista de tempo de pressão de cada tecla
    math_problem.setText(problem)
    math_resp.reset()
    # keep track of which components have finished
    distractorComponents = [math_problem, math_prompt, math_resp]
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
        # remove espaços vazios
        math_resp.text = math_resp.text.strip()
        
        if len(math_resp.text) > max_length:
            math_resp.text.strip()[:max_length]
        
        # monitora valor do relógio para que tarefa dure 60 s
        if my_clock.getTime() >= 60:
            # atualiza ranking
            ranking_update(ranking_name = ranking, nickname = expInfo['nome'], score = my_score):
            distractor_period.finished = True # encerra loop
            continueRoutine = False # encerra tentativa
        
        
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
        
        # *math_resp* updates
        if math_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_resp.frameNStart = frameN  # exact frame index
            math_resp.tStart = t  # local t and not account for scr refresh
            math_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'math_resp.started')
            math_resp.setAutoDraw(True)
        
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
    thisExp.addData('Código', participant_code)
    
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
    if (math_resp.text.strip()[:max_length] == str(product)):
        distractor_corr = 1
    else:
        distractor_corr = 0
    
    # salva acerto ou erro no arquivo de saídas
    thisExp.addData("distractor_resp_corr", distractor_corr)
    
    if distractor_period.finished:
        thisExp.addData("my_score", my_score)
        feedback = f"Você fez {my_score} ponto(s)."
    
    
    
    thisExp.addData('math_resp.text',math_resp.text)
    # the Routine "distractor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 999 repeats of 'distractor_period'

# get names of stimulus parameters
if distractor_period.trialList in ([], [None], None):
    params = []
else:
    params = distractor_period.trialList[0].keys()
# save data for this loop
distractor_period.saveAsExcel(filename + '.xlsx', sheetName='distractor_period',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
distractor_period.saveAsText(filename + 'distractor_period.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "show_ranking" ---
continueRoutine = True
# update component parameters for each repeat
feedback_text.setText(feedback)
nicknames_msg.setText(nicknames_text)
scores_text.setText(nicknames_text)
show_ranking_resp.keys = []
show_ranking_resp.rt = []
_show_ranking_resp_allKeys = []
# keep track of which components have finished
show_rankingComponents = [feedback_text, nicknames_msg, scores_text, show_ranking_spacebar, show_ranking_resp]
for thisComponent in show_rankingComponents:
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

# --- Run Routine "show_ranking" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedback_text* updates
    if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_text.frameNStart = frameN  # exact frame index
        feedback_text.tStart = t  # local t and not account for scr refresh
        feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_text.started')
        feedback_text.setAutoDraw(True)
    
    # *nicknames_msg* updates
    if nicknames_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nicknames_msg.frameNStart = frameN  # exact frame index
        nicknames_msg.tStart = t  # local t and not account for scr refresh
        nicknames_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nicknames_msg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'nicknames_msg.started')
        nicknames_msg.setAutoDraw(True)
    
    # *scores_text* updates
    if scores_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scores_text.frameNStart = frameN  # exact frame index
        scores_text.tStart = t  # local t and not account for scr refresh
        scores_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scores_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'scores_text.started')
        scores_text.setAutoDraw(True)
    
    # *show_ranking_spacebar* updates
    if show_ranking_spacebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        show_ranking_spacebar.frameNStart = frameN  # exact frame index
        show_ranking_spacebar.tStart = t  # local t and not account for scr refresh
        show_ranking_spacebar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(show_ranking_spacebar, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'show_ranking_spacebar.started')
        show_ranking_spacebar.setAutoDraw(True)
    
    # *show_ranking_resp* updates
    waitOnFlip = False
    if show_ranking_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        show_ranking_resp.frameNStart = frameN  # exact frame index
        show_ranking_resp.tStart = t  # local t and not account for scr refresh
        show_ranking_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(show_ranking_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'show_ranking_resp.started')
        show_ranking_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(show_ranking_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(show_ranking_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if show_ranking_resp.status == STARTED and not waitOnFlip:
        theseKeys = show_ranking_resp.getKeys(keyList=['space'], waitRelease=False)
        _show_ranking_resp_allKeys.extend(theseKeys)
        if len(_show_ranking_resp_allKeys):
            show_ranking_resp.keys = _show_ranking_resp_allKeys[-1].name  # just the last key pressed
            show_ranking_resp.rt = _show_ranking_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in show_rankingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "show_ranking" ---
for thisComponent in show_rankingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "show_ranking" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "thanks" ---
continueRoutine = True
# update component parameters for each repeat
thanks_prompt.setText(thanks_txt)
thanks_resp.keys = []
thanks_resp.rt = []
_thanks_resp_allKeys = []
# keep track of which components have finished
thanksComponents = [thanks_prompt, thanks_spacebar, thanks_resp]
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
    
    # *thanks_spacebar* updates
    if thanks_spacebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_spacebar.frameNStart = frameN  # exact frame index
        thanks_spacebar.tStart = t  # local t and not account for scr refresh
        thanks_spacebar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_spacebar, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thanks_spacebar.started')
        thanks_spacebar.setAutoDraw(True)
    
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
