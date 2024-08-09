#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on janeiro 31, 2024, at 13:22
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from instr_code


# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'LoP_task'  # from the Builder filename that created this script
expInfo = {
    'ID': '',
    'Nome Completo': '',
    'E-mail': '',
    'Telefone': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
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
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s_%s' % (expInfo['ID'].zfill(3), expInfo['date'], expInfo['Nome Completo'], expName)
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Python para Psicólogos\\psychopy-em-portugues\\Aula 050 – Tarefa de Níveis de Processamento\\LoP_task.py',
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
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
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
            size=[900, 600], fullscr=False, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.000,-1.000,-1.000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'norm'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
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
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='ptb')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
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
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='PsychToolbox')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
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
    inputs : dict
        Dictionary of input devices by name.
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
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
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
    # Run 'Begin Experiment' code from welcome_code
    import random
    from os.path import exists
    
    expInfo["ID"] = expInfo["ID"].zfill(3)
    
    # cria lista que armazena as possíveis condições
    conditions = ["structural", "rhyme", "sentence"]
    random.shuffle(conditions)
    my_condition = conditions[0]
    participant_code = expInfo["ID"] + my_condition[:3].upper()
    
    if not exists("unique_IDs.txt"):
        arquivo = open("unique_IDs.txt", "w")
        # cria cabeçalho do arquivo
        arquivo.write("ID\tName\n")
        arquivo.write(participant_code + "\t" + expInfo["Nome Completo"] + "\n")
        arquivo.close()
    else:
        novo_arquivo = open("unique_IDs.txt", "a")
        novo_arquivo.write(participant_code + "\t" + expInfo["Nome Completo"] + "\n")
        novo_arquivo.close()
    welcome_msg = visual.TextStim(win=win, name='welcome_msg',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.12, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    welcome_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instruction" ---
    # Run 'Begin Experiment' code from instr_code
    # índices de instruções
    current_instruction = 0
    
    # lista de instruções
    instruction_list = ["instruction1", "instruction2", "instruction3", f"instruction4_{my_condition}", "instruction5"]
    # primeiro nome do participante
    if expInfo["Nome Completo"] == "":
        first_name = "participante"
    else:
        first_name = expInfo["Nome Completo"].strip().split()[0].title()
    
    welcome_txt = f"""Olá, {first_name}! 
    
    Agradecemos sua disponibilidade em colaborar com nossa pesquisa!
    
    Pressione [BARRA DE ESPAÇO] para iniciar."""
    
    thanks_txt = f"""Fim do experimento, {first_name}.
    
    Agradecemos sua participação! ☺"""
    instr_resp = keyboard.Keyboard()
    instruction_images = visual.ImageStim(
        win=win,
        name='instruction_images', units='norm', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "fixation" ---
    fixation_cross = visual.TextStim(win=win, name='fixation_cross',
        text='+',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "main_task" ---
    # Run 'Begin Experiment' code from main_task_code
    words = [["bola", "cola", "roupa", "Ele pegou a ____ para jogar futebol", "Ele pegou o ferro para passar a ____"],
             ["dedo", "medo", "queijo", "É falta de educação mostrar o ____ do meio", "Comi pão com margarina e ____"],
             ["massa", "praça", "orelha", "Macarrão e pizza são tipos de comida de ____", "Ela chegou com um novo brinco na ____"],
             ["brinquedo", "enredo", "banana", "No Natal, criança gosta de ganhar ____", "Macaco gosta de comer ____"],
             ["boné", "chulé", "sapato", "Para me proteger do sol, comprei um ____", "Esse problema era uma pedra no meu ____"],
             ["eleição", "maratona", "A ____ é um esporte praticado em uma piscina", "A ____ é uma corrida de 42 km"],
             ["baleia", "sereia", "girafa", "Na história, Pinóquio foi engolido por uma ____", "A ____ tem um pescoço longo"],
             ["chupeta", "camiseta", "bicicleta", "O bebê chorava porque derrubou sua ____", "Ele se machucou após cair de ____"]
             ]
             
    random.shuffle(words)
    
    trials = [0, 1] * 4
    random.shuffle(trials)
    prompt_msg = visual.TextStim(win=win, name='prompt_msg',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0.8), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='orange', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    word_msg = visual.TextStim(win=win, name='word_msg',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.2, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    main_task_resp = keyboard.Keyboard()
    
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
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('welcome.started', globalClock.getTime())
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
            endExperiment(thisExp, inputs=inputs, win=win)
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
    thisExp.addData('welcome.stopped', globalClock.getTime())
    # Run 'End Routine' code from welcome_code
    thisExp.addData('Código', participant_code)
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    study_instructions = data.TrialHandler(nReps=999, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='study_instructions')
    thisExp.addLoop(study_instructions)  # add the loop to the experiment
    thisStudy_instruction = study_instructions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStudy_instruction.rgb)
    if thisStudy_instruction != None:
        for paramName in thisStudy_instruction:
            globals()[paramName] = thisStudy_instruction[paramName]
    
    for thisStudy_instruction in study_instructions:
        currentLoop = study_instructions
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisStudy_instruction.rgb)
        if thisStudy_instruction != None:
            for paramName in thisStudy_instruction:
                globals()[paramName] = thisStudy_instruction[paramName]
        
        # --- Prepare to start Routine "instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instruction.started', globalClock.getTime())
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
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = instr_resp.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _instr_resp_allKeys.extend(theseKeys)
                if len(_instr_resp_allKeys):
                    instr_resp.keys = _instr_resp_allKeys[0].name  # just the first key pressed
                    instr_resp.rt = _instr_resp_allKeys[0].rt
                    instr_resp.duration = _instr_resp_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *instruction_images* updates
            
            # if instruction_images is starting this frame...
            if instruction_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instruction_images.frameNStart = frameN  # exact frame index
                instruction_images.tStart = t  # local t and not account for scr refresh
                instruction_images.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction_images, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_images.started')
                # update status
                instruction_images.status = STARTED
                instruction_images.setAutoDraw(True)
            
            # if instruction_images is active this frame...
            if instruction_images.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
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
        thisExp.addData('instruction.stopped', globalClock.getTime())
        # Run 'End Routine' code from instr_code
        thisExp.addData('Código', participant_code)
        
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
            study_instructions.finished = True # e encerra loop de estudo
            
        
        # check responses
        if instr_resp.keys in ['', [], None]:  # No response was made
            instr_resp.keys = None
        study_instructions.addData('instr_resp.keys',instr_resp.keys)
        if instr_resp.keys != None:  # we had a response
            study_instructions.addData('instr_resp.rt', instr_resp.rt)
            study_instructions.addData('instr_resp.duration', instr_resp.duration)
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 999 repeats of 'study_instructions'
    
    # get names of stimulus parameters
    if study_instructions.trialList in ([], [None], None):
        params = []
    else:
        params = study_instructions.trialList[0].keys()
    # save data for this loop
    study_instructions.saveAsExcel(filename + '.xlsx', sheetName='study_instructions',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    study_instructions.saveAsText(filename + 'study_instructions.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    main_task_trials = data.TrialHandler(nReps=len(words), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='main_task_trials')
    thisExp.addLoop(main_task_trials)  # add the loop to the experiment
    thisMain_task_trial = main_task_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMain_task_trial.rgb)
    if thisMain_task_trial != None:
        for paramName in thisMain_task_trial:
            globals()[paramName] = thisMain_task_trial[paramName]
    
    for thisMain_task_trial in main_task_trials:
        currentLoop = main_task_trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisMain_task_trial.rgb)
        if thisMain_task_trial != None:
            for paramName in thisMain_task_trial:
                globals()[paramName] = thisMain_task_trial[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation.started', globalClock.getTime())
        # keep track of which components have finished
        fixationComponents = [fixation_cross]
        for thisComponent in fixationComponents:
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
        
        # --- Run Routine "fixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            
            # if fixation_cross is starting this frame...
            if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.tStart = t  # local t and not account for scr refresh
                fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross.started')
                # update status
                fixation_cross.status = STARTED
                fixation_cross.setAutoDraw(True)
            
            # if fixation_cross is active this frame...
            if fixation_cross.status == STARTED:
                # update params
                pass
            
            # if fixation_cross is stopping this frame...
            if fixation_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross.tStop = t  # not accounting for scr refresh
                    fixation_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                    # update status
                    fixation_cross.status = FINISHED
                    fixation_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "main_task" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('main_task.started', globalClock.getTime())
        # Run 'Begin Routine' code from main_task_code
        aux = ""
        
        if my_condition == "structural":
            prompt = "A palavra está em maiúsculas?"
            if trials == 1:
                word = words[main_task_trials.thisN][0].upper()
                corr = 1
            elif trials == 0:
                word = words[main_task_trials.thisN][0].lower()
                corr = 0
                
        elif my_condition == "rhyme":   
            word = words[main_task_trials.thisN][0]
            if trials == 1:
                aux = words[main_task_trials.thisN][1]
                corr = 1
            elif trials == 0:
                aux = words[main_task_trials.thisN][2]
                corr = 0
            prompt = f"A palavra rima com {aux.upper()}?"
        
        elif my_condition == "sentence":
            word = words[main_task_trials.thisN][0]
            if trials == 1:
                aux = words[main_task_trials.thisN][3]
                corr = 1
            elif trials == 0:
                aux = words[main_task_trials.thisN][4]
                corr = 0
            prompt = f'A palavra se ajusta à frase \"{aux}\"?'
        prompt_msg.setText(prompt)
        word_msg.setText(word)
        main_task_resp.keys = []
        main_task_resp.rt = []
        _main_task_resp_allKeys = []
        # keep track of which components have finished
        main_taskComponents = [prompt_msg, word_msg, main_task_resp]
        for thisComponent in main_taskComponents:
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
        
        # --- Run Routine "main_task" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prompt_msg* updates
            
            # if prompt_msg is starting this frame...
            if prompt_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_msg.frameNStart = frameN  # exact frame index
                prompt_msg.tStart = t  # local t and not account for scr refresh
                prompt_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_msg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_msg.started')
                # update status
                prompt_msg.status = STARTED
                prompt_msg.setAutoDraw(True)
            
            # if prompt_msg is active this frame...
            if prompt_msg.status == STARTED:
                # update params
                pass
            
            # *word_msg* updates
            
            # if word_msg is starting this frame...
            if word_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                word_msg.frameNStart = frameN  # exact frame index
                word_msg.tStart = t  # local t and not account for scr refresh
                word_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word_msg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'word_msg.started')
                # update status
                word_msg.status = STARTED
                word_msg.setAutoDraw(True)
            
            # if word_msg is active this frame...
            if word_msg.status == STARTED:
                # update params
                pass
            
            # *main_task_resp* updates
            waitOnFlip = False
            
            # if main_task_resp is starting this frame...
            if main_task_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                main_task_resp.frameNStart = frameN  # exact frame index
                main_task_resp.tStart = t  # local t and not account for scr refresh
                main_task_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_task_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_task_resp.started')
                # update status
                main_task_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(main_task_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(main_task_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if main_task_resp.status == STARTED and not waitOnFlip:
                theseKeys = main_task_resp.getKeys(keyList=['1', '2', 'num_1', 'num_2'], ignoreKeys=["escape"], waitRelease=False)
                _main_task_resp_allKeys.extend(theseKeys)
                if len(_main_task_resp_allKeys):
                    main_task_resp.keys = _main_task_resp_allKeys[0].name  # just the first key pressed
                    main_task_resp.rt = _main_task_resp_allKeys[0].rt
                    main_task_resp.duration = _main_task_resp_allKeys[0].duration
                    # was this correct?
                    if (main_task_resp.keys == str(corr)) or (main_task_resp.keys == corr):
                        main_task_resp.corr = 1
                    else:
                        main_task_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in main_taskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "main_task" ---
        for thisComponent in main_taskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('main_task.stopped', globalClock.getTime())
        # Run 'End Routine' code from main_task_code
        thisExp.addData('Código', participant_code)
        thisExp.addData('word', word)
        thisExp.addData('corr', corr)
        thisExp.addData('condition', my_condition)
        # check responses
        if main_task_resp.keys in ['', [], None]:  # No response was made
            main_task_resp.keys = None
            # was no response the correct answer?!
            if str(corr).lower() == 'none':
               main_task_resp.corr = 1;  # correct non-response
            else:
               main_task_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for main_task_trials (TrialHandler)
        main_task_trials.addData('main_task_resp.keys',main_task_resp.keys)
        main_task_trials.addData('main_task_resp.corr', main_task_resp.corr)
        if main_task_resp.keys != None:  # we had a response
            main_task_trials.addData('main_task_resp.rt', main_task_resp.rt)
            main_task_trials.addData('main_task_resp.duration', main_task_resp.duration)
        # the Routine "main_task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed len(words) repeats of 'main_task_trials'
    
    # get names of stimulus parameters
    if main_task_trials.trialList in ([], [None], None):
        params = []
    else:
        params = main_task_trials.trialList[0].keys()
    # save data for this loop
    main_task_trials.saveAsExcel(filename + '.xlsx', sheetName='main_task_trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    main_task_trials.saveAsText(filename + 'main_task_trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "thanks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks.started', globalClock.getTime())
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
            endExperiment(thisExp, inputs=inputs, win=win)
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
    thisExp.addData('thanks.stopped', globalClock.getTime())
    # the Routine "thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # Run 'End Experiment' code from instr_code
    # código do participante
    thisExp.addData("participant_code", participant_code)
    
    # salvando duração da sessão...
    thisExp.addData("session_duration", globalClock.getTime())
    
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


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


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
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
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
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
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
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
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
