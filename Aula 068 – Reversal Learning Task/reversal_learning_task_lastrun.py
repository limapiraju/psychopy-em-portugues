#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.5),
    on junho 27, 2025, at 22:26
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from initial_instr_code


# Run 'Before Experiment' code from code
def gerar_reforcos(n_trials=150):
    """
    Gera reforços com proporção de 0.75 (3 em 4 tentativas recebem reforço positivo)
    """
    reforcos = []
    n_blocos = n_trials // 4
    sobra = n_trials % 4

    for _ in range(n_blocos):
        bloco = [True, True, True, False]
        np.random.shuffle(bloco)
        reforcos.extend(bloco)

    if sobra > 0:
        resto_pool = [True, True, False, False]
        np.random.shuffle(resto_pool)
        reforcos.extend(resto_pool[:sobra])

    return reforcos

reforcos = gerar_reforcos()
print(len(reforcos))

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.5'
expName = 'reversal_learning_task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [900, 600]
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 068 – Reversal Learning Task\\reversal_learning_task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'norm'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = True
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('instr_initial_resp') is None:
        # initialise instr_initial_resp
        instr_initial_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_initial_resp',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('thanks_resp') is None:
        # initialise thanks_resp
        thanks_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='thanks_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instruction" ---
    # Run 'Begin Experiment' code from initial_instr_code
    # lista de instruções
    initial_instruction_list = ["instructions\practice_instruction_01.jpg",
                                "instructions\practice_instruction_02.jpg", 
                                "instructions\practice_instruction_03.jpg",
                                "instructions\practice_instruction_04.jpg", 
                                "instructions\practice_instruction_05.jpg", 
                                "instructions\practice_instruction_06.jpg",
                                "instructions\practice_instruction_07.jpg", 
                                "instructions\practice_instruction_08.jpg", 
                                "instructions\practice_instruction_09.jpg",
                                "instructions\practice_instruction_10.jpg", 
                                "instructions\practice_instruction_11.jpg", 
                                "instructions\practice_instruction_12.jpg",
                                "instructions\practice_instruction_13.jpg", 
                                "instructions\practice_instruction_18.jpg", 
                                "instructions\practice_instruction_19.jpg"]
    
    current_index = 0
    
    # BEGIN EXPERIMENT
    ausencias_consecutivas = 0
    ausencias_totais = 0
    
    
    instr_initial_resp = keyboard.Keyboard(deviceName='instr_initial_resp')
    initial_instruction_images = visual.ImageStim(
        win=win,
        name='initial_instruction_images', units='norm', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code
    # inicializa variáveis
    x_pos = score = 0
    point_msg = ""
    
    # define alvo inicial
    if random() > 0.5:
        target = r"images\fractal1.jpg"
    else:
        target = r"images\fractal2.jpg"
    
    
    def switching(length = 150, n_switches = 9, intervalo_min = 12, intervalo_max = 18):
        assert intervalo_min * n_switches <= length <= intervalo_max * n_switches, "Impossível encaixar os switches."
    
        while True:
            # Amostra os primeiros n_switches - 1 intervalos
            primeiros = np.random.randint(intervalo_min, intervalo_max + 1, size=n_switches - 1)
            soma_parcial = primeiros.sum()
            ultimo = length - soma_parcial
    
            # Verifica se o último intervalo cabe
            if intervalo_min <= ultimo <= intervalo_max:
                intervalos = list(primeiros) + [ultimo]
                break
    
        cumulativos = np.cumsum(intervalos)
        switch = [False] * length
        for i in cumulativos:
            switch[i - 1] = True
    
        return switch
    
    # monitora mudanças
    switches = switching()
    fixation = visual.TextStim(win=win, name='fixation',
        text='+',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    polygon = visual.Rect(
        win=win, name='polygon',units='norm', 
        width=(0.7, 0.7)[0], height=(0.7, 0.7)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=6.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
        opacity=1.0, depth=-2.0, interpolate=True)
    stim_left = visual.ImageStim(
        win=win,
        name='stim_left', units='norm', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.7, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    stim_right = visual.ImageStim(
        win=win,
        name='stim_right', units='norm', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.7, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "trial_feedback" ---
    point_feedback = visual.TextStim(win=win, name='point_feedback',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "cumulative_score" ---
    cum_score_title = visual.TextStim(win=win, name='cum_score_title',
        text='Pontuação Acumulada',
        font='Times New Roman',
        units='norm', pos=(0, 0.8), height=0.2, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    cum_score = visual.TextStim(win=win, name='cum_score',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "thanks" ---
    thanks_msg = visual.TextStim(win=win, name='thanks_msg',
        text='Fim do experimento!\n\nObrigado por sua participação!\n\nPressione [BARRA DE ESPAÇO] para fechar a janela.',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    thanks_resp = keyboard.Keyboard(deviceName='thanks_resp')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # set up handler to look after randomisation of conditions etc
    instructions = data.TrialHandler(nReps=9999.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instructions')
    thisExp.addLoop(instructions)  # add the loop to the experiment
    thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            globals()[paramName] = thisInstruction[paramName]
    
    for thisInstruction in instructions:
        currentLoop = instructions
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
        if thisInstruction != None:
            for paramName in thisInstruction:
                globals()[paramName] = thisInstruction[paramName]
        
        # --- Prepare to start Routine "instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instruction.started', globalClock.getTime(format='float'))
        # create starting attributes for instr_initial_resp
        instr_initial_resp.keys = []
        instr_initial_resp.rt = []
        _instr_initial_resp_allKeys = []
        initial_instruction_images.setImage(initial_instruction_list[current_index])
        # keep track of which components have finished
        instructionComponents = [instr_initial_resp, initial_instruction_images]
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
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instr_initial_resp* updates
            waitOnFlip = False
            
            # if instr_initial_resp is starting this frame...
            if instr_initial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr_initial_resp.frameNStart = frameN  # exact frame index
                instr_initial_resp.tStart = t  # local t and not account for scr refresh
                instr_initial_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_initial_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instr_initial_resp.started')
                # update status
                instr_initial_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(instr_initial_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(instr_initial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if instr_initial_resp.status == STARTED and not waitOnFlip:
                theseKeys = instr_initial_resp.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _instr_initial_resp_allKeys.extend(theseKeys)
                if len(_instr_initial_resp_allKeys):
                    instr_initial_resp.keys = _instr_initial_resp_allKeys[0].name  # just the first key pressed
                    instr_initial_resp.rt = _instr_initial_resp_allKeys[0].rt
                    instr_initial_resp.duration = _instr_initial_resp_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *initial_instruction_images* updates
            
            # if initial_instruction_images is starting this frame...
            if initial_instruction_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                initial_instruction_images.frameNStart = frameN  # exact frame index
                initial_instruction_images.tStart = t  # local t and not account for scr refresh
                initial_instruction_images.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(initial_instruction_images, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initial_instruction_images.started')
                # update status
                initial_instruction_images.status = STARTED
                initial_instruction_images.setAutoDraw(True)
            
            # if initial_instruction_images is active this frame...
            if initial_instruction_images.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
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
        thisExp.addData('instruction.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from initial_instr_code
        if instr_initial_resp.keys == "left":
            current_index -= 1
        elif instr_initial_resp.keys == "right":
            current_index += 1
        
        # Se a instrução atual for -1
        if current_index == -1:
            # Resete o valor para ser 0
            current_index = 0
        # Se a instrução atual é igual ao comprimento da lista de instruções
        elif current_index == len(initial_instruction_list):
            instructions.finished = True
        
        # check responses
        if instr_initial_resp.keys in ['', [], None]:  # No response was made
            instr_initial_resp.keys = None
        instructions.addData('instr_initial_resp.keys',instr_initial_resp.keys)
        if instr_initial_resp.keys != None:  # we had a response
            instructions.addData('instr_initial_resp.rt', instr_initial_resp.rt)
            instructions.addData('instr_initial_resp.duration', instr_initial_resp.duration)
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 9999.0 repeats of 'instructions'
    
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=150.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        # corr_target → Resposta "correta" teórica
        # imagem_reforcada → Imagem que será reforçada neste trial
        # corr → Resposta correta do ponto de vista comportamental
        
        opa = 0
        
        # monitora mudança de alvo
        if switches[trials.thisN]:
            target = r"images\fractal2.jpg" if target == r"images\fractal1.jpg" else r"images\fractal1.jpg"
        
        # define posição dos estímulos (randomização esquerda/direita)
        if random() > 0.5:
            fractal_left, fractal_right = r"images\fractal1.jpg", r"images\fractal2.jpg"
        else:
            fractal_left, fractal_right = r"images\fractal2.jpg", r"images\fractal1.jpg"
        
        # define reforço deste trial
        reforco_aplicado = reforcos[trials.thisN]
        
        # define qual imagem está sendo reforçada
        if reforco_aplicado:
            imagem_reforcada = target
        else:
            imagem_reforcada = fractal_left if target == fractal_right else fractal_right
        
        # define qual tecla está associada à imagem reforçada
        if imagem_reforcada == fractal_left:
            corr = "left"
        else:
            corr = "right"
        
        # (opcional) define qual seria a resposta correta se o target fosse determinístico
        if target == fractal_left:
            corr_target = "left"
        else:
            corr_target = "right"
            
        debug_info = (
            f"Trial: {trials.thisN + 1}\n"
            f"Target image: {target}\n"
            f"Fractal left: {fractal_left}\n"
            f"Fractal right: {fractal_right}\n"
            f"Switch trial: {switches[trials.thisN]}\n"
            f"Reforço aplicado: {reforco_aplicado}\n"
            f"Imagem reforçada: {imagem_reforcada}\n"
            f"Correct response (reforço): {corr}\n"
            f"Correct response (target, ignorando reforço): {corr_target}\n"
            f"Pontos acumulados até agora: {score}"
        )
        
        stim_left.setImage(fractal_left)
        stim_right.setImage(fractal_right)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [fixation, polygon, stim_left, stim_right, key_resp]
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
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            if key_resp.keys == "left":
                x_pos = -0.5
                opa = 1
            elif key_resp.keys == "right":
                x_pos = 0.5
                opa = 1
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                polygon.setOpacity(opa, log=False)
                polygon.setPos((x_pos, 0), log=False)
            
            # if polygon is stopping this frame...
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            
            # *stim_left* updates
            
            # if stim_left is starting this frame...
            if stim_left.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stim_left.frameNStart = frameN  # exact frame index
                stim_left.tStart = t  # local t and not account for scr refresh
                stim_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_left.started')
                # update status
                stim_left.status = STARTED
                stim_left.setAutoDraw(True)
            
            # if stim_left is active this frame...
            if stim_left.status == STARTED:
                # update params
                pass
            
            # if stim_left is stopping this frame...
            if stim_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim_left.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_left.tStop = t  # not accounting for scr refresh
                    stim_left.tStopRefresh = tThisFlipGlobal  # on global time
                    stim_left.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_left.stopped')
                    # update status
                    stim_left.status = FINISHED
                    stim_left.setAutoDraw(False)
            
            # *stim_right* updates
            
            # if stim_right is starting this frame...
            if stim_right.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stim_right.frameNStart = frameN  # exact frame index
                stim_right.tStart = t  # local t and not account for scr refresh
                stim_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_right.started')
                # update status
                stim_right.status = STARTED
                stim_right.setAutoDraw(True)
            
            # if stim_right is active this frame...
            if stim_right.status == STARTED:
                # update params
                pass
            
            # if stim_right is stopping this frame...
            if stim_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim_right.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_right.tStop = t  # not accounting for scr refresh
                    stim_right.tStopRefresh = tThisFlipGlobal  # on global time
                    stim_right.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_right.stopped')
                    # update status
                    stim_right.status = FINISHED
                    stim_right.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
                    key_resp.duration = _key_resp_allKeys[0].duration
                    # was this correct?
                    if (key_resp.keys == str(corr)) or (key_resp.keys == corr):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
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
        thisExp.addData('trial.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code
        # reforco_aplicado = True se o participante deve receber ponto por acertar a imagem correta
        reforco_aplicado = reforcos[trials.thisN]
        
        # Nenhuma resposta foi dada
        if not key_resp.keys: 
            score -= 1
            point_msg = "–1"
            ausencias_consecutivas += 1
            ausencias_totais += 1   
        else:
            ausencias_consecutivas = 0  # zera a contagem se houve resposta
            
            if key_resp.corr:
                score += 1
                point_msg = "+1"
        
            # Resposta incorreta
            else:
                score -= 1
                point_msg = "–1"
        
        
        if score > 0:
            cum_score_msg = f"+{abs(score)}"
        elif score < 0:
            cum_score_msg = f"–{abs(score)}"
        else:
            cum_score_msg = "0"
        
        thisExp.addData("left_image", fractal_left)
        thisExp.addData("right_image", fractal_right)
        thisExp.addData("target_image", target)
        thisExp.addData("switch_trial", switches[trials.thisN])
        thisExp.addData("reinforcement", reforco_aplicado)
        thisExp.addData("reinforced_image", imagem_reforcada)
        thisExp.addData("corr_resp", corr)
        thisExp.addData("deterministic_corr_resp", corr_target)
        thisExp.addData("participant_resp", key_resp.keys)
        thisExp.addData("feedback", point_msg)
        thisExp.addData("score", score)
        
        # Verifica critérios de encerramento
        if ausencias_consecutivas >= 5 or ausencias_totais >= 9:
            if ausencias_consecutivas >= 5:
                motivo_fim = "Encerrado por 5 ausências consecutivas"
            else:
                motivo_fim = "Encerrado por 9 ausências totais"
        
            # Log de encerramento
            thisExp.addData("motivo_encerramento", motivo_fim)
            thisExp.addData("ausencias_consecutivas", ausencias_consecutivas)
            thisExp.addData("ausencias_totais", ausencias_totais)
        
            # (opcional) Mostra mensagem final ao participante
            trials.finished = True
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corr).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.500000)
        
        # --- Prepare to start Routine "trial_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial_feedback.started', globalClock.getTime(format='float'))
        point_feedback.setText(point_msg)
        # keep track of which components have finished
        trial_feedbackComponents = [point_feedback]
        for thisComponent in trial_feedbackComponents:
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
        
        # --- Run Routine "trial_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *point_feedback* updates
            
            # if point_feedback is starting this frame...
            if point_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                point_feedback.frameNStart = frameN  # exact frame index
                point_feedback.tStart = t  # local t and not account for scr refresh
                point_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(point_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'point_feedback.started')
                # update status
                point_feedback.status = STARTED
                point_feedback.setAutoDraw(True)
            
            # if point_feedback is active this frame...
            if point_feedback.status == STARTED:
                # update params
                pass
            
            # if point_feedback is stopping this frame...
            if point_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > point_feedback.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    point_feedback.tStop = t  # not accounting for scr refresh
                    point_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    point_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'point_feedback.stopped')
                    # update status
                    point_feedback.status = FINISHED
                    point_feedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_feedback" ---
        for thisComponent in trial_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial_feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "cumulative_score" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('cumulative_score.started', globalClock.getTime(format='float'))
        cum_score.setText(cum_score_msg)
        # keep track of which components have finished
        cumulative_scoreComponents = [cum_score_title, cum_score]
        for thisComponent in cumulative_scoreComponents:
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
        
        # --- Run Routine "cumulative_score" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cum_score_title* updates
            
            # if cum_score_title is starting this frame...
            if cum_score_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cum_score_title.frameNStart = frameN  # exact frame index
                cum_score_title.tStart = t  # local t and not account for scr refresh
                cum_score_title.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cum_score_title, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cum_score_title.started')
                # update status
                cum_score_title.status = STARTED
                cum_score_title.setAutoDraw(True)
            
            # if cum_score_title is active this frame...
            if cum_score_title.status == STARTED:
                # update params
                pass
            
            # if cum_score_title is stopping this frame...
            if cum_score_title.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cum_score_title.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    cum_score_title.tStop = t  # not accounting for scr refresh
                    cum_score_title.tStopRefresh = tThisFlipGlobal  # on global time
                    cum_score_title.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cum_score_title.stopped')
                    # update status
                    cum_score_title.status = FINISHED
                    cum_score_title.setAutoDraw(False)
            
            # *cum_score* updates
            
            # if cum_score is starting this frame...
            if cum_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cum_score.frameNStart = frameN  # exact frame index
                cum_score.tStart = t  # local t and not account for scr refresh
                cum_score.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cum_score, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cum_score.started')
                # update status
                cum_score.status = STARTED
                cum_score.setAutoDraw(True)
            
            # if cum_score is active this frame...
            if cum_score.status == STARTED:
                # update params
                pass
            
            # if cum_score is stopping this frame...
            if cum_score.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cum_score.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cum_score.tStop = t  # not accounting for scr refresh
                    cum_score.tStopRefresh = tThisFlipGlobal  # on global time
                    cum_score.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cum_score.stopped')
                    # update status
                    cum_score.status = FINISHED
                    cum_score.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cumulative_scoreComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cumulative_score" ---
        for thisComponent in cumulative_scoreComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('cumulative_score.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 150.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "thanks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks.started', globalClock.getTime(format='float'))
    # create starting attributes for thanks_resp
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thanks_msg* updates
        
        # if thanks_msg is starting this frame...
        if thanks_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thanks_msg.frameNStart = frameN  # exact frame index
            thanks_msg.tStart = t  # local t and not account for scr refresh
            thanks_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks_msg.started')
            # update status
            thanks_msg.status = STARTED
            thanks_msg.setAutoDraw(True)
        
        # if thanks_msg is active this frame...
        if thanks_msg.status == STARTED:
            # update params
            pass
        
        # *thanks_resp* updates
        waitOnFlip = False
        
        # if thanks_resp is starting this frame...
        if thanks_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thanks_resp.frameNStart = frameN  # exact frame index
            thanks_resp.tStart = t  # local t and not account for scr refresh
            thanks_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks_resp.started')
            # update status
            thanks_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(thanks_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(thanks_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if thanks_resp.status == STARTED and not waitOnFlip:
            theseKeys = thanks_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _thanks_resp_allKeys.extend(theseKeys)
            if len(_thanks_resp_allKeys):
                thanks_resp.keys = _thanks_resp_allKeys[-1].name  # just the last key pressed
                thanks_resp.rt = _thanks_resp_allKeys[-1].rt
                thanks_resp.duration = _thanks_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
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
    thisExp.addData('thanks.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
