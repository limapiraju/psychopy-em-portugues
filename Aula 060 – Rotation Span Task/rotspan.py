#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.5),
    on dezembro 31, 2024, at 19:52
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


# Run 'Before Experiment' code from instr_code


# Run 'Before Experiment' code from instr_code


# Run 'Before Experiment' code from instr_code


# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.5'
expName = 'rotspan'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'ID': f"{randint(0, 999999):06.0f}",
    'Nome Completo': '',
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
    filename = u'data/%s_%s_%s_%s' % (expInfo['ID'].zfill(9), expName, expInfo['Nome Completo'], expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\limap\\OneDrive\\Documentos\\Psychology\\8. YouTube\\psychopy-em-portugues\\Aula 060 – Rotation Span Task\\rotspan.py',
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
    # Run 'Begin Experiment' code from welcome_code
    import random
    from os.path import exists
    
    expInfo["ID"] = expInfo["ID"].zfill(9)
    
    participant_code = expInfo["ID"]
    
    if not exists("unique_IDs.txt"):
        arquivo = open("unique_IDs.txt", "w")
        # cria cabeçalho do arquivo
        arquivo.write("ID_number\tName\n")
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
    welcome_next = visual.ImageStim(
        win=win,
        name='welcome_next', units='norm', 
        image='images/next_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    welcome_resp = event.Mouse(win=win)
    x, y = [None, None]
    welcome_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "instruction" ---
    # Run 'Begin Experiment' code from instr_code
    # índices de instruções
    current_instruction = 0
    instruction_block = 0
     
    instruction_list = [# arrow (memory) task
                       ["""
    Neste experimento, você tentará as posições e direções de setas que você verá na tela enquanto você avalia se as letras estão na posição normal ou invertida.
    
    Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a tarefa de memória com as setas.""",
    """
    Para essa prática, setas aparecerão na tela, em diferentes posições e direções. Tente lembrar a posição e direção de cada seta na ordem em que ela apareceu.
    
    Depois que 2 setas aparecerem, você verá uma tela com 16 setas. Seu trabalho é clicar nas setas na mesma ordem em que elas foram apresentadas. 
    
    Para fazer isso, use o mouse para clicar nas setas para selecioná-las. As setas selecionadas ficarão na cor azul.""",
    """
    Depois que selecionar todas as setas que compõem sua resposta, e elas estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.
    
    Se errar sua resposta, aperte o botão [Limpar] para começar novamente. Se esquecer a posição de uma das setas, aperte o botão [Branco] para marcar a posição que a seta esquecida deve estar.
    
    Lembre-se, é muito importante selecionar as setas na mesma ordem que foram apresentadas. Se você esquecer uma seta, use o botão [Branco] para marcar a sua posição.""",
    """
    Favor chamar o pesquisador se tiver alguma pergunta.
    
    Quando você estiver pronto, clique em [Avançar] para começar a prática com as setas.
    """], 
    # distractor (rotation) task
    ["""
    Agora você irá praticar a tarefa de rotação deste experimento. Nessa tarefa, você verá uma letra na tela. Essa letra poderá ou não estar rotacionada na tela.
    
    Sua tarefa será avaliar se a letra pode ser rotacionada em uma posição que ela corresponda a uma letra do nosso alfabeto.
    
    Depois que tiver avaliado a letra, clique no botão [Continuar].
    """,
    """
    Por exemplo, se aparecer na tela um "F", clique no botão [Sim], pois essa símbolo é uma letra do nosso alfabeto. Responda [Sim] mesmo que a letra apareça rotacionada na tela.
    
    Se aparecer na tela um "ꟻ", clique no botão [Não], pois esse símbolo não faz parte do nosso alfabeto. Responda [Não] mesmo que o "ꟻ" apareça rotacionado na tela.
    """,
    """
    Depois que clicar em um dos botões, o computador irá lhe dizer se fez a escolha certa.
    
    É muito importante que você consiga avaliar a letra, esteja ela rotacionada ou não. Também é importante que você consiga fazer essa avaliação o mais rapidamente possível.
    
    Favor chamar o pesquisador se você tiver perguntas.
    
    Quando você estiver pronto, clique em [Avançar] para começar a praticar.
    """],
    # ROTSPAN training
    ["""
    Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá avaliar as letras rotacionadas. Assim que decidir a sua resposta, uma seta aparecerá na tela. Tente se lembrar da posição dessa seta.
    
    Na etapa anterior na qual você apenas avaliou as letras, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar pela letra, pular a tela de resposta e contar o problema como erro.
    
    Por isso é muito importante você resolver os problemas o mais rápida e corretamente possível.""",
    """
    Depois que a seta desaparecer, outra letra irá aparecer, e depois outra seta. No final de cada sequência, uma tela de resposta aparecerá na tela. Use o mouse para indicar as posições e direções das setas que acabou de ver.
    
    Tente lembrar a ordem correta das setas. É muito importante que você trabalhe rapidamente e corretamente nas letras. Tenha certeza que você sabe a resposta do problema de rotação antes de ir para a próxima tela.
    """,
    """
    O computador não irá dizer se a resposta está correta. Depois da tela de resposta, você receberá o resultado do seu desempenho para o número setas lembradas e a porcentagem de respostas corretas nos problemas de rotação.
    
    Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas de rotação que você respondeu corretamente para o experimento inteiro.
    """,
    """
    É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas de rotação.
    
    Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas de rotação E lembrar o máximo de setas possíveis.
    
    Favor chamar o pesquisador se tiver perguntas.
    """
    ],
    # ROTSPAN testing
    ["""
    Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.
    
    Primeiro você terá que resolver um problema de rotação, depois terá que memorizar a posição e direção de uma seta. Quando ver a tela de resposta, indique as posições das setas na ordem em que foram apresentadas. Se esquecer de uma seta, clique no botão [Branco] para marcar onde a seta deve ir.
    
    Algumas combinações terão mais problemas de rotação e setas do que outras.
    """,
    """
    É importante que você faça o melhor possível nos problemas de rotação e na parte onde tiver que lembrar das setas. 
    
    Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas de rotação. Também lembre-se de acertar 85% dos problemas.
    
    Favor chamar o pesquisador se tiver alguma pergunta.
    
    Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
    """
    ]]
                       
    # cor do feedback das operações matemáticas
    rotation_color = [0.0000, 0.0000, 0.0000]
    
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
        units='norm', pos=[0,0], height=0.09, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    previous = visual.ImageStim(
        win=win,
        name='previous', units='norm', 
        image='images/previous_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    next = visual.ImageStim(
        win=win,
        name='next', units='norm', 
        image='images/next_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    instr_resp = event.Mouse(win=win)
    x, y = [None, None]
    instr_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "arrow_memory" ---
    # Run 'Begin Experiment' code from arrow_memory_code
    import string
    
    orientations = list(range(0, 360, 45)) * 2
    letters = string.ascii_uppercase[:16]
    positions = [(0, 0.1)] * 8 + [(0, 0.4), (0.165, 0.32), (0.225, 0.1), (0.165, -0.12),
                                  (0, -0.2), (-0.165, -0.12), (-0.225, 0.1), (-0.165, 0.32)]
    arrow_positions = list()
    
    for ori, pos, letter in zip(orientations, positions, letters):
        arrow_positions.append((ori, pos, letter))
    
    arrow_positions_list = list()
    
    for i in range(16):
        arrow_positions_list.append("")
    arrow = visual.ShapeStim(
        win=win, name='arrow', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=1.0, pos=[0,0], anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "recall" ---
    # Run 'Begin Experiment' code from code_recall
    def EditDistanceScore(target, recall):
        """
        Recebe duas strings que serão comparadas. Retorna o edit distance score,
        que consiste em len(target) – distância de Damerau–Levenshtein. Se a substração resultar em 
        valor negativo, fixa valor em 0.
        """
        # se strings são idênticas
        if recall == target:
            return len(target) # edit distance = tamanho da string
        # se nada foi lembrado
        elif recall == "": # edit distance = 0
            return 0
    
        stimDict = {target[0]: "0"}
    
        for targetIndex in range(0, len(target)):
            if target[targetIndex] not in stimDict:
                stimDict[target[targetIndex]] = "0"
    
        for recallIndex in range(0, len(recall)):
            if recall[recallIndex] not in stimDict:
                stimDict[recall[recallIndex]] = "0"
    
        disMatrix = np.zeros(shape=(len(target) + 2, len(recall) + 2))
    
        inf = len(target) + len(recall)
    
        for targetIndex in range(0, len(target) + 1):
            disMatrix[targetIndex + 1, 0] = inf
            disMatrix[targetIndex + 1, 1] = targetIndex
    
        for recallIndex in range(0, len(recall)+1):
            disMatrix[0, recallIndex + 1] = inf
            disMatrix[1, recallIndex + 1] = recallIndex
    
        for targetIndex in range(1, len(target)+1):
            present = 0
            for recallIndex in range(1, len(recall) + 1):
                if recall[recallIndex-1] in stimDict:
                    targetIndex2 = int(stimDict[recall[recallIndex - 1]])
    
                recallIndex2 = present
                cost = 1
    
                if target[targetIndex - 1] == recall[recallIndex - 1]:
                    cost = 0
                    present = recallIndex
    
                Substitution = disMatrix[targetIndex, recallIndex] + cost
                Insertion = disMatrix[targetIndex + 1, recallIndex] + 1
                Deletion = disMatrix[targetIndex, recallIndex + 1] + 1
                Transposition = disMatrix[targetIndex2, recallIndex2] + (targetIndex - targetIndex2 - 1) + 1 + (recallIndex - recallIndex2 - 1)
    
                if Substitution < Insertion and Substitution < Deletion and Substitution < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Substitution
                elif Insertion < Deletion and Insertion < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Insertion
                elif Deletion < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Deletion
                else:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Transposition
    
    
            stimDict[target[targetIndex - 1]] = str(targetIndex)
    
        # se edit distance < 0, fixa valor em zero
        if len(target) - disMatrix[len(target) + 1, len(recall) + 1] < 0:
            return 0
        # caso contrário, retorna o valor da medida
        else:
            return(int(len(target) - disMatrix[len(target) + 1, len(recall) + 1]))
    
    def partial_credit(string1, string2):
        score = 0
        for letter1, letter2 in zip(string1, string2):
            if letter1 == letter2:
                score += 1
                
        return score
    
    final_full_credit_score = final_partial_credit_score = final_edit_distance_score = 0
    
    
    prompt_recall = visual.TextStim(win=win, name='prompt_recall',
        text='Selecione as setas na mesma ordem em que foram apresentadas. Use o botão [Branco] para indicar as setas que esqueceu.',
        font='Times New Roman',
        units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    A = visual.ShapeStim(
        win=win, name='A', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=0.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-2.0, interpolate=True)
    B = visual.ShapeStim(
        win=win, name='B', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=45.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-3.0, interpolate=True)
    C = visual.ShapeStim(
        win=win, name='C', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=90.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-4.0, interpolate=True)
    D = visual.ShapeStim(
        win=win, name='D', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=135.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-5.0, interpolate=True)
    E = visual.ShapeStim(
        win=win, name='E', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=180.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-6.0, interpolate=True)
    F = visual.ShapeStim(
        win=win, name='F', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=225.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-7.0, interpolate=True)
    G = visual.ShapeStim(
        win=win, name='G', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=270.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-8.0, interpolate=True)
    H = visual.ShapeStim(
        win=win, name='H', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=315.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-9.0, interpolate=True)
    I = visual.ShapeStim(
        win=win, name='I', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=0.0, pos=(0, 0.4), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-10.0, interpolate=True)
    J = visual.ShapeStim(
        win=win, name='J', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=45.0, pos=(0.165, 0.32), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-11.0, interpolate=True)
    K = visual.ShapeStim(
        win=win, name='K', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=90.0, pos=(0.225, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-12.0, interpolate=True)
    L = visual.ShapeStim(
        win=win, name='L', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=135.0, pos=(0.165, -0.12), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-13.0, interpolate=True)
    M = visual.ShapeStim(
        win=win, name='M', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=180.0, pos=(0, -0.2), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-14.0, interpolate=True)
    N = visual.ShapeStim(
        win=win, name='N', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=225.0, pos=(-0.165, -0.12), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-15.0, interpolate=True)
    O = visual.ShapeStim(
        win=win, name='O', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=270.0, pos=(-0.225, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-16.0, interpolate=True)
    P = visual.ShapeStim(
        win=win, name='P', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=315.0, pos=(-0.165, 0.32), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-17.0, interpolate=True)
    clear_ = visual.ImageStim(
        win=win,
        name='clear_', units='norm', 
        image='images/clear_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-18.0)
    blank = visual.ImageStim(
        win=win,
        name='blank', units='norm', 
        image='images/blank_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-19.0)
    send = visual.ImageStim(
        win=win,
        name='send', units='norm', 
        image='images/send_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-20.0)
    square = visual.Rect(
        win=win, name='square',units='height', 
        width=(0.075, 0.075)[0], height=(0.075, 0.075)[1],
        ori=0.0, pos=(0, 0.05), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
        opacity=0.0, depth=-21.0, interpolate=True)
    recall_response = event.Mouse(win=win)
    x, y = [None, None]
    recall_response.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "recall_feedback" ---
    recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    rotation_feedback_prompt = visual.TextStim(win=win, name='rotation_feedback_prompt',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    rotation_feedback_performance = visual.TextStim(win=win, name='rotation_feedback_performance',
        text='',
        font='Times New Roman',
        units='norm', pos=(0.9, 0.9), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "instruction" ---
    # Run 'Begin Experiment' code from instr_code
    # índices de instruções
    current_instruction = 0
    instruction_block = 0
     
    instruction_list = [# arrow (memory) task
                       ["""
    Neste experimento, você tentará as posições e direções de setas que você verá na tela enquanto você avalia se as letras estão na posição normal ou invertida.
    
    Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a tarefa de memória com as setas.""",
    """
    Para essa prática, setas aparecerão na tela, em diferentes posições e direções. Tente lembrar a posição e direção de cada seta na ordem em que ela apareceu.
    
    Depois que 2 setas aparecerem, você verá uma tela com 16 setas. Seu trabalho é clicar nas setas na mesma ordem em que elas foram apresentadas. 
    
    Para fazer isso, use o mouse para clicar nas setas para selecioná-las. As setas selecionadas ficarão na cor azul.""",
    """
    Depois que selecionar todas as setas que compõem sua resposta, e elas estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.
    
    Se errar sua resposta, aperte o botão [Limpar] para começar novamente. Se esquecer a posição de uma das setas, aperte o botão [Branco] para marcar a posição que a seta esquecida deve estar.
    
    Lembre-se, é muito importante selecionar as setas na mesma ordem que foram apresentadas. Se você esquecer uma seta, use o botão [Branco] para marcar a sua posição.""",
    """
    Favor chamar o pesquisador se tiver alguma pergunta.
    
    Quando você estiver pronto, clique em [Avançar] para começar a prática com as setas.
    """], 
    # distractor (rotation) task
    ["""
    Agora você irá praticar a tarefa de rotação deste experimento. Nessa tarefa, você verá uma letra na tela. Essa letra poderá ou não estar rotacionada na tela.
    
    Sua tarefa será avaliar se a letra pode ser rotacionada em uma posição que ela corresponda a uma letra do nosso alfabeto.
    
    Depois que tiver avaliado a letra, clique no botão [Continuar].
    """,
    """
    Por exemplo, se aparecer na tela um "F", clique no botão [Sim], pois essa símbolo é uma letra do nosso alfabeto. Responda [Sim] mesmo que a letra apareça rotacionada na tela.
    
    Se aparecer na tela um "ꟻ", clique no botão [Não], pois esse símbolo não faz parte do nosso alfabeto. Responda [Não] mesmo que o "ꟻ" apareça rotacionado na tela.
    """,
    """
    Depois que clicar em um dos botões, o computador irá lhe dizer se fez a escolha certa.
    
    É muito importante que você consiga avaliar a letra, esteja ela rotacionada ou não. Também é importante que você consiga fazer essa avaliação o mais rapidamente possível.
    
    Favor chamar o pesquisador se você tiver perguntas.
    
    Quando você estiver pronto, clique em [Avançar] para começar a praticar.
    """],
    # ROTSPAN training
    ["""
    Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá avaliar as letras rotacionadas. Assim que decidir a sua resposta, uma seta aparecerá na tela. Tente se lembrar da posição dessa seta.
    
    Na etapa anterior na qual você apenas avaliou as letras, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar pela letra, pular a tela de resposta e contar o problema como erro.
    
    Por isso é muito importante você resolver os problemas o mais rápida e corretamente possível.""",
    """
    Depois que a seta desaparecer, outra letra irá aparecer, e depois outra seta. No final de cada sequência, uma tela de resposta aparecerá na tela. Use o mouse para indicar as posições e direções das setas que acabou de ver.
    
    Tente lembrar a ordem correta das setas. É muito importante que você trabalhe rapidamente e corretamente nas letras. Tenha certeza que você sabe a resposta do problema de rotação antes de ir para a próxima tela.
    """,
    """
    O computador não irá dizer se a resposta está correta. Depois da tela de resposta, você receberá o resultado do seu desempenho para o número setas lembradas e a porcentagem de respostas corretas nos problemas de rotação.
    
    Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas de rotação que você respondeu corretamente para o experimento inteiro.
    """,
    """
    É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas de rotação.
    
    Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas de rotação E lembrar o máximo de setas possíveis.
    
    Favor chamar o pesquisador se tiver perguntas.
    """
    ],
    # ROTSPAN testing
    ["""
    Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.
    
    Primeiro você terá que resolver um problema de rotação, depois terá que memorizar a posição e direção de uma seta. Quando ver a tela de resposta, indique as posições das setas na ordem em que foram apresentadas. Se esquecer de uma seta, clique no botão [Branco] para marcar onde a seta deve ir.
    
    Algumas combinações terão mais problemas de rotação e setas do que outras.
    """,
    """
    É importante que você faça o melhor possível nos problemas de rotação e na parte onde tiver que lembrar das setas. 
    
    Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas de rotação. Também lembre-se de acertar 85% dos problemas.
    
    Favor chamar o pesquisador se tiver alguma pergunta.
    
    Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
    """
    ]]
                       
    # cor do feedback das operações matemáticas
    rotation_color = [0.0000, 0.0000, 0.0000]
    
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
        units='norm', pos=[0,0], height=0.09, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    previous = visual.ImageStim(
        win=win,
        name='previous', units='norm', 
        image='images/previous_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    next = visual.ImageStim(
        win=win,
        name='next', units='norm', 
        image='images/next_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    instr_resp = event.Mouse(win=win)
    x, y = [None, None]
    instr_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "rotation" ---
    # Run 'Begin Experiment' code from rotation_code
    # cria lista de estímulos
    letters = list("GFR") * 2
    oris = list(range(0, 360, 45))
    flips = (True, False)
    stimuli = list()
    
    for flip in flips:
        if flip:
            temp = "no"
        else:
            temp = "yes"
        for letter in letters:
            for ori in oris:
                stimuli.append((letter, ori, flip, temp))
    
    random.shuffle(stimuli)
        
    # contador de letras
    letter_count = 0
    
    # contador de tentativas e acertos na tarefa de simetria
    rotation_total_trials = rotation_trials_correct = speed_errors = 0
    abort_trial = False # controla interrupção da tarefa de rotação
    
    # contador de tempo no treino
    rotation_training_time = list()
    
    rotation_prompt = visual.TextStim(win=win, name='rotation_prompt',
        text='Quando você tiver resolvido o problema, clique em [Continuar]',
        font='Times New Roman',
        units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    continue_ = visual.ImageStim(
        win=win,
        name='continue_', units='norm', 
        image='images/continue_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    symmetry_problem_next = event.Mouse(win=win)
    x, y = [None, None]
    symmetry_problem_next.mouseClock = core.Clock()
    rotation_problem = visual.TextStim(win=win, name='rotation_problem',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0.2), height=0.3, wrapWidth=1.8, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "rotation_answer" ---
    rotation_answer_screen = visual.TextStim(win=win, name='rotation_answer_screen',
        text='A letra está virada do lado correto?',
        font='Times New Roman',
        units='norm', pos=(0, 0.6), height=0.15, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    yes = visual.ImageStim(
        win=win,
        name='yes', units='norm', 
        image='images/yes_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    no = visual.ImageStim(
        win=win,
        name='no', units='norm', 
        image='images/no_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    rotation_response = event.Mouse(win=win)
    x, y = [None, None]
    rotation_response.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "rotation_answer_feedback" ---
    true_feedback = visual.ImageStim(
        win=win,
        name='true_feedback', units='norm', 
        image='images/yes_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    false_feedback = visual.ImageStim(
        win=win,
        name='false_feedback', units='norm', 
        image='images/no_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    rotation_corrective_feedback_msg = visual.TextStim(win=win, name='rotation_corrective_feedback_msg',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, -0.6), height=0.2, wrapWidth=1.8, ori=0.0, 
        color=[-1.0000, -1.0000, 0.0902], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "instruction" ---
    # Run 'Begin Experiment' code from instr_code
    # índices de instruções
    current_instruction = 0
    instruction_block = 0
     
    instruction_list = [# arrow (memory) task
                       ["""
    Neste experimento, você tentará as posições e direções de setas que você verá na tela enquanto você avalia se as letras estão na posição normal ou invertida.
    
    Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a tarefa de memória com as setas.""",
    """
    Para essa prática, setas aparecerão na tela, em diferentes posições e direções. Tente lembrar a posição e direção de cada seta na ordem em que ela apareceu.
    
    Depois que 2 setas aparecerem, você verá uma tela com 16 setas. Seu trabalho é clicar nas setas na mesma ordem em que elas foram apresentadas. 
    
    Para fazer isso, use o mouse para clicar nas setas para selecioná-las. As setas selecionadas ficarão na cor azul.""",
    """
    Depois que selecionar todas as setas que compõem sua resposta, e elas estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.
    
    Se errar sua resposta, aperte o botão [Limpar] para começar novamente. Se esquecer a posição de uma das setas, aperte o botão [Branco] para marcar a posição que a seta esquecida deve estar.
    
    Lembre-se, é muito importante selecionar as setas na mesma ordem que foram apresentadas. Se você esquecer uma seta, use o botão [Branco] para marcar a sua posição.""",
    """
    Favor chamar o pesquisador se tiver alguma pergunta.
    
    Quando você estiver pronto, clique em [Avançar] para começar a prática com as setas.
    """], 
    # distractor (rotation) task
    ["""
    Agora você irá praticar a tarefa de rotação deste experimento. Nessa tarefa, você verá uma letra na tela. Essa letra poderá ou não estar rotacionada na tela.
    
    Sua tarefa será avaliar se a letra pode ser rotacionada em uma posição que ela corresponda a uma letra do nosso alfabeto.
    
    Depois que tiver avaliado a letra, clique no botão [Continuar].
    """,
    """
    Por exemplo, se aparecer na tela um "F", clique no botão [Sim], pois essa símbolo é uma letra do nosso alfabeto. Responda [Sim] mesmo que a letra apareça rotacionada na tela.
    
    Se aparecer na tela um "ꟻ", clique no botão [Não], pois esse símbolo não faz parte do nosso alfabeto. Responda [Não] mesmo que o "ꟻ" apareça rotacionado na tela.
    """,
    """
    Depois que clicar em um dos botões, o computador irá lhe dizer se fez a escolha certa.
    
    É muito importante que você consiga avaliar a letra, esteja ela rotacionada ou não. Também é importante que você consiga fazer essa avaliação o mais rapidamente possível.
    
    Favor chamar o pesquisador se você tiver perguntas.
    
    Quando você estiver pronto, clique em [Avançar] para começar a praticar.
    """],
    # ROTSPAN training
    ["""
    Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá avaliar as letras rotacionadas. Assim que decidir a sua resposta, uma seta aparecerá na tela. Tente se lembrar da posição dessa seta.
    
    Na etapa anterior na qual você apenas avaliou as letras, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar pela letra, pular a tela de resposta e contar o problema como erro.
    
    Por isso é muito importante você resolver os problemas o mais rápida e corretamente possível.""",
    """
    Depois que a seta desaparecer, outra letra irá aparecer, e depois outra seta. No final de cada sequência, uma tela de resposta aparecerá na tela. Use o mouse para indicar as posições e direções das setas que acabou de ver.
    
    Tente lembrar a ordem correta das setas. É muito importante que você trabalhe rapidamente e corretamente nas letras. Tenha certeza que você sabe a resposta do problema de rotação antes de ir para a próxima tela.
    """,
    """
    O computador não irá dizer se a resposta está correta. Depois da tela de resposta, você receberá o resultado do seu desempenho para o número setas lembradas e a porcentagem de respostas corretas nos problemas de rotação.
    
    Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas de rotação que você respondeu corretamente para o experimento inteiro.
    """,
    """
    É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas de rotação.
    
    Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas de rotação E lembrar o máximo de setas possíveis.
    
    Favor chamar o pesquisador se tiver perguntas.
    """
    ],
    # ROTSPAN testing
    ["""
    Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.
    
    Primeiro você terá que resolver um problema de rotação, depois terá que memorizar a posição e direção de uma seta. Quando ver a tela de resposta, indique as posições das setas na ordem em que foram apresentadas. Se esquecer de uma seta, clique no botão [Branco] para marcar onde a seta deve ir.
    
    Algumas combinações terão mais problemas de rotação e setas do que outras.
    """,
    """
    É importante que você faça o melhor possível nos problemas de rotação e na parte onde tiver que lembrar das setas. 
    
    Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas de rotação. Também lembre-se de acertar 85% dos problemas.
    
    Favor chamar o pesquisador se tiver alguma pergunta.
    
    Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
    """
    ]]
                       
    # cor do feedback das operações matemáticas
    rotation_color = [0.0000, 0.0000, 0.0000]
    
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
        units='norm', pos=[0,0], height=0.09, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    previous = visual.ImageStim(
        win=win,
        name='previous', units='norm', 
        image='images/previous_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    next = visual.ImageStim(
        win=win,
        name='next', units='norm', 
        image='images/next_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    instr_resp = event.Mouse(win=win)
    x, y = [None, None]
    instr_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "rotation" ---
    # Run 'Begin Experiment' code from rotation_code
    # cria lista de estímulos
    letters = list("GFR") * 2
    oris = list(range(0, 360, 45))
    flips = (True, False)
    stimuli = list()
    
    for flip in flips:
        if flip:
            temp = "no"
        else:
            temp = "yes"
        for letter in letters:
            for ori in oris:
                stimuli.append((letter, ori, flip, temp))
    
    random.shuffle(stimuli)
        
    # contador de letras
    letter_count = 0
    
    # contador de tentativas e acertos na tarefa de simetria
    rotation_total_trials = rotation_trials_correct = speed_errors = 0
    abort_trial = False # controla interrupção da tarefa de rotação
    
    # contador de tempo no treino
    rotation_training_time = list()
    
    rotation_prompt = visual.TextStim(win=win, name='rotation_prompt',
        text='Quando você tiver resolvido o problema, clique em [Continuar]',
        font='Times New Roman',
        units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    continue_ = visual.ImageStim(
        win=win,
        name='continue_', units='norm', 
        image='images/continue_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    symmetry_problem_next = event.Mouse(win=win)
    x, y = [None, None]
    symmetry_problem_next.mouseClock = core.Clock()
    rotation_problem = visual.TextStim(win=win, name='rotation_problem',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0.2), height=0.3, wrapWidth=1.8, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "rotation_answer" ---
    rotation_answer_screen = visual.TextStim(win=win, name='rotation_answer_screen',
        text='A letra está virada do lado correto?',
        font='Times New Roman',
        units='norm', pos=(0, 0.6), height=0.15, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    yes = visual.ImageStim(
        win=win,
        name='yes', units='norm', 
        image='images/yes_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    no = visual.ImageStim(
        win=win,
        name='no', units='norm', 
        image='images/no_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    rotation_response = event.Mouse(win=win)
    x, y = [None, None]
    rotation_response.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "arrow_memory" ---
    # Run 'Begin Experiment' code from arrow_memory_code
    import string
    
    orientations = list(range(0, 360, 45)) * 2
    letters = string.ascii_uppercase[:16]
    positions = [(0, 0.1)] * 8 + [(0, 0.4), (0.165, 0.32), (0.225, 0.1), (0.165, -0.12),
                                  (0, -0.2), (-0.165, -0.12), (-0.225, 0.1), (-0.165, 0.32)]
    arrow_positions = list()
    
    for ori, pos, letter in zip(orientations, positions, letters):
        arrow_positions.append((ori, pos, letter))
    
    arrow_positions_list = list()
    
    for i in range(16):
        arrow_positions_list.append("")
    arrow = visual.ShapeStim(
        win=win, name='arrow', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=1.0, pos=[0,0], anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "recall" ---
    # Run 'Begin Experiment' code from code_recall
    def EditDistanceScore(target, recall):
        """
        Recebe duas strings que serão comparadas. Retorna o edit distance score,
        que consiste em len(target) – distância de Damerau–Levenshtein. Se a substração resultar em 
        valor negativo, fixa valor em 0.
        """
        # se strings são idênticas
        if recall == target:
            return len(target) # edit distance = tamanho da string
        # se nada foi lembrado
        elif recall == "": # edit distance = 0
            return 0
    
        stimDict = {target[0]: "0"}
    
        for targetIndex in range(0, len(target)):
            if target[targetIndex] not in stimDict:
                stimDict[target[targetIndex]] = "0"
    
        for recallIndex in range(0, len(recall)):
            if recall[recallIndex] not in stimDict:
                stimDict[recall[recallIndex]] = "0"
    
        disMatrix = np.zeros(shape=(len(target) + 2, len(recall) + 2))
    
        inf = len(target) + len(recall)
    
        for targetIndex in range(0, len(target) + 1):
            disMatrix[targetIndex + 1, 0] = inf
            disMatrix[targetIndex + 1, 1] = targetIndex
    
        for recallIndex in range(0, len(recall)+1):
            disMatrix[0, recallIndex + 1] = inf
            disMatrix[1, recallIndex + 1] = recallIndex
    
        for targetIndex in range(1, len(target)+1):
            present = 0
            for recallIndex in range(1, len(recall) + 1):
                if recall[recallIndex-1] in stimDict:
                    targetIndex2 = int(stimDict[recall[recallIndex - 1]])
    
                recallIndex2 = present
                cost = 1
    
                if target[targetIndex - 1] == recall[recallIndex - 1]:
                    cost = 0
                    present = recallIndex
    
                Substitution = disMatrix[targetIndex, recallIndex] + cost
                Insertion = disMatrix[targetIndex + 1, recallIndex] + 1
                Deletion = disMatrix[targetIndex, recallIndex + 1] + 1
                Transposition = disMatrix[targetIndex2, recallIndex2] + (targetIndex - targetIndex2 - 1) + 1 + (recallIndex - recallIndex2 - 1)
    
                if Substitution < Insertion and Substitution < Deletion and Substitution < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Substitution
                elif Insertion < Deletion and Insertion < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Insertion
                elif Deletion < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Deletion
                else:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Transposition
    
    
            stimDict[target[targetIndex - 1]] = str(targetIndex)
    
        # se edit distance < 0, fixa valor em zero
        if len(target) - disMatrix[len(target) + 1, len(recall) + 1] < 0:
            return 0
        # caso contrário, retorna o valor da medida
        else:
            return(int(len(target) - disMatrix[len(target) + 1, len(recall) + 1]))
    
    def partial_credit(string1, string2):
        score = 0
        for letter1, letter2 in zip(string1, string2):
            if letter1 == letter2:
                score += 1
                
        return score
    
    final_full_credit_score = final_partial_credit_score = final_edit_distance_score = 0
    
    
    prompt_recall = visual.TextStim(win=win, name='prompt_recall',
        text='Selecione as setas na mesma ordem em que foram apresentadas. Use o botão [Branco] para indicar as setas que esqueceu.',
        font='Times New Roman',
        units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    A = visual.ShapeStim(
        win=win, name='A', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=0.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-2.0, interpolate=True)
    B = visual.ShapeStim(
        win=win, name='B', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=45.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-3.0, interpolate=True)
    C = visual.ShapeStim(
        win=win, name='C', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=90.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-4.0, interpolate=True)
    D = visual.ShapeStim(
        win=win, name='D', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=135.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-5.0, interpolate=True)
    E = visual.ShapeStim(
        win=win, name='E', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=180.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-6.0, interpolate=True)
    F = visual.ShapeStim(
        win=win, name='F', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=225.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-7.0, interpolate=True)
    G = visual.ShapeStim(
        win=win, name='G', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=270.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-8.0, interpolate=True)
    H = visual.ShapeStim(
        win=win, name='H', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=315.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-9.0, interpolate=True)
    I = visual.ShapeStim(
        win=win, name='I', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=0.0, pos=(0, 0.4), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-10.0, interpolate=True)
    J = visual.ShapeStim(
        win=win, name='J', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=45.0, pos=(0.165, 0.32), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-11.0, interpolate=True)
    K = visual.ShapeStim(
        win=win, name='K', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=90.0, pos=(0.225, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-12.0, interpolate=True)
    L = visual.ShapeStim(
        win=win, name='L', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=135.0, pos=(0.165, -0.12), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-13.0, interpolate=True)
    M = visual.ShapeStim(
        win=win, name='M', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=180.0, pos=(0, -0.2), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-14.0, interpolate=True)
    N = visual.ShapeStim(
        win=win, name='N', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=225.0, pos=(-0.165, -0.12), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-15.0, interpolate=True)
    O = visual.ShapeStim(
        win=win, name='O', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=270.0, pos=(-0.225, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-16.0, interpolate=True)
    P = visual.ShapeStim(
        win=win, name='P', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=315.0, pos=(-0.165, 0.32), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-17.0, interpolate=True)
    clear_ = visual.ImageStim(
        win=win,
        name='clear_', units='norm', 
        image='images/clear_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-18.0)
    blank = visual.ImageStim(
        win=win,
        name='blank', units='norm', 
        image='images/blank_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-19.0)
    send = visual.ImageStim(
        win=win,
        name='send', units='norm', 
        image='images/send_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-20.0)
    square = visual.Rect(
        win=win, name='square',units='height', 
        width=(0.075, 0.075)[0], height=(0.075, 0.075)[1],
        ori=0.0, pos=(0, 0.05), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
        opacity=0.0, depth=-21.0, interpolate=True)
    recall_response = event.Mouse(win=win)
    x, y = [None, None]
    recall_response.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "recall_feedback" ---
    recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    rotation_feedback_prompt = visual.TextStim(win=win, name='rotation_feedback_prompt',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    rotation_feedback_performance = visual.TextStim(win=win, name='rotation_feedback_performance',
        text='',
        font='Times New Roman',
        units='norm', pos=(0.9, 0.9), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "instruction" ---
    # Run 'Begin Experiment' code from instr_code
    # índices de instruções
    current_instruction = 0
    instruction_block = 0
     
    instruction_list = [# arrow (memory) task
                       ["""
    Neste experimento, você tentará as posições e direções de setas que você verá na tela enquanto você avalia se as letras estão na posição normal ou invertida.
    
    Nos próximos minutos, você irá praticar para se familiarizar com o experimento. Nós começaremos praticando a tarefa de memória com as setas.""",
    """
    Para essa prática, setas aparecerão na tela, em diferentes posições e direções. Tente lembrar a posição e direção de cada seta na ordem em que ela apareceu.
    
    Depois que 2 setas aparecerem, você verá uma tela com 16 setas. Seu trabalho é clicar nas setas na mesma ordem em que elas foram apresentadas. 
    
    Para fazer isso, use o mouse para clicar nas setas para selecioná-las. As setas selecionadas ficarão na cor azul.""",
    """
    Depois que selecionar todas as setas que compõem sua resposta, e elas estiverem na ordem correta, clique no botão [Enviar] no canto inferior direito da tela.
    
    Se errar sua resposta, aperte o botão [Limpar] para começar novamente. Se esquecer a posição de uma das setas, aperte o botão [Branco] para marcar a posição que a seta esquecida deve estar.
    
    Lembre-se, é muito importante selecionar as setas na mesma ordem que foram apresentadas. Se você esquecer uma seta, use o botão [Branco] para marcar a sua posição.""",
    """
    Favor chamar o pesquisador se tiver alguma pergunta.
    
    Quando você estiver pronto, clique em [Avançar] para começar a prática com as setas.
    """], 
    # distractor (rotation) task
    ["""
    Agora você irá praticar a tarefa de rotação deste experimento. Nessa tarefa, você verá uma letra na tela. Essa letra poderá ou não estar rotacionada na tela.
    
    Sua tarefa será avaliar se a letra pode ser rotacionada em uma posição que ela corresponda a uma letra do nosso alfabeto.
    
    Depois que tiver avaliado a letra, clique no botão [Continuar].
    """,
    """
    Por exemplo, se aparecer na tela um "F", clique no botão [Sim], pois essa símbolo é uma letra do nosso alfabeto. Responda [Sim] mesmo que a letra apareça rotacionada na tela.
    
    Se aparecer na tela um "ꟻ", clique no botão [Não], pois esse símbolo não faz parte do nosso alfabeto. Responda [Não] mesmo que o "ꟻ" apareça rotacionado na tela.
    """,
    """
    Depois que clicar em um dos botões, o computador irá lhe dizer se fez a escolha certa.
    
    É muito importante que você consiga avaliar a letra, esteja ela rotacionada ou não. Também é importante que você consiga fazer essa avaliação o mais rapidamente possível.
    
    Favor chamar o pesquisador se você tiver perguntas.
    
    Quando você estiver pronto, clique em [Avançar] para começar a praticar.
    """],
    # ROTSPAN training
    ["""
    Agora você irá praticar as duas partes do experimento ao mesmo tempo. Na próxima prática, você irá avaliar as letras rotacionadas. Assim que decidir a sua resposta, uma seta aparecerá na tela. Tente se lembrar da posição dessa seta.
    
    Na etapa anterior na qual você apenas avaliou as letras, o computador calculou o seu tempo médio para resolver os problemas. Se você demorar mais que o tempo médio, o computador irá automaticamente passar pela letra, pular a tela de resposta e contar o problema como erro.
    
    Por isso é muito importante você resolver os problemas o mais rápida e corretamente possível.""",
    """
    Depois que a seta desaparecer, outra letra irá aparecer, e depois outra seta. No final de cada sequência, uma tela de resposta aparecerá na tela. Use o mouse para indicar as posições e direções das setas que acabou de ver.
    
    Tente lembrar a ordem correta das setas. É muito importante que você trabalhe rapidamente e corretamente nas letras. Tenha certeza que você sabe a resposta do problema de rotação antes de ir para a próxima tela.
    """,
    """
    O computador não irá dizer se a resposta está correta. Depois da tela de resposta, você receberá o resultado do seu desempenho para o número setas lembradas e a porcentagem de respostas corretas nos problemas de rotação.
    
    Durante o resultado, você verá um número vermelho no canto direito na parte de cima da tela. Isso indica a porcentagem de problemas de rotação que você respondeu corretamente para o experimento inteiro.
    """,
    """
    É muito importante que a porcentagem seja no mínimo 85%. Para o nosso experimento, só podemos usar dados de pessoas com no mínimo 85% de respostas corretas nos problemas de rotação.
    
    Para você ser chamado novamente para participar em futuros experimentos, você deve responder no mínimo 85% de respostas corretas nos problemas de rotação E lembrar o máximo de setas possíveis.
    
    Favor chamar o pesquisador se tiver perguntas.
    """
    ],
    # ROTSPAN testing
    ["""
    Este é o final da prática. O experimento de verdade será igual a prática que acabou de completar.
    
    Primeiro você terá que resolver um problema de rotação, depois terá que memorizar a posição e direção de uma seta. Quando ver a tela de resposta, indique as posições das setas na ordem em que foram apresentadas. Se esquecer de uma seta, clique no botão [Branco] para marcar onde a seta deve ir.
    
    Algumas combinações terão mais problemas de rotação e setas do que outras.
    """,
    """
    É importante que você faça o melhor possível nos problemas de rotação e na parte onde tiver que lembrar das setas. 
    
    Lembre-se de trabalhar o mais rápido e corretamente possível nos problemas de rotação. Também lembre-se de acertar 85% dos problemas.
    
    Favor chamar o pesquisador se tiver alguma pergunta.
    
    Quando você estiver pronto, clique em [Avançar] para começar a tarefa.
    """
    ]]
                       
    # cor do feedback das operações matemáticas
    rotation_color = [0.0000, 0.0000, 0.0000]
    
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
        units='norm', pos=[0,0], height=0.09, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    previous = visual.ImageStim(
        win=win,
        name='previous', units='norm', 
        image='images/previous_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    next = visual.ImageStim(
        win=win,
        name='next', units='norm', 
        image='images/next_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    instr_resp = event.Mouse(win=win)
    x, y = [None, None]
    instr_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "rotation" ---
    # Run 'Begin Experiment' code from rotation_code
    # cria lista de estímulos
    letters = list("GFR") * 2
    oris = list(range(0, 360, 45))
    flips = (True, False)
    stimuli = list()
    
    for flip in flips:
        if flip:
            temp = "no"
        else:
            temp = "yes"
        for letter in letters:
            for ori in oris:
                stimuli.append((letter, ori, flip, temp))
    
    random.shuffle(stimuli)
        
    # contador de letras
    letter_count = 0
    
    # contador de tentativas e acertos na tarefa de simetria
    rotation_total_trials = rotation_trials_correct = speed_errors = 0
    abort_trial = False # controla interrupção da tarefa de rotação
    
    # contador de tempo no treino
    rotation_training_time = list()
    
    rotation_prompt = visual.TextStim(win=win, name='rotation_prompt',
        text='Quando você tiver resolvido o problema, clique em [Continuar]',
        font='Times New Roman',
        units='norm', pos=(0, -0.5), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    continue_ = visual.ImageStim(
        win=win,
        name='continue_', units='norm', 
        image='images/continue_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.0, -0.8), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    symmetry_problem_next = event.Mouse(win=win)
    x, y = [None, None]
    symmetry_problem_next.mouseClock = core.Clock()
    rotation_problem = visual.TextStim(win=win, name='rotation_problem',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0.2), height=0.3, wrapWidth=1.8, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "rotation_answer" ---
    rotation_answer_screen = visual.TextStim(win=win, name='rotation_answer_screen',
        text='A letra está virada do lado correto?',
        font='Times New Roman',
        units='norm', pos=(0, 0.6), height=0.15, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    yes = visual.ImageStim(
        win=win,
        name='yes', units='norm', 
        image='images/yes_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    no = visual.ImageStim(
        win=win,
        name='no', units='norm', 
        image='images/no_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.35, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    rotation_response = event.Mouse(win=win)
    x, y = [None, None]
    rotation_response.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "arrow_memory" ---
    # Run 'Begin Experiment' code from arrow_memory_code
    import string
    
    orientations = list(range(0, 360, 45)) * 2
    letters = string.ascii_uppercase[:16]
    positions = [(0, 0.1)] * 8 + [(0, 0.4), (0.165, 0.32), (0.225, 0.1), (0.165, -0.12),
                                  (0, -0.2), (-0.165, -0.12), (-0.225, 0.1), (-0.165, 0.32)]
    arrow_positions = list()
    
    for ori, pos, letter in zip(orientations, positions, letters):
        arrow_positions.append((ori, pos, letter))
    
    arrow_positions_list = list()
    
    for i in range(16):
        arrow_positions_list.append("")
    arrow = visual.ShapeStim(
        win=win, name='arrow', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=1.0, pos=[0,0], anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "recall" ---
    # Run 'Begin Experiment' code from code_recall
    def EditDistanceScore(target, recall):
        """
        Recebe duas strings que serão comparadas. Retorna o edit distance score,
        que consiste em len(target) – distância de Damerau–Levenshtein. Se a substração resultar em 
        valor negativo, fixa valor em 0.
        """
        # se strings são idênticas
        if recall == target:
            return len(target) # edit distance = tamanho da string
        # se nada foi lembrado
        elif recall == "": # edit distance = 0
            return 0
    
        stimDict = {target[0]: "0"}
    
        for targetIndex in range(0, len(target)):
            if target[targetIndex] not in stimDict:
                stimDict[target[targetIndex]] = "0"
    
        for recallIndex in range(0, len(recall)):
            if recall[recallIndex] not in stimDict:
                stimDict[recall[recallIndex]] = "0"
    
        disMatrix = np.zeros(shape=(len(target) + 2, len(recall) + 2))
    
        inf = len(target) + len(recall)
    
        for targetIndex in range(0, len(target) + 1):
            disMatrix[targetIndex + 1, 0] = inf
            disMatrix[targetIndex + 1, 1] = targetIndex
    
        for recallIndex in range(0, len(recall)+1):
            disMatrix[0, recallIndex + 1] = inf
            disMatrix[1, recallIndex + 1] = recallIndex
    
        for targetIndex in range(1, len(target)+1):
            present = 0
            for recallIndex in range(1, len(recall) + 1):
                if recall[recallIndex-1] in stimDict:
                    targetIndex2 = int(stimDict[recall[recallIndex - 1]])
    
                recallIndex2 = present
                cost = 1
    
                if target[targetIndex - 1] == recall[recallIndex - 1]:
                    cost = 0
                    present = recallIndex
    
                Substitution = disMatrix[targetIndex, recallIndex] + cost
                Insertion = disMatrix[targetIndex + 1, recallIndex] + 1
                Deletion = disMatrix[targetIndex, recallIndex + 1] + 1
                Transposition = disMatrix[targetIndex2, recallIndex2] + (targetIndex - targetIndex2 - 1) + 1 + (recallIndex - recallIndex2 - 1)
    
                if Substitution < Insertion and Substitution < Deletion and Substitution < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Substitution
                elif Insertion < Deletion and Insertion < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Insertion
                elif Deletion < Transposition:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Deletion
                else:
                    disMatrix[targetIndex + 1, recallIndex + 1] = Transposition
    
    
            stimDict[target[targetIndex - 1]] = str(targetIndex)
    
        # se edit distance < 0, fixa valor em zero
        if len(target) - disMatrix[len(target) + 1, len(recall) + 1] < 0:
            return 0
        # caso contrário, retorna o valor da medida
        else:
            return(int(len(target) - disMatrix[len(target) + 1, len(recall) + 1]))
    
    def partial_credit(string1, string2):
        score = 0
        for letter1, letter2 in zip(string1, string2):
            if letter1 == letter2:
                score += 1
                
        return score
    
    final_full_credit_score = final_partial_credit_score = final_edit_distance_score = 0
    
    
    prompt_recall = visual.TextStim(win=win, name='prompt_recall',
        text='Selecione as setas na mesma ordem em que foram apresentadas. Use o botão [Branco] para indicar as setas que esqueceu.',
        font='Times New Roman',
        units='norm', pos=(0, 0.85), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    A = visual.ShapeStim(
        win=win, name='A', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=0.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-2.0, interpolate=True)
    B = visual.ShapeStim(
        win=win, name='B', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=45.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-3.0, interpolate=True)
    C = visual.ShapeStim(
        win=win, name='C', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=90.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-4.0, interpolate=True)
    D = visual.ShapeStim(
        win=win, name='D', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=135.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-5.0, interpolate=True)
    E = visual.ShapeStim(
        win=win, name='E', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=180.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-6.0, interpolate=True)
    F = visual.ShapeStim(
        win=win, name='F', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=225.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-7.0, interpolate=True)
    G = visual.ShapeStim(
        win=win, name='G', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=270.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-8.0, interpolate=True)
    H = visual.ShapeStim(
        win=win, name='H', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=315.0, pos=(0, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-9.0, interpolate=True)
    I = visual.ShapeStim(
        win=win, name='I', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=0.0, pos=(0, 0.4), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-10.0, interpolate=True)
    J = visual.ShapeStim(
        win=win, name='J', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=45.0, pos=(0.165, 0.32), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-11.0, interpolate=True)
    K = visual.ShapeStim(
        win=win, name='K', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=90.0, pos=(0.225, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-12.0, interpolate=True)
    L = visual.ShapeStim(
        win=win, name='L', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=135.0, pos=(0.165, -0.12), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-13.0, interpolate=True)
    M = visual.ShapeStim(
        win=win, name='M', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=180.0, pos=(0, -0.2), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-14.0, interpolate=True)
    N = visual.ShapeStim(
        win=win, name='N', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=225.0, pos=(-0.165, -0.12), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-15.0, interpolate=True)
    O = visual.ShapeStim(
        win=win, name='O', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=270.0, pos=(-0.225, 0.1), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-16.0, interpolate=True)
    P = visual.ShapeStim(
        win=win, name='P', vertices='arrow',units='norm', 
        size=(0.05, 0.35),
        ori=315.0, pos=(-0.165, 0.32), anchor='bottom-center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-17.0, interpolate=True)
    clear_ = visual.ImageStim(
        win=win,
        name='clear_', units='norm', 
        image='images/clear_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.6, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-18.0)
    blank = visual.ImageStim(
        win=win,
        name='blank', units='norm', 
        image='images/blank_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.0, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-19.0)
    send = visual.ImageStim(
        win=win,
        name='send', units='norm', 
        image='images/send_button.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.8), size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-20.0)
    square = visual.Rect(
        win=win, name='square',units='height', 
        width=(0.075, 0.075)[0], height=(0.075, 0.075)[1],
        ori=0.0, pos=(0, 0.05), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
        opacity=0.0, depth=-21.0, interpolate=True)
    recall_response = event.Mouse(win=win)
    x, y = [None, None]
    recall_response.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "recall_feedback" ---
    recall_feedback_prompt = visual.TextStim(win=win, name='recall_feedback_prompt',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, 0), height=0.11, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    rotation_feedback_prompt = visual.TextStim(win=win, name='rotation_feedback_prompt',
        text='',
        font='Times New Roman',
        units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    rotation_feedback_performance = visual.TextStim(win=win, name='rotation_feedback_performance',
        text='',
        font='Times New Roman',
        units='norm', pos=(0.9, 0.9), height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
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
    # Run 'End Routine' code from welcome_code
    thisExp.addData('participant_code', participant_code)
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    arrow_memory_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='arrow_memory_instructions')
    thisExp.addLoop(arrow_memory_instructions)  # add the loop to the experiment
    thisArrow_memory_instruction = arrow_memory_instructions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisArrow_memory_instruction.rgb)
    if thisArrow_memory_instruction != None:
        for paramName in thisArrow_memory_instruction:
            globals()[paramName] = thisArrow_memory_instruction[paramName]
    
    for thisArrow_memory_instruction in arrow_memory_instructions:
        currentLoop = arrow_memory_instructions
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisArrow_memory_instruction.rgb)
        if thisArrow_memory_instruction != None:
            for paramName in thisArrow_memory_instruction:
                globals()[paramName] = thisArrow_memory_instruction[paramName]
        
        # --- Prepare to start Routine "instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instruction.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from instr_code
        my_count = 0 # contador de tentativas da tarefa distratora
        instr_msg.setPos((0, 0.2))
        instr_msg.setText(instruction_list[instruction_block][current_instruction])
        # setup some python lists for storing info about the instr_resp
        instr_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        instructionComponents = [instr_msg, previous, next, instr_resp]
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
            
            # *previous* updates
            
            # if previous is starting this frame...
            if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                previous.frameNStart = frameN  # exact frame index
                previous.tStart = t  # local t and not account for scr refresh
                previous.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'previous.started')
                # update status
                previous.status = STARTED
                previous.setAutoDraw(True)
            
            # if previous is active this frame...
            if previous.status == STARTED:
                # update params
                pass
            
            # *next* updates
            
            # if next is starting this frame...
            if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                next.frameNStart = frameN  # exact frame index
                next.tStart = t  # local t and not account for scr refresh
                next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'next.started')
                # update status
                next.status = STARTED
                next.setAutoDraw(True)
            
            # if next is active this frame...
            if next.status == STARTED:
                # update params
                pass
            # *instr_resp* updates
            
            # if instr_resp is starting this frame...
            if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr_resp.frameNStart = frameN  # exact frame index
                instr_resp.tStart = t  # local t and not account for scr refresh
                instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('instr_resp.started', t)
                # update status
                instr_resp.status = STARTED
                instr_resp.mouseClock.reset()
                prevButtonState = instr_resp.getPressed()  # if button is down already this ISN'T a new click
            if instr_resp.status == STARTED:  # only update if started and not finished!
                buttons = instr_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([previous, next], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(instr_resp):
                                gotValidClick = True
                                instr_resp.clicked_name.append(obj.name)
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
        thisExp.addData('participant_code', participant_code)
        
        if instr_resp.clicked_name[0] == "previous":
            current_instruction -= 1
        elif instr_resp.clicked_name[0] == "next":
            current_instruction += 1
        
        # Se a instrução atual for -1
        if current_instruction == -1:
            # Resete o valor para ser 0
            current_instruction = 0
        # Se a instrução atual é igual ao comprimento da lista de instruções
        elif current_instruction == len(instruction_list[instruction_block]):
            current_instruction = 0 # zera contador de instruções
            if instruction_block == 0:
                instruction_block += 1
                arrow_memory_instructions.finished = True # encerra o loop do treino da tarefa de memória
            elif instruction_block == 1:
                instruction_block += 1
                rotation_instructions.finished = True # encerra o loop do treino da tarefa matemática
            elif instruction_block == 2:
                instruction_block += 1
                rotspan_training_instructions.finished = True # encerra o loop de treino do OSPAN
            elif instruction_block == 3:
                instruction_block += 1
                rotspan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
        
        # store data for arrow_memory_instructions (TrialHandler)
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 999.0 repeats of 'arrow_memory_instructions'
    
    
    # set up handler to look after randomisation of conditions etc
    arrow_memory_practice_trials = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('span.xlsx', selection='0:1'),
        seed=None, name='arrow_memory_practice_trials')
    thisExp.addLoop(arrow_memory_practice_trials)  # add the loop to the experiment
    thisArrow_memory_practice_trial = arrow_memory_practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisArrow_memory_practice_trial.rgb)
    if thisArrow_memory_practice_trial != None:
        for paramName in thisArrow_memory_practice_trial:
            globals()[paramName] = thisArrow_memory_practice_trial[paramName]
    
    for thisArrow_memory_practice_trial in arrow_memory_practice_trials:
        currentLoop = arrow_memory_practice_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisArrow_memory_practice_trial.rgb)
        if thisArrow_memory_practice_trial != None:
            for paramName in thisArrow_memory_practice_trial:
                globals()[paramName] = thisArrow_memory_practice_trial[paramName]
        
        # set up handler to look after randomisation of conditions etc
        arrow_memory_practice = data.TrialHandler(nReps=current_span, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='arrow_memory_practice')
        thisExp.addLoop(arrow_memory_practice)  # add the loop to the experiment
        thisArrow_memory_practice = arrow_memory_practice.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisArrow_memory_practice.rgb)
        if thisArrow_memory_practice != None:
            for paramName in thisArrow_memory_practice:
                globals()[paramName] = thisArrow_memory_practice[paramName]
        
        for thisArrow_memory_practice in arrow_memory_practice:
            currentLoop = arrow_memory_practice
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisArrow_memory_practice.rgb)
            if thisArrow_memory_practice != None:
                for paramName in thisArrow_memory_practice:
                    globals()[paramName] = thisArrow_memory_practice[paramName]
            
            # --- Prepare to start Routine "arrow_memory" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('arrow_memory.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from arrow_memory_code
            # tenta atribuir o valor da repetição do loop atual à variável index
            # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
            try:
                index = arrow_memory_practice.thisN
            except:
                pass
                
            try:
                index = rotspan_training_trial.thisN
            except:
                pass
            
            try:
                index = rotspan_testing_trial.thisN
            except:
                pass
            
            # tenta embaralhar as posições do grid sempre que estivermos em uma nova tentativa
            try:
                # se é a primeira execução do loop...
                if arrow_memory_practice.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                    correct_response = "".join(temp)
            except:
                pass
            
            try:
                # se é a primeira execução do loop...
                if rotspan_training_trial.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                        
                    correct_response = "".join(temp)
            except:
                pass
            
            try:
                # se é a primeira execução do loop...
                if rotspan_testing_trial.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                        
                    correct_response = "".join(temp)
            
            except:
                pass
            arrow.setPos([correct_positions[index]])
            arrow.setOri(correct_orientations[index])
            # keep track of which components have finished
            arrow_memoryComponents = [arrow]
            for thisComponent in arrow_memoryComponents:
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
            
            # --- Run Routine "arrow_memory" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *arrow* updates
                
                # if arrow is starting this frame...
                if arrow.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    arrow.frameNStart = frameN  # exact frame index
                    arrow.tStart = t  # local t and not account for scr refresh
                    arrow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'arrow.started')
                    # update status
                    arrow.status = STARTED
                    arrow.setAutoDraw(True)
                
                # if arrow is active this frame...
                if arrow.status == STARTED:
                    # update params
                    pass
                
                # if arrow is stopping this frame...
                if arrow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > arrow.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        arrow.tStop = t  # not accounting for scr refresh
                        arrow.tStopRefresh = tThisFlipGlobal  # on global time
                        arrow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'arrow.stopped')
                        # update status
                        arrow.status = FINISHED
                        arrow.setAutoDraw(False)
                
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
                for thisComponent in arrow_memoryComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "arrow_memory" ---
            for thisComponent in arrow_memoryComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('arrow_memory.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed current_span repeats of 'arrow_memory_practice'
        
        
        # --- Prepare to start Routine "recall" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('recall.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_recall
        clicked_things = []
        arrow_colors = ["black"] * 16
        
        clickables = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank, square]
        allowed_send = False
        allowed_blank = True
        
        my_response = list()
        
        try:
            if arrow_memory_practice_trials.thisN == 0:
                task_phase = "arrow_memory_practice_phase"
        except:
            pass
        
        try:
            if rotspan_training_trials.thisN == 0:
                task_phase = "rotspan_training_trials"
        except:
            pass
        
        try:
            if rotspan_testing_trials.thisN == 0:
                task_phase = "rotspan_testing_trials"
        except:
            pass
        
        
        # setup some python lists for storing info about the recall_response
        recall_response.x = []
        recall_response.y = []
        recall_response.leftButton = []
        recall_response.midButton = []
        recall_response.rightButton = []
        recall_response.time = []
        recall_response.corr = []
        recall_response.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        recallComponents = [prompt_recall, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, clear_, blank, send, square, recall_response]
        for thisComponent in recallComponents:
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
        
        # --- Run Routine "recall" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_recall
            for i, clickable in enumerate(clickables):
                if (clickable == square):
                    pass
                # and it was the blank button:
                elif recall_response.isPressedIn(clickable) and (clickable == blank) and (allowed_blank == True):
                    if len(clicked_things) <= 15:
                        clicked_things.append(clickable.name)
                        # to prevent two consecutive responses
                        allowed_blank = False 
                        blank_clock = core.Clock() 
                        #clicked_things.append(clickable.name)
                        my_response.append("–")
                        allowed_send = True
                # if a button was pressed in
                elif recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                    # and it wasn't send, clear_, and blank buttons
                    if (clickable != send) and (clickable != clear_) and (clickable != blank):
                        if len(clicked_things) <= 15:
                            clicked_things.append(clickable.name)
                            clickable.fillColor = "darkblue"
                            clickable.color = "darkblue"
                            my_response.append(clickable.name)
                            allowed_send = True
                    # and it was the clear_ button
                    elif clickable == clear_:
                        for i, clickable in enumerate(clickables[:-4]):
                            clickable.fillColor = "black"
                            clickable.color = "black"
                        # reset values
                        clicked_things = []
                        my_response = list()
                        allowed_send = False # reset
                    elif (clickable == send) and (allowed_send == True):
                        continueRoutine = False
            
            # it allows the blank button again
            try:
                if blank_clock.getTime() > 1:
                    allowed_blank = True
            except NameError:
                pass
            
            # *prompt_recall* updates
            
            # if prompt_recall is starting this frame...
            if prompt_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_recall.frameNStart = frameN  # exact frame index
                prompt_recall.tStart = t  # local t and not account for scr refresh
                prompt_recall.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_recall, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_recall.started')
                # update status
                prompt_recall.status = STARTED
                prompt_recall.setAutoDraw(True)
            
            # if prompt_recall is active this frame...
            if prompt_recall.status == STARTED:
                # update params
                pass
            
            # *A* updates
            
            # if A is starting this frame...
            if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                A.frameNStart = frameN  # exact frame index
                A.tStart = t  # local t and not account for scr refresh
                A.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A.started')
                # update status
                A.status = STARTED
                A.setAutoDraw(True)
            
            # if A is active this frame...
            if A.status == STARTED:
                # update params
                pass
            
            # *B* updates
            
            # if B is starting this frame...
            if B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B.frameNStart = frameN  # exact frame index
                B.tStart = t  # local t and not account for scr refresh
                B.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'B.started')
                # update status
                B.status = STARTED
                B.setAutoDraw(True)
            
            # if B is active this frame...
            if B.status == STARTED:
                # update params
                pass
            
            # *C* updates
            
            # if C is starting this frame...
            if C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                C.frameNStart = frameN  # exact frame index
                C.tStart = t  # local t and not account for scr refresh
                C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'C.started')
                # update status
                C.status = STARTED
                C.setAutoDraw(True)
            
            # if C is active this frame...
            if C.status == STARTED:
                # update params
                pass
            
            # *D* updates
            
            # if D is starting this frame...
            if D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                D.frameNStart = frameN  # exact frame index
                D.tStart = t  # local t and not account for scr refresh
                D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D.started')
                # update status
                D.status = STARTED
                D.setAutoDraw(True)
            
            # if D is active this frame...
            if D.status == STARTED:
                # update params
                pass
            
            # *E* updates
            
            # if E is starting this frame...
            if E.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                E.frameNStart = frameN  # exact frame index
                E.tStart = t  # local t and not account for scr refresh
                E.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(E, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'E.started')
                # update status
                E.status = STARTED
                E.setAutoDraw(True)
            
            # if E is active this frame...
            if E.status == STARTED:
                # update params
                pass
            
            # *F* updates
            
            # if F is starting this frame...
            if F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                F.frameNStart = frameN  # exact frame index
                F.tStart = t  # local t and not account for scr refresh
                F.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'F.started')
                # update status
                F.status = STARTED
                F.setAutoDraw(True)
            
            # if F is active this frame...
            if F.status == STARTED:
                # update params
                pass
            
            # *G* updates
            
            # if G is starting this frame...
            if G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                G.frameNStart = frameN  # exact frame index
                G.tStart = t  # local t and not account for scr refresh
                G.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(G, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'G.started')
                # update status
                G.status = STARTED
                G.setAutoDraw(True)
            
            # if G is active this frame...
            if G.status == STARTED:
                # update params
                pass
            
            # *H* updates
            
            # if H is starting this frame...
            if H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                H.frameNStart = frameN  # exact frame index
                H.tStart = t  # local t and not account for scr refresh
                H.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(H, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'H.started')
                # update status
                H.status = STARTED
                H.setAutoDraw(True)
            
            # if H is active this frame...
            if H.status == STARTED:
                # update params
                pass
            
            # *I* updates
            
            # if I is starting this frame...
            if I.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                I.frameNStart = frameN  # exact frame index
                I.tStart = t  # local t and not account for scr refresh
                I.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(I, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'I.started')
                # update status
                I.status = STARTED
                I.setAutoDraw(True)
            
            # if I is active this frame...
            if I.status == STARTED:
                # update params
                pass
            
            # *J* updates
            
            # if J is starting this frame...
            if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                J.frameNStart = frameN  # exact frame index
                J.tStart = t  # local t and not account for scr refresh
                J.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'J.started')
                # update status
                J.status = STARTED
                J.setAutoDraw(True)
            
            # if J is active this frame...
            if J.status == STARTED:
                # update params
                pass
            
            # *K* updates
            
            # if K is starting this frame...
            if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                K.frameNStart = frameN  # exact frame index
                K.tStart = t  # local t and not account for scr refresh
                K.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'K.started')
                # update status
                K.status = STARTED
                K.setAutoDraw(True)
            
            # if K is active this frame...
            if K.status == STARTED:
                # update params
                pass
            
            # *L* updates
            
            # if L is starting this frame...
            if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L.frameNStart = frameN  # exact frame index
                L.tStart = t  # local t and not account for scr refresh
                L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L.started')
                # update status
                L.status = STARTED
                L.setAutoDraw(True)
            
            # if L is active this frame...
            if L.status == STARTED:
                # update params
                pass
            
            # *M* updates
            
            # if M is starting this frame...
            if M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                M.frameNStart = frameN  # exact frame index
                M.tStart = t  # local t and not account for scr refresh
                M.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(M, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'M.started')
                # update status
                M.status = STARTED
                M.setAutoDraw(True)
            
            # if M is active this frame...
            if M.status == STARTED:
                # update params
                pass
            
            # *N* updates
            
            # if N is starting this frame...
            if N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                N.frameNStart = frameN  # exact frame index
                N.tStart = t  # local t and not account for scr refresh
                N.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(N, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'N.started')
                # update status
                N.status = STARTED
                N.setAutoDraw(True)
            
            # if N is active this frame...
            if N.status == STARTED:
                # update params
                pass
            
            # *O* updates
            
            # if O is starting this frame...
            if O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                O.frameNStart = frameN  # exact frame index
                O.tStart = t  # local t and not account for scr refresh
                O.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(O, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'O.started')
                # update status
                O.status = STARTED
                O.setAutoDraw(True)
            
            # if O is active this frame...
            if O.status == STARTED:
                # update params
                pass
            
            # *P* updates
            
            # if P is starting this frame...
            if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P.frameNStart = frameN  # exact frame index
                P.tStart = t  # local t and not account for scr refresh
                P.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P.started')
                # update status
                P.status = STARTED
                P.setAutoDraw(True)
            
            # if P is active this frame...
            if P.status == STARTED:
                # update params
                pass
            
            # *clear_* updates
            
            # if clear_ is starting this frame...
            if clear_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clear_.frameNStart = frameN  # exact frame index
                clear_.tStart = t  # local t and not account for scr refresh
                clear_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clear_, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clear_.started')
                # update status
                clear_.status = STARTED
                clear_.setAutoDraw(True)
            
            # if clear_ is active this frame...
            if clear_.status == STARTED:
                # update params
                pass
            
            # *blank* updates
            
            # if blank is starting this frame...
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.started')
                # update status
                blank.status = STARTED
                blank.setAutoDraw(True)
            
            # if blank is active this frame...
            if blank.status == STARTED:
                # update params
                pass
            
            # *send* updates
            
            # if send is starting this frame...
            if send.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                send.frameNStart = frameN  # exact frame index
                send.tStart = t  # local t and not account for scr refresh
                send.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(send, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'send.started')
                # update status
                send.status = STARTED
                send.setAutoDraw(True)
            
            # if send is active this frame...
            if send.status == STARTED:
                # update params
                pass
            
            # *square* updates
            
            # if square is starting this frame...
            if square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square.frameNStart = frameN  # exact frame index
                square.tStart = t  # local t and not account for scr refresh
                square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square.started')
                # update status
                square.status = STARTED
                square.setAutoDraw(True)
            
            # if square is active this frame...
            if square.status == STARTED:
                # update params
                pass
            # *recall_response* updates
            
            # if recall_response is starting this frame...
            if recall_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recall_response.frameNStart = frameN  # exact frame index
                recall_response.tStart = t  # local t and not account for scr refresh
                recall_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('recall_response.started', t)
                # update status
                recall_response.status = STARTED
                recall_response.mouseClock.reset()
                prevButtonState = recall_response.getPressed()  # if button is down already this ISN'T a new click
            if recall_response.status == STARTED:  # only update if started and not finished!
                buttons = recall_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank, square], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(recall_response):
                                gotValidClick = True
                                recall_response.clicked_name.append(obj.name)
                        # check whether click was in correct object
                        if gotValidClick:
                            _corr = 0
                            _corrAns = environmenttools.getFromNames([], namespace=locals())
                            for obj in _corrAns:
                                # is this object clicked on?
                                if obj.contains(recall_response):
                                    _corr = 1
                            recall_response.corr.append(_corr)
                        if gotValidClick:
                            x, y = recall_response.getPos()
                            recall_response.x.append(x)
                            recall_response.y.append(y)
                            buttons = recall_response.getPressed()
                            recall_response.leftButton.append(buttons[0])
                            recall_response.midButton.append(buttons[1])
                            recall_response.rightButton.append(buttons[2])
                            recall_response.time.append(recall_response.mouseClock.getTime())
            
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
            for thisComponent in recallComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recall" ---
        for thisComponent in recallComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('recall.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_recall
        # juntando respostas, mas eliminando respostas repetidas e "send"
        participant_response = "".join(my_response)
        
        # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
        if participant_response == correct_response:
            full_credit_score = current_span
        else:
            full_credit_score = 0
        
        # crédito parcial (pontua apenas acertos na mesma posição serial)
        partial_credit_score = partial_credit(participant_response, correct_response)
        
        # edit distance score
        edit_distance_score = EditDistanceScore(correct_response, participant_response)
        
        # créditos completo parcial e edit distance, somatório da sessão (máx. 42)
        try:
            if rotspan_testing_trials.thisN >= 0:
                final_full_credit_score += full_credit_score
                final_partial_credit_score += partial_credit_score
                final_edit_distance_score += edit_distance_score
        except:
            pass
        
        # criando texto para feedback
        if partial_credit_score > 1:
            word = "setas"    
        elif partial_credit_score <= 1:
            word = "seta"
        
        # mensagens de feedback de recordação e das setas
        recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
        
        try:
            rotation_percent_correct = (rotation_trials_correct / rotation_total_trials) * 100
        except ZeroDivisionError:
            rotation_percent_correct = 0
        
        rotation_performance_msg = f"{rotation_percent_correct:.0f}%"
        
        try:
            if rotation_errors > 1:
                rotation_feedback_msg = f"Você cometeu {rotation_errors} erros neste conjunto de tentativas" 
            elif rotation_errors == 1:
                rotation_feedback_msg = f"Você cometeu {rotation_errors} erro neste conjunto de tentativas"
            else:
                rotation_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
        except:
            rotation_feedback_msg = ""
           
        # salva respostas
        thisExp.addData("correct_response", correct_response)
        thisExp.addData("participant_response", participant_response)
        thisExp.addData("full_credit_score", full_credit_score)
        thisExp.addData("partial_credit_score", partial_credit_score)
        thisExp.addData("edit_distance_score", edit_distance_score)
        thisExp.addData("task_phase", task_phase)
        thisExp.addData("rotationtrials_correct", rotation_trials_correct)
        thisExp.addData("rotation_total_trials", rotation_total_trials)
        thisExp.addData("rotation_percent_correct", rotation_percent_correct)
        try:
            thisExp.addData("rotation_errors", rotation_errors)
        except:
            pass
        
        # reseta para a próxima tentativa
        for clickable in clickables[:-4]:
            clickable.fillColor = "black"
            clickable.color = "black"
        # store data for arrow_memory_practice_trials (TrialHandler)
        arrow_memory_practice_trials.addData('recall_response.x', recall_response.x)
        arrow_memory_practice_trials.addData('recall_response.y', recall_response.y)
        arrow_memory_practice_trials.addData('recall_response.leftButton', recall_response.leftButton)
        arrow_memory_practice_trials.addData('recall_response.midButton', recall_response.midButton)
        arrow_memory_practice_trials.addData('recall_response.rightButton', recall_response.rightButton)
        arrow_memory_practice_trials.addData('recall_response.time', recall_response.time)
        arrow_memory_practice_trials.addData('recall_response.corr', recall_response.corr)
        arrow_memory_practice_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
        # the Routine "recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "recall_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('recall_feedback.started', globalClock.getTime(format='float'))
        recall_feedback_prompt.setText(recall_feedback_msg)
        rotation_feedback_prompt.setText(rotation_feedback_msg)
        rotation_feedback_performance.setColor(rotation_color, colorSpace='rgb')
        rotation_feedback_performance.setText(rotation_performance_msg)
        # keep track of which components have finished
        recall_feedbackComponents = [recall_feedback_prompt, rotation_feedback_prompt, rotation_feedback_performance]
        for thisComponent in recall_feedbackComponents:
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
        
        # --- Run Routine "recall_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_feedback_prompt* updates
            
            # if recall_feedback_prompt is starting this frame...
            if recall_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recall_feedback_prompt.frameNStart = frameN  # exact frame index
                recall_feedback_prompt.tStart = t  # local t and not account for scr refresh
                recall_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_feedback_prompt.started')
                # update status
                recall_feedback_prompt.status = STARTED
                recall_feedback_prompt.setAutoDraw(True)
            
            # if recall_feedback_prompt is active this frame...
            if recall_feedback_prompt.status == STARTED:
                # update params
                pass
            
            # if recall_feedback_prompt is stopping this frame...
            if recall_feedback_prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > recall_feedback_prompt.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    recall_feedback_prompt.tStop = t  # not accounting for scr refresh
                    recall_feedback_prompt.tStopRefresh = tThisFlipGlobal  # on global time
                    recall_feedback_prompt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recall_feedback_prompt.stopped')
                    # update status
                    recall_feedback_prompt.status = FINISHED
                    recall_feedback_prompt.setAutoDraw(False)
            
            # *rotation_feedback_prompt* updates
            
            # if rotation_feedback_prompt is starting this frame...
            if rotation_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_feedback_prompt.frameNStart = frameN  # exact frame index
                rotation_feedback_prompt.tStart = t  # local t and not account for scr refresh
                rotation_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_feedback_prompt.started')
                # update status
                rotation_feedback_prompt.status = STARTED
                rotation_feedback_prompt.setAutoDraw(True)
            
            # if rotation_feedback_prompt is active this frame...
            if rotation_feedback_prompt.status == STARTED:
                # update params
                pass
            
            # if rotation_feedback_prompt is stopping this frame...
            if rotation_feedback_prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rotation_feedback_prompt.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    rotation_feedback_prompt.tStop = t  # not accounting for scr refresh
                    rotation_feedback_prompt.tStopRefresh = tThisFlipGlobal  # on global time
                    rotation_feedback_prompt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_feedback_prompt.stopped')
                    # update status
                    rotation_feedback_prompt.status = FINISHED
                    rotation_feedback_prompt.setAutoDraw(False)
            
            # *rotation_feedback_performance* updates
            
            # if rotation_feedback_performance is starting this frame...
            if rotation_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_feedback_performance.frameNStart = frameN  # exact frame index
                rotation_feedback_performance.tStart = t  # local t and not account for scr refresh
                rotation_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_feedback_performance, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_feedback_performance.started')
                # update status
                rotation_feedback_performance.status = STARTED
                rotation_feedback_performance.setAutoDraw(True)
            
            # if rotation_feedback_performance is active this frame...
            if rotation_feedback_performance.status == STARTED:
                # update params
                pass
            
            # if rotation_feedback_performance is stopping this frame...
            if rotation_feedback_performance.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rotation_feedback_performance.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    rotation_feedback_performance.tStop = t  # not accounting for scr refresh
                    rotation_feedback_performance.tStopRefresh = tThisFlipGlobal  # on global time
                    rotation_feedback_performance.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_feedback_performance.stopped')
                    # update status
                    rotation_feedback_performance.status = FINISHED
                    rotation_feedback_performance.setAutoDraw(False)
            
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
            for thisComponent in recall_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recall_feedback" ---
        for thisComponent in recall_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('recall_feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 3.0 repeats of 'arrow_memory_practice_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    rotation_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rotation_instructions')
    thisExp.addLoop(rotation_instructions)  # add the loop to the experiment
    thisRotation_instruction = rotation_instructions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRotation_instruction.rgb)
    if thisRotation_instruction != None:
        for paramName in thisRotation_instruction:
            globals()[paramName] = thisRotation_instruction[paramName]
    
    for thisRotation_instruction in rotation_instructions:
        currentLoop = rotation_instructions
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRotation_instruction.rgb)
        if thisRotation_instruction != None:
            for paramName in thisRotation_instruction:
                globals()[paramName] = thisRotation_instruction[paramName]
        
        # --- Prepare to start Routine "instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instruction.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from instr_code
        my_count = 0 # contador de tentativas da tarefa distratora
        instr_msg.setPos((0, 0.2))
        instr_msg.setText(instruction_list[instruction_block][current_instruction])
        # setup some python lists for storing info about the instr_resp
        instr_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        instructionComponents = [instr_msg, previous, next, instr_resp]
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
            
            # *previous* updates
            
            # if previous is starting this frame...
            if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                previous.frameNStart = frameN  # exact frame index
                previous.tStart = t  # local t and not account for scr refresh
                previous.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'previous.started')
                # update status
                previous.status = STARTED
                previous.setAutoDraw(True)
            
            # if previous is active this frame...
            if previous.status == STARTED:
                # update params
                pass
            
            # *next* updates
            
            # if next is starting this frame...
            if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                next.frameNStart = frameN  # exact frame index
                next.tStart = t  # local t and not account for scr refresh
                next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'next.started')
                # update status
                next.status = STARTED
                next.setAutoDraw(True)
            
            # if next is active this frame...
            if next.status == STARTED:
                # update params
                pass
            # *instr_resp* updates
            
            # if instr_resp is starting this frame...
            if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr_resp.frameNStart = frameN  # exact frame index
                instr_resp.tStart = t  # local t and not account for scr refresh
                instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('instr_resp.started', t)
                # update status
                instr_resp.status = STARTED
                instr_resp.mouseClock.reset()
                prevButtonState = instr_resp.getPressed()  # if button is down already this ISN'T a new click
            if instr_resp.status == STARTED:  # only update if started and not finished!
                buttons = instr_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([previous, next], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(instr_resp):
                                gotValidClick = True
                                instr_resp.clicked_name.append(obj.name)
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
        thisExp.addData('participant_code', participant_code)
        
        if instr_resp.clicked_name[0] == "previous":
            current_instruction -= 1
        elif instr_resp.clicked_name[0] == "next":
            current_instruction += 1
        
        # Se a instrução atual for -1
        if current_instruction == -1:
            # Resete o valor para ser 0
            current_instruction = 0
        # Se a instrução atual é igual ao comprimento da lista de instruções
        elif current_instruction == len(instruction_list[instruction_block]):
            current_instruction = 0 # zera contador de instruções
            if instruction_block == 0:
                instruction_block += 1
                arrow_memory_instructions.finished = True # encerra o loop do treino da tarefa de memória
            elif instruction_block == 1:
                instruction_block += 1
                rotation_instructions.finished = True # encerra o loop do treino da tarefa matemática
            elif instruction_block == 2:
                instruction_block += 1
                rotspan_training_instructions.finished = True # encerra o loop de treino do OSPAN
            elif instruction_block == 3:
                instruction_block += 1
                rotspan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
        
        # store data for rotation_instructions (TrialHandler)
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 999.0 repeats of 'rotation_instructions'
    
    
    # set up handler to look after randomisation of conditions etc
    rotation_practice_trials = data.TrialHandler(nReps=15.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rotation_practice_trials')
    thisExp.addLoop(rotation_practice_trials)  # add the loop to the experiment
    thisRotation_practice_trial = rotation_practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRotation_practice_trial.rgb)
    if thisRotation_practice_trial != None:
        for paramName in thisRotation_practice_trial:
            globals()[paramName] = thisRotation_practice_trial[paramName]
    
    for thisRotation_practice_trial in rotation_practice_trials:
        currentLoop = rotation_practice_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRotation_practice_trial.rgb)
        if thisRotation_practice_trial != None:
            for paramName in thisRotation_practice_trial:
                globals()[paramName] = thisRotation_practice_trial[paramName]
        
        # --- Prepare to start Routine "rotation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('rotation.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from rotation_code
        rotation_clock = core.Clock()
        
        rotation_problem.flipHoriz = stimuli[letter_count][2]
        rotation_problem.flipVert = False
        
        try:
            # se é a primeira execução do loop...
            if rotation_practice_trials.thisN == 0:
                rotation_color = "red" # agora teremos feedback na cor vermelha
                rotation_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if rotspan_training_trial.thisN == 0:
                rotation_errors = 0
        except:
            pass
            
        try:
            # se é a primeira execução do loop...
            if rotspan_testing_trial.thisN == 0:
                rotation_errors = 0
        except:
            pass
            
        # reseta os contadores quando começa o ROTSPAN para valer
        try:
            if (rotspan_testing_trials.thisN == 0) and (rotspan_testing_trial.thisN == 0):
                rotation_total_trials = rotation_trials_correct = speed_errors = 0
        except:
            pass
        # setup some python lists for storing info about the symmetry_problem_next
        symmetry_problem_next.clicked_name = []
        gotValidClick = False  # until a click is received
        rotation_problem.setOri(stimuli[letter_count][1])
        rotation_problem.setText(stimuli[letter_count][0])
        # keep track of which components have finished
        rotationComponents = [rotation_prompt, continue_, symmetry_problem_next, rotation_problem]
        for thisComponent in rotationComponents:
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
        
        # --- Run Routine "rotation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from rotation_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if rotation_clock.getTime() >= rotation_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
              
            
            # *rotation_prompt* updates
            
            # if rotation_prompt is starting this frame...
            if rotation_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_prompt.frameNStart = frameN  # exact frame index
                rotation_prompt.tStart = t  # local t and not account for scr refresh
                rotation_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_prompt.started')
                # update status
                rotation_prompt.status = STARTED
                rotation_prompt.setAutoDraw(True)
            
            # if rotation_prompt is active this frame...
            if rotation_prompt.status == STARTED:
                # update params
                pass
            
            # *continue_* updates
            
            # if continue_ is starting this frame...
            if continue_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_.frameNStart = frameN  # exact frame index
                continue_.tStart = t  # local t and not account for scr refresh
                continue_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_.started')
                # update status
                continue_.status = STARTED
                continue_.setAutoDraw(True)
            
            # if continue_ is active this frame...
            if continue_.status == STARTED:
                # update params
                pass
            # *symmetry_problem_next* updates
            
            # if symmetry_problem_next is starting this frame...
            if symmetry_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_problem_next.frameNStart = frameN  # exact frame index
                symmetry_problem_next.tStart = t  # local t and not account for scr refresh
                symmetry_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_problem_next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('symmetry_problem_next.started', t)
                # update status
                symmetry_problem_next.status = STARTED
                symmetry_problem_next.mouseClock.reset()
                prevButtonState = symmetry_problem_next.getPressed()  # if button is down already this ISN'T a new click
            if symmetry_problem_next.status == STARTED:  # only update if started and not finished!
                buttons = symmetry_problem_next.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(continue_, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(symmetry_problem_next):
                                gotValidClick = True
                                symmetry_problem_next.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # *rotation_problem* updates
            
            # if rotation_problem is starting this frame...
            if rotation_problem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_problem.frameNStart = frameN  # exact frame index
                rotation_problem.tStart = t  # local t and not account for scr refresh
                rotation_problem.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_problem, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_problem.started')
                # update status
                rotation_problem.status = STARTED
                rotation_problem.setAutoDraw(True)
            
            # if rotation_problem is active this frame...
            if rotation_problem.status == STARTED:
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
            for thisComponent in rotationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rotation" ---
        for thisComponent in rotationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('rotation.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from rotation_code
        # salva variáveis
        thisExp.addData("rotation_letter", stimuli[letter_count][0]) # nome da imagem
        thisExp.addData("rotation_orientation", stimuli[letter_count][1]) # orientation
        thisExp.addData("rotation_flip", stimuli[letter_count][2]) # flipped vs. non-flipped
        thisExp.addData("rotation_corr", stimuli[letter_count][3]) # gabarito
        
        if abort_trial:
            rotation_speed_error = 1 # abortou devido a velocidade
        else:
            rotation_speed_error = 0 # abortou devido a velocidade
        
        try:
            thisExp.addData("problem_rt", rotation_clock.getTime()) # problem RT
        except:
            pass
        
        # store data for rotation_practice_trials (TrialHandler)
        # the Routine "rotation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "rotation_answer" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('rotation_answer.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from rotation_answer_code
        answer_clock = core.Clock()
        
        if abort_trial:
            continueRoutine = False
        # setup some python lists for storing info about the rotation_response
        rotation_response.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rotation_answerComponents = [rotation_answer_screen, yes, no, rotation_response]
        for thisComponent in rotation_answerComponents:
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
        
        # --- Run Routine "rotation_answer" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from rotation_answer_code
            try:
                # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                if rotation_clock.getTime() >= rotation_criterion:
                    speed_errors += 1
                    abort_trial = True
                    continueRoutine = False
            except:
                pass
            
            
            # *rotation_answer_screen* updates
            
            # if rotation_answer_screen is starting this frame...
            if rotation_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_answer_screen.frameNStart = frameN  # exact frame index
                rotation_answer_screen.tStart = t  # local t and not account for scr refresh
                rotation_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_answer_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_answer_screen.started')
                # update status
                rotation_answer_screen.status = STARTED
                rotation_answer_screen.setAutoDraw(True)
            
            # if rotation_answer_screen is active this frame...
            if rotation_answer_screen.status == STARTED:
                # update params
                pass
            
            # *yes* updates
            
            # if yes is starting this frame...
            if yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                yes.frameNStart = frameN  # exact frame index
                yes.tStart = t  # local t and not account for scr refresh
                yes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yes, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yes.started')
                # update status
                yes.status = STARTED
                yes.setAutoDraw(True)
            
            # if yes is active this frame...
            if yes.status == STARTED:
                # update params
                pass
            
            # *no* updates
            
            # if no is starting this frame...
            if no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                no.frameNStart = frameN  # exact frame index
                no.tStart = t  # local t and not account for scr refresh
                no.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no.started')
                # update status
                no.status = STARTED
                no.setAutoDraw(True)
            
            # if no is active this frame...
            if no.status == STARTED:
                # update params
                pass
            # *rotation_response* updates
            
            # if rotation_response is starting this frame...
            if rotation_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_response.frameNStart = frameN  # exact frame index
                rotation_response.tStart = t  # local t and not account for scr refresh
                rotation_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('rotation_response.started', t)
                # update status
                rotation_response.status = STARTED
                rotation_response.mouseClock.reset()
                prevButtonState = rotation_response.getPressed()  # if button is down already this ISN'T a new click
            if rotation_response.status == STARTED:  # only update if started and not finished!
                buttons = rotation_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([yes, no], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(rotation_response):
                                gotValidClick = True
                                rotation_response.clicked_name.append(obj.name)
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
            for thisComponent in rotation_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rotation_answer" ---
        for thisComponent in rotation_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('rotation_answer.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from rotation_answer_code
        try:
            if rotation_response.clicked_name[0] == "yes":
                rotation_participant_response = "yes"
            else:
                rotation_participant_response = "no"
        except:
            rotation_participant_response = ""
            rotation_speed_error = 1
        
        try:
            thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
        except:
            pass
        
        # se o participante acertou
        if rotation_participant_response == stimuli[letter_count][3]:
            rotation_participant_corr = 1
            rotation_accuracy_error = 0 # contagem de erros de acurácia
            rotation_trials_correct += 1 # incrementa número de acertos da sessão toda
            rotation_corrective_feedback = "Correto"
        else:
            rotation_participant_corr = 0
            rotation_corrective_feedback = "Incorreto"
            rotation_errors += 1 # incrementa o número de erros apenas da presente tentativa
        
            if rotation_speed_error == 0:
                rotation_accuracy_error = 1
            else:
                rotation_accuracy_error = 0
        
        # sempre incrementa o contador de tentativas
        rotation_total_trials += 1
        
        if abort_trial:
            thisExp.addData("rotation_speed_error", 1) # erro de velocidade
            abort_trial = False # reseta para a próxima tentativa
        else:
            thisExp.addData("rotation_speed_error", 0)
        
        # salva variáveis
        thisExp.addData("rotation_accuracy_error", rotation_accuracy_error) # erro de acurácia
        thisExp.addData("rotation_participant_corr", rotation_participant_corr) # 1 = acerto, 0 = erro
        thisExp.addData("rotation_problem", stimuli[letter_count][0]) # enunciado
        thisExp.addData("rotation_status", stimuli[letter_count][1]) # gabarito
        thisExp.addData("rotation_corr", stimuli[letter_count][2]) # resposta correta
        thisExp.addData("rotation_participant_response", rotation_participant_response) # resposta do participante
        
        # debug
        # print(f"Letra: {stimuli[letter_count][0]} --- Flip: {stimuli[letter_count][2]} --- Flip2: {rotation_problem.flipHoriz} --- Gabarito: {stimuli[letter_count][3]} --- Resposta: {rotation_participant_response} --- Feedback: {rotation_corrective_feedback}")
        
        # incrementa operação para próxima iteração
        letter_count += 1
        
        # soma a duração da tarefa matemática
        try:
            if rotation_practice_trials.thisN < 15:
                rotation_training_time.append(rotation_clock.getTime()) # e guarda tempo em uma lista
                # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
                if rotation_practice_trials.thisN == 14:
                    rotation_time_mean = np.mean(np.array(rotation_training_time))
                    rotation_time_sd = np.std(np.array(rotation_training_time), ddof = 1)
                    rotation_criterion = rotation_time_mean + 2 * rotation_time_sd
                    
        except:
            pass
        
        
        # store data for rotation_practice_trials (TrialHandler)
        # the Routine "rotation_answer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "rotation_answer_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('rotation_answer_feedback.started', globalClock.getTime(format='float'))
        rotation_corrective_feedback_msg.setText(rotation_corrective_feedback)
        # keep track of which components have finished
        rotation_answer_feedbackComponents = [true_feedback, false_feedback, rotation_corrective_feedback_msg]
        for thisComponent in rotation_answer_feedbackComponents:
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
        
        # --- Run Routine "rotation_answer_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *true_feedback* updates
            
            # if true_feedback is starting this frame...
            if true_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                true_feedback.frameNStart = frameN  # exact frame index
                true_feedback.tStart = t  # local t and not account for scr refresh
                true_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(true_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'true_feedback.started')
                # update status
                true_feedback.status = STARTED
                true_feedback.setAutoDraw(True)
            
            # if true_feedback is active this frame...
            if true_feedback.status == STARTED:
                # update params
                pass
            
            # if true_feedback is stopping this frame...
            if true_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > true_feedback.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    true_feedback.tStop = t  # not accounting for scr refresh
                    true_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    true_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'true_feedback.stopped')
                    # update status
                    true_feedback.status = FINISHED
                    true_feedback.setAutoDraw(False)
            
            # *false_feedback* updates
            
            # if false_feedback is starting this frame...
            if false_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                false_feedback.frameNStart = frameN  # exact frame index
                false_feedback.tStart = t  # local t and not account for scr refresh
                false_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(false_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'false_feedback.started')
                # update status
                false_feedback.status = STARTED
                false_feedback.setAutoDraw(True)
            
            # if false_feedback is active this frame...
            if false_feedback.status == STARTED:
                # update params
                pass
            
            # if false_feedback is stopping this frame...
            if false_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > false_feedback.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    false_feedback.tStop = t  # not accounting for scr refresh
                    false_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    false_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'false_feedback.stopped')
                    # update status
                    false_feedback.status = FINISHED
                    false_feedback.setAutoDraw(False)
            
            # *rotation_corrective_feedback_msg* updates
            
            # if rotation_corrective_feedback_msg is starting this frame...
            if rotation_corrective_feedback_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_corrective_feedback_msg.frameNStart = frameN  # exact frame index
                rotation_corrective_feedback_msg.tStart = t  # local t and not account for scr refresh
                rotation_corrective_feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_corrective_feedback_msg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_corrective_feedback_msg.started')
                # update status
                rotation_corrective_feedback_msg.status = STARTED
                rotation_corrective_feedback_msg.setAutoDraw(True)
            
            # if rotation_corrective_feedback_msg is active this frame...
            if rotation_corrective_feedback_msg.status == STARTED:
                # update params
                pass
            
            # if rotation_corrective_feedback_msg is stopping this frame...
            if rotation_corrective_feedback_msg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rotation_corrective_feedback_msg.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rotation_corrective_feedback_msg.tStop = t  # not accounting for scr refresh
                    rotation_corrective_feedback_msg.tStopRefresh = tThisFlipGlobal  # on global time
                    rotation_corrective_feedback_msg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_corrective_feedback_msg.stopped')
                    # update status
                    rotation_corrective_feedback_msg.status = FINISHED
                    rotation_corrective_feedback_msg.setAutoDraw(False)
            
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
            for thisComponent in rotation_answer_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rotation_answer_feedback" ---
        for thisComponent in rotation_answer_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('rotation_answer_feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 15.0 repeats of 'rotation_practice_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    rotspan_training_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rotspan_training_instructions')
    thisExp.addLoop(rotspan_training_instructions)  # add the loop to the experiment
    thisRotspan_training_instruction = rotspan_training_instructions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRotspan_training_instruction.rgb)
    if thisRotspan_training_instruction != None:
        for paramName in thisRotspan_training_instruction:
            globals()[paramName] = thisRotspan_training_instruction[paramName]
    
    for thisRotspan_training_instruction in rotspan_training_instructions:
        currentLoop = rotspan_training_instructions
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRotspan_training_instruction.rgb)
        if thisRotspan_training_instruction != None:
            for paramName in thisRotspan_training_instruction:
                globals()[paramName] = thisRotspan_training_instruction[paramName]
        
        # --- Prepare to start Routine "instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instruction.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from instr_code
        my_count = 0 # contador de tentativas da tarefa distratora
        instr_msg.setPos((0, 0.2))
        instr_msg.setText(instruction_list[instruction_block][current_instruction])
        # setup some python lists for storing info about the instr_resp
        instr_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        instructionComponents = [instr_msg, previous, next, instr_resp]
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
            
            # *previous* updates
            
            # if previous is starting this frame...
            if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                previous.frameNStart = frameN  # exact frame index
                previous.tStart = t  # local t and not account for scr refresh
                previous.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'previous.started')
                # update status
                previous.status = STARTED
                previous.setAutoDraw(True)
            
            # if previous is active this frame...
            if previous.status == STARTED:
                # update params
                pass
            
            # *next* updates
            
            # if next is starting this frame...
            if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                next.frameNStart = frameN  # exact frame index
                next.tStart = t  # local t and not account for scr refresh
                next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'next.started')
                # update status
                next.status = STARTED
                next.setAutoDraw(True)
            
            # if next is active this frame...
            if next.status == STARTED:
                # update params
                pass
            # *instr_resp* updates
            
            # if instr_resp is starting this frame...
            if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr_resp.frameNStart = frameN  # exact frame index
                instr_resp.tStart = t  # local t and not account for scr refresh
                instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('instr_resp.started', t)
                # update status
                instr_resp.status = STARTED
                instr_resp.mouseClock.reset()
                prevButtonState = instr_resp.getPressed()  # if button is down already this ISN'T a new click
            if instr_resp.status == STARTED:  # only update if started and not finished!
                buttons = instr_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([previous, next], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(instr_resp):
                                gotValidClick = True
                                instr_resp.clicked_name.append(obj.name)
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
        thisExp.addData('participant_code', participant_code)
        
        if instr_resp.clicked_name[0] == "previous":
            current_instruction -= 1
        elif instr_resp.clicked_name[0] == "next":
            current_instruction += 1
        
        # Se a instrução atual for -1
        if current_instruction == -1:
            # Resete o valor para ser 0
            current_instruction = 0
        # Se a instrução atual é igual ao comprimento da lista de instruções
        elif current_instruction == len(instruction_list[instruction_block]):
            current_instruction = 0 # zera contador de instruções
            if instruction_block == 0:
                instruction_block += 1
                arrow_memory_instructions.finished = True # encerra o loop do treino da tarefa de memória
            elif instruction_block == 1:
                instruction_block += 1
                rotation_instructions.finished = True # encerra o loop do treino da tarefa matemática
            elif instruction_block == 2:
                instruction_block += 1
                rotspan_training_instructions.finished = True # encerra o loop de treino do OSPAN
            elif instruction_block == 3:
                instruction_block += 1
                rotspan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
        
        # store data for rotspan_training_instructions (TrialHandler)
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 999.0 repeats of 'rotspan_training_instructions'
    
    
    # set up handler to look after randomisation of conditions etc
    rotspan_training_trials = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('span.xlsx', selection='0:1'),
        seed=None, name='rotspan_training_trials')
    thisExp.addLoop(rotspan_training_trials)  # add the loop to the experiment
    thisRotspan_training_trial = rotspan_training_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRotspan_training_trial.rgb)
    if thisRotspan_training_trial != None:
        for paramName in thisRotspan_training_trial:
            globals()[paramName] = thisRotspan_training_trial[paramName]
    
    for thisRotspan_training_trial in rotspan_training_trials:
        currentLoop = rotspan_training_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRotspan_training_trial.rgb)
        if thisRotspan_training_trial != None:
            for paramName in thisRotspan_training_trial:
                globals()[paramName] = thisRotspan_training_trial[paramName]
        
        # set up handler to look after randomisation of conditions etc
        rotspan_training_trial = data.TrialHandler(nReps=current_span, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='rotspan_training_trial')
        thisExp.addLoop(rotspan_training_trial)  # add the loop to the experiment
        thisRotspan_training_trial = rotspan_training_trial.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRotspan_training_trial.rgb)
        if thisRotspan_training_trial != None:
            for paramName in thisRotspan_training_trial:
                globals()[paramName] = thisRotspan_training_trial[paramName]
        
        for thisRotspan_training_trial in rotspan_training_trial:
            currentLoop = rotspan_training_trial
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisRotspan_training_trial.rgb)
            if thisRotspan_training_trial != None:
                for paramName in thisRotspan_training_trial:
                    globals()[paramName] = thisRotspan_training_trial[paramName]
            
            # --- Prepare to start Routine "rotation" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rotation.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from rotation_code
            rotation_clock = core.Clock()
            
            rotation_problem.flipHoriz = stimuli[letter_count][2]
            rotation_problem.flipVert = False
            
            try:
                # se é a primeira execução do loop...
                if rotation_practice_trials.thisN == 0:
                    rotation_color = "red" # agora teremos feedback na cor vermelha
                    rotation_errors = 0
            except:
                pass
                
            try:
                # se é a primeira execução do loop...
                if rotspan_training_trial.thisN == 0:
                    rotation_errors = 0
            except:
                pass
                
            try:
                # se é a primeira execução do loop...
                if rotspan_testing_trial.thisN == 0:
                    rotation_errors = 0
            except:
                pass
                
            # reseta os contadores quando começa o ROTSPAN para valer
            try:
                if (rotspan_testing_trials.thisN == 0) and (rotspan_testing_trial.thisN == 0):
                    rotation_total_trials = rotation_trials_correct = speed_errors = 0
            except:
                pass
            # setup some python lists for storing info about the symmetry_problem_next
            symmetry_problem_next.clicked_name = []
            gotValidClick = False  # until a click is received
            rotation_problem.setOri(stimuli[letter_count][1])
            rotation_problem.setText(stimuli[letter_count][0])
            # keep track of which components have finished
            rotationComponents = [rotation_prompt, continue_, symmetry_problem_next, rotation_problem]
            for thisComponent in rotationComponents:
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
            
            # --- Run Routine "rotation" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from rotation_code
                try:
                    # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                    if rotation_clock.getTime() >= rotation_criterion:
                        speed_errors += 1
                        abort_trial = True
                        continueRoutine = False
                except:
                    pass
                  
                
                # *rotation_prompt* updates
                
                # if rotation_prompt is starting this frame...
                if rotation_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rotation_prompt.frameNStart = frameN  # exact frame index
                    rotation_prompt.tStart = t  # local t and not account for scr refresh
                    rotation_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rotation_prompt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_prompt.started')
                    # update status
                    rotation_prompt.status = STARTED
                    rotation_prompt.setAutoDraw(True)
                
                # if rotation_prompt is active this frame...
                if rotation_prompt.status == STARTED:
                    # update params
                    pass
                
                # *continue_* updates
                
                # if continue_ is starting this frame...
                if continue_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    continue_.frameNStart = frameN  # exact frame index
                    continue_.tStart = t  # local t and not account for scr refresh
                    continue_.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(continue_, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'continue_.started')
                    # update status
                    continue_.status = STARTED
                    continue_.setAutoDraw(True)
                
                # if continue_ is active this frame...
                if continue_.status == STARTED:
                    # update params
                    pass
                # *symmetry_problem_next* updates
                
                # if symmetry_problem_next is starting this frame...
                if symmetry_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    symmetry_problem_next.frameNStart = frameN  # exact frame index
                    symmetry_problem_next.tStart = t  # local t and not account for scr refresh
                    symmetry_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(symmetry_problem_next, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('symmetry_problem_next.started', t)
                    # update status
                    symmetry_problem_next.status = STARTED
                    symmetry_problem_next.mouseClock.reset()
                    prevButtonState = symmetry_problem_next.getPressed()  # if button is down already this ISN'T a new click
                if symmetry_problem_next.status == STARTED:  # only update if started and not finished!
                    buttons = symmetry_problem_next.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames(continue_, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(symmetry_problem_next):
                                    gotValidClick = True
                                    symmetry_problem_next.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                
                # *rotation_problem* updates
                
                # if rotation_problem is starting this frame...
                if rotation_problem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rotation_problem.frameNStart = frameN  # exact frame index
                    rotation_problem.tStart = t  # local t and not account for scr refresh
                    rotation_problem.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rotation_problem, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_problem.started')
                    # update status
                    rotation_problem.status = STARTED
                    rotation_problem.setAutoDraw(True)
                
                # if rotation_problem is active this frame...
                if rotation_problem.status == STARTED:
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
                for thisComponent in rotationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rotation" ---
            for thisComponent in rotationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rotation.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from rotation_code
            # salva variáveis
            thisExp.addData("rotation_letter", stimuli[letter_count][0]) # nome da imagem
            thisExp.addData("rotation_orientation", stimuli[letter_count][1]) # orientation
            thisExp.addData("rotation_flip", stimuli[letter_count][2]) # flipped vs. non-flipped
            thisExp.addData("rotation_corr", stimuli[letter_count][3]) # gabarito
            
            if abort_trial:
                rotation_speed_error = 1 # abortou devido a velocidade
            else:
                rotation_speed_error = 0 # abortou devido a velocidade
            
            try:
                thisExp.addData("problem_rt", rotation_clock.getTime()) # problem RT
            except:
                pass
            
            # store data for rotspan_training_trial (TrialHandler)
            # the Routine "rotation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "rotation_answer" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rotation_answer.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from rotation_answer_code
            answer_clock = core.Clock()
            
            if abort_trial:
                continueRoutine = False
            # setup some python lists for storing info about the rotation_response
            rotation_response.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            rotation_answerComponents = [rotation_answer_screen, yes, no, rotation_response]
            for thisComponent in rotation_answerComponents:
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
            
            # --- Run Routine "rotation_answer" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from rotation_answer_code
                try:
                    # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                    if rotation_clock.getTime() >= rotation_criterion:
                        speed_errors += 1
                        abort_trial = True
                        continueRoutine = False
                except:
                    pass
                
                
                # *rotation_answer_screen* updates
                
                # if rotation_answer_screen is starting this frame...
                if rotation_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rotation_answer_screen.frameNStart = frameN  # exact frame index
                    rotation_answer_screen.tStart = t  # local t and not account for scr refresh
                    rotation_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rotation_answer_screen, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_answer_screen.started')
                    # update status
                    rotation_answer_screen.status = STARTED
                    rotation_answer_screen.setAutoDraw(True)
                
                # if rotation_answer_screen is active this frame...
                if rotation_answer_screen.status == STARTED:
                    # update params
                    pass
                
                # *yes* updates
                
                # if yes is starting this frame...
                if yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yes.frameNStart = frameN  # exact frame index
                    yes.tStart = t  # local t and not account for scr refresh
                    yes.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yes, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yes.started')
                    # update status
                    yes.status = STARTED
                    yes.setAutoDraw(True)
                
                # if yes is active this frame...
                if yes.status == STARTED:
                    # update params
                    pass
                
                # *no* updates
                
                # if no is starting this frame...
                if no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    no.frameNStart = frameN  # exact frame index
                    no.tStart = t  # local t and not account for scr refresh
                    no.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'no.started')
                    # update status
                    no.status = STARTED
                    no.setAutoDraw(True)
                
                # if no is active this frame...
                if no.status == STARTED:
                    # update params
                    pass
                # *rotation_response* updates
                
                # if rotation_response is starting this frame...
                if rotation_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rotation_response.frameNStart = frameN  # exact frame index
                    rotation_response.tStart = t  # local t and not account for scr refresh
                    rotation_response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rotation_response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('rotation_response.started', t)
                    # update status
                    rotation_response.status = STARTED
                    rotation_response.mouseClock.reset()
                    prevButtonState = rotation_response.getPressed()  # if button is down already this ISN'T a new click
                if rotation_response.status == STARTED:  # only update if started and not finished!
                    buttons = rotation_response.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames([yes, no], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(rotation_response):
                                    gotValidClick = True
                                    rotation_response.clicked_name.append(obj.name)
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
                for thisComponent in rotation_answerComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rotation_answer" ---
            for thisComponent in rotation_answerComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rotation_answer.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from rotation_answer_code
            try:
                if rotation_response.clicked_name[0] == "yes":
                    rotation_participant_response = "yes"
                else:
                    rotation_participant_response = "no"
            except:
                rotation_participant_response = ""
                rotation_speed_error = 1
            
            try:
                thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
            except:
                pass
            
            # se o participante acertou
            if rotation_participant_response == stimuli[letter_count][3]:
                rotation_participant_corr = 1
                rotation_accuracy_error = 0 # contagem de erros de acurácia
                rotation_trials_correct += 1 # incrementa número de acertos da sessão toda
                rotation_corrective_feedback = "Correto"
            else:
                rotation_participant_corr = 0
                rotation_corrective_feedback = "Incorreto"
                rotation_errors += 1 # incrementa o número de erros apenas da presente tentativa
            
                if rotation_speed_error == 0:
                    rotation_accuracy_error = 1
                else:
                    rotation_accuracy_error = 0
            
            # sempre incrementa o contador de tentativas
            rotation_total_trials += 1
            
            if abort_trial:
                thisExp.addData("rotation_speed_error", 1) # erro de velocidade
                abort_trial = False # reseta para a próxima tentativa
            else:
                thisExp.addData("rotation_speed_error", 0)
            
            # salva variáveis
            thisExp.addData("rotation_accuracy_error", rotation_accuracy_error) # erro de acurácia
            thisExp.addData("rotation_participant_corr", rotation_participant_corr) # 1 = acerto, 0 = erro
            thisExp.addData("rotation_problem", stimuli[letter_count][0]) # enunciado
            thisExp.addData("rotation_status", stimuli[letter_count][1]) # gabarito
            thisExp.addData("rotation_corr", stimuli[letter_count][2]) # resposta correta
            thisExp.addData("rotation_participant_response", rotation_participant_response) # resposta do participante
            
            # debug
            # print(f"Letra: {stimuli[letter_count][0]} --- Flip: {stimuli[letter_count][2]} --- Flip2: {rotation_problem.flipHoriz} --- Gabarito: {stimuli[letter_count][3]} --- Resposta: {rotation_participant_response} --- Feedback: {rotation_corrective_feedback}")
            
            # incrementa operação para próxima iteração
            letter_count += 1
            
            # soma a duração da tarefa matemática
            try:
                if rotation_practice_trials.thisN < 15:
                    rotation_training_time.append(rotation_clock.getTime()) # e guarda tempo em uma lista
                    # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
                    if rotation_practice_trials.thisN == 14:
                        rotation_time_mean = np.mean(np.array(rotation_training_time))
                        rotation_time_sd = np.std(np.array(rotation_training_time), ddof = 1)
                        rotation_criterion = rotation_time_mean + 2 * rotation_time_sd
                        
            except:
                pass
            
            
            # store data for rotspan_training_trial (TrialHandler)
            # the Routine "rotation_answer" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "arrow_memory" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('arrow_memory.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from arrow_memory_code
            # tenta atribuir o valor da repetição do loop atual à variável index
            # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
            try:
                index = arrow_memory_practice.thisN
            except:
                pass
                
            try:
                index = rotspan_training_trial.thisN
            except:
                pass
            
            try:
                index = rotspan_testing_trial.thisN
            except:
                pass
            
            # tenta embaralhar as posições do grid sempre que estivermos em uma nova tentativa
            try:
                # se é a primeira execução do loop...
                if arrow_memory_practice.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                    correct_response = "".join(temp)
            except:
                pass
            
            try:
                # se é a primeira execução do loop...
                if rotspan_training_trial.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                        
                    correct_response = "".join(temp)
            except:
                pass
            
            try:
                # se é a primeira execução do loop...
                if rotspan_testing_trial.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                        
                    correct_response = "".join(temp)
            
            except:
                pass
            arrow.setPos([correct_positions[index]])
            arrow.setOri(correct_orientations[index])
            # keep track of which components have finished
            arrow_memoryComponents = [arrow]
            for thisComponent in arrow_memoryComponents:
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
            
            # --- Run Routine "arrow_memory" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *arrow* updates
                
                # if arrow is starting this frame...
                if arrow.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    arrow.frameNStart = frameN  # exact frame index
                    arrow.tStart = t  # local t and not account for scr refresh
                    arrow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'arrow.started')
                    # update status
                    arrow.status = STARTED
                    arrow.setAutoDraw(True)
                
                # if arrow is active this frame...
                if arrow.status == STARTED:
                    # update params
                    pass
                
                # if arrow is stopping this frame...
                if arrow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > arrow.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        arrow.tStop = t  # not accounting for scr refresh
                        arrow.tStopRefresh = tThisFlipGlobal  # on global time
                        arrow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'arrow.stopped')
                        # update status
                        arrow.status = FINISHED
                        arrow.setAutoDraw(False)
                
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
                for thisComponent in arrow_memoryComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "arrow_memory" ---
            for thisComponent in arrow_memoryComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('arrow_memory.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed current_span repeats of 'rotspan_training_trial'
        
        
        # --- Prepare to start Routine "recall" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('recall.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_recall
        clicked_things = []
        arrow_colors = ["black"] * 16
        
        clickables = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank, square]
        allowed_send = False
        allowed_blank = True
        
        my_response = list()
        
        try:
            if arrow_memory_practice_trials.thisN == 0:
                task_phase = "arrow_memory_practice_phase"
        except:
            pass
        
        try:
            if rotspan_training_trials.thisN == 0:
                task_phase = "rotspan_training_trials"
        except:
            pass
        
        try:
            if rotspan_testing_trials.thisN == 0:
                task_phase = "rotspan_testing_trials"
        except:
            pass
        
        
        # setup some python lists for storing info about the recall_response
        recall_response.x = []
        recall_response.y = []
        recall_response.leftButton = []
        recall_response.midButton = []
        recall_response.rightButton = []
        recall_response.time = []
        recall_response.corr = []
        recall_response.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        recallComponents = [prompt_recall, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, clear_, blank, send, square, recall_response]
        for thisComponent in recallComponents:
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
        
        # --- Run Routine "recall" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_recall
            for i, clickable in enumerate(clickables):
                if (clickable == square):
                    pass
                # and it was the blank button:
                elif recall_response.isPressedIn(clickable) and (clickable == blank) and (allowed_blank == True):
                    if len(clicked_things) <= 15:
                        clicked_things.append(clickable.name)
                        # to prevent two consecutive responses
                        allowed_blank = False 
                        blank_clock = core.Clock() 
                        #clicked_things.append(clickable.name)
                        my_response.append("–")
                        allowed_send = True
                # if a button was pressed in
                elif recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                    # and it wasn't send, clear_, and blank buttons
                    if (clickable != send) and (clickable != clear_) and (clickable != blank):
                        if len(clicked_things) <= 15:
                            clicked_things.append(clickable.name)
                            clickable.fillColor = "darkblue"
                            clickable.color = "darkblue"
                            my_response.append(clickable.name)
                            allowed_send = True
                    # and it was the clear_ button
                    elif clickable == clear_:
                        for i, clickable in enumerate(clickables[:-4]):
                            clickable.fillColor = "black"
                            clickable.color = "black"
                        # reset values
                        clicked_things = []
                        my_response = list()
                        allowed_send = False # reset
                    elif (clickable == send) and (allowed_send == True):
                        continueRoutine = False
            
            # it allows the blank button again
            try:
                if blank_clock.getTime() > 1:
                    allowed_blank = True
            except NameError:
                pass
            
            # *prompt_recall* updates
            
            # if prompt_recall is starting this frame...
            if prompt_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_recall.frameNStart = frameN  # exact frame index
                prompt_recall.tStart = t  # local t and not account for scr refresh
                prompt_recall.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_recall, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_recall.started')
                # update status
                prompt_recall.status = STARTED
                prompt_recall.setAutoDraw(True)
            
            # if prompt_recall is active this frame...
            if prompt_recall.status == STARTED:
                # update params
                pass
            
            # *A* updates
            
            # if A is starting this frame...
            if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                A.frameNStart = frameN  # exact frame index
                A.tStart = t  # local t and not account for scr refresh
                A.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A.started')
                # update status
                A.status = STARTED
                A.setAutoDraw(True)
            
            # if A is active this frame...
            if A.status == STARTED:
                # update params
                pass
            
            # *B* updates
            
            # if B is starting this frame...
            if B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B.frameNStart = frameN  # exact frame index
                B.tStart = t  # local t and not account for scr refresh
                B.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'B.started')
                # update status
                B.status = STARTED
                B.setAutoDraw(True)
            
            # if B is active this frame...
            if B.status == STARTED:
                # update params
                pass
            
            # *C* updates
            
            # if C is starting this frame...
            if C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                C.frameNStart = frameN  # exact frame index
                C.tStart = t  # local t and not account for scr refresh
                C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'C.started')
                # update status
                C.status = STARTED
                C.setAutoDraw(True)
            
            # if C is active this frame...
            if C.status == STARTED:
                # update params
                pass
            
            # *D* updates
            
            # if D is starting this frame...
            if D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                D.frameNStart = frameN  # exact frame index
                D.tStart = t  # local t and not account for scr refresh
                D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D.started')
                # update status
                D.status = STARTED
                D.setAutoDraw(True)
            
            # if D is active this frame...
            if D.status == STARTED:
                # update params
                pass
            
            # *E* updates
            
            # if E is starting this frame...
            if E.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                E.frameNStart = frameN  # exact frame index
                E.tStart = t  # local t and not account for scr refresh
                E.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(E, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'E.started')
                # update status
                E.status = STARTED
                E.setAutoDraw(True)
            
            # if E is active this frame...
            if E.status == STARTED:
                # update params
                pass
            
            # *F* updates
            
            # if F is starting this frame...
            if F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                F.frameNStart = frameN  # exact frame index
                F.tStart = t  # local t and not account for scr refresh
                F.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'F.started')
                # update status
                F.status = STARTED
                F.setAutoDraw(True)
            
            # if F is active this frame...
            if F.status == STARTED:
                # update params
                pass
            
            # *G* updates
            
            # if G is starting this frame...
            if G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                G.frameNStart = frameN  # exact frame index
                G.tStart = t  # local t and not account for scr refresh
                G.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(G, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'G.started')
                # update status
                G.status = STARTED
                G.setAutoDraw(True)
            
            # if G is active this frame...
            if G.status == STARTED:
                # update params
                pass
            
            # *H* updates
            
            # if H is starting this frame...
            if H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                H.frameNStart = frameN  # exact frame index
                H.tStart = t  # local t and not account for scr refresh
                H.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(H, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'H.started')
                # update status
                H.status = STARTED
                H.setAutoDraw(True)
            
            # if H is active this frame...
            if H.status == STARTED:
                # update params
                pass
            
            # *I* updates
            
            # if I is starting this frame...
            if I.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                I.frameNStart = frameN  # exact frame index
                I.tStart = t  # local t and not account for scr refresh
                I.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(I, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'I.started')
                # update status
                I.status = STARTED
                I.setAutoDraw(True)
            
            # if I is active this frame...
            if I.status == STARTED:
                # update params
                pass
            
            # *J* updates
            
            # if J is starting this frame...
            if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                J.frameNStart = frameN  # exact frame index
                J.tStart = t  # local t and not account for scr refresh
                J.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'J.started')
                # update status
                J.status = STARTED
                J.setAutoDraw(True)
            
            # if J is active this frame...
            if J.status == STARTED:
                # update params
                pass
            
            # *K* updates
            
            # if K is starting this frame...
            if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                K.frameNStart = frameN  # exact frame index
                K.tStart = t  # local t and not account for scr refresh
                K.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'K.started')
                # update status
                K.status = STARTED
                K.setAutoDraw(True)
            
            # if K is active this frame...
            if K.status == STARTED:
                # update params
                pass
            
            # *L* updates
            
            # if L is starting this frame...
            if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L.frameNStart = frameN  # exact frame index
                L.tStart = t  # local t and not account for scr refresh
                L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L.started')
                # update status
                L.status = STARTED
                L.setAutoDraw(True)
            
            # if L is active this frame...
            if L.status == STARTED:
                # update params
                pass
            
            # *M* updates
            
            # if M is starting this frame...
            if M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                M.frameNStart = frameN  # exact frame index
                M.tStart = t  # local t and not account for scr refresh
                M.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(M, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'M.started')
                # update status
                M.status = STARTED
                M.setAutoDraw(True)
            
            # if M is active this frame...
            if M.status == STARTED:
                # update params
                pass
            
            # *N* updates
            
            # if N is starting this frame...
            if N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                N.frameNStart = frameN  # exact frame index
                N.tStart = t  # local t and not account for scr refresh
                N.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(N, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'N.started')
                # update status
                N.status = STARTED
                N.setAutoDraw(True)
            
            # if N is active this frame...
            if N.status == STARTED:
                # update params
                pass
            
            # *O* updates
            
            # if O is starting this frame...
            if O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                O.frameNStart = frameN  # exact frame index
                O.tStart = t  # local t and not account for scr refresh
                O.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(O, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'O.started')
                # update status
                O.status = STARTED
                O.setAutoDraw(True)
            
            # if O is active this frame...
            if O.status == STARTED:
                # update params
                pass
            
            # *P* updates
            
            # if P is starting this frame...
            if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P.frameNStart = frameN  # exact frame index
                P.tStart = t  # local t and not account for scr refresh
                P.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P.started')
                # update status
                P.status = STARTED
                P.setAutoDraw(True)
            
            # if P is active this frame...
            if P.status == STARTED:
                # update params
                pass
            
            # *clear_* updates
            
            # if clear_ is starting this frame...
            if clear_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clear_.frameNStart = frameN  # exact frame index
                clear_.tStart = t  # local t and not account for scr refresh
                clear_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clear_, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clear_.started')
                # update status
                clear_.status = STARTED
                clear_.setAutoDraw(True)
            
            # if clear_ is active this frame...
            if clear_.status == STARTED:
                # update params
                pass
            
            # *blank* updates
            
            # if blank is starting this frame...
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.started')
                # update status
                blank.status = STARTED
                blank.setAutoDraw(True)
            
            # if blank is active this frame...
            if blank.status == STARTED:
                # update params
                pass
            
            # *send* updates
            
            # if send is starting this frame...
            if send.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                send.frameNStart = frameN  # exact frame index
                send.tStart = t  # local t and not account for scr refresh
                send.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(send, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'send.started')
                # update status
                send.status = STARTED
                send.setAutoDraw(True)
            
            # if send is active this frame...
            if send.status == STARTED:
                # update params
                pass
            
            # *square* updates
            
            # if square is starting this frame...
            if square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square.frameNStart = frameN  # exact frame index
                square.tStart = t  # local t and not account for scr refresh
                square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square.started')
                # update status
                square.status = STARTED
                square.setAutoDraw(True)
            
            # if square is active this frame...
            if square.status == STARTED:
                # update params
                pass
            # *recall_response* updates
            
            # if recall_response is starting this frame...
            if recall_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recall_response.frameNStart = frameN  # exact frame index
                recall_response.tStart = t  # local t and not account for scr refresh
                recall_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('recall_response.started', t)
                # update status
                recall_response.status = STARTED
                recall_response.mouseClock.reset()
                prevButtonState = recall_response.getPressed()  # if button is down already this ISN'T a new click
            if recall_response.status == STARTED:  # only update if started and not finished!
                buttons = recall_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank, square], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(recall_response):
                                gotValidClick = True
                                recall_response.clicked_name.append(obj.name)
                        # check whether click was in correct object
                        if gotValidClick:
                            _corr = 0
                            _corrAns = environmenttools.getFromNames([], namespace=locals())
                            for obj in _corrAns:
                                # is this object clicked on?
                                if obj.contains(recall_response):
                                    _corr = 1
                            recall_response.corr.append(_corr)
                        if gotValidClick:
                            x, y = recall_response.getPos()
                            recall_response.x.append(x)
                            recall_response.y.append(y)
                            buttons = recall_response.getPressed()
                            recall_response.leftButton.append(buttons[0])
                            recall_response.midButton.append(buttons[1])
                            recall_response.rightButton.append(buttons[2])
                            recall_response.time.append(recall_response.mouseClock.getTime())
            
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
            for thisComponent in recallComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recall" ---
        for thisComponent in recallComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('recall.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_recall
        # juntando respostas, mas eliminando respostas repetidas e "send"
        participant_response = "".join(my_response)
        
        # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
        if participant_response == correct_response:
            full_credit_score = current_span
        else:
            full_credit_score = 0
        
        # crédito parcial (pontua apenas acertos na mesma posição serial)
        partial_credit_score = partial_credit(participant_response, correct_response)
        
        # edit distance score
        edit_distance_score = EditDistanceScore(correct_response, participant_response)
        
        # créditos completo parcial e edit distance, somatório da sessão (máx. 42)
        try:
            if rotspan_testing_trials.thisN >= 0:
                final_full_credit_score += full_credit_score
                final_partial_credit_score += partial_credit_score
                final_edit_distance_score += edit_distance_score
        except:
            pass
        
        # criando texto para feedback
        if partial_credit_score > 1:
            word = "setas"    
        elif partial_credit_score <= 1:
            word = "seta"
        
        # mensagens de feedback de recordação e das setas
        recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
        
        try:
            rotation_percent_correct = (rotation_trials_correct / rotation_total_trials) * 100
        except ZeroDivisionError:
            rotation_percent_correct = 0
        
        rotation_performance_msg = f"{rotation_percent_correct:.0f}%"
        
        try:
            if rotation_errors > 1:
                rotation_feedback_msg = f"Você cometeu {rotation_errors} erros neste conjunto de tentativas" 
            elif rotation_errors == 1:
                rotation_feedback_msg = f"Você cometeu {rotation_errors} erro neste conjunto de tentativas"
            else:
                rotation_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
        except:
            rotation_feedback_msg = ""
           
        # salva respostas
        thisExp.addData("correct_response", correct_response)
        thisExp.addData("participant_response", participant_response)
        thisExp.addData("full_credit_score", full_credit_score)
        thisExp.addData("partial_credit_score", partial_credit_score)
        thisExp.addData("edit_distance_score", edit_distance_score)
        thisExp.addData("task_phase", task_phase)
        thisExp.addData("rotationtrials_correct", rotation_trials_correct)
        thisExp.addData("rotation_total_trials", rotation_total_trials)
        thisExp.addData("rotation_percent_correct", rotation_percent_correct)
        try:
            thisExp.addData("rotation_errors", rotation_errors)
        except:
            pass
        
        # reseta para a próxima tentativa
        for clickable in clickables[:-4]:
            clickable.fillColor = "black"
            clickable.color = "black"
        # store data for rotspan_training_trials (TrialHandler)
        rotspan_training_trials.addData('recall_response.x', recall_response.x)
        rotspan_training_trials.addData('recall_response.y', recall_response.y)
        rotspan_training_trials.addData('recall_response.leftButton', recall_response.leftButton)
        rotspan_training_trials.addData('recall_response.midButton', recall_response.midButton)
        rotspan_training_trials.addData('recall_response.rightButton', recall_response.rightButton)
        rotspan_training_trials.addData('recall_response.time', recall_response.time)
        rotspan_training_trials.addData('recall_response.corr', recall_response.corr)
        rotspan_training_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
        # the Routine "recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "recall_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('recall_feedback.started', globalClock.getTime(format='float'))
        recall_feedback_prompt.setText(recall_feedback_msg)
        rotation_feedback_prompt.setText(rotation_feedback_msg)
        rotation_feedback_performance.setColor(rotation_color, colorSpace='rgb')
        rotation_feedback_performance.setText(rotation_performance_msg)
        # keep track of which components have finished
        recall_feedbackComponents = [recall_feedback_prompt, rotation_feedback_prompt, rotation_feedback_performance]
        for thisComponent in recall_feedbackComponents:
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
        
        # --- Run Routine "recall_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_feedback_prompt* updates
            
            # if recall_feedback_prompt is starting this frame...
            if recall_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recall_feedback_prompt.frameNStart = frameN  # exact frame index
                recall_feedback_prompt.tStart = t  # local t and not account for scr refresh
                recall_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_feedback_prompt.started')
                # update status
                recall_feedback_prompt.status = STARTED
                recall_feedback_prompt.setAutoDraw(True)
            
            # if recall_feedback_prompt is active this frame...
            if recall_feedback_prompt.status == STARTED:
                # update params
                pass
            
            # if recall_feedback_prompt is stopping this frame...
            if recall_feedback_prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > recall_feedback_prompt.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    recall_feedback_prompt.tStop = t  # not accounting for scr refresh
                    recall_feedback_prompt.tStopRefresh = tThisFlipGlobal  # on global time
                    recall_feedback_prompt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recall_feedback_prompt.stopped')
                    # update status
                    recall_feedback_prompt.status = FINISHED
                    recall_feedback_prompt.setAutoDraw(False)
            
            # *rotation_feedback_prompt* updates
            
            # if rotation_feedback_prompt is starting this frame...
            if rotation_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_feedback_prompt.frameNStart = frameN  # exact frame index
                rotation_feedback_prompt.tStart = t  # local t and not account for scr refresh
                rotation_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_feedback_prompt.started')
                # update status
                rotation_feedback_prompt.status = STARTED
                rotation_feedback_prompt.setAutoDraw(True)
            
            # if rotation_feedback_prompt is active this frame...
            if rotation_feedback_prompt.status == STARTED:
                # update params
                pass
            
            # if rotation_feedback_prompt is stopping this frame...
            if rotation_feedback_prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rotation_feedback_prompt.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    rotation_feedback_prompt.tStop = t  # not accounting for scr refresh
                    rotation_feedback_prompt.tStopRefresh = tThisFlipGlobal  # on global time
                    rotation_feedback_prompt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_feedback_prompt.stopped')
                    # update status
                    rotation_feedback_prompt.status = FINISHED
                    rotation_feedback_prompt.setAutoDraw(False)
            
            # *rotation_feedback_performance* updates
            
            # if rotation_feedback_performance is starting this frame...
            if rotation_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_feedback_performance.frameNStart = frameN  # exact frame index
                rotation_feedback_performance.tStart = t  # local t and not account for scr refresh
                rotation_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_feedback_performance, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_feedback_performance.started')
                # update status
                rotation_feedback_performance.status = STARTED
                rotation_feedback_performance.setAutoDraw(True)
            
            # if rotation_feedback_performance is active this frame...
            if rotation_feedback_performance.status == STARTED:
                # update params
                pass
            
            # if rotation_feedback_performance is stopping this frame...
            if rotation_feedback_performance.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rotation_feedback_performance.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    rotation_feedback_performance.tStop = t  # not accounting for scr refresh
                    rotation_feedback_performance.tStopRefresh = tThisFlipGlobal  # on global time
                    rotation_feedback_performance.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_feedback_performance.stopped')
                    # update status
                    rotation_feedback_performance.status = FINISHED
                    rotation_feedback_performance.setAutoDraw(False)
            
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
            for thisComponent in recall_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recall_feedback" ---
        for thisComponent in recall_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('recall_feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 3.0 repeats of 'rotspan_training_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    rotspan_testing_instructions = data.TrialHandler(nReps=999.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rotspan_testing_instructions')
    thisExp.addLoop(rotspan_testing_instructions)  # add the loop to the experiment
    thisRotspan_testing_instruction = rotspan_testing_instructions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRotspan_testing_instruction.rgb)
    if thisRotspan_testing_instruction != None:
        for paramName in thisRotspan_testing_instruction:
            globals()[paramName] = thisRotspan_testing_instruction[paramName]
    
    for thisRotspan_testing_instruction in rotspan_testing_instructions:
        currentLoop = rotspan_testing_instructions
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRotspan_testing_instruction.rgb)
        if thisRotspan_testing_instruction != None:
            for paramName in thisRotspan_testing_instruction:
                globals()[paramName] = thisRotspan_testing_instruction[paramName]
        
        # --- Prepare to start Routine "instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instruction.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from instr_code
        my_count = 0 # contador de tentativas da tarefa distratora
        instr_msg.setPos((0, 0.2))
        instr_msg.setText(instruction_list[instruction_block][current_instruction])
        # setup some python lists for storing info about the instr_resp
        instr_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        instructionComponents = [instr_msg, previous, next, instr_resp]
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
            
            # *previous* updates
            
            # if previous is starting this frame...
            if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                previous.frameNStart = frameN  # exact frame index
                previous.tStart = t  # local t and not account for scr refresh
                previous.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'previous.started')
                # update status
                previous.status = STARTED
                previous.setAutoDraw(True)
            
            # if previous is active this frame...
            if previous.status == STARTED:
                # update params
                pass
            
            # *next* updates
            
            # if next is starting this frame...
            if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                next.frameNStart = frameN  # exact frame index
                next.tStart = t  # local t and not account for scr refresh
                next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'next.started')
                # update status
                next.status = STARTED
                next.setAutoDraw(True)
            
            # if next is active this frame...
            if next.status == STARTED:
                # update params
                pass
            # *instr_resp* updates
            
            # if instr_resp is starting this frame...
            if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr_resp.frameNStart = frameN  # exact frame index
                instr_resp.tStart = t  # local t and not account for scr refresh
                instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('instr_resp.started', t)
                # update status
                instr_resp.status = STARTED
                instr_resp.mouseClock.reset()
                prevButtonState = instr_resp.getPressed()  # if button is down already this ISN'T a new click
            if instr_resp.status == STARTED:  # only update if started and not finished!
                buttons = instr_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([previous, next], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(instr_resp):
                                gotValidClick = True
                                instr_resp.clicked_name.append(obj.name)
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
        thisExp.addData('participant_code', participant_code)
        
        if instr_resp.clicked_name[0] == "previous":
            current_instruction -= 1
        elif instr_resp.clicked_name[0] == "next":
            current_instruction += 1
        
        # Se a instrução atual for -1
        if current_instruction == -1:
            # Resete o valor para ser 0
            current_instruction = 0
        # Se a instrução atual é igual ao comprimento da lista de instruções
        elif current_instruction == len(instruction_list[instruction_block]):
            current_instruction = 0 # zera contador de instruções
            if instruction_block == 0:
                instruction_block += 1
                arrow_memory_instructions.finished = True # encerra o loop do treino da tarefa de memória
            elif instruction_block == 1:
                instruction_block += 1
                rotation_instructions.finished = True # encerra o loop do treino da tarefa matemática
            elif instruction_block == 2:
                instruction_block += 1
                rotspan_training_instructions.finished = True # encerra o loop de treino do OSPAN
            elif instruction_block == 3:
                instruction_block += 1
                rotspan_testing_instructions.finished = True # encerra o loop de teste do OSPAN
        
        # store data for rotspan_testing_instructions (TrialHandler)
        # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 999.0 repeats of 'rotspan_testing_instructions'
    
    
    # set up handler to look after randomisation of conditions etc
    rotspan_testing_trials = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('span.xlsx'),
        seed=None, name='rotspan_testing_trials')
    thisExp.addLoop(rotspan_testing_trials)  # add the loop to the experiment
    thisRotspan_testing_trial = rotspan_testing_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRotspan_testing_trial.rgb)
    if thisRotspan_testing_trial != None:
        for paramName in thisRotspan_testing_trial:
            globals()[paramName] = thisRotspan_testing_trial[paramName]
    
    for thisRotspan_testing_trial in rotspan_testing_trials:
        currentLoop = rotspan_testing_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRotspan_testing_trial.rgb)
        if thisRotspan_testing_trial != None:
            for paramName in thisRotspan_testing_trial:
                globals()[paramName] = thisRotspan_testing_trial[paramName]
        
        # set up handler to look after randomisation of conditions etc
        rotspan_testing_trial = data.TrialHandler(nReps=current_span, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='rotspan_testing_trial')
        thisExp.addLoop(rotspan_testing_trial)  # add the loop to the experiment
        thisRotspan_testing_trial = rotspan_testing_trial.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRotspan_testing_trial.rgb)
        if thisRotspan_testing_trial != None:
            for paramName in thisRotspan_testing_trial:
                globals()[paramName] = thisRotspan_testing_trial[paramName]
        
        for thisRotspan_testing_trial in rotspan_testing_trial:
            currentLoop = rotspan_testing_trial
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisRotspan_testing_trial.rgb)
            if thisRotspan_testing_trial != None:
                for paramName in thisRotspan_testing_trial:
                    globals()[paramName] = thisRotspan_testing_trial[paramName]
            
            # --- Prepare to start Routine "rotation" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rotation.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from rotation_code
            rotation_clock = core.Clock()
            
            rotation_problem.flipHoriz = stimuli[letter_count][2]
            rotation_problem.flipVert = False
            
            try:
                # se é a primeira execução do loop...
                if rotation_practice_trials.thisN == 0:
                    rotation_color = "red" # agora teremos feedback na cor vermelha
                    rotation_errors = 0
            except:
                pass
                
            try:
                # se é a primeira execução do loop...
                if rotspan_training_trial.thisN == 0:
                    rotation_errors = 0
            except:
                pass
                
            try:
                # se é a primeira execução do loop...
                if rotspan_testing_trial.thisN == 0:
                    rotation_errors = 0
            except:
                pass
                
            # reseta os contadores quando começa o ROTSPAN para valer
            try:
                if (rotspan_testing_trials.thisN == 0) and (rotspan_testing_trial.thisN == 0):
                    rotation_total_trials = rotation_trials_correct = speed_errors = 0
            except:
                pass
            # setup some python lists for storing info about the symmetry_problem_next
            symmetry_problem_next.clicked_name = []
            gotValidClick = False  # until a click is received
            rotation_problem.setOri(stimuli[letter_count][1])
            rotation_problem.setText(stimuli[letter_count][0])
            # keep track of which components have finished
            rotationComponents = [rotation_prompt, continue_, symmetry_problem_next, rotation_problem]
            for thisComponent in rotationComponents:
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
            
            # --- Run Routine "rotation" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from rotation_code
                try:
                    # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                    if rotation_clock.getTime() >= rotation_criterion:
                        speed_errors += 1
                        abort_trial = True
                        continueRoutine = False
                except:
                    pass
                  
                
                # *rotation_prompt* updates
                
                # if rotation_prompt is starting this frame...
                if rotation_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rotation_prompt.frameNStart = frameN  # exact frame index
                    rotation_prompt.tStart = t  # local t and not account for scr refresh
                    rotation_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rotation_prompt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_prompt.started')
                    # update status
                    rotation_prompt.status = STARTED
                    rotation_prompt.setAutoDraw(True)
                
                # if rotation_prompt is active this frame...
                if rotation_prompt.status == STARTED:
                    # update params
                    pass
                
                # *continue_* updates
                
                # if continue_ is starting this frame...
                if continue_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    continue_.frameNStart = frameN  # exact frame index
                    continue_.tStart = t  # local t and not account for scr refresh
                    continue_.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(continue_, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'continue_.started')
                    # update status
                    continue_.status = STARTED
                    continue_.setAutoDraw(True)
                
                # if continue_ is active this frame...
                if continue_.status == STARTED:
                    # update params
                    pass
                # *symmetry_problem_next* updates
                
                # if symmetry_problem_next is starting this frame...
                if symmetry_problem_next.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    symmetry_problem_next.frameNStart = frameN  # exact frame index
                    symmetry_problem_next.tStart = t  # local t and not account for scr refresh
                    symmetry_problem_next.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(symmetry_problem_next, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('symmetry_problem_next.started', t)
                    # update status
                    symmetry_problem_next.status = STARTED
                    symmetry_problem_next.mouseClock.reset()
                    prevButtonState = symmetry_problem_next.getPressed()  # if button is down already this ISN'T a new click
                if symmetry_problem_next.status == STARTED:  # only update if started and not finished!
                    buttons = symmetry_problem_next.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames(continue_, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(symmetry_problem_next):
                                    gotValidClick = True
                                    symmetry_problem_next.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                
                # *rotation_problem* updates
                
                # if rotation_problem is starting this frame...
                if rotation_problem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rotation_problem.frameNStart = frameN  # exact frame index
                    rotation_problem.tStart = t  # local t and not account for scr refresh
                    rotation_problem.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rotation_problem, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_problem.started')
                    # update status
                    rotation_problem.status = STARTED
                    rotation_problem.setAutoDraw(True)
                
                # if rotation_problem is active this frame...
                if rotation_problem.status == STARTED:
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
                for thisComponent in rotationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rotation" ---
            for thisComponent in rotationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rotation.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from rotation_code
            # salva variáveis
            thisExp.addData("rotation_letter", stimuli[letter_count][0]) # nome da imagem
            thisExp.addData("rotation_orientation", stimuli[letter_count][1]) # orientation
            thisExp.addData("rotation_flip", stimuli[letter_count][2]) # flipped vs. non-flipped
            thisExp.addData("rotation_corr", stimuli[letter_count][3]) # gabarito
            
            if abort_trial:
                rotation_speed_error = 1 # abortou devido a velocidade
            else:
                rotation_speed_error = 0 # abortou devido a velocidade
            
            try:
                thisExp.addData("problem_rt", rotation_clock.getTime()) # problem RT
            except:
                pass
            
            # store data for rotspan_testing_trial (TrialHandler)
            # the Routine "rotation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "rotation_answer" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rotation_answer.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from rotation_answer_code
            answer_clock = core.Clock()
            
            if abort_trial:
                continueRoutine = False
            # setup some python lists for storing info about the rotation_response
            rotation_response.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            rotation_answerComponents = [rotation_answer_screen, yes, no, rotation_response]
            for thisComponent in rotation_answerComponents:
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
            
            # --- Run Routine "rotation_answer" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from rotation_answer_code
                try:
                    # se a duração da rotina excedeu o tempo combinado, interrompa a tentativa
                    if rotation_clock.getTime() >= rotation_criterion:
                        speed_errors += 1
                        abort_trial = True
                        continueRoutine = False
                except:
                    pass
                
                
                # *rotation_answer_screen* updates
                
                # if rotation_answer_screen is starting this frame...
                if rotation_answer_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rotation_answer_screen.frameNStart = frameN  # exact frame index
                    rotation_answer_screen.tStart = t  # local t and not account for scr refresh
                    rotation_answer_screen.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rotation_answer_screen, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_answer_screen.started')
                    # update status
                    rotation_answer_screen.status = STARTED
                    rotation_answer_screen.setAutoDraw(True)
                
                # if rotation_answer_screen is active this frame...
                if rotation_answer_screen.status == STARTED:
                    # update params
                    pass
                
                # *yes* updates
                
                # if yes is starting this frame...
                if yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yes.frameNStart = frameN  # exact frame index
                    yes.tStart = t  # local t and not account for scr refresh
                    yes.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yes, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yes.started')
                    # update status
                    yes.status = STARTED
                    yes.setAutoDraw(True)
                
                # if yes is active this frame...
                if yes.status == STARTED:
                    # update params
                    pass
                
                # *no* updates
                
                # if no is starting this frame...
                if no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    no.frameNStart = frameN  # exact frame index
                    no.tStart = t  # local t and not account for scr refresh
                    no.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'no.started')
                    # update status
                    no.status = STARTED
                    no.setAutoDraw(True)
                
                # if no is active this frame...
                if no.status == STARTED:
                    # update params
                    pass
                # *rotation_response* updates
                
                # if rotation_response is starting this frame...
                if rotation_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rotation_response.frameNStart = frameN  # exact frame index
                    rotation_response.tStart = t  # local t and not account for scr refresh
                    rotation_response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rotation_response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('rotation_response.started', t)
                    # update status
                    rotation_response.status = STARTED
                    rotation_response.mouseClock.reset()
                    prevButtonState = rotation_response.getPressed()  # if button is down already this ISN'T a new click
                if rotation_response.status == STARTED:  # only update if started and not finished!
                    buttons = rotation_response.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames([yes, no], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(rotation_response):
                                    gotValidClick = True
                                    rotation_response.clicked_name.append(obj.name)
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
                for thisComponent in rotation_answerComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rotation_answer" ---
            for thisComponent in rotation_answerComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rotation_answer.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from rotation_answer_code
            try:
                if rotation_response.clicked_name[0] == "yes":
                    rotation_participant_response = "yes"
                else:
                    rotation_participant_response = "no"
            except:
                rotation_participant_response = ""
                rotation_speed_error = 1
            
            try:
                thisExp.addData("answer_rt", answer_clock.getTime()) # answer RT
            except:
                pass
            
            # se o participante acertou
            if rotation_participant_response == stimuli[letter_count][3]:
                rotation_participant_corr = 1
                rotation_accuracy_error = 0 # contagem de erros de acurácia
                rotation_trials_correct += 1 # incrementa número de acertos da sessão toda
                rotation_corrective_feedback = "Correto"
            else:
                rotation_participant_corr = 0
                rotation_corrective_feedback = "Incorreto"
                rotation_errors += 1 # incrementa o número de erros apenas da presente tentativa
            
                if rotation_speed_error == 0:
                    rotation_accuracy_error = 1
                else:
                    rotation_accuracy_error = 0
            
            # sempre incrementa o contador de tentativas
            rotation_total_trials += 1
            
            if abort_trial:
                thisExp.addData("rotation_speed_error", 1) # erro de velocidade
                abort_trial = False # reseta para a próxima tentativa
            else:
                thisExp.addData("rotation_speed_error", 0)
            
            # salva variáveis
            thisExp.addData("rotation_accuracy_error", rotation_accuracy_error) # erro de acurácia
            thisExp.addData("rotation_participant_corr", rotation_participant_corr) # 1 = acerto, 0 = erro
            thisExp.addData("rotation_problem", stimuli[letter_count][0]) # enunciado
            thisExp.addData("rotation_status", stimuli[letter_count][1]) # gabarito
            thisExp.addData("rotation_corr", stimuli[letter_count][2]) # resposta correta
            thisExp.addData("rotation_participant_response", rotation_participant_response) # resposta do participante
            
            # debug
            # print(f"Letra: {stimuli[letter_count][0]} --- Flip: {stimuli[letter_count][2]} --- Flip2: {rotation_problem.flipHoriz} --- Gabarito: {stimuli[letter_count][3]} --- Resposta: {rotation_participant_response} --- Feedback: {rotation_corrective_feedback}")
            
            # incrementa operação para próxima iteração
            letter_count += 1
            
            # soma a duração da tarefa matemática
            try:
                if rotation_practice_trials.thisN < 15:
                    rotation_training_time.append(rotation_clock.getTime()) # e guarda tempo em uma lista
                    # e, na última tentativa, salva o critério de tempo a ser usado posteriormente
                    if rotation_practice_trials.thisN == 14:
                        rotation_time_mean = np.mean(np.array(rotation_training_time))
                        rotation_time_sd = np.std(np.array(rotation_training_time), ddof = 1)
                        rotation_criterion = rotation_time_mean + 2 * rotation_time_sd
                        
            except:
                pass
            
            
            # store data for rotspan_testing_trial (TrialHandler)
            # the Routine "rotation_answer" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "arrow_memory" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('arrow_memory.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from arrow_memory_code
            # tenta atribuir o valor da repetição do loop atual à variável index
            # isso facilitará o acesso e a apresentação de cada letra na sequência de uma tentativa
            try:
                index = arrow_memory_practice.thisN
            except:
                pass
                
            try:
                index = rotspan_training_trial.thisN
            except:
                pass
            
            try:
                index = rotspan_testing_trial.thisN
            except:
                pass
            
            # tenta embaralhar as posições do grid sempre que estivermos em uma nova tentativa
            try:
                # se é a primeira execução do loop...
                if arrow_memory_practice.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                    correct_response = "".join(temp)
            except:
                pass
            
            try:
                # se é a primeira execução do loop...
                if rotspan_training_trial.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                        
                    correct_response = "".join(temp)
            except:
                pass
            
            try:
                # se é a primeira execução do loop...
                if rotspan_testing_trial.thisN == 0:
                    # embaralha setas usada na tarefa de armazenamento
                    np.random.shuffle(arrow_positions) 
                    # e seleciona a sequência que será o gabarito da atual rodada
                    correct_positions = list()
                    correct_orientations = list()
                    temp = list()
                    for i in range(current_span):
                        correct_orientations.append(arrow_positions[i][0])
                        correct_positions.append(arrow_positions[i][1])
                        temp.append(arrow_positions[i][2])
                        
                    correct_response = "".join(temp)
            
            except:
                pass
            arrow.setPos([correct_positions[index]])
            arrow.setOri(correct_orientations[index])
            # keep track of which components have finished
            arrow_memoryComponents = [arrow]
            for thisComponent in arrow_memoryComponents:
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
            
            # --- Run Routine "arrow_memory" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *arrow* updates
                
                # if arrow is starting this frame...
                if arrow.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    arrow.frameNStart = frameN  # exact frame index
                    arrow.tStart = t  # local t and not account for scr refresh
                    arrow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'arrow.started')
                    # update status
                    arrow.status = STARTED
                    arrow.setAutoDraw(True)
                
                # if arrow is active this frame...
                if arrow.status == STARTED:
                    # update params
                    pass
                
                # if arrow is stopping this frame...
                if arrow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > arrow.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        arrow.tStop = t  # not accounting for scr refresh
                        arrow.tStopRefresh = tThisFlipGlobal  # on global time
                        arrow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'arrow.stopped')
                        # update status
                        arrow.status = FINISHED
                        arrow.setAutoDraw(False)
                
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
                for thisComponent in arrow_memoryComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "arrow_memory" ---
            for thisComponent in arrow_memoryComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('arrow_memory.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed current_span repeats of 'rotspan_testing_trial'
        
        
        # --- Prepare to start Routine "recall" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('recall.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_recall
        clicked_things = []
        arrow_colors = ["black"] * 16
        
        clickables = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank, square]
        allowed_send = False
        allowed_blank = True
        
        my_response = list()
        
        try:
            if arrow_memory_practice_trials.thisN == 0:
                task_phase = "arrow_memory_practice_phase"
        except:
            pass
        
        try:
            if rotspan_training_trials.thisN == 0:
                task_phase = "rotspan_training_trials"
        except:
            pass
        
        try:
            if rotspan_testing_trials.thisN == 0:
                task_phase = "rotspan_testing_trials"
        except:
            pass
        
        
        # setup some python lists for storing info about the recall_response
        recall_response.x = []
        recall_response.y = []
        recall_response.leftButton = []
        recall_response.midButton = []
        recall_response.rightButton = []
        recall_response.time = []
        recall_response.corr = []
        recall_response.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        recallComponents = [prompt_recall, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, clear_, blank, send, square, recall_response]
        for thisComponent in recallComponents:
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
        
        # --- Run Routine "recall" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_recall
            for i, clickable in enumerate(clickables):
                if (clickable == square):
                    pass
                # and it was the blank button:
                elif recall_response.isPressedIn(clickable) and (clickable == blank) and (allowed_blank == True):
                    if len(clicked_things) <= 15:
                        clicked_things.append(clickable.name)
                        # to prevent two consecutive responses
                        allowed_blank = False 
                        blank_clock = core.Clock() 
                        #clicked_things.append(clickable.name)
                        my_response.append("–")
                        allowed_send = True
                # if a button was pressed in
                elif recall_response.isPressedIn(clickable) and (clickable.name not in clicked_things):
                    # and it wasn't send, clear_, and blank buttons
                    if (clickable != send) and (clickable != clear_) and (clickable != blank):
                        if len(clicked_things) <= 15:
                            clicked_things.append(clickable.name)
                            clickable.fillColor = "darkblue"
                            clickable.color = "darkblue"
                            my_response.append(clickable.name)
                            allowed_send = True
                    # and it was the clear_ button
                    elif clickable == clear_:
                        for i, clickable in enumerate(clickables[:-4]):
                            clickable.fillColor = "black"
                            clickable.color = "black"
                        # reset values
                        clicked_things = []
                        my_response = list()
                        allowed_send = False # reset
                    elif (clickable == send) and (allowed_send == True):
                        continueRoutine = False
            
            # it allows the blank button again
            try:
                if blank_clock.getTime() > 1:
                    allowed_blank = True
            except NameError:
                pass
            
            # *prompt_recall* updates
            
            # if prompt_recall is starting this frame...
            if prompt_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_recall.frameNStart = frameN  # exact frame index
                prompt_recall.tStart = t  # local t and not account for scr refresh
                prompt_recall.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_recall, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_recall.started')
                # update status
                prompt_recall.status = STARTED
                prompt_recall.setAutoDraw(True)
            
            # if prompt_recall is active this frame...
            if prompt_recall.status == STARTED:
                # update params
                pass
            
            # *A* updates
            
            # if A is starting this frame...
            if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                A.frameNStart = frameN  # exact frame index
                A.tStart = t  # local t and not account for scr refresh
                A.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A.started')
                # update status
                A.status = STARTED
                A.setAutoDraw(True)
            
            # if A is active this frame...
            if A.status == STARTED:
                # update params
                pass
            
            # *B* updates
            
            # if B is starting this frame...
            if B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                B.frameNStart = frameN  # exact frame index
                B.tStart = t  # local t and not account for scr refresh
                B.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'B.started')
                # update status
                B.status = STARTED
                B.setAutoDraw(True)
            
            # if B is active this frame...
            if B.status == STARTED:
                # update params
                pass
            
            # *C* updates
            
            # if C is starting this frame...
            if C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                C.frameNStart = frameN  # exact frame index
                C.tStart = t  # local t and not account for scr refresh
                C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'C.started')
                # update status
                C.status = STARTED
                C.setAutoDraw(True)
            
            # if C is active this frame...
            if C.status == STARTED:
                # update params
                pass
            
            # *D* updates
            
            # if D is starting this frame...
            if D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                D.frameNStart = frameN  # exact frame index
                D.tStart = t  # local t and not account for scr refresh
                D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D.started')
                # update status
                D.status = STARTED
                D.setAutoDraw(True)
            
            # if D is active this frame...
            if D.status == STARTED:
                # update params
                pass
            
            # *E* updates
            
            # if E is starting this frame...
            if E.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                E.frameNStart = frameN  # exact frame index
                E.tStart = t  # local t and not account for scr refresh
                E.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(E, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'E.started')
                # update status
                E.status = STARTED
                E.setAutoDraw(True)
            
            # if E is active this frame...
            if E.status == STARTED:
                # update params
                pass
            
            # *F* updates
            
            # if F is starting this frame...
            if F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                F.frameNStart = frameN  # exact frame index
                F.tStart = t  # local t and not account for scr refresh
                F.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'F.started')
                # update status
                F.status = STARTED
                F.setAutoDraw(True)
            
            # if F is active this frame...
            if F.status == STARTED:
                # update params
                pass
            
            # *G* updates
            
            # if G is starting this frame...
            if G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                G.frameNStart = frameN  # exact frame index
                G.tStart = t  # local t and not account for scr refresh
                G.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(G, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'G.started')
                # update status
                G.status = STARTED
                G.setAutoDraw(True)
            
            # if G is active this frame...
            if G.status == STARTED:
                # update params
                pass
            
            # *H* updates
            
            # if H is starting this frame...
            if H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                H.frameNStart = frameN  # exact frame index
                H.tStart = t  # local t and not account for scr refresh
                H.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(H, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'H.started')
                # update status
                H.status = STARTED
                H.setAutoDraw(True)
            
            # if H is active this frame...
            if H.status == STARTED:
                # update params
                pass
            
            # *I* updates
            
            # if I is starting this frame...
            if I.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                I.frameNStart = frameN  # exact frame index
                I.tStart = t  # local t and not account for scr refresh
                I.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(I, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'I.started')
                # update status
                I.status = STARTED
                I.setAutoDraw(True)
            
            # if I is active this frame...
            if I.status == STARTED:
                # update params
                pass
            
            # *J* updates
            
            # if J is starting this frame...
            if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                J.frameNStart = frameN  # exact frame index
                J.tStart = t  # local t and not account for scr refresh
                J.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'J.started')
                # update status
                J.status = STARTED
                J.setAutoDraw(True)
            
            # if J is active this frame...
            if J.status == STARTED:
                # update params
                pass
            
            # *K* updates
            
            # if K is starting this frame...
            if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                K.frameNStart = frameN  # exact frame index
                K.tStart = t  # local t and not account for scr refresh
                K.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'K.started')
                # update status
                K.status = STARTED
                K.setAutoDraw(True)
            
            # if K is active this frame...
            if K.status == STARTED:
                # update params
                pass
            
            # *L* updates
            
            # if L is starting this frame...
            if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L.frameNStart = frameN  # exact frame index
                L.tStart = t  # local t and not account for scr refresh
                L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L.started')
                # update status
                L.status = STARTED
                L.setAutoDraw(True)
            
            # if L is active this frame...
            if L.status == STARTED:
                # update params
                pass
            
            # *M* updates
            
            # if M is starting this frame...
            if M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                M.frameNStart = frameN  # exact frame index
                M.tStart = t  # local t and not account for scr refresh
                M.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(M, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'M.started')
                # update status
                M.status = STARTED
                M.setAutoDraw(True)
            
            # if M is active this frame...
            if M.status == STARTED:
                # update params
                pass
            
            # *N* updates
            
            # if N is starting this frame...
            if N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                N.frameNStart = frameN  # exact frame index
                N.tStart = t  # local t and not account for scr refresh
                N.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(N, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'N.started')
                # update status
                N.status = STARTED
                N.setAutoDraw(True)
            
            # if N is active this frame...
            if N.status == STARTED:
                # update params
                pass
            
            # *O* updates
            
            # if O is starting this frame...
            if O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                O.frameNStart = frameN  # exact frame index
                O.tStart = t  # local t and not account for scr refresh
                O.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(O, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'O.started')
                # update status
                O.status = STARTED
                O.setAutoDraw(True)
            
            # if O is active this frame...
            if O.status == STARTED:
                # update params
                pass
            
            # *P* updates
            
            # if P is starting this frame...
            if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P.frameNStart = frameN  # exact frame index
                P.tStart = t  # local t and not account for scr refresh
                P.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P.started')
                # update status
                P.status = STARTED
                P.setAutoDraw(True)
            
            # if P is active this frame...
            if P.status == STARTED:
                # update params
                pass
            
            # *clear_* updates
            
            # if clear_ is starting this frame...
            if clear_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clear_.frameNStart = frameN  # exact frame index
                clear_.tStart = t  # local t and not account for scr refresh
                clear_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clear_, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clear_.started')
                # update status
                clear_.status = STARTED
                clear_.setAutoDraw(True)
            
            # if clear_ is active this frame...
            if clear_.status == STARTED:
                # update params
                pass
            
            # *blank* updates
            
            # if blank is starting this frame...
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.started')
                # update status
                blank.status = STARTED
                blank.setAutoDraw(True)
            
            # if blank is active this frame...
            if blank.status == STARTED:
                # update params
                pass
            
            # *send* updates
            
            # if send is starting this frame...
            if send.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                send.frameNStart = frameN  # exact frame index
                send.tStart = t  # local t and not account for scr refresh
                send.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(send, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'send.started')
                # update status
                send.status = STARTED
                send.setAutoDraw(True)
            
            # if send is active this frame...
            if send.status == STARTED:
                # update params
                pass
            
            # *square* updates
            
            # if square is starting this frame...
            if square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square.frameNStart = frameN  # exact frame index
                square.tStart = t  # local t and not account for scr refresh
                square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square.started')
                # update status
                square.status = STARTED
                square.setAutoDraw(True)
            
            # if square is active this frame...
            if square.status == STARTED:
                # update params
                pass
            # *recall_response* updates
            
            # if recall_response is starting this frame...
            if recall_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recall_response.frameNStart = frameN  # exact frame index
                recall_response.tStart = t  # local t and not account for scr refresh
                recall_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('recall_response.started', t)
                # update status
                recall_response.status = STARTED
                recall_response.mouseClock.reset()
                prevButtonState = recall_response.getPressed()  # if button is down already this ISN'T a new click
            if recall_response.status == STARTED:  # only update if started and not finished!
                buttons = recall_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, send, clear_, blank, square], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(recall_response):
                                gotValidClick = True
                                recall_response.clicked_name.append(obj.name)
                        # check whether click was in correct object
                        if gotValidClick:
                            _corr = 0
                            _corrAns = environmenttools.getFromNames([], namespace=locals())
                            for obj in _corrAns:
                                # is this object clicked on?
                                if obj.contains(recall_response):
                                    _corr = 1
                            recall_response.corr.append(_corr)
                        if gotValidClick:
                            x, y = recall_response.getPos()
                            recall_response.x.append(x)
                            recall_response.y.append(y)
                            buttons = recall_response.getPressed()
                            recall_response.leftButton.append(buttons[0])
                            recall_response.midButton.append(buttons[1])
                            recall_response.rightButton.append(buttons[2])
                            recall_response.time.append(recall_response.mouseClock.getTime())
            
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
            for thisComponent in recallComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recall" ---
        for thisComponent in recallComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('recall.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_recall
        # juntando respostas, mas eliminando respostas repetidas e "send"
        participant_response = "".join(my_response)
        
        # crédito completo (pontua apenas sequência idêntica ao gabarito, incluindo ordenação)
        if participant_response == correct_response:
            full_credit_score = current_span
        else:
            full_credit_score = 0
        
        # crédito parcial (pontua apenas acertos na mesma posição serial)
        partial_credit_score = partial_credit(participant_response, correct_response)
        
        # edit distance score
        edit_distance_score = EditDistanceScore(correct_response, participant_response)
        
        # créditos completo parcial e edit distance, somatório da sessão (máx. 42)
        try:
            if rotspan_testing_trials.thisN >= 0:
                final_full_credit_score += full_credit_score
                final_partial_credit_score += partial_credit_score
                final_edit_distance_score += edit_distance_score
        except:
            pass
        
        # criando texto para feedback
        if partial_credit_score > 1:
            word = "setas"    
        elif partial_credit_score <= 1:
            word = "seta"
        
        # mensagens de feedback de recordação e das setas
        recall_feedback_msg = f"Você lembrou corretamente de {partial_credit_score} {word} de um total de {current_span}."
        
        try:
            rotation_percent_correct = (rotation_trials_correct / rotation_total_trials) * 100
        except ZeroDivisionError:
            rotation_percent_correct = 0
        
        rotation_performance_msg = f"{rotation_percent_correct:.0f}%"
        
        try:
            if rotation_errors > 1:
                rotation_feedback_msg = f"Você cometeu {rotation_errors} erros neste conjunto de tentativas" 
            elif rotation_errors == 1:
                rotation_feedback_msg = f"Você cometeu {rotation_errors} erro neste conjunto de tentativas"
            else:
                rotation_feedback_msg =  f"Você não cometeu erros erros neste conjunto de tentativas"
        except:
            rotation_feedback_msg = ""
           
        # salva respostas
        thisExp.addData("correct_response", correct_response)
        thisExp.addData("participant_response", participant_response)
        thisExp.addData("full_credit_score", full_credit_score)
        thisExp.addData("partial_credit_score", partial_credit_score)
        thisExp.addData("edit_distance_score", edit_distance_score)
        thisExp.addData("task_phase", task_phase)
        thisExp.addData("rotationtrials_correct", rotation_trials_correct)
        thisExp.addData("rotation_total_trials", rotation_total_trials)
        thisExp.addData("rotation_percent_correct", rotation_percent_correct)
        try:
            thisExp.addData("rotation_errors", rotation_errors)
        except:
            pass
        
        # reseta para a próxima tentativa
        for clickable in clickables[:-4]:
            clickable.fillColor = "black"
            clickable.color = "black"
        # store data for rotspan_testing_trials (TrialHandler)
        rotspan_testing_trials.addData('recall_response.x', recall_response.x)
        rotspan_testing_trials.addData('recall_response.y', recall_response.y)
        rotspan_testing_trials.addData('recall_response.leftButton', recall_response.leftButton)
        rotspan_testing_trials.addData('recall_response.midButton', recall_response.midButton)
        rotspan_testing_trials.addData('recall_response.rightButton', recall_response.rightButton)
        rotspan_testing_trials.addData('recall_response.time', recall_response.time)
        rotspan_testing_trials.addData('recall_response.corr', recall_response.corr)
        rotspan_testing_trials.addData('recall_response.clicked_name', recall_response.clicked_name)
        # the Routine "recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "recall_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('recall_feedback.started', globalClock.getTime(format='float'))
        recall_feedback_prompt.setText(recall_feedback_msg)
        rotation_feedback_prompt.setText(rotation_feedback_msg)
        rotation_feedback_performance.setColor(rotation_color, colorSpace='rgb')
        rotation_feedback_performance.setText(rotation_performance_msg)
        # keep track of which components have finished
        recall_feedbackComponents = [recall_feedback_prompt, rotation_feedback_prompt, rotation_feedback_performance]
        for thisComponent in recall_feedbackComponents:
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
        
        # --- Run Routine "recall_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_feedback_prompt* updates
            
            # if recall_feedback_prompt is starting this frame...
            if recall_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recall_feedback_prompt.frameNStart = frameN  # exact frame index
                recall_feedback_prompt.tStart = t  # local t and not account for scr refresh
                recall_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_feedback_prompt.started')
                # update status
                recall_feedback_prompt.status = STARTED
                recall_feedback_prompt.setAutoDraw(True)
            
            # if recall_feedback_prompt is active this frame...
            if recall_feedback_prompt.status == STARTED:
                # update params
                pass
            
            # if recall_feedback_prompt is stopping this frame...
            if recall_feedback_prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > recall_feedback_prompt.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    recall_feedback_prompt.tStop = t  # not accounting for scr refresh
                    recall_feedback_prompt.tStopRefresh = tThisFlipGlobal  # on global time
                    recall_feedback_prompt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recall_feedback_prompt.stopped')
                    # update status
                    recall_feedback_prompt.status = FINISHED
                    recall_feedback_prompt.setAutoDraw(False)
            
            # *rotation_feedback_prompt* updates
            
            # if rotation_feedback_prompt is starting this frame...
            if rotation_feedback_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_feedback_prompt.frameNStart = frameN  # exact frame index
                rotation_feedback_prompt.tStart = t  # local t and not account for scr refresh
                rotation_feedback_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_feedback_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_feedback_prompt.started')
                # update status
                rotation_feedback_prompt.status = STARTED
                rotation_feedback_prompt.setAutoDraw(True)
            
            # if rotation_feedback_prompt is active this frame...
            if rotation_feedback_prompt.status == STARTED:
                # update params
                pass
            
            # if rotation_feedback_prompt is stopping this frame...
            if rotation_feedback_prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rotation_feedback_prompt.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    rotation_feedback_prompt.tStop = t  # not accounting for scr refresh
                    rotation_feedback_prompt.tStopRefresh = tThisFlipGlobal  # on global time
                    rotation_feedback_prompt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_feedback_prompt.stopped')
                    # update status
                    rotation_feedback_prompt.status = FINISHED
                    rotation_feedback_prompt.setAutoDraw(False)
            
            # *rotation_feedback_performance* updates
            
            # if rotation_feedback_performance is starting this frame...
            if rotation_feedback_performance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rotation_feedback_performance.frameNStart = frameN  # exact frame index
                rotation_feedback_performance.tStart = t  # local t and not account for scr refresh
                rotation_feedback_performance.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rotation_feedback_performance, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rotation_feedback_performance.started')
                # update status
                rotation_feedback_performance.status = STARTED
                rotation_feedback_performance.setAutoDraw(True)
            
            # if rotation_feedback_performance is active this frame...
            if rotation_feedback_performance.status == STARTED:
                # update params
                pass
            
            # if rotation_feedback_performance is stopping this frame...
            if rotation_feedback_performance.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rotation_feedback_performance.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    rotation_feedback_performance.tStop = t  # not accounting for scr refresh
                    rotation_feedback_performance.tStopRefresh = tThisFlipGlobal  # on global time
                    rotation_feedback_performance.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rotation_feedback_performance.stopped')
                    # update status
                    rotation_feedback_performance.status = FINISHED
                    rotation_feedback_performance.setAutoDraw(False)
            
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
            for thisComponent in recall_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recall_feedback" ---
        for thisComponent in recall_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('recall_feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 3.0 repeats of 'rotspan_testing_trials'
    
    
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
    # Run 'End Experiment' code from welcome_code
    # código do participante
    thisExp.addData("participant_code", participant_code)
    
    # salvando duração da sessão...
    thisExp.addData("session_duration", globalClock.getTime())
    # Run 'End Experiment' code from instr_code
    # código do participante
    thisExp.addData("participant_code", participant_code)
    
    # salvando duração da sessão...
    thisExp.addData("session_duration", globalClock.getTime())
    
    # Run 'End Experiment' code from code_recall
    thisExp.addData("final_full_credit_score", final_full_credit_score)
    thisExp.addData("final_partial_credit_score", final_partial_credit_score)
    thisExp.addData("final_edit_distance_score", final_edit_distance_score)
    
    # Run 'End Experiment' code from instr_code
    # código do participante
    thisExp.addData("participant_code", participant_code)
    
    # salvando duração da sessão...
    thisExp.addData("session_duration", globalClock.getTime())
    
    # Run 'End Experiment' code from rotation_answer_code
    thisExp.addData("rotation_time_mean", rotation_time_mean)
    thisExp.addData("rotation_time_sd", rotation_time_sd)
    thisExp.addData("rotation_criterion", rotation_criterion)
    # Run 'End Experiment' code from instr_code
    # código do participante
    thisExp.addData("participant_code", participant_code)
    
    # salvando duração da sessão...
    thisExp.addData("session_duration", globalClock.getTime())
    
    # Run 'End Experiment' code from rotation_answer_code
    thisExp.addData("rotation_time_mean", rotation_time_mean)
    thisExp.addData("rotation_time_sd", rotation_time_sd)
    thisExp.addData("rotation_criterion", rotation_criterion)
    # Run 'End Experiment' code from code_recall
    thisExp.addData("final_full_credit_score", final_full_credit_score)
    thisExp.addData("final_partial_credit_score", final_partial_credit_score)
    thisExp.addData("final_edit_distance_score", final_edit_distance_score)
    
    # Run 'End Experiment' code from instr_code
    # código do participante
    thisExp.addData("participant_code", participant_code)
    
    # salvando duração da sessão...
    thisExp.addData("session_duration", globalClock.getTime())
    
    # Run 'End Experiment' code from rotation_answer_code
    thisExp.addData("rotation_time_mean", rotation_time_mean)
    thisExp.addData("rotation_time_sd", rotation_time_sd)
    thisExp.addData("rotation_criterion", rotation_criterion)
    # Run 'End Experiment' code from code_recall
    thisExp.addData("final_full_credit_score", final_full_credit_score)
    thisExp.addData("final_partial_credit_score", final_partial_credit_score)
    thisExp.addData("final_edit_distance_score", final_edit_distance_score)
    
    
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
