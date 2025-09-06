#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on September 06, 2025, at 12:42
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




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'keep-track-task'  # from the Builder filename that created this script
expInfo = {
    'ID': f"{randint(1, 999999999):06.0f}",
    'Nome Completo': '',
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 071 – Keep Track Task\\keep-track-task_lastrun.py',
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
    monitor='testMonitor', color='0.0000, 0.0000, 0.0000', colorSpace='rgb',
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
 
instruction_list = [
"""
Neste estudo, você verá sequências de palavras na tela. As palavras são de diferentes categorias semânticas.

Por exemplo, as palavras "Camiseta", "Calça" e "Blusa" são da categoria Vestuários; já as palavras "Bateria", "Flauta" e "Violão" são da categoria Instrumentos Musicais. 
""",
"""
Em cada tentativa, sua tarefa será monitorar qual foi a última palavra vista de cada categoria-alvo. 

Os nomes das categorias-alvo de cada tentativa aparecerão na parte superior da tela durante a tentativa.
""",
"""
Ao final, você será questionado sobre quais foram as últimas palavras de cada uma das categorias-alvo. 

Por exemplo, suponha que você viu "Camiseta", "Bateria", "Flauta", "Calça", e as categorias-alvo são Vestuários e Instrumentos Musicais.

Neste caso, as respostas serão "Flauta" e "Calça", pois essas foram as últimas palavras vistas de suas respectivas categorias.
""",
"""
O número de categorias que você deverá memorizar a última palavra variará de tentativa para tentativa.

Lembre-se de memorizar apenas a última palavra de cada categoria-alvo.""",
"""
As questões aparecerão da seguinte maneira:
    
Qual foi o último vestuário que você viu?

[ 1 ] Camiseta
[ 2 ] Calça
[ 3 ] Blusa

Use as teclas numéricas para dar sua resposta.
""",
"""
Em seguida, daremos início à tarefa. Se tiver dúvidas, chame o pesquisador antes de começar. 

Quando estiver pronto, clique em [Avançar] para começar a tarefa.
"""
]

                   
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

# --- Initialize components for Routine "new_trial" ---
# Run 'Begin Experiment' code from new_trial_code
import random

# -----------------------------
# Estímulos do experimento
# -----------------------------
words = {
    "Frutas":   ["Maçã", "Banana", "Morango"],
    "Metais":   ["Alumínio", "Ferro", "Cobre"],
    "Países":   ["Japão", "Alemanha", "Canadá"],
    "Cores":    ["Vermelho", "Azul", "Amarelo"],
    "Parentes": ["Tia", "Pai", "Filha"],
    "Animais":  ["Zebra", "Baleia", "Urso"]
}

categories = list(words.keys())

# -----------------------------
# Parâmetros de desenho
# -----------------------------
# 12 tentativas: 4 blocos de [2,3,4] categorias-alvo embaralhados
number_of_categories = [2, 3, 4] * 4
random.shuffle(number_of_categories)

N_TRIALS = 12
ITEMS_PER_TRIAL = 15             # 15 palavras por tentativa (9 + 6)
ALL_CATS = categories[:]         # 6 categorias sempre presentes

# -----------------------------
# Auxiliares de linguagem (português)
# -----------------------------
gender = { "Frutas":"f","Metais":"m","Países":"m","Cores":"f","Parentes":"m","Animais":"m" }
singular = { "Frutas":"fruta","Metais":"metal","Países":"país","Cores":"cor","Parentes":"parente","Animais":"animal" }

def pergunta_ultima(cat: str) -> str:
    g = gender[cat]
    artigo = "o" if g == "m" else "a"
    ult = "último" if g == "m" else "última"
    return f"Qual foi {artigo} {ult} {singular[cat]}?"

# -----------------------------
# Geração de tentativas
# -----------------------------
trials = []

for t_idx, length in enumerate(number_of_categories[:N_TRIALS], start=1):
    # 1) Sorteia as categorias-alvo desta tentativa (entre as 6)
    random.shuffle(categories)
    current_targets = categories[:length]  # 2, 3 ou 4 categorias a recordar

    # 2) Define quais categorias terão 3 exemplares (3 cats) e quais terão 2 (as outras 3)
    cats_3 = set(random.sample(ALL_CATS, 3))          # 3 categorias com 3 palavras
    cats_2 = [c for c in ALL_CATS if c not in cats_3] # 3 categorias com 2 palavras

    # 3) Seleciona as palavras ÚNICAS do trial:
    #    - Para cats_3, entram as 3 palavras (sem drop)
    #    - Para cats_2, "dropar" 1 palavra aleatória (ficam 2)
    trial_pool = []  # lista de (categoria, palavra) QUE COMPORÃO o trial (15 únicas)
    for cat in ALL_CATS:
        pool = words[cat][:]  # cópia
        if cat in cats_2:
            # drop 1 aleatória → ficam 2
            dropped = random.choice(pool)
            pool.remove(dropped)
        # se cat in cats_3, mantém as 3 palavras
        for w in pool:
            trial_pool.append((cat, w))

    # Sanity checks de unicidade e contagem
    assert len(trial_pool) == ITEMS_PER_TRIAL, "Trial não tem 15 itens."
    assert len(set(trial_pool)) == ITEMS_PER_TRIAL, "Existem palavras duplicadas no trial."

    # 4) Embaralha a ordem de apresentação e rastreia a última vista por categoria
    random.shuffle(trial_pool)
    sequence = trial_pool[:]      # ordem de apresentação (15 tuplas únicas)
    last_seen = {}                # cat -> última palavra vista
    for cat, w in sequence:
        last_seen[cat] = w

    # 5) Constrói as perguntas SOMENTE para as categorias-alvo,
    #    com 3 alternativas da MESMA categoria (embaralhadas),
    #    garantindo presença da correta e salvando índice/value corretos.
    questions = []
    for cat in current_targets:
        prompt = pergunta_ultima(cat)
        correct_value = last_seen[cat]  # deve existir (todas as 6 categorias aparecem)

        # Opções: sempre os 3 exemplares "canônicos" da categoria (não apenas os do trial)
        opts = words[cat][:]           # tem exatamente 3 itens na sua estrutura atual
        # (Se no futuro houver >3, você pode sortear 2 distratores contendo a correta)
        random.shuffle(opts)
        correct_index = opts.index(correct_value) + 1  # 1-based

        questions.append({
            "category": cat,
            "prompt": prompt,
            "options": opts,              # 3 alternativas da MESMA categoria
            "correct_value": correct_value,
            "correct_index": correct_index
        })

    # 6) Empacota a tentativa
    trials.append({
        "trial_number": t_idx,
        "targets": current_targets,
        "cats_with_3": sorted(cats_3),
        "cats_with_2": sorted(cats_2),
        "sequence": sequence,                # 15 (cat, palavra) únicos e embaralhados
        "last_seen_by_category": last_seen,  # gabarito completo
        "questions": questions               # prompts + 3 alternativas + gabarito
    })



new_trial_prompt = visual.TextStim(win=win, name='new_trial_prompt',
    text='Clique em [Avançar] para iniciar a próxima tentativa',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
new_trial_next = visual.ImageStim(
    win=win,
    name='new_trial_next', units='norm', 
    image='images/next_button.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.7), size=(0.35, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
new_trial_resp = event.Mouse(win=win)
x, y = [None, None]
new_trial_resp.mouseClock = core.Clock()

# --- Initialize components for Routine "word_stim" ---
# Run 'Begin Experiment' code from word_code


to_be_remembered_categories = visual.TextStim(win=win, name='to_be_remembered_categories',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.8), height=0.15, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
to_be_remembered = visual.TextStim(win=win, name='to_be_remembered',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "recall" ---
to_be_remembered_categories_2 = visual.TextStim(win=win, name='to_be_remembered_categories_2',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.8), height=0.15, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prompt_recall = visual.TextStim(win=win, name='prompt_recall',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.4), height=0.2, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prompt_recall_letter = visual.TextStim(win=win, name='prompt_recall_letter',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, -0.4), height=0.16, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
recall_response = keyboard.Keyboard()

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
# Run 'End Routine' code from welcome_code
thisExp.addData('participant_code', participant_code)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=999, method='sequential', 
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
    instr_msg.setText(instruction_list[current_instruction])
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
        
        # *previous* updates
        if previous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            previous.frameNStart = frameN  # exact frame index
            previous.tStart = t  # local t and not account for scr refresh
            previous.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(previous, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'previous.started')
            previous.setAutoDraw(True)
        
        # *next* updates
        if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next.frameNStart = frameN  # exact frame index
            next.tStart = t  # local t and not account for scr refresh
            next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next.started')
            next.setAutoDraw(True)
        # *instr_resp* updates
        if instr_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('instr_resp.started', t)
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
                    try:
                        iter([previous, next])
                        clickableList = [previous, next]
                    except:
                        clickableList = [[previous, next]]
                    for obj in clickableList:
                        if obj.contains(instr_resp):
                            gotValidClick = True
                            instr_resp.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
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
    elif current_instruction == len(instruction_list):
        current_instruction = 0 # zera contador de instruções
        instructions.finished = True # encerra o loop de teste do OSPAN
    
    # store data for instructions (TrialHandler)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
keeping_track_trials = data.TrialHandler(nReps=len(number_of_categories), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='keeping_track_trials')
thisExp.addLoop(keeping_track_trials)  # add the loop to the experiment
thisKeeping_track_trial = keeping_track_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisKeeping_track_trial.rgb)
if thisKeeping_track_trial != None:
    for paramName in thisKeeping_track_trial:
        exec('{} = thisKeeping_track_trial[paramName]'.format(paramName))

for thisKeeping_track_trial in keeping_track_trials:
    currentLoop = keeping_track_trials
    # abbreviate parameter names if possible (e.g. rgb = thisKeeping_track_trial.rgb)
    if thisKeeping_track_trial != None:
        for paramName in thisKeeping_track_trial:
            exec('{} = thisKeeping_track_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "new_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from new_trial_code
    
    
    # setup some python lists for storing info about the new_trial_resp
    new_trial_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    new_trialComponents = [new_trial_prompt, new_trial_next, new_trial_resp]
    for thisComponent in new_trialComponents:
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
    
    # --- Run Routine "new_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *new_trial_prompt* updates
        if new_trial_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_trial_prompt.frameNStart = frameN  # exact frame index
            new_trial_prompt.tStart = t  # local t and not account for scr refresh
            new_trial_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_trial_prompt.started')
            new_trial_prompt.setAutoDraw(True)
        
        # *new_trial_next* updates
        if new_trial_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_trial_next.frameNStart = frameN  # exact frame index
            new_trial_next.tStart = t  # local t and not account for scr refresh
            new_trial_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_trial_next.started')
            new_trial_next.setAutoDraw(True)
        # *new_trial_resp* updates
        if new_trial_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_trial_resp.frameNStart = frameN  # exact frame index
            new_trial_resp.tStart = t  # local t and not account for scr refresh
            new_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_trial_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('new_trial_resp.started', t)
            new_trial_resp.status = STARTED
            new_trial_resp.mouseClock.reset()
            prevButtonState = new_trial_resp.getPressed()  # if button is down already this ISN'T a new click
        if new_trial_resp.status == STARTED:  # only update if started and not finished!
            buttons = new_trial_resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(new_trial_next)
                        clickableList = new_trial_next
                    except:
                        clickableList = [new_trial_next]
                    for obj in clickableList:
                        if obj.contains(new_trial_resp):
                            gotValidClick = True
                            new_trial_resp.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in new_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "new_trial" ---
    for thisComponent in new_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from new_trial_code
    thisExp.addData('participant_code', participant_code)
    # store data for keeping_track_trials (TrialHandler)
    # the Routine "new_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    keeping_track_word = data.TrialHandler(nReps=ITEMS_PER_TRIAL, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='keeping_track_word')
    thisExp.addLoop(keeping_track_word)  # add the loop to the experiment
    thisKeeping_track_word = keeping_track_word.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisKeeping_track_word.rgb)
    if thisKeeping_track_word != None:
        for paramName in thisKeeping_track_word:
            exec('{} = thisKeeping_track_word[paramName]'.format(paramName))
    
    for thisKeeping_track_word in keeping_track_word:
        currentLoop = keeping_track_word
        # abbreviate parameter names if possible (e.g. rgb = thisKeeping_track_word.rgb)
        if thisKeeping_track_word != None:
            for paramName in thisKeeping_track_word:
                exec('{} = thisKeeping_track_word[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "word_stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from word_code
        current_categories = "   ".join(trials[keeping_track_trials.thisN]["targets"])
        to_be_remembered_categories.setText(current_categories)
        to_be_remembered.setText(trials[keeping_track_trials.thisN]["sequence"][keeping_track_word.thisN][1])
        # keep track of which components have finished
        word_stimComponents = [to_be_remembered_categories, to_be_remembered]
        for thisComponent in word_stimComponents:
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
        
        # --- Run Routine "word_stim" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *to_be_remembered_categories* updates
            if to_be_remembered_categories.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                to_be_remembered_categories.frameNStart = frameN  # exact frame index
                to_be_remembered_categories.tStart = t  # local t and not account for scr refresh
                to_be_remembered_categories.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(to_be_remembered_categories, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'to_be_remembered_categories.started')
                to_be_remembered_categories.setAutoDraw(True)
            if to_be_remembered_categories.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > to_be_remembered_categories.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    to_be_remembered_categories.tStop = t  # not accounting for scr refresh
                    to_be_remembered_categories.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'to_be_remembered_categories.stopped')
                    to_be_remembered_categories.setAutoDraw(False)
            
            # *to_be_remembered* updates
            if to_be_remembered.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                to_be_remembered.frameNStart = frameN  # exact frame index
                to_be_remembered.tStart = t  # local t and not account for scr refresh
                to_be_remembered.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(to_be_remembered, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'to_be_remembered.started')
                to_be_remembered.setAutoDraw(True)
            if to_be_remembered.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > to_be_remembered.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    to_be_remembered.tStop = t  # not accounting for scr refresh
                    to_be_remembered.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'to_be_remembered.stopped')
                    to_be_remembered.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in word_stimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "word_stim" ---
        for thisComponent in word_stimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from word_code
        thisExp.addData('participant_code', participant_code)
        thisExp.addData('current_categories', current_categories)
        thisExp.addData("category", trials[keeping_track_trials.thisN]["sequence"][keeping_track_word.thisN][0])
        thisExp.addData('word', trials[keeping_track_trials.thisN]["sequence"][keeping_track_word.thisN][1])
        
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed ITEMS_PER_TRIAL repeats of 'keeping_track_word'
    
    
    # set up handler to look after randomisation of conditions etc
    keeping_track_questions = data.TrialHandler(nReps=len(trials[keeping_track_trials.thisN]["targets"]), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='keeping_track_questions')
    thisExp.addLoop(keeping_track_questions)  # add the loop to the experiment
    thisKeeping_track_question = keeping_track_questions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisKeeping_track_question.rgb)
    if thisKeeping_track_question != None:
        for paramName in thisKeeping_track_question:
            exec('{} = thisKeeping_track_question[paramName]'.format(paramName))
    
    for thisKeeping_track_question in keeping_track_questions:
        currentLoop = keeping_track_questions
        # abbreviate parameter names if possible (e.g. rgb = thisKeeping_track_question.rgb)
        if thisKeeping_track_question != None:
            for paramName in thisKeeping_track_question:
                exec('{} = thisKeeping_track_question[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "recall" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_recall
        options = f"""
        [ 1 ] {trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["options"][0]}
        [ 2 ] {trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["options"][1]}
        [ 3 ] {trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["options"][2]}
        """
        
        prompt_recall_letter.alignText = 'left'
        
        to_be_remembered_categories_2.setText(current_categories)
        prompt_recall.setText(trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["prompt"])
        prompt_recall_letter.setText(options)
        recall_response.keys = []
        recall_response.rt = []
        _recall_response_allKeys = []
        # keep track of which components have finished
        recallComponents = [to_be_remembered_categories_2, prompt_recall, prompt_recall_letter, recall_response]
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *to_be_remembered_categories_2* updates
            if to_be_remembered_categories_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                to_be_remembered_categories_2.frameNStart = frameN  # exact frame index
                to_be_remembered_categories_2.tStart = t  # local t and not account for scr refresh
                to_be_remembered_categories_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(to_be_remembered_categories_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'to_be_remembered_categories_2.started')
                to_be_remembered_categories_2.setAutoDraw(True)
            
            # *prompt_recall* updates
            if prompt_recall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_recall.frameNStart = frameN  # exact frame index
                prompt_recall.tStart = t  # local t and not account for scr refresh
                prompt_recall.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_recall, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_recall.started')
                prompt_recall.setAutoDraw(True)
            
            # *prompt_recall_letter* updates
            if prompt_recall_letter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_recall_letter.frameNStart = frameN  # exact frame index
                prompt_recall_letter.tStart = t  # local t and not account for scr refresh
                prompt_recall_letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_recall_letter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_recall_letter.started')
                prompt_recall_letter.setAutoDraw(True)
            
            # *recall_response* updates
            waitOnFlip = False
            if recall_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recall_response.frameNStart = frameN  # exact frame index
                recall_response.tStart = t  # local t and not account for scr refresh
                recall_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_response.started')
                recall_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(recall_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(recall_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if recall_response.status == STARTED and not waitOnFlip:
                theseKeys = recall_response.getKeys(keyList=['1', '2', '3', 'num_1', 'num_2', 'num_3'], waitRelease=False)
                _recall_response_allKeys.extend(theseKeys)
                if len(_recall_response_allKeys):
                    recall_response.keys = _recall_response_allKeys[0].name  # just the first key pressed
                    recall_response.rt = _recall_response_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
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
        # Run 'End Routine' code from code_recall
        thisExp.addData('participant_code', participant_code)
        thisExp.addData('current_categories', current_categories)
        thisExp.addData('n_targets', len(trials[keeping_track_trials.thisN]["targets"]))
        thisExp.addData("target_category", trials[keeping_track_trials.thisN]["targets"][keeping_track_questions.thisN])
        thisExp.addData('option_1', trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["options"][0])
        thisExp.addData('option_2', trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["options"][1])
        thisExp.addData('option_3', trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["options"][2])
        thisExp.addData('correct_value', trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["correct_value"])
        thisExp.addData('resp', recall_response.keys[-1])
        thisExp.addData('resp_corr', trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["correct_index"])
        
        if int(recall_response.keys[-1]) == trials[keeping_track_trials.thisN]["questions"][keeping_track_questions.thisN]["correct_index"]:
            score = 1
        else:
            score = 0
        
        thisExp.addData('score', score)
        # check responses
        if recall_response.keys in ['', [], None]:  # No response was made
            recall_response.keys = None
        keeping_track_questions.addData('recall_response.keys',recall_response.keys)
        if recall_response.keys != None:  # we had a response
            keeping_track_questions.addData('recall_response.rt', recall_response.rt)
        # the Routine "recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed len(trials[keeping_track_trials.thisN]["targets"]) repeats of 'keeping_track_questions'
    
    thisExp.nextEntry()
    
# completed len(number_of_categories) repeats of 'keeping_track_trials'


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
