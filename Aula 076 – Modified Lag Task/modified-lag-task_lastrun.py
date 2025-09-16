#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on September 16, 2025, at 10:24
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
expName = 'modified-lag-task'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\limap\\OneDrive\\Área de Trabalho\\Aula 076 – Modified Lag Task\\modified-lag-task_lastrun.py',
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
Neste estudo, você verá sequências curtas de palavras na tela.

Cada palavra aparecerá uma de cada vez.

Ao final de cada sequência, faremos UMA pergunta sobre a posição de uma palavra na lista.
""",
"""
A pergunta poderá ser:

- "Qual foi a última palavra da lista?"
- "Qual foi a penúltima palavra da lista?"
- "Qual foi a antepenúltima palavra da lista?"
- "Qual foi a quarta palavra, a contar do final da lista?" (isto é, a ante-antepenúltima)
""",
"""
Responda digitando a palavra correspondente. 

Pressione [Enter] para enviar sua resposta.
""",
"""
Por exemplo, suponha que a sequência apresentada foi: Argentina, Brasil, Chile, Dinamarca e que a pergunta seja "Qual foi a última palavra da lista?".

Neste caso, a resposta correta será Dinamarca, pois essa foi a última palavra da lista anterior.
""",
"""
Agora, suponha que a sequência apresentada foi: Argentina, Brasil, Chile, Dinamarca e que a pergunta seja "Qual foi a penúltima palavra da lista?".

Neste caso, a resposta correta será Chile, pois essa foi a penúltima palavra da lista anterior.
""",
"""
Desta vez, suponha que a sequência apresentada foi: Argentina, Brasil, Chile, Dinamarca e que a pergunta seja "Qual foi a antepenúltima palavra da lista?".

Neste caso, a resposta correta será Brasil, pois essa foi a antepenúltima palavra da lista anterior.
""",
"""
Por fim, suponha que a sequência apresentada foi: Argentina, Brasil, Chile, Dinamarca e que a pergunta seja "Qual foi a quarta palavra, a contar do final da lista?".

Neste caso, a resposta correta será Argentina, pois ela foi a quarta palavra, a contar do final da lista (a "ante-antepenúltima"), da lista anterior.
""",
"""
Dicas:
    
- Concentre-se na ordem em que as palavras aparecem.
- Não é necessário falar em voz alta; apenas memorize silenciosamente.
- Se tiver dúvidas durante a tarefa, chame o pesquisador antes de prosseguir.
""",
"""
Em seguida, iniciaremos a tarefa.

Quando estiver pronto(a), clique em [Avançar] para começar.
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
words = ['água', 'agulha', 'animal', 'aranha', 'areia', 'árvore',
         'asa', 'bala', 'baleia', 'banana', 'banco', 'banho', 'barba',
         'barco', 'beijo', 'bicho', 'blusa', 'bocejo', 'bolo', 'bolso',
         'boneca', 'botão', 'brinco', 'bule', 'bíblia', 'cabelo', 'cabeça',
         'cabra', 'cadeia', 'café', 'caixão', 'caju', 'calo', 'calça', 'cama',
         'camisa', 'caneta', 'cantor', 'carro', 'carta', 'casa', 'casaco', 'cesto',
         'chapéu', 'chuchu', 'chute', 'chuva', 'chá', 'chão', 'cidade', 'cinto', 'circo',
         'comida', 'copo', 'coroa', 'corpo', 'couve', 'cárie', 'céu', 'dança', 'dedo',
         'dente', 'disco', 'escola', 'escova', 'estojo', 'farda', 'farelo', 'ferida',
         'filho', 'fio', 'flor', 'fogão', 'fogo', 'fruta', 'gato', 'gelo', 'girafa', 'goiaba',
         'gol', 'gola', 'gordo', 'gosma', 'grade', 'grama', 'haste', 'homem', 'igreja',
         'inseto', 'janela', 'jardim', 'jaula', 'juba', 'lã', 'ladrão', 'lagoa', 'lancha',
         'lanche', 'lápis', 'lata', 'látex', 'leão', 'leite', 'letra', 'linha', 'livro',
         'lixa', 'lixo', 'louça', 'lua', 'mãe', 'magro', 'manga', 'mão', 'mar', 'marcha',
         'marido', 'marte', 'massa', 'mastro', 'médico', 'meia', 'mel', 'menina', 'mesa',
         'metal', 'morro', 'mosca', 'moto', 'motor', 'móvel', 'mulher', 'muro', 'nadar',
         'nariz', 'neve', 'nudez', 'nuvens', 'objeto', 'pai', 'panela', 'pano', 'pão',
         'papel', 'parede', 'pátio', 'pato', 'pé', 'pedra', 'peixe', 'pele', 'pêra',
         'perna', 'pessoa', 'picada', 'pires', 'pneu', 'pó', 'ponte', 'porco', 'porta',
         'prato', 'prisão', 'prova', 'prédio', 'pulmão', 'quarto', 'queijo', 'rádio',
         'rainha', 'rede', 'rio', 'rocha', 'roda', 'rosa', 'roupa', 'rua', 'saco',
         'saia', 'sala', 'salada', 'sangue', 'sapato', 'selva', 'serra', 'sofá', 'sol',
         'sopa', 'suco', 'tabaco', 'tampa', 'tecido', 'teia', 'tênis', 'tinta', 'torta',
         'tosse', 'tricô', 'trigo', 'trono', 'túmulo', 'unha', 'uva', 'vaca', 'veneno',
         'vidro', 'violão', 'vulcão', 'xadrez', 'xícara']

"""
Modified lag task (Shelton et al., 2007, 2009) - Gerador de tentativas
Requisitos do experimento:
- Fatores:
    * list_len ∈ {4, 6}
    * n_back  ∈ {0, 1, 2, 3}  (0 = última; 1 = penúltima; 2 = antepenúltima; 3 = ante-antepenúltima)
    * reps_per_cell = 5
- Total de tentativas = 2 × 4 × 5 = 40.
- Palavras são amostradas de `words` SEM reposição global (nenhuma palavra se repete na tarefa).
- Para cada tentativa, salvar gabarito (palavra-alvo) e a lista integral.
"""

# =========================
# PARÂMETROS DO EXPERIMENTO
# =========================
LIST_LENGTHS = [4, 6]          # dois comprimentos possíveis de lista (4 ou 6 itens)
N_BACK_LEVELS = [0, 1, 2, 3]   # n-back alvo: 0=última, 1=penúltima, 2=antepenúltima, 3=ante-antepenúltima
REPS_PER_CELL = 5              # número de repetições por combinação (list_len × n_back)

# ===========================
# GERAR O PLANO FATORIAL 2x4
# ===========================
# Cria todas as combinações (list_len, n_back), repetidas REPS_PER_CELL vezes.
design = []  # esta lista terá 40 dicionários, um por tentativa (ordem embaralhada depois)
for list_len in LIST_LENGTHS:            # itera por 4 e 6
    for n_back in N_BACK_LEVELS:         # itera por 0, 1, 2, 3
        for rep in range(1, REPS_PER_CELL + 1):  # repetições 1..5
            # cada célula do fatorial é um dicionário com metadados da tentativa
            design.append({"list_len": list_len, "n_back": n_back, "rep": rep})

# Embaralhe a ordem de apresentação das tentativas
# (apenas a ordem; os conteúdos ainda serão sorteados depois)
random.shuffle(design)

# ====================================
# AMOSTRAGEM SEM REPOSIÇÃO DAS PALAVRAS
# ====================================
# Estratégia: embaralhar `words` e consumir sequencialmente o número exato de
# palavras por tentativa (4 ou 6), garantindo que nenhuma palavra se repita no experimento.
pool = words[:]                 # cópia rasa da lista global 'words' para não alterá-la
random.shuffle(pool)            # embaralha o banco de palavras uma vez (reposição global: NÃO)
pool_pointer = 0                # ponteiro/índice de consumo sequencial dentro de 'pool'

# ==========================
# GERAÇÃO DAS TENTATIVAS
# ==========================
trials = []     # onde guardamos as tentativas já “resolvidas” (lista e gabarito)
trial_index = 0 # contador de tentativas (1..40), útil para inspeção

for cell in design:
    trial_index += 1                   # incrementa o índice da tentativa atual
    L = cell["list_len"]               # comprimento da lista desta tentativa (4 ou 6)
    n = cell["n_back"]                 # defasagem n-back (0..3)

    # Pega L palavras únicas do banco de palavras
    # Como 'pool' foi embaralhada e consumimos em fatias não sobrepostas, não há repetição global.
    my_list = pool[pool_pointer:pool_pointer + L]
    pool_pointer += L                  # avança o ponteiro para a próxima fatia

    # Índice-alvo (0-based): última = L-1, penúltima = L-1-1, etc.
    # Ex.: L=4, n=0 -> idx=3 (quarta posição); L=6, n=3 -> idx=2 (terceira posição)
    target_index = L - 1 - n
    assert 0 <= target_index < L, "n_back inválido para o comprimento da lista."
    # (Com L ∈ {4,6} e n ∈ {0,1,2,3}, esta asserção sempre deve ser verdadeira.)

    # Gabarito (palavra que o participante deve recordar)
    target_word = my_list[target_index]

    # Salva linha completa
    # - 'list_as_str' é útil para depuração/checagem manual.
    # - índices 0b (base 0) e 1b (base 1) ajudam a cruzar com logs humanos.
    trials.append({
        "trial_index": trial_index,
        "list_len": L,
        "n_back": n,
        "rep": cell["rep"],
        "target_index_0b": target_index,         # índice alvo (0-based)
        "target_index_1b": target_index + 1,     # índice alvo (1-based) - útil p/ checagem humana
        "target_word": target_word,
        "my_list": my_list[:] 
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

# --- Initialize components for Routine "word_trial" ---
to_be_remembered = visual.TextStim(win=win, name='to_be_remembered',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.3, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "recall" ---
prompt_recall = visual.TextStim(win=win, name='prompt_recall',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0.75), height=0.15, wrapWidth=1.8, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
target_resp = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.2),units='norm',     letterHeight=0.2,
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
     name='target_resp',
     autoLog=True,
)

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
modified_lag_task_trials = data.TrialHandler(nReps=len(trials), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='modified_lag_task_trials')
thisExp.addLoop(modified_lag_task_trials)  # add the loop to the experiment
thisModified_lag_task_trial = modified_lag_task_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisModified_lag_task_trial.rgb)
if thisModified_lag_task_trial != None:
    for paramName in thisModified_lag_task_trial:
        exec('{} = thisModified_lag_task_trial[paramName]'.format(paramName))

for thisModified_lag_task_trial in modified_lag_task_trials:
    currentLoop = modified_lag_task_trials
    # abbreviate parameter names if possible (e.g. rgb = thisModified_lag_task_trial.rgb)
    if thisModified_lag_task_trial != None:
        for paramName in thisModified_lag_task_trial:
            exec('{} = thisModified_lag_task_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "new_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
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
    thisExp.addData("participant_code", participant_code)
    # store data for modified_lag_task_trials (TrialHandler)
    # the Routine "new_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    modified_lag_task_word = data.TrialHandler(nReps=trials[modified_lag_task_trials.thisN]['list_len'], method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='modified_lag_task_word')
    thisExp.addLoop(modified_lag_task_word)  # add the loop to the experiment
    thisModified_lag_task_word = modified_lag_task_word.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisModified_lag_task_word.rgb)
    if thisModified_lag_task_word != None:
        for paramName in thisModified_lag_task_word:
            exec('{} = thisModified_lag_task_word[paramName]'.format(paramName))
    
    for thisModified_lag_task_word in modified_lag_task_word:
        currentLoop = modified_lag_task_word
        # abbreviate parameter names if possible (e.g. rgb = thisModified_lag_task_word.rgb)
        if thisModified_lag_task_word != None:
            for paramName in thisModified_lag_task_word:
                exec('{} = thisModified_lag_task_word[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "word_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from word_trial_code
        my_word = trials[modified_lag_task_trials.thisN]['my_list'][modified_lag_task_word.thisN]
        list_len = trials[modified_lag_task_trials.thisN]['list_len']
        n_back = trials[modified_lag_task_trials.thisN]['n_back']
        target_index_0b = trials[modified_lag_task_trials.thisN]['target_index_0b']
        target_index_1b = trials[modified_lag_task_trials.thisN]['target_index_1b']
        target_word = trials[modified_lag_task_trials.thisN]['target_word']
        my_list = trials[modified_lag_task_trials.thisN]['my_list']
        
        
        to_be_remembered.setText(my_word)
        # keep track of which components have finished
        word_trialComponents = [to_be_remembered]
        for thisComponent in word_trialComponents:
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
        
        # --- Run Routine "word_trial" ---
        while continueRoutine and routineTimer.getTime() < 1.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *to_be_remembered* updates
            if to_be_remembered.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
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
                if tThisFlipGlobal > to_be_remembered.tStartRefresh + 1-frameTolerance:
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
            for thisComponent in word_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "word_trial" ---
        for thisComponent in word_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-1.200000)
    # completed trials[modified_lag_task_trials.thisN]['list_len'] repeats of 'modified_lag_task_word'
    
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_recall
    kb = keyboard.Keyboard()
    
    if n_back == 0:
        my_prompt = "Qual foi a última palavra da lista?"
    elif n_back == 1:
        my_prompt = "Qual foi a penúltima palavra da lista?"
    elif n_back == 2:
        my_prompt = "Qual foi a antepenúltima palavra da lista?"
    elif n_back == 3:
        my_prompt = "Qual foi a quarta palavra, a contar do final da lista?"
        
        
    # inicializa variáveis importantes para a rotina
    max_length = 13
    min_length = 3
    
    event.clearEvents('keyboard')
    
    prompt_recall.setText(my_prompt)
    target_resp.reset()
    # keep track of which components have finished
    recallComponents = [prompt_recall, target_resp]
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
        # Run 'Each Frame' code from code_recall
        target_resp.text = target_resp.text.strip()
        
        # garante que palavra tem comprimento máximo de max_length
        if len(target_resp.text) > max_length:
            target_resp.text = target_resp.text.strip()[:max_length]
        
        # checa se return foi pressionado
        keys = kb.getKeys(['return'], waitRelease = True)
        # se Enter foi pressionado e a resposta tem pelo menos 3 caracteres
        if ('return' in keys) and (len(target_resp.text) >= min_length):
            continueRoutine = False
        
        
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
    modified_lag_task_trials.addData('participant_code', participant_code)
    modified_lag_task_trials.addData('word', my_word)
    modified_lag_task_trials.addData('list_len', list_len)
    modified_lag_task_trials.addData('n_back', n_back)
    modified_lag_task_trials.addData('target_index_0b', target_index_0b)
    modified_lag_task_trials.addData('target_index_1b', target_index_1b)
    modified_lag_task_trials.addData('list', my_list)
    modified_lag_task_trials.addData('target_word', target_word)
    modified_lag_task_trials.addData('participant_response', target_resp.text.strip())
    
    if target_resp.text.strip() == target_word:
        score = 1
        weighted_score = (n_back + 1)
    else:
        score = 0
        weighted_score = 0
        
    modified_lag_task_trials.addData('score', score)  
    modified_lag_task_trials.addData('weighted_score', weighted_score)
    
    # reseta variável para não bugar output
    target_resp.text = ""
    modified_lag_task_trials.addData('target_resp.text',target_resp.text)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed len(trials) repeats of 'modified_lag_task_trials'


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
