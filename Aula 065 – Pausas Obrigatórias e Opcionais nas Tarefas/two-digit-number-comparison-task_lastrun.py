#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.5),
    on novembro 07, 2024, at 12:41
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

# Run 'Before Experiment' code from instr_code


# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.5'
expName = 'two-digit-number-comparison-task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'Nome Completo': '',
    'total_blocks': '10',
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
_fullScr = True
_winSize = [1366, 768]
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
    filename = u'data/%s_%s_%s' % (expInfo['Nome Completo'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\limap\\OneDrive\\Documentos\\Psychology\\8. YouTube\\psychopy-em-portugues\\Aula 065 – Pausas Obrigatórias e Opcionais nas Tarefas\\two-digit-number-comparison-task_lastrun.py',
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
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
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
    if deviceManager.getDevice('welcome_resp') is None:
        # initialise welcome_resp
        welcome_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='welcome_resp',
        )
    if deviceManager.getDevice('instr_resp') is None:
        # initialise instr_resp
        instr_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_resp',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('rest_resp') is None:
        # initialise rest_resp
        rest_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='rest_resp',
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
    
    # --- Initialize components for Routine "welcome" ---
    welcome_msg = visual.TextStim(win=win, name='welcome_msg',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    welcome_resp = keyboard.Keyboard(deviceName='welcome_resp')
    
    # --- Initialize components for Routine "instruction" ---
    # Run 'Begin Experiment' code from instr_code
    # primeiro nome do participante
    if expInfo["Nome Completo"] == "":
        first_name = "participante"
    else:
        first_name = expInfo["Nome Completo"].strip().split()[0].title()
    
    
    
    
    welcome_txt = f"""Olá, {first_name}! 
    
    Agradecemos sua disponibilidade em colaborar com nossa pesquisa!
    
    Pressione [Barra de Espaço] para iniciar."""
    
    thanks_txt = f"""Esta atividade acabou, {first_name}.
    
    Favor chamar o pesquisador! ☺"""
    
    instr_msg = visual.TextStim(win=win, name='instr_msg',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.09, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    instr_resp = keyboard.Keyboard(deviceName='instr_resp')
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code
    import math
    
    # Define a condição do participante quanto ao mapeamento
    # das teclas e das respostas MAIOR/MENOR
    if random() > .5:
        left_msg, right_msg = "Menor que 55", "Maior que 55"
        button_condition = "left-lower/right-greater"
        lower, greater = " ← ", " → "
    else:
        left_msg, right_msg = "Maior que 55", "Menor que 55"
        button_condition = "left-greater/right-lower"
        lower, greater = " → ", " ← "
        
    instr = [f"""
    Nesta tarefa, você verá números de dois dígitos. Sua tarefa será responder o mais rápida e acuradamente possível se o número na tela é menor ou maior que 55.
    
    • Se o número na tela for MENOR QUE 55, responda [{lower}]. 
    • Se o número na tela for MAIOR QUE 55, responda [{greater}].
    
    Pressione [Barra de Espaço] para iniciar.""",
    f"""
    A seguir, você realizará mais uma rodada da mesma tarefa.
    
    • Se o número na tela for MENOR QUE 55, responde [{lower}]. 
    • Se o número na tela for MAIOR QUE 55, responda [{greater}]."""]
    number = visual.TextStim(win=win, name='number',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.35, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    alternatives = visual.ImageStim(
        win=win,
        name='alternatives', units='norm', 
        image='arrows.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.75), size=(0.5, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    left_alt = visual.TextStim(win=win, name='left_alt',
        text='',
        font='Times New Roman',
        units='norm', pos=(-0.6, -0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    right_alt = visual.TextStim(win=win, name='right_alt',
        text='',
        font='Times New Roman',
        units='norm', pos=(0.6, -0.75), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "rest" ---
    # Run 'Begin Experiment' code from rest_code
    try:
        total_blocks = int(expInfo["total_blocks"])
        # checa se o número de blocos é ímpar
        if (total_blocks % 2) == 1:
            total_blocks += 1
            
    except:
        total_blocks = 10
        
    # variáveis que controlam instruções
    instr_idx = 0
    enabled = True
    rest_prompt = visual.TextStim(win=win, name='rest_prompt',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0.2), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    rest_clock = visual.TextStim(win=win, name='rest_clock',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, -0.2), height=0.25, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    rest_resp = keyboard.Keyboard(deviceName='rest_resp')
    
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
    
    # --- Prepare to start Routine "welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('welcome.started', globalClock.getTime(format='float'))
    welcome_msg.setText(welcome_txt)
    # create starting attributes for welcome_resp
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_msg* updates
        
        # if welcome_msg is starting this frame...
        if welcome_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_msg.frameNStart = frameN  # exact frame index
            welcome_msg.tStart = t  # local t and not account for scr refresh
            welcome_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_msg.started')
            # update status
            welcome_msg.status = STARTED
            welcome_msg.setAutoDraw(True)
        
        # if welcome_msg is active this frame...
        if welcome_msg.status == STARTED:
            # update params
            pass
        
        # *welcome_resp* updates
        waitOnFlip = False
        
        # if welcome_resp is starting this frame...
        if welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_resp.frameNStart = frameN  # exact frame index
            welcome_resp.tStart = t  # local t and not account for scr refresh
            welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_resp.started')
            # update status
            welcome_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcome_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcome_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcome_resp.status == STARTED and not waitOnFlip:
            theseKeys = welcome_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _welcome_resp_allKeys.extend(theseKeys)
            if len(_welcome_resp_allKeys):
                welcome_resp.keys = _welcome_resp_allKeys[-1].name  # just the last key pressed
                welcome_resp.rt = _welcome_resp_allKeys[-1].rt
                welcome_resp.duration = _welcome_resp_allKeys[-1].duration
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
    thisExp.addData('welcome.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=total_blocks, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            globals()[paramName] = thisBlock[paramName]
    
    for thisBlock in blocks:
        currentLoop = blocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                globals()[paramName] = thisBlock[paramName]
        
        # --- Prepare to start Routine "instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instruction.started', globalClock.getTime(format='float'))
        instr_msg.setText(instr[instr_idx])
        # create starting attributes for instr_resp
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
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instr_msg* updates
            
            # if instr_msg is starting this frame...
            if instr_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr_msg.frameNStart = frameN  # exact frame index
                instr_msg.tStart = t  # local t and not account for scr refresh
                instr_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_msg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instr_msg.started')
                # update status
                instr_msg.status = STARTED
                instr_msg.setAutoDraw(True)
            
            # if instr_msg is active this frame...
            if instr_msg.status == STARTED:
                # update params
                pass
            
            # *instr_resp* updates
            waitOnFlip = False
            
            # if instr_resp is starting this frame...
            if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr_resp.frameNStart = frameN  # exact frame index
                instr_resp.tStart = t  # local t and not account for scr refresh
                instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instr_resp.started')
                # update status
                instr_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if instr_resp.status == STARTED and not waitOnFlip:
                theseKeys = instr_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _instr_resp_allKeys.extend(theseKeys)
                if len(_instr_resp_allKeys):
                    instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
                    instr_resp.rt = _instr_resp_allKeys[-1].rt
                    instr_resp.duration = _instr_resp_allKeys[-1].duration
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
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('stim.xlsx'),
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
            # Define gabarito a depender do target_number e do
            # button_condition em vigor
            if target_number < 55:
                if button_condition == "left-lower/right-greater":
                    corr = "left"
                else:
                    corr = "right"
                    
            elif target_number > 55:
                if button_condition == "left-lower/right-greater":
                    corr = "right"
                else:
                    corr = "left"
            number.setText(target_number)
            # create starting attributes for key_resp
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            left_alt.setText(left_msg)
            right_alt.setText(right_msg)
            # keep track of which components have finished
            trialComponents = [number, key_resp, alternatives, left_alt, right_alt]
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
            while continueRoutine and routineTimer.getTime() < 4.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *number* updates
                
                # if number is starting this frame...
                if number.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    number.frameNStart = frameN  # exact frame index
                    number.tStart = t  # local t and not account for scr refresh
                    number.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(number, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'number.started')
                    # update status
                    number.status = STARTED
                    number.setAutoDraw(True)
                
                # if number is active this frame...
                if number.status == STARTED:
                    # update params
                    pass
                
                # if number is stopping this frame...
                if number.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > number.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        number.tStop = t  # not accounting for scr refresh
                        number.tStopRefresh = tThisFlipGlobal  # on global time
                        number.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'number.stopped')
                        # update status
                        number.status = FINISHED
                        number.setAutoDraw(False)
                
                # *key_resp* updates
                waitOnFlip = False
                
                # if key_resp is starting this frame...
                if key_resp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
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
                        # a response ends the routine
                        continueRoutine = False
                
                # *alternatives* updates
                
                # if alternatives is starting this frame...
                if alternatives.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    alternatives.frameNStart = frameN  # exact frame index
                    alternatives.tStart = t  # local t and not account for scr refresh
                    alternatives.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(alternatives, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'alternatives.started')
                    # update status
                    alternatives.status = STARTED
                    alternatives.setAutoDraw(True)
                
                # if alternatives is active this frame...
                if alternatives.status == STARTED:
                    # update params
                    pass
                
                # if alternatives is stopping this frame...
                if alternatives.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > alternatives.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        alternatives.tStop = t  # not accounting for scr refresh
                        alternatives.tStopRefresh = tThisFlipGlobal  # on global time
                        alternatives.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'alternatives.stopped')
                        # update status
                        alternatives.status = FINISHED
                        alternatives.setAutoDraw(False)
                
                # *left_alt* updates
                
                # if left_alt is starting this frame...
                if left_alt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    left_alt.frameNStart = frameN  # exact frame index
                    left_alt.tStart = t  # local t and not account for scr refresh
                    left_alt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(left_alt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_alt.started')
                    # update status
                    left_alt.status = STARTED
                    left_alt.setAutoDraw(True)
                
                # if left_alt is active this frame...
                if left_alt.status == STARTED:
                    # update params
                    pass
                
                # if left_alt is stopping this frame...
                if left_alt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > left_alt.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        left_alt.tStop = t  # not accounting for scr refresh
                        left_alt.tStopRefresh = tThisFlipGlobal  # on global time
                        left_alt.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'left_alt.stopped')
                        # update status
                        left_alt.status = FINISHED
                        left_alt.setAutoDraw(False)
                
                # *right_alt* updates
                
                # if right_alt is starting this frame...
                if right_alt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    right_alt.frameNStart = frameN  # exact frame index
                    right_alt.tStart = t  # local t and not account for scr refresh
                    right_alt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(right_alt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_alt.started')
                    # update status
                    right_alt.status = STARTED
                    right_alt.setAutoDraw(True)
                
                # if right_alt is active this frame...
                if right_alt.status == STARTED:
                    # update params
                    pass
                
                # if right_alt is stopping this frame...
                if right_alt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > right_alt.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        right_alt.tStop = t  # not accounting for scr refresh
                        right_alt.tStopRefresh = tThisFlipGlobal  # on global time
                        right_alt.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'right_alt.stopped')
                        # update status
                        right_alt.status = FINISHED
                        right_alt.setAutoDraw(False)
                
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
            # salva variáveis importantes
            thisExp.addData("left_msg", left_msg)
            thisExp.addData("right_msg", right_msg)
            thisExp.addData("button_condition", button_condition)
            thisExp.addData("corr", corr)
            
            
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
                routineTimer.addTime(-4.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials'
        
        
        # --- Prepare to start Routine "rest" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('rest.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from rest_code
        # metade da tarefa, pausa obrigatória
        if blocks.thisN == (total_blocks / 2 - 1):
            rest_msg = "Pausa obrigatória de 5 minutos. Aguarde o fim do tempo para avançar."
            timer = core.CountdownTimer(start = 300) # 300 s = 5 min
            timer_color = "green"
        
        # encerra a sessão
        elif blocks.thisN == (total_blocks - 1):
            blocks.finished = True
            continueRoutine = False
        
        # pausas opcionais nos demais ciclos
        elif blocks.thisN != (total_blocks / 2 - 1):
            rest_msg = "Pausa opcional de 1 minuto. Aproveite para tomar água e se alongar, ou pressione [Barra de Espaço] para prosseguir."
            timer = core.CountdownTimer(start = 60) # 60 s = 1 min
            timer_color = "green"
            
        
            
            
        
        rest_prompt.setText(rest_msg)
        # create starting attributes for rest_resp
        rest_resp.keys = []
        rest_resp.rt = []
        _rest_resp_allKeys = []
        # keep track of which components have finished
        restComponents = [rest_prompt, rest_clock, rest_resp]
        for thisComponent in restComponents:
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
        
        # --- Run Routine "rest" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from rest_code
            minutes = math.floor(timer.getTime() / 60)
            seconds = math.floor(timer.getTime() - minutes * 60)
            timing = str(int(minutes)).zfill(2) + ":" + str(int(seconds)).zfill(2)
            
            # monitora a cor do relógio
            if (math.floor(timer.getTime()) <= 5):
                timer_color = "red"
            
            # monitora encerramento do relógio
            if (timer.getTime() <= 0):
                continueRoutine = False
            
            if ("space" in rest_resp.keys) and ("opcional" in rest_msg):
                continueRoutine = False
            
            # *rest_prompt* updates
            
            # if rest_prompt is starting this frame...
            if rest_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest_prompt.frameNStart = frameN  # exact frame index
                rest_prompt.tStart = t  # local t and not account for scr refresh
                rest_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_prompt.started')
                # update status
                rest_prompt.status = STARTED
                rest_prompt.setAutoDraw(True)
            
            # if rest_prompt is active this frame...
            if rest_prompt.status == STARTED:
                # update params
                pass
            
            # *rest_clock* updates
            
            # if rest_clock is starting this frame...
            if rest_clock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest_clock.frameNStart = frameN  # exact frame index
                rest_clock.tStart = t  # local t and not account for scr refresh
                rest_clock.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_clock, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_clock.started')
                # update status
                rest_clock.status = STARTED
                rest_clock.setAutoDraw(True)
            
            # if rest_clock is active this frame...
            if rest_clock.status == STARTED:
                # update params
                rest_clock.setColor(timer_color, colorSpace='rgb', log=False)
                rest_clock.setText(timing, log=False)
            
            # *rest_resp* updates
            waitOnFlip = False
            
            # if rest_resp is starting this frame...
            if rest_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest_resp.frameNStart = frameN  # exact frame index
                rest_resp.tStart = t  # local t and not account for scr refresh
                rest_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_resp.started')
                # update status
                rest_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rest_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rest_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rest_resp.status == STARTED and not waitOnFlip:
                theseKeys = rest_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _rest_resp_allKeys.extend(theseKeys)
                if len(_rest_resp_allKeys):
                    rest_resp.keys = _rest_resp_allKeys[-1].name  # just the last key pressed
                    rest_resp.rt = _rest_resp_allKeys[-1].rt
                    rest_resp.duration = _rest_resp_allKeys[-1].duration
            
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
            for thisComponent in restComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rest" ---
        for thisComponent in restComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('rest.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from rest_code
        if enabled:
            instr_idx += 1
            enabled = False
            
        # the Routine "rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed total_blocks repeats of 'blocks'
    
    
    # --- Prepare to start Routine "thanks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks.started', globalClock.getTime(format='float'))
    thanks_prompt.setText(thanks_txt)
    # create starting attributes for thanks_resp
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thanks_prompt* updates
        
        # if thanks_prompt is starting this frame...
        if thanks_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thanks_prompt.frameNStart = frameN  # exact frame index
            thanks_prompt.tStart = t  # local t and not account for scr refresh
            thanks_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks_prompt.started')
            # update status
            thanks_prompt.status = STARTED
            thanks_prompt.setAutoDraw(True)
        
        # if thanks_prompt is active this frame...
        if thanks_prompt.status == STARTED:
            # update params
            pass
        
        # *thanks_spacebar* updates
        
        # if thanks_spacebar is starting this frame...
        if thanks_spacebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thanks_spacebar.frameNStart = frameN  # exact frame index
            thanks_spacebar.tStart = t  # local t and not account for scr refresh
            thanks_spacebar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks_spacebar, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks_spacebar.started')
            # update status
            thanks_spacebar.status = STARTED
            thanks_spacebar.setAutoDraw(True)
        
        # if thanks_spacebar is active this frame...
        if thanks_spacebar.status == STARTED:
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
    # Run 'End Experiment' code from instr_code
    # salvando duração da sessão...
    thisExp.addData("session_duration", globalClock.getTime())
    
    
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
