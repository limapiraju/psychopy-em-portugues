#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.5),
    on outubro 11, 2024, at 10:00
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
expName = 'go-no-go-task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'Nome Completo': '',
    'Símbolos': '4',
    'Cores': '4',
    'Ambos': '10',
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
        originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 056 – Go No-Go Task\\go-no-go-task_lastrun.py',
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
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
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
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('performance_fb_resp') is None:
        # initialise performance_fb_resp
        performance_fb_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='performance_fb_resp',
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
    try:
        expInfo["Símbolos"] = int(expInfo["Símbolos"])
    except:
        expInfo["Símbolos"] = 4
    
    try:
        expInfo["Cores"] = int(expInfo["Cores"])
    except:
        expInfo["Cores"] = 4
        
    try:
        expInfo["Ambos"] = int(expInfo["Ambos"])
    except:
        expInfo["Ambos"] = 10
    
    N_reps = [expInfo["Símbolos"],
              expInfo["Cores"],
              expInfo["Ambos"]
              ]
    
    cond_idx = -1
    
    # índices de instruções
    current_instruction = 0
    instruction_block = 0
    
    # lista de instruções
    instruction_list = [ # tarefa de símbolos
    ["""Esta sessão se dividirá em três etapas. Na primeira etapa, você verá círculos contendo símbolos no centro deles.
    
    Sua tarefa será pressionar [Barra de Espaço] sempre que o símbolo na tela for ✓. Quando o símbolo for ✗, você não deverá responder.
    
    Responda o mais rápida e acuradamente possível.""",
    """Lembre-se:
        
    • Se o símbolo for ✓, pressione [Barra de Espaço].
    • Se o símbolo for ✗, não responda.
    
    Iremos iniciar a tarefa a seguir. Caso tenha alguma dúvida, pergunte ao pesquisador."""],
    [# tarefa de cores
    """Na segunda etapa, você verá círculos de diferentes cores. 
    
    Sua tarefa será pressionar [Barra de Espaço] sempre que o círculo tiver a cor VERDE. Quando o círculo tiver a cor VERMELHA, você não deverá responder. 
    
    Responda o mais rápida e acuradamente possível.""",
    """Lembre-se:
        
    • Se o círculo for VERDE, pressione [Barra de Espaço]. 
    • Se o círculo for VERMELHO, não responda.
    
    Iremos iniciar a tarefa a seguir. Caso tenha alguma dúvida, pergunte ao pesquisador."""],
    [# tarefa principal
    """Na terceira e última etapa, você verá círculos contendo símbolos no centro deles. 
    
    Sua tarefa será pressionar [Barra de Espaço] sempre que o círculo for verde OU tiver o símbolo ✓ dentro dele.
    
    Quando o círculo for vermelho E o símbolo for ✗, você não deverá responder. 
    
    Responda o mais rápida e acuradamente possível.""",
    """Lembre-se: você deve pressionar [Barra de Espaço] quando: 
        
    • O círculo for verde e tiver o símbolo ✓.
    • O círculo for verde e tiver o símbolo ✗.
    • O círculo for vermelho e tiver o símbolo ✓.
    
    Você NÃO DEVE responder quando o círculo for vermelho e tiver o símbolo ✗.
    
    Iremos iniciar a tarefa a seguir. Caso tenha alguma dúvida, pergunte ao pesquisador."""]]
    
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
    instr_previous = visual.ImageStim(
        win=win,
        name='instr_previous', units='norm', 
        image='previous_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    instr_next = visual.ImageStim(
        win=win,
        name='instr_next', units='norm', 
        image='next_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    instr_mouse = event.Mouse(win=win)
    x, y = [None, None]
    instr_mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial" ---
    fixation = visual.TextStim(win=win, name='fixation',
        text='+',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    circle = visual.ShapeStim(
        win=win, name='circle',units='height', 
        size=(0.25, 0.25), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
        opacity=None, depth=-1.0, interpolate=True)
    token = visual.TextStim(win=win, name='token',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "feedback" ---
    # Run 'Begin Experiment' code from feedback_code
    RTs = list()
    feedback_msg = visual.TextStim(win=win, name='feedback_msg',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "performance_feedback" ---
    performance_fb_msg = visual.TextStim(win=win, name='performance_fb_msg',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0.1), height=0.12, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    performance_fb_resp = keyboard.Keyboard(deviceName='performance_fb_resp')
    
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
        
        # *welcome_next* updates
        
        # if welcome_next is starting this frame...
        if welcome_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_next.frameNStart = frameN  # exact frame index
            welcome_next.tStart = t  # local t and not account for scr refresh
            welcome_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_next.started')
            # update status
            welcome_next.status = STARTED
            welcome_next.setAutoDraw(True)
        
        # if welcome_next is active this frame...
        if welcome_next.status == STARTED:
            # update params
            pass
        # *welcome_resp* updates
        
        # if welcome_resp is starting this frame...
        if welcome_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_resp.frameNStart = frameN  # exact frame index
            welcome_resp.tStart = t  # local t and not account for scr refresh
            welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('welcome_resp.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(welcome_next, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(welcome_resp):
                            gotValidClick = True
                            welcome_resp.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
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
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    tasks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.xlsx'),
        seed=None, name='tasks')
    thisExp.addLoop(tasks)  # add the loop to the experiment
    thisTask = tasks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
    if thisTask != None:
        for paramName in thisTask:
            globals()[paramName] = thisTask[paramName]
    
    for thisTask in tasks:
        currentLoop = tasks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
        if thisTask != None:
            for paramName in thisTask:
                globals()[paramName] = thisTask[paramName]
        
        # set up handler to look after randomisation of conditions etc
        instruction_trials = data.TrialHandler(nReps=9999.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='instruction_trials')
        thisExp.addLoop(instruction_trials)  # add the loop to the experiment
        thisInstruction_trial = instruction_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInstruction_trial.rgb)
        if thisInstruction_trial != None:
            for paramName in thisInstruction_trial:
                globals()[paramName] = thisInstruction_trial[paramName]
        
        for thisInstruction_trial in instruction_trials:
            currentLoop = instruction_trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisInstruction_trial.rgb)
            if thisInstruction_trial != None:
                for paramName in thisInstruction_trial:
                    globals()[paramName] = thisInstruction_trial[paramName]
            
            # --- Prepare to start Routine "instruction" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('instruction.started', globalClock.getTime(format='float'))
            instr_msg.setText(instruction_list[instruction_block][current_instruction])
            # setup some python lists for storing info about the instr_mouse
            instr_mouse.x = []
            instr_mouse.y = []
            instr_mouse.leftButton = []
            instr_mouse.midButton = []
            instr_mouse.rightButton = []
            instr_mouse.time = []
            instr_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            instructionComponents = [instr_msg, instr_previous, instr_next, instr_mouse]
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
                
                # *instr_previous* updates
                
                # if instr_previous is starting this frame...
                if instr_previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instr_previous.frameNStart = frameN  # exact frame index
                    instr_previous.tStart = t  # local t and not account for scr refresh
                    instr_previous.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instr_previous, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instr_previous.started')
                    # update status
                    instr_previous.status = STARTED
                    instr_previous.setAutoDraw(True)
                
                # if instr_previous is active this frame...
                if instr_previous.status == STARTED:
                    # update params
                    pass
                
                # *instr_next* updates
                
                # if instr_next is starting this frame...
                if instr_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instr_next.frameNStart = frameN  # exact frame index
                    instr_next.tStart = t  # local t and not account for scr refresh
                    instr_next.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instr_next, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instr_next.started')
                    # update status
                    instr_next.status = STARTED
                    instr_next.setAutoDraw(True)
                
                # if instr_next is active this frame...
                if instr_next.status == STARTED:
                    # update params
                    pass
                # *instr_mouse* updates
                
                # if instr_mouse is starting this frame...
                if instr_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instr_mouse.frameNStart = frameN  # exact frame index
                    instr_mouse.tStart = t  # local t and not account for scr refresh
                    instr_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instr_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('instr_mouse.started', t)
                    # update status
                    instr_mouse.status = STARTED
                    instr_mouse.mouseClock.reset()
                    prevButtonState = instr_mouse.getPressed()  # if button is down already this ISN'T a new click
                if instr_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = instr_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames([instr_previous, instr_next], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(instr_mouse):
                                    gotValidClick = True
                                    instr_mouse.clicked_name.append(obj.name)
                            x, y = instr_mouse.getPos()
                            instr_mouse.x.append(x)
                            instr_mouse.y.append(y)
                            buttons = instr_mouse.getPressed()
                            instr_mouse.leftButton.append(buttons[0])
                            instr_mouse.midButton.append(buttons[1])
                            instr_mouse.rightButton.append(buttons[2])
                            instr_mouse.time.append(instr_mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # end routine on response
                
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
            # Run 'End Routine' code from instr_code
            if instr_mouse.clicked_name[0] == "instr_previous":
                current_instruction -= 1
            elif instr_mouse.clicked_name[0] == "instr_next":
                current_instruction += 1
            
            # Se a instrução atual for -1
            if current_instruction == -1:
                # Resete o valor para ser 0
                current_instruction = 0
            # Se a instrução atual é igual ao comprimento da lista de instruções
            elif current_instruction == len(instruction_list[instruction_block]):
                current_instruction = 0 # zera contador de instruções
                cond_idx += 1
                instruction_trials.finished = True
                instruction_block += 1 # incrementa bloco de instruções
            # store data for instruction_trials (TrialHandler)
            instruction_trials.addData('instr_mouse.x', instr_mouse.x)
            instruction_trials.addData('instr_mouse.y', instr_mouse.y)
            instruction_trials.addData('instr_mouse.leftButton', instr_mouse.leftButton)
            instruction_trials.addData('instr_mouse.midButton', instr_mouse.midButton)
            instruction_trials.addData('instr_mouse.rightButton', instr_mouse.rightButton)
            instruction_trials.addData('instr_mouse.time', instr_mouse.time)
            instruction_trials.addData('instr_mouse.clicked_name', instr_mouse.clicked_name)
            # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 9999.0 repeats of 'instruction_trials'
        
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=N_reps[tasks.thisN], method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(condition_file),
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
            circle.setLineColor(color)
            token.setColor(color_symbol, colorSpace='rgb')
            token.setText(symbol)
            # create starting attributes for key_resp
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # keep track of which components have finished
            trialComponents = [fixation, circle, token, key_resp]
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
            while continueRoutine and routineTimer.getTime() < 1.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
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
                    if tThisFlipGlobal > fixation.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation.tStop = t  # not accounting for scr refresh
                        fixation.tStopRefresh = tThisFlipGlobal  # on global time
                        fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation.stopped')
                        # update status
                        fixation.status = FINISHED
                        fixation.setAutoDraw(False)
                
                # *circle* updates
                
                # if circle is starting this frame...
                if circle.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                    # keep track of start time/frame for later
                    circle.frameNStart = frameN  # exact frame index
                    circle.tStart = t  # local t and not account for scr refresh
                    circle.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle.started')
                    # update status
                    circle.status = STARTED
                    circle.setAutoDraw(True)
                
                # if circle is active this frame...
                if circle.status == STARTED:
                    # update params
                    pass
                
                # if circle is stopping this frame...
                if circle.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > circle.tStartRefresh + 1.25-frameTolerance:
                        # keep track of stop time/frame for later
                        circle.tStop = t  # not accounting for scr refresh
                        circle.tStopRefresh = tThisFlipGlobal  # on global time
                        circle.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'circle.stopped')
                        # update status
                        circle.status = FINISHED
                        circle.setAutoDraw(False)
                
                # *token* updates
                
                # if token is starting this frame...
                if token.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                    # keep track of start time/frame for later
                    token.frameNStart = frameN  # exact frame index
                    token.tStart = t  # local t and not account for scr refresh
                    token.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(token, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'token.started')
                    # update status
                    token.status = STARTED
                    token.setAutoDraw(True)
                
                # if token is active this frame...
                if token.status == STARTED:
                    # update params
                    pass
                
                # if token is stopping this frame...
                if token.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > token.tStartRefresh + 1.25-frameTolerance:
                        # keep track of stop time/frame for later
                        token.tStop = t  # not accounting for scr refresh
                        token.tStopRefresh = tThisFlipGlobal  # on global time
                        token.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'token.stopped')
                        # update status
                        token.status = FINISHED
                        token.setAutoDraw(False)
                
                # *key_resp* updates
                waitOnFlip = False
                
                # if key_resp is starting this frame...
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
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
                    if tThisFlipGlobal > key_resp.tStartRefresh + 1.25-frameTolerance:
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
                    theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
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
                routineTimer.addTime(-1.500000)
            
            # --- Prepare to start Routine "feedback" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('feedback.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from feedback_code
            if key_resp.corr == 1:
                fb_msg = "Correto!"
                if key_resp.keys == "space":
                    RTs.append(key_resp.rt)
                    print(RTs)
            else:
                fb_msg = "Incorreto!"
                
            
            feedback_msg.setText(fb_msg)
            # keep track of which components have finished
            feedbackComponents = [feedback_msg]
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
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_msg* updates
                
                # if feedback_msg is starting this frame...
                if feedback_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_msg.frameNStart = frameN  # exact frame index
                    feedback_msg.tStart = t  # local t and not account for scr refresh
                    feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_msg, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_msg.started')
                    # update status
                    feedback_msg.status = STARTED
                    feedback_msg.setAutoDraw(True)
                
                # if feedback_msg is active this frame...
                if feedback_msg.status == STARTED:
                    # update params
                    pass
                
                # if feedback_msg is stopping this frame...
                if feedback_msg.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_msg.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_msg.tStop = t  # not accounting for scr refresh
                        feedback_msg.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_msg.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_msg.stopped')
                        # update status
                        feedback_msg.status = FINISHED
                        feedback_msg.setAutoDraw(False)
                
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
            thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from feedback_code
            thisExp.addData("feedback", fb_msg)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed N_reps[tasks.thisN] repeats of 'trials'
        
        
        # --- Prepare to start Routine "performance_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('performance_feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from performance_fb_code
        rt = np.array(RTs).mean()
        
        fb_msg = f"""\nSeu tempo de reação nesta fase foi de {rt * 1000:.0f} ms.\n\nPressione [Barra de Espaço] para prosseguir."""
        performance_fb_msg.setText(fb_msg)
        # create starting attributes for performance_fb_resp
        performance_fb_resp.keys = []
        performance_fb_resp.rt = []
        _performance_fb_resp_allKeys = []
        # keep track of which components have finished
        performance_feedbackComponents = [performance_fb_msg, performance_fb_resp]
        for thisComponent in performance_feedbackComponents:
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
        
        # --- Run Routine "performance_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *performance_fb_msg* updates
            
            # if performance_fb_msg is starting this frame...
            if performance_fb_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                performance_fb_msg.frameNStart = frameN  # exact frame index
                performance_fb_msg.tStart = t  # local t and not account for scr refresh
                performance_fb_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(performance_fb_msg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'performance_fb_msg.started')
                # update status
                performance_fb_msg.status = STARTED
                performance_fb_msg.setAutoDraw(True)
            
            # if performance_fb_msg is active this frame...
            if performance_fb_msg.status == STARTED:
                # update params
                pass
            
            # *performance_fb_resp* updates
            waitOnFlip = False
            
            # if performance_fb_resp is starting this frame...
            if performance_fb_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                performance_fb_resp.frameNStart = frameN  # exact frame index
                performance_fb_resp.tStart = t  # local t and not account for scr refresh
                performance_fb_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(performance_fb_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'performance_fb_resp.started')
                # update status
                performance_fb_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(performance_fb_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(performance_fb_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if performance_fb_resp.status == STARTED and not waitOnFlip:
                theseKeys = performance_fb_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _performance_fb_resp_allKeys.extend(theseKeys)
                if len(_performance_fb_resp_allKeys):
                    performance_fb_resp.keys = _performance_fb_resp_allKeys[-1].name  # just the last key pressed
                    performance_fb_resp.rt = _performance_fb_resp_allKeys[-1].rt
                    performance_fb_resp.duration = _performance_fb_resp_allKeys[-1].duration
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
            for thisComponent in performance_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "performance_feedback" ---
        for thisComponent in performance_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('performance_feedback.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from performance_fb_code
        thisExp.addData("RT", rt)
        
        RT = list()
        # the Routine "performance_feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'tasks'
    
    
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
