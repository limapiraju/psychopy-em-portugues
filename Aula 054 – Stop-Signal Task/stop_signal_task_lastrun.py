#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on September 12, 2024, at 09:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.1')


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

# Run 'Before Experiment' code from instr_code


# Run 'Before Experiment' code from instr_code




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'session1'  # from the Builder filename that created this script
expInfo = {
    'ID': f"{randint(1, 999999999):06.0f}",
    'Nome Completo': '',
    'E-mail': '',
    'Telefone': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['ID'].zfill(9), expInfo['date'], expInfo['Nome Completo'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 054 – Stop-Signal Task\\stop_signal_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
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
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "welcome" ---
welcome_msg = visual.TextStim(win=win, name='welcome_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_next = visual.ImageStim(
    win=win,
    name='welcome_next', units='norm', 
    image='next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
welcome_resp = event.Mouse(win=win)
x, y = [None, None]
welcome_resp.mouseClock = core.Clock()

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
# lista de instruções
instruction_list = ["""
Nesta tarefa, você deve responder o mais rápido que você puder a uma seta apontando para a esquerda ou para a direita. Use as teclas [←] e [→].

Você terá somente 1 segundo, o que é bem pouco tempo. Então você deve dedicar toda a sua atenção para a realização dessa tarefa.

No primeiro bloco, você treinará um pouco para responder rápido. O bloco terminará apenas quando você acertar pelo menos 20 tentativas consecutivas. O treinamento continuará até que você consiga atingir esse critério (ou se você tiver feito 50 tentativas).""",
"""
Se você chegou até aqui, então você conseguiu realizar a tarefa adequadamente. Parabéns!

Mas essa foi a parte fácil. Agora, você seguirá fazendo a mesma tarefa. No entanto, quando você ouvir um som, você NÃO DEVE RESPONDER. Esse som é um sinal de parada, ou seja, um indicativo de que você deve deixar de dar uma resposta naquela tentativa.

Pressione [BARRA DE ESPAÇO] para iniciar a tarefa."""]

idx = 0


# primeiro nome do participante
if expInfo["Nome Completo"] == "":
    first_name = "participante"
else:
    first_name = expInfo["Nome Completo"].strip().split()[0].title()

welcome_txt = f"""Olá, {first_name}! 

Agradecemos sua disponibilidade em colaborar com nossa pesquisa!

Clique em [Avançar] para iniciar."""

thanks_txt = f"""Esta atividade acabou, {first_name}.

Favor chamar o pesquisador! ☺"""

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from trial_code
# monitora se participante acertou 20 seguidas na prática
consecutive_correct = 0

# monitora se participante passou no critério e, portanto
# fará o teste
instruction_reps = testing_trials_reps = 0


circle = visual.ShapeStim(
    win=win, name='circle',units='height', 
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=1.0, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
arrow = visual.ImageStim(
    win=win,
    name='arrow', units='norm', 
    image='arrow.png', mask=None, anchor='center',
    ori=1.0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
resp = keyboard.Keyboard()
stop_signal_tone = sound.Sound('A', secs=0.15, stereo=True, hamming=True,
    name='stop_signal_tone')
stop_signal_tone.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
circle_fb = visual.ShapeStim(
    win=win, name='circle_fb',units='height', 
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
msg_fb = visual.TextStim(win=win, name='msg_fb',
    text='',
    font='Arial',
    units='norm', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "instruction" ---
# Run 'Begin Experiment' code from instr_code
# lista de instruções
instruction_list = ["""
Nesta tarefa, você deve responder o mais rápido que você puder a uma seta apontando para a esquerda ou para a direita. Use as teclas [←] e [→].

Você terá somente 1 segundo, o que é bem pouco tempo. Então você deve dedicar toda a sua atenção para a realização dessa tarefa.

No primeiro bloco, você treinará um pouco para responder rápido. O bloco terminará apenas quando você acertar pelo menos 20 tentativas consecutivas. O treinamento continuará até que você consiga atingir esse critério (ou se você tiver feito 50 tentativas).""",
"""
Se você chegou até aqui, então você conseguiu realizar a tarefa adequadamente. Parabéns!

Mas essa foi a parte fácil. Agora, você seguirá fazendo a mesma tarefa. No entanto, quando você ouvir um som, você NÃO DEVE RESPONDER. Esse som é um sinal de parada, ou seja, um indicativo de que você deve deixar de dar uma resposta naquela tentativa.

Pressione [BARRA DE ESPAÇO] para iniciar a tarefa."""]

idx = 0


# primeiro nome do participante
if expInfo["Nome Completo"] == "":
    first_name = "participante"
else:
    first_name = expInfo["Nome Completo"].strip().split()[0].title()

welcome_txt = f"""Olá, {first_name}! 

Agradecemos sua disponibilidade em colaborar com nossa pesquisa!

Clique em [Avançar] para iniciar."""

thanks_txt = f"""Esta atividade acabou, {first_name}.

Favor chamar o pesquisador! ☺"""

instr_msg = visual.TextStim(win=win, name='instr_msg',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.2), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from trial_code
# monitora se participante acertou 20 seguidas na prática
consecutive_correct = 0

# monitora se participante passou no critério e, portanto
# fará o teste
instruction_reps = testing_trials_reps = 0


circle = visual.ShapeStim(
    win=win, name='circle',units='height', 
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=1.0, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
arrow = visual.ImageStim(
    win=win,
    name='arrow', units='norm', 
    image='arrow.png', mask=None, anchor='center',
    ori=1.0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
resp = keyboard.Keyboard()
stop_signal_tone = sound.Sound('A', secs=0.15, stereo=True, hamming=True,
    name='stop_signal_tone')
stop_signal_tone.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
circle_fb = visual.ShapeStim(
    win=win, name='circle_fb',units='height', 
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
msg_fb = visual.TextStim(win=win, name='msg_fb',
    text='',
    font='Arial',
    units='norm', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

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
# setup some python lists for storing info about the welcome_resp
welcome_resp.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
welcomeComponents = [welcome_msg, welcome_next, welcome_resp]
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
    
    # *welcome_next* updates
    if welcome_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_next.frameNStart = frameN  # exact frame index
        welcome_next.tStart = t  # local t and not account for scr refresh
        welcome_next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_next, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_next.started')
        welcome_next.setAutoDraw(True)
    # *welcome_resp* updates
    if welcome_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('welcome_resp.started', t)
        welcome_resp.status = STARTED
        welcome_resp.mouseClock.reset()
        prevButtonState = welcome_resp.getPressed()  # if button is down already this ISN'T a new click
    if welcome_resp.status == STARTED:  # only update if started and not finished!
        buttons = welcome_resp.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(welcome_next)
                    clickableList = welcome_next
                except:
                    clickableList = [welcome_next]
                for obj in clickableList:
                    if obj.contains(welcome_resp):
                        gotValidClick = True
                        welcome_resp.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
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
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction" ---
continueRoutine = True
# update component parameters for each repeat
instr_msg.setText(instruction_list[idx])
instr_resp.keys = []
instr_resp.rt = []
_instr_resp_allKeys = []
# keep track of which components have finished
instructionComponents = [instr_msg, instr_resp]
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
idx += 1
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=50.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trial_code
    border_color = "white"
    feedback_msg = ""
    feedback_type = "no feedback"
    fixation_cross_size = 0
    
    # define se a seta estará orientada para a esquerda
    if random() > 0.5:
        ori = 0
    # ou para a direita
    else:
        ori = 180
        
    try:
        # se já estamos no teste
        if testing_trials.thisN >= 0:
            # em ~25% das tentativas, defina-a como stop trials
            if random() < 0.25:
                # quando o som começa, em ms (em relação ao início da seta)
                sound_onset = randchoice([0, .100, .200, .300, .400])
                # volume do som
                volume = 30
                # explicita que a tentativa é stop trial
                trial = "stop"
                # a resposta correta é não responder (None)
                corr_resp = None
            # caso contrário, estamos numa no-stop trial
            else:
                # define o início do tom como 0
                sound_onset = 0
                # define volume 0 (efetivamente, participante não ouve o stop signal)
                volume = 0
                # explicita que a tentativa é no-stop trial
                trial = "no-stop"
                # se a orientação é 0, resposta correta é esquerda
                if ori == 0:
                    corr_resp = "left"
                # caso contrário, orientação é 180 e resposta correta é direita
                else:
                    corr_resp = "right"
    # tratamento de exceção se aplica se ainda estou na fase de prática  
    except:
        # define o início do tom como 0
        sound_onset = 0
        # define volume 0 (efetivamente, participante não ouve o stop signal)
        volume = 0
        # explicita que a tentativa é no-stop trial
        trial = "no-stop"
        # se a orientação é 0, resposta correta é esquerda
        if ori == 0:
            corr_resp = "left"
        # caso contrário, orientação é 180 e resposta correta é direita    
        else:
            corr_resp = "right"      
    circle.setLineColor(border_color)
    arrow.setOri(ori)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    stop_signal_tone.setSound('B', secs=0.15, hamming=True)
    stop_signal_tone.setVolume(volume, log=False)
    # keep track of which components have finished
    trialComponents = [circle, fixation_cross, arrow, resp, stop_signal_tone]
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
        # Run 'Each Frame' code from trial_code
        # variável t representa o tempo transcorrido na presente rotina
        # logo, o tamanho da cruz de fixação será proporcional à passagem
        # do tempo (y = ax + b OU tamanho = a * tempo + constante)
        fixation_cross_size = 1 * t
        
        
        
        
        
        # *circle* updates
        if circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle.frameNStart = frameN  # exact frame index
            circle.tStart = t  # local t and not account for scr refresh
            circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle.started')
            circle.setAutoDraw(True)
        if circle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle.tStartRefresh + 0.90-frameTolerance:
                # keep track of stop time/frame for later
                circle.tStop = t  # not accounting for scr refresh
                circle.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle.stopped')
                circle.setAutoDraw(False)
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross.started')
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                fixation_cross.setAutoDraw(False)
        if fixation_cross.status == STARTED:  # only update if drawing
            fixation_cross.setHeight(fixation_cross_size, log=False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'arrow.started')
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow.tStartRefresh + 0.55-frameTolerance:
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arrow.stopped')
                arrow.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
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
            if tThisFlipGlobal > resp.tStartRefresh + 0.55-frameTolerance:
                # keep track of stop time/frame for later
                resp.tStop = t  # not accounting for scr refresh
                resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp.stopped')
                resp.status = FINISHED
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[0].name  # just the first key pressed
                resp.rt = _resp_allKeys[0].rt
                # was this correct?
                if (resp.keys == str(corr_resp)) or (resp.keys == corr_resp):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop stop_signal_tone
        if stop_signal_tone.status == NOT_STARTED and tThisFlip >= sound_onset + 0.35-frameTolerance:
            # keep track of start time/frame for later
            stop_signal_tone.frameNStart = frameN  # exact frame index
            stop_signal_tone.tStart = t  # local t and not account for scr refresh
            stop_signal_tone.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('stop_signal_tone.started', tThisFlipGlobal)
            stop_signal_tone.play(when=win)  # sync with win flip
        if stop_signal_tone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_signal_tone.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                stop_signal_tone.tStop = t  # not accounting for scr refresh
                stop_signal_tone.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stop_signal_tone.stopped')
                stop_signal_tone.stop()
        
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
    # se o participante errou...
    if resp.corr == 0:
        # o loop de feedback DEVE acontecer
        feedback_loop = 1
        # reseta número de acertos consecutivos
        consecutive_correct = 0
        # se o participante cometeu um erro de "COMISSÃO"
        if resp.keys:
            # ...quando ele não deveria responder
            if corr_resp is None:
                feedback_msg = "NÃO\nRESPONDA"
                feedback_type = "comission"
                border_color = "red"
            # ...quando a resposta era o oposto do respondido
            else:    
                feedback_msg = "RESPOSTA\nERRADA"
                feedback_type = "wrong answer"
                border_color = "yellow"
        # se o participante cometeu um erro de OMISSÃO
        elif resp.keys not in ["left", "right"]:
            feedback_msg = "VOCÊ\nDEVERIA\nTER\nRESPONDIDO"
            feedback_type = "omission"
            border_color = [-0.6235, 0.9608, -1.0000] # verde
    # se o participante acertou...
    else:
        # o loop não deve acontecer
        feedback_loop = 0
        # e o contador de acertos incrementa
        consecutive_correct += 1
        # monitora se o número de acertos é igual a 20
        if consecutive_correct == 20:
            instruction_reps = 1
            testing_trials_reps = 1000
            practice_trials.finished = True
    
    # salva algumas variáveis
    thisExp.addData("trial", trial)
    # SOA = stimulus onset asyncrony
    thisExp.addData("sound_onset", sound_onset)
    thisExp.addData("corr_resp", corr_resp)
    thisExp.addData("consecutive_correct", consecutive_correct)
    thisExp.addData("feedback_type", feedback_type)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('resp.keys',resp.keys)
    practice_trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        practice_trials.addData('resp.rt', resp.rt)
    stop_signal_tone.stop()  # ensure sound has stopped at end of routine
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    feedback_trial = data.TrialHandler(nReps=feedback_loop, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='feedback_trial')
    thisExp.addLoop(feedback_trial)  # add the loop to the experiment
    thisFeedback_trial = feedback_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedback_trial.rgb)
    if thisFeedback_trial != None:
        for paramName in thisFeedback_trial:
            exec('{} = thisFeedback_trial[paramName]'.format(paramName))
    
    for thisFeedback_trial in feedback_trial:
        currentLoop = feedback_trial
        # abbreviate parameter names if possible (e.g. rgb = thisFeedback_trial.rgb)
        if thisFeedback_trial != None:
            for paramName in thisFeedback_trial:
                exec('{} = thisFeedback_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        circle_fb.setFillColor('black')
        circle_fb.setLineColor(border_color)
        msg_fb.setColor(border_color, colorSpace='rgb')
        msg_fb.setText(feedback_msg)
        # keep track of which components have finished
        feedbackComponents = [circle_fb, msg_fb]
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
        frameN = -1
        
        # --- Run Routine "feedback" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *circle_fb* updates
            if circle_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_fb.frameNStart = frameN  # exact frame index
                circle_fb.tStart = t  # local t and not account for scr refresh
                circle_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_fb.started')
                circle_fb.setAutoDraw(True)
            if circle_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_fb.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_fb.tStop = t  # not accounting for scr refresh
                    circle_fb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_fb.stopped')
                    circle_fb.setAutoDraw(False)
            
            # *msg_fb* updates
            if msg_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                msg_fb.frameNStart = frameN  # exact frame index
                msg_fb.tStart = t  # local t and not account for scr refresh
                msg_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_fb.started')
                msg_fb.setAutoDraw(True)
            if msg_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_fb.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_fb.tStop = t  # not accounting for scr refresh
                    msg_fb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_fb.stopped')
                    msg_fb.setAutoDraw(False)
            
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
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-0.500000)
    # completed feedback_loop repeats of 'feedback_trial'
    
    thisExp.nextEntry()
    
# completed 50.0 repeats of 'practice_trials'


# set up handler to look after randomisation of conditions etc
instruction_trial = data.TrialHandler(nReps=instruction_reps, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instruction_trial')
thisExp.addLoop(instruction_trial)  # add the loop to the experiment
thisInstruction_trial = instruction_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction_trial.rgb)
if thisInstruction_trial != None:
    for paramName in thisInstruction_trial:
        exec('{} = thisInstruction_trial[paramName]'.format(paramName))

for thisInstruction_trial in instruction_trial:
    currentLoop = instruction_trial
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction_trial.rgb)
    if thisInstruction_trial != None:
        for paramName in thisInstruction_trial:
            exec('{} = thisInstruction_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    instr_msg.setText(instruction_list[idx])
    instr_resp.keys = []
    instr_resp.rt = []
    _instr_resp_allKeys = []
    # keep track of which components have finished
    instructionComponents = [instr_msg, instr_resp]
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
    idx += 1
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed instruction_reps repeats of 'instruction_trial'


# set up handler to look after randomisation of conditions etc
testing_trials = data.TrialHandler(nReps=testing_trials_reps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='testing_trials')
thisExp.addLoop(testing_trials)  # add the loop to the experiment
thisTesting_trial = testing_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTesting_trial.rgb)
if thisTesting_trial != None:
    for paramName in thisTesting_trial:
        exec('{} = thisTesting_trial[paramName]'.format(paramName))

for thisTesting_trial in testing_trials:
    currentLoop = testing_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTesting_trial.rgb)
    if thisTesting_trial != None:
        for paramName in thisTesting_trial:
            exec('{} = thisTesting_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trial_code
    border_color = "white"
    feedback_msg = ""
    feedback_type = "no feedback"
    fixation_cross_size = 0
    
    # define se a seta estará orientada para a esquerda
    if random() > 0.5:
        ori = 0
    # ou para a direita
    else:
        ori = 180
        
    try:
        # se já estamos no teste
        if testing_trials.thisN >= 0:
            # em ~25% das tentativas, defina-a como stop trials
            if random() < 0.25:
                # quando o som começa, em ms (em relação ao início da seta)
                sound_onset = randchoice([0, .100, .200, .300, .400])
                # volume do som
                volume = 30
                # explicita que a tentativa é stop trial
                trial = "stop"
                # a resposta correta é não responder (None)
                corr_resp = None
            # caso contrário, estamos numa no-stop trial
            else:
                # define o início do tom como 0
                sound_onset = 0
                # define volume 0 (efetivamente, participante não ouve o stop signal)
                volume = 0
                # explicita que a tentativa é no-stop trial
                trial = "no-stop"
                # se a orientação é 0, resposta correta é esquerda
                if ori == 0:
                    corr_resp = "left"
                # caso contrário, orientação é 180 e resposta correta é direita
                else:
                    corr_resp = "right"
    # tratamento de exceção se aplica se ainda estou na fase de prática  
    except:
        # define o início do tom como 0
        sound_onset = 0
        # define volume 0 (efetivamente, participante não ouve o stop signal)
        volume = 0
        # explicita que a tentativa é no-stop trial
        trial = "no-stop"
        # se a orientação é 0, resposta correta é esquerda
        if ori == 0:
            corr_resp = "left"
        # caso contrário, orientação é 180 e resposta correta é direita    
        else:
            corr_resp = "right"      
    circle.setLineColor(border_color)
    arrow.setOri(ori)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    stop_signal_tone.setSound('B', secs=0.15, hamming=True)
    stop_signal_tone.setVolume(volume, log=False)
    # keep track of which components have finished
    trialComponents = [circle, fixation_cross, arrow, resp, stop_signal_tone]
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
        # Run 'Each Frame' code from trial_code
        # variável t representa o tempo transcorrido na presente rotina
        # logo, o tamanho da cruz de fixação será proporcional à passagem
        # do tempo (y = ax + b OU tamanho = a * tempo + constante)
        fixation_cross_size = 1 * t
        
        
        
        
        
        # *circle* updates
        if circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle.frameNStart = frameN  # exact frame index
            circle.tStart = t  # local t and not account for scr refresh
            circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle.started')
            circle.setAutoDraw(True)
        if circle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle.tStartRefresh + 0.90-frameTolerance:
                # keep track of stop time/frame for later
                circle.tStop = t  # not accounting for scr refresh
                circle.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle.stopped')
                circle.setAutoDraw(False)
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross.started')
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                fixation_cross.setAutoDraw(False)
        if fixation_cross.status == STARTED:  # only update if drawing
            fixation_cross.setHeight(fixation_cross_size, log=False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'arrow.started')
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow.tStartRefresh + 0.55-frameTolerance:
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arrow.stopped')
                arrow.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
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
            if tThisFlipGlobal > resp.tStartRefresh + 0.55-frameTolerance:
                # keep track of stop time/frame for later
                resp.tStop = t  # not accounting for scr refresh
                resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp.stopped')
                resp.status = FINISHED
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[0].name  # just the first key pressed
                resp.rt = _resp_allKeys[0].rt
                # was this correct?
                if (resp.keys == str(corr_resp)) or (resp.keys == corr_resp):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop stop_signal_tone
        if stop_signal_tone.status == NOT_STARTED and tThisFlip >= sound_onset + 0.35-frameTolerance:
            # keep track of start time/frame for later
            stop_signal_tone.frameNStart = frameN  # exact frame index
            stop_signal_tone.tStart = t  # local t and not account for scr refresh
            stop_signal_tone.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('stop_signal_tone.started', tThisFlipGlobal)
            stop_signal_tone.play(when=win)  # sync with win flip
        if stop_signal_tone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_signal_tone.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                stop_signal_tone.tStop = t  # not accounting for scr refresh
                stop_signal_tone.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stop_signal_tone.stopped')
                stop_signal_tone.stop()
        
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
    # se o participante errou...
    if resp.corr == 0:
        # o loop de feedback DEVE acontecer
        feedback_loop = 1
        # reseta número de acertos consecutivos
        consecutive_correct = 0
        # se o participante cometeu um erro de "COMISSÃO"
        if resp.keys:
            # ...quando ele não deveria responder
            if corr_resp is None:
                feedback_msg = "NÃO\nRESPONDA"
                feedback_type = "comission"
                border_color = "red"
            # ...quando a resposta era o oposto do respondido
            else:    
                feedback_msg = "RESPOSTA\nERRADA"
                feedback_type = "wrong answer"
                border_color = "yellow"
        # se o participante cometeu um erro de OMISSÃO
        elif resp.keys not in ["left", "right"]:
            feedback_msg = "VOCÊ\nDEVERIA\nTER\nRESPONDIDO"
            feedback_type = "omission"
            border_color = [-0.6235, 0.9608, -1.0000] # verde
    # se o participante acertou...
    else:
        # o loop não deve acontecer
        feedback_loop = 0
        # e o contador de acertos incrementa
        consecutive_correct += 1
        # monitora se o número de acertos é igual a 20
        if consecutive_correct == 20:
            instruction_reps = 1
            testing_trials_reps = 1000
            practice_trials.finished = True
    
    # salva algumas variáveis
    thisExp.addData("trial", trial)
    # SOA = stimulus onset asyncrony
    thisExp.addData("sound_onset", sound_onset)
    thisExp.addData("corr_resp", corr_resp)
    thisExp.addData("consecutive_correct", consecutive_correct)
    thisExp.addData("feedback_type", feedback_type)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for testing_trials (TrialHandler)
    testing_trials.addData('resp.keys',resp.keys)
    testing_trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        testing_trials.addData('resp.rt', resp.rt)
    stop_signal_tone.stop()  # ensure sound has stopped at end of routine
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    feedback_testing_trial = data.TrialHandler(nReps=feedback_loop, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='feedback_testing_trial')
    thisExp.addLoop(feedback_testing_trial)  # add the loop to the experiment
    thisFeedback_testing_trial = feedback_testing_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedback_testing_trial.rgb)
    if thisFeedback_testing_trial != None:
        for paramName in thisFeedback_testing_trial:
            exec('{} = thisFeedback_testing_trial[paramName]'.format(paramName))
    
    for thisFeedback_testing_trial in feedback_testing_trial:
        currentLoop = feedback_testing_trial
        # abbreviate parameter names if possible (e.g. rgb = thisFeedback_testing_trial.rgb)
        if thisFeedback_testing_trial != None:
            for paramName in thisFeedback_testing_trial:
                exec('{} = thisFeedback_testing_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        circle_fb.setFillColor('black')
        circle_fb.setLineColor(border_color)
        msg_fb.setColor(border_color, colorSpace='rgb')
        msg_fb.setText(feedback_msg)
        # keep track of which components have finished
        feedbackComponents = [circle_fb, msg_fb]
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
        frameN = -1
        
        # --- Run Routine "feedback" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *circle_fb* updates
            if circle_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_fb.frameNStart = frameN  # exact frame index
                circle_fb.tStart = t  # local t and not account for scr refresh
                circle_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_fb.started')
                circle_fb.setAutoDraw(True)
            if circle_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_fb.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_fb.tStop = t  # not accounting for scr refresh
                    circle_fb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_fb.stopped')
                    circle_fb.setAutoDraw(False)
            
            # *msg_fb* updates
            if msg_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                msg_fb.frameNStart = frameN  # exact frame index
                msg_fb.tStart = t  # local t and not account for scr refresh
                msg_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msg_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_fb.started')
                msg_fb.setAutoDraw(True)
            if msg_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msg_fb.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    msg_fb.tStop = t  # not accounting for scr refresh
                    msg_fb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msg_fb.stopped')
                    msg_fb.setAutoDraw(False)
            
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
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-0.500000)
    # completed feedback_loop repeats of 'feedback_testing_trial'
    
    thisExp.nextEntry()
    
# completed testing_trials_reps repeats of 'testing_trials'


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
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
