from collections import Counter
from datetime import datetime
from bs4 import BeautifulSoup
from os import listdir, path
from tkinter.ttk import *
from tkinter import * 
import tkinter as tk
import requests
import random
import csv
import os

#MAIN FRAME ##################################################
root = tk.Tk()
root.title('FillerAgent v1.03 by classman')
root.geometry("400x420")
root.resizable(False, False)
root.iconbitmap(r"icons/valorant.ico")

canvas1 = tk.Canvas(root, width = 400, height = 400, bg='#0f1923')
bgPhoto = PhotoImage(file = "icons/Bg.png")
canvas1.create_image(10, 10, image = bgPhoto, anchor = NW)
canvas1.pack()

global label1
label1 = tk.Label(root, text='')
global label3
label3 = tk.Label(root, text='')

label6 = tk.Label(root, text='Filler Agent v1.03', bg='#0f1923')
label6.config(font=('helvetica', 14, 'bold'), fg='white')
canvas1.create_window(200, 30, window=label6)

label4 = tk.Label(root, text='(OCT2022 5.08)', bg='#0f1923')
label4.config(font=('helvetica', 10), fg='white')
canvas1.create_window(200, 52, window=label4)

label2 = tk.Label(root, text='Select 4 picked agents:', bg='#0f1923')
label2.config(font=('helvetica', 10, 'bold'), fg='white')
canvas1.create_window(200, 150, window=label2)

label5 = tk.Label(root, text='Possible filler agents:', bg='#0f1923')
label5.config(font=('helvetica', 10, 'bold'), fg='white')
canvas1.create_window(200, 350, window=label5)

#SECONDARY FRAMES ##################################################
def disable_event():
  pass
#update check Window
updateWindow = Toplevel(root,bg='#0f1923')
updateWindow.title("[Update]")
tUpdate = "A newer version has been detected. Please update to the latest version."
mFill = Message(updateWindow, text=tUpdate, width = 380, bg = "#0f1923", font=('helvetica', 12, 'bold'), fg='white').pack(side=TOP, anchor=N)
okButtonUpdate = tk.Button(updateWindow,height = 1, width = 8,text='Ok',bg='red', fg='white',font=('helvetica', 9, 'bold'), activebackground="#292929",command=lambda:[helpMenuOnclicks(""),updateWindow.withdraw(),os.system("start \"\" https://github.com/Maxsafer/ValorantFillerAgent/archive/refs/heads/main.zip")]).pack(side = BOTTOM, anchor = S)
#fillButton dropdown Window
fillWindow = Toplevel(root,bg='#0f1923')
fillWindow.title("[Help] for the 'Fill' button")
tFill = "• The fill button will fill a composition recommending the top 5 agents in descending order that could complete a composition.\n\n• In order for it to work, a map and 4 agents must be selected."
mFill = Message(fillWindow, text=tFill, width = 380, bg = "#0f1923", font=('helvetica', 12, 'bold'), fg='white').pack(side=TOP, anchor=N)
okButtonFill = tk.Button(fillWindow,height = 1, width = 8,text='Ok',bg='red', fg='white',font=('helvetica', 9, 'bold'), activebackground="#292929",command=lambda:[helpMenuOnclicks("")]).pack(side = BOTTOM, anchor = S)
#fullButton dropdown Window
fullWindow = Toplevel(root,bg='#0f1923')
fullWindow.title("[Help] for the 'Full' button")
tFull = "• The full button will select a top 10 composition played by professionals. These compositions are top 10 based on win rate.\n\n• If only 1 agent is selected, it will pop a composition with that agent."
mFull = Message(fullWindow, text=tFull, width = 380, bg = "#0f1923", font=('helvetica', 12, 'bold'), fg='white').pack(side=TOP, anchor=N)
okButtonFull = tk.Button(fullWindow,height = 1, width = 8,text='Ok',bg='red', fg='white',font=('helvetica', 9, 'bold'), activebackground="#292929",command=lambda:[helpMenuOnclicks("")]).pack(side = BOTTOM, anchor = S)
#symbolButton dropdown Window
symbolWindow = Toplevel(root,bg='#0f1923')
symbolWindow.title("[Help] for the symbol nomenclature")
tSymbol = "☆: Means the composition was filled based on a pro composition.\n\nX: Composition was filled based on an analysis. (This requires previous knowledge to understand what is a good recommendation)"
mSymbol = Message(symbolWindow, text=tSymbol, width = 380, bg = "#0f1923", font=('helvetica', 12, 'bold'), fg='white').pack(side=TOP, anchor=N)
okButtonSymbol = tk.Button(symbolWindow,height = 1, width = 8,text='Ok',bg='red', fg='white',font=('helvetica', 9, 'bold'), activebackground="#292929",command=lambda:[helpMenuOnclicks("")]).pack(side = BOTTOM, anchor = S)
#numberButton dropdown Window
numberWindow = Toplevel(root,bg='#0f1923')
numberWindow.title("[Help] what does the number mean")
tNumber = "• The number on the agent list represents the times an agent has been picked on the selected map.\n\n*Note* It does not represent the times that an agent has been picked with that composition."
mNumber = Message(numberWindow, text=tNumber, width = 380, bg = "#0f1923", font=('helvetica', 12, 'bold'), fg='white').pack(side=TOP, anchor=N)
okButtonWindow = tk.Button(numberWindow,height = 1, width = 8,text='Ok',bg='red', fg='white',font=('helvetica', 9, 'bold'), activebackground="#292929",command=lambda:[helpMenuOnclicks("")]).pack(side = BOTTOM, anchor = S)

#DROP DOWN MENU ##################################################
def helpMenuOnclicks(string):
  x = root.winfo_rootx() + 380
  y = root.winfo_rooty() - 50
  for menuButton in menuButtons:
    menuButton.withdraw()
    menuButton.protocol("WM_DELETE_WINDOW", disable_event)
    menuButton.resizable(False, False)
    menuButton.transient(root)
    menuButton.iconbitmap("icons/valorant.ico")
    menuButton.geometry(f'400x150+{x}+{y}')
  match string:
    case "Fill":
      fillWindow.deiconify()
    case "Full":
      fullWindow.deiconify()
    case "Symbol":
      symbolWindow.deiconify()
    case "Number":
      numberWindow.deiconify()
    case "Link":
      os.system("start \"\" https://github.com/Maxsafer/ValorantFillerAgent")
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Fill button", command=lambda:[helpMenuOnclicks("Fill")])
filemenu.add_command(label="Full button", command=lambda:[helpMenuOnclicks("Full")])
filemenu.add_command(label="What does '☆' or 'X' mean", command=lambda:[helpMenuOnclicks("Symbol")])
filemenu.add_command(label="What does the number before an agent mean", command=lambda:[helpMenuOnclicks("Number")])
filemenu.add_command(label="Take me to the Instructions on GitHub", command=lambda:[helpMenuOnclicks("Link")])
menubar.add_cascade(label="Help", menu=filemenu)

#SELECT MAPS ##################################################
def selectMap(mapz, button): 
  map.clear()
  map.append(mapz)
  recommended.clear()
  label3.destroy()
  buttonSuggest['state'] = 'normal'
  buttonRecomend['state'] = 'normal'
  for mapx in maps:
    eval(f'button{mapx}')['state'] = 'normal'
  button['state'] = 'disabled'
#ASCENT
buttonAscent = tk.Button(height = 1, width = 8, text='Ascent', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Ascent", buttonAscent)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(60, 80, window=buttonAscent)
#BIND
buttonBind = tk.Button(height = 1, width = 8, text='Bind', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Bind", buttonBind)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(130, 80, window=buttonBind)
#BREEZE
buttonBreeze = tk.Button(height = 1, width = 8, text='Breeze', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Breeze", buttonBreeze)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(200, 80, window=buttonBreeze)
#FRACTURE
buttonFracture = tk.Button(height = 1, width = 8, text='Fracture', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Fracture", buttonFracture)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(270, 80, window=buttonFracture)
#HAVEN
buttonHaven = tk.Button(height = 1, width = 8, text='Haven', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Haven", buttonHaven)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(340, 80, window=buttonHaven)
#ICEBOX
buttonIcebox = tk.Button(height = 1, width = 8, text='Icebox', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Icebox", buttonIcebox)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(60, 110, window=buttonIcebox)
#SPLIT
buttonSplit = tk.Button(height = 1, width = 8, text='Split', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Split", buttonSplit)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(130, 110, window=buttonSplit)
#PEARL
buttonPearl = tk.Button(height = 1, width = 8, text='Pearl', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Pearl", buttonPearl)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(200, 110, window=buttonPearl)
# #HELL                                                               ++++++++++++++++++
# buttonHell = tk.Button(height = 1, width = 8, text='Hell', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Hell", buttonHell)], bg='#292929', fg='white', activebackground="#e04252")
# canvas1.create_window(270, 110, window=buttonHell)

#SELECT AGENTS ############################################
def appendAgent(name,button,five):  
  buttonRecomend['state'] = 'normal'
  buttonSuggest['state'] = 'normal'
  label3.destroy()
  if name in agents:
    agents.remove(name)
    nameLower = name[0].lower() + name[1:]
    button.config(bg='white', height = 21, width = 63, image = eval(f'{nameLower}Photo'.replace(r'/','')))
    buttons.remove(button)
  elif len(agents) < 4 or five == 1:
    button.config(height = 1, width = 7, image = '', bg='#e04252') #formats the clicked button
    agents.append(name) #appends the clicked agent
      
  delLabel()
  global label1
  label1 = tk.Label(root, width = 55, text= agents, bg='#0f1923', fg='white')
  canvas1.create_window(200, 300, window=label1)
  buttons.append(button) 
#ASTRA
astraPhoto = PhotoImage(file = "icons/Astra_icon.png")
buttonAstra = tk.Button(height = 21, width = 63, text='Astra', command=lambda:[appendAgent("Astra", buttonAstra, 0)], image = astraPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(60, 180, window=buttonAstra)
#BREACH2
breachPhoto = PhotoImage(file = "icons/Breach_icon.png")
buttonBreach = tk.Button(height = 21, width = 63, text='Breach', command=lambda:[appendAgent("Breach", buttonBreach, 0)], image = breachPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(130, 180, window=buttonBreach)
#BRIM3
brimstonePhoto = PhotoImage(file = "icons/Brimstone_icon.png")
buttonBrimstone = tk.Button(height = 21, width = 63, text='Brimstone', command=lambda:[appendAgent("Brimstone", buttonBrimstone, 0)], image = brimstonePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(200, 180, window=buttonBrimstone)
#CHAMBER4
chamberPhoto = PhotoImage(file = "icons/Chamber_icon.png")
buttonChamber = tk.Button(height = 21, width = 63, text='Chamber', command=lambda:[appendAgent("Chamber", buttonChamber, 0)], image = chamberPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(270, 180, window=buttonChamber)
#CYPHER5
cypherPhoto = PhotoImage(file = "icons/Cypher_icon.png")
buttonCypher = tk.Button(height = 21, width = 63, text='Cypher', command=lambda:[appendAgent("Cypher", buttonCypher, 0)], image = cypherPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(340, 180, window=buttonCypher)
#JETT6
jettPhoto = PhotoImage(file = "icons/Jett_icon.png")
buttonJett = tk.Button(height = 21, width = 63, text='Jett', command=lambda:[appendAgent("Jett", buttonJett, 0)], image = jettPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(60, 210, window=buttonJett)
#KO7
kAYOPhoto = PhotoImage(file = "icons/KAYO_icon.png")
buttonKAYO = tk.Button(height = 21, width = 63, text='KAY/O', command=lambda:[appendAgent("KAY/O", buttonKAYO, 0)], image = kAYOPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(130, 210, window=buttonKAYO)
#KJ8
killjoyPhoto = PhotoImage(file = "icons/Killjoy_icon.png")
buttonKilljoy = tk.Button(height = 21, width = 63, text='Killjoy', command=lambda:[appendAgent("Killjoy", buttonKilljoy, 0)], image = killjoyPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(200, 210, window=buttonKilljoy)
#NEON9
neonPhoto = PhotoImage(file = "icons/Killjoy1.png")
buttonNeon = tk.Button(height = 21, width = 63, text='Neon', command=lambda:[appendAgent("Neon", buttonNeon, 0)], image = neonPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(270, 210, window=buttonNeon)
#OMEN10
omenPhoto = PhotoImage(file = "icons/Omen_icon.png")
buttonOmen = tk.Button(height = 21, width = 63, text='Omen', command=lambda:[appendAgent("Omen", buttonOmen, 0)], image = omenPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(340, 210, window=buttonOmen)
#PHOENIX11
phoenixPhoto = PhotoImage(file = "icons/Phoenix_icon.png")
buttonPhoenix = tk.Button(height = 21, width = 63, text='Phoenix', command=lambda:[appendAgent("Phoenix", buttonPhoenix, 0)], image = phoenixPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(60, 240, window=buttonPhoenix)
#RAZE12
razePhoto = PhotoImage(file = "icons/Raze_icon.png")
buttonRaze = tk.Button(height = 21, width = 63, text='Raze', command=lambda:[appendAgent("Raze", buttonRaze, 0)], image = razePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(130, 240, window=buttonRaze)
#REYNA13
reynaPhoto = PhotoImage(file = "icons/Reyna_icon.png")
buttonReyna = tk.Button(height = 21, width = 63, text='Reyna', command=lambda:[appendAgent("Reyna", buttonReyna, 0)], image = reynaPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(200, 240, window=buttonReyna)
#SAGE14
sagePhoto = PhotoImage(file = "icons/Sage_icon.png")
buttonSage = tk.Button(height = 21, width = 63, text='Sage', command=lambda:[appendAgent("Sage", buttonSage, 0)], image = sagePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(270, 240, window=buttonSage)
#SKYE15
skyePhoto = PhotoImage(file = "icons/Skye_icon.png")
buttonSkye = tk.Button(height = 21, width = 63, text='Skye', command=lambda:[appendAgent("Skye", buttonSkye, 0)], image = skyePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(340, 240, window=buttonSkye)
#SOVA16
sovaPhoto = PhotoImage(file = "icons/Sova_icon.png")
buttonSova = tk.Button(height = 21, width = 63, text='Sova', command=lambda:[appendAgent("Sova", buttonSova, 0)], image = sovaPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(60, 270, window=buttonSova)
#VIPER17
viperPhoto = PhotoImage(file = "icons/Viper_icon.png")
buttonViper = tk.Button(height = 21, width = 63, text='Viper', command=lambda:[appendAgent("Viper", buttonViper, 0)], image = viperPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(130, 270, window=buttonViper)
#YORU18
yoruPhoto = PhotoImage(file = "icons/Yoru_icon.png")
buttonYoru = tk.Button(height = 21, width = 63, text='Yoru', command=lambda:[appendAgent("Yoru", buttonYoru, 0)], image = yoruPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(200, 270, window=buttonYoru)
#FADE19
fadePhoto = PhotoImage(file = "icons/Fade_icon.png")
buttonFade = tk.Button(height = 21, width = 63, text='Fade', command=lambda:[appendAgent("Fade", buttonFade, 0)], image = fadePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(270, 270, window=buttonFade)
#HARBOR20
harborPhoto = PhotoImage(file = "icons/Harbor_icon.png")
buttonHarbor = tk.Button(height = 21, width = 63, text='Harbor', command=lambda:[appendAgent("Harbor", buttonHarbor, 0)], image = harborPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(340, 270, window=buttonHarbor)
# #MAX20                                                              ++++++++++++++++++
# maxPhoto = PhotoImage(file = "icons/Max_icon.png")
# buttonMax = tk.Button(height = 21, width = 63, text='Max', command=lambda:[appendAgent("Max", buttonMax, 0)], image = maxPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
# canvas1.create_window(340, 270, window=buttonMax)

#SELECT ACTIONS ####################################################
#DELETE LABEL
def delLabel(): 
  label1.destroy()

#CLEARS
def clear():  
  agents.clear() #clears agents selected array
  recommended.clear() #clears agents recommended array
  label1.destroy()
  label3.destroy()

  #for loop each agent button selected and reset it
  for button in buttons:
    agentx = button['text']
    agentx = agentx[0].lower() + agentx[1:]
    button.config(bg='white', height = 21, width = 63, image = eval(f'{agentx}Photo'.replace(r'/','')))
  buttons.clear() #clears agents button array

  buttonRecomend['state'] = 'normal'
  buttonSuggest['state'] = 'normal'
clearPhoto = PhotoImage(file = "icons/clear.png")
buttonClear = tk.Button(height = 22, width = 63, text='Clear', command=clear, image = clearPhoto, bg='#0f1923', borderwidth=0, activebackground="#0f1923")
canvas1.create_window(130, 325, window=buttonClear)

#RECOMMEND BASED ON PRO COMPS ######################################
def recommend():
  recommended.clear()
  topAgentsPrint = []
  mapString = map[0]
  mapString = mapString[0].lower() + mapString[1] + mapString[2]
  #MAP DETECTED AND 4 AGENTS
  if len(agents) == 4 and map[0] != 'noMap':
    for comps in eval(mapString) :
      if all(x in comps for x in agents) == 1:
        for element in comps:
          if element not in agents:
            recommended.append(element) 
    #ordering by pick
    if recommended:
      topAgentsPrint = orderwDic(recommended,mapString)
      topAgentsPrint.insert(0,'☆:')
  #NOMAP      
  elif map[0] == 'noMap' :
    topAgentsPrint.append('Select_a_Map')
  #NO4AGENTS     
  elif len(agents) < 4 :
    topAgentsPrint.append('Select_4_Agents')
  #NOCLUE
  if not topAgentsPrint and len(agents) != 5:
    topAgentsPrint.append('Uncertain')
    topAgentsPrint = make(topAgentsPrint,mapString)

  buttonRecomend['state'] = 'disabled'
  buttonSuggest['state'] = 'disabled'
  global label3
  label3 = tk.Label(root, width = 43, text= topAgentsPrint, bg='#0f1923', fg='white')
  label3.config(font=('helvetica', 11))
  canvas1.create_window(200, 370, window=label3)
fillPhoto = PhotoImage(file = "icons/ill.png")
buttonRecomend = tk.Button(height = 22, width = 63, text='Fill', command=recommend, image = fillPhoto, bg='#0f1923', borderwidth=0, activebackground="#0f1923")
canvas1.create_window(200, 325, window=buttonRecomend)

#SUGGEST FULL COMP #################################################
def suggest():  
  mapString = map[0]
  mapString = mapString[0].lower() + mapString[1] + mapString[2]
  delLabel()
  label3.destroy()
  global label1
  comp = []
  #NOMAP      
  if map[0] == 'noMap' :
    clear()
    label1 = tk.Label(root, width = 55, text= 'Select_a_Map', bg='#0f1923', fg='white')
  elif len(agents) == 1:
    compsWAgent = []
    for compx in eval(mapString):
      if agents[0] in compx and len(compsWAgent) <= 9:
        compsWAgent.append(compx)
      elif len(compsWAgent) == 10:
        break
    clear()
    if compsWAgent:
      comp = compsWAgent[random.randint(0,len(compsWAgent)-1)]
    else:
      label1 = tk.Label(root, width = 55, text= f'Not_Found', bg='#0f1923', fg='white')
  else:
    clear()
    comp = eval(mapString)[random.randint(0,9)]
  
  for agent in comp:
    appendAgent(agent, eval(f'button{agent}'.replace(r'/','')), 1)

  canvas1.create_window(200, 300, window=label1)
  buttonRecomend['state'] = 'disabled'
  buttonSuggest['state'] = 'disabled'
fullPhoto = PhotoImage(file = "icons/ill2.png")
buttonSuggest = tk.Button(height = 22, width = 63, text='FullSuggest', command=suggest, image = fullPhoto, bg='#0f1923', borderwidth=0, activebackground="#0f1923")
canvas1.create_window(270, 325, window=buttonSuggest)

#NO COMP FOUND, RECOMMEND SOMETHING
def make(xprint,mapString): 
  # controller, initiator, sentinel, duelist
  roles = [0,0,0,0]
  typesR = [controllerS, initiatorS, sentinelS, duelistS]
  for agentx in agents:
    for x,typex in enumerate(typesR):
      if agentx in typex:
        roles[x] = 1
        break
  xprint.clear()
  xprint.append("X:")
  if sum(roles) != 3:
    xprint = xprint + secondMake(mapString)
  else:
    match roles:
      case [0,1,1,1]:
        xprint.insert(0, "Controller")
        xprint = xprint + orderwDic(typesR[0],mapString)
      case [1,0,1,1]:
        xprint.insert(0, "Initiator")
        xprint = xprint + orderwDic(typesR[1],mapString)
      case [1,1,0,1]:
        xprint.insert(0, "Sentinel")
        xprint = xprint + orderwDic(typesR[2],mapString)
      case [1,1,1,0]:
        xprint.insert(0, "Duelist")
        xprint = xprint + orderwDic(typesR[3],mapString)
  return xprint

#MAKE() METHOD FAILED, TRY THIS
def secondMake(mapString):
  roleToAgent = []
  agentsType = agentType(agents)
  for compx in eval(mapString):
    typeCompx = agentType(compx)
    if set(agentsType) == set(['C', 'I', 'S', 'D']):
      diff = list((Counter(typeCompx) - Counter(agentsType)).elements())
      for x,typex in enumerate(typeCompx):
        if typex == diff[0] and compx[x] not in agents and compx[x] not in roleToAgent:
          roleToAgent.append(compx[x])
  if roleToAgent: return orderwDic(roleToAgent, mapString)
  else: return ['Not_Found']

#GETS SELECTED AGENTS AGENT TYPE
def agentType(agentList):
  typesR = [controllerS, initiatorS, sentinelS, duelistS]
  receivedTypes = []
  for agentx in agentList:
    for x,typex in enumerate(typesR):
      if agentx in typex:
        match x:
          case 0:
            receivedTypes.append('C')
          case 1:
            receivedTypes.append('I')
          case 2:
            receivedTypes.append('S')
          case 3:
            receivedTypes.append('D')
        break
  return receivedTypes

#ORDER AGENTS BY TIMES PICKED     
def orderwDic(list, mapString):
  topAgentsPrint = []
  topAgents = [list[0]]
  for agentx in list:
    for x,top in enumerate(topAgents):
      if agentx not in topAgents :
        if dict[f'{mapString}{agentx}'] > dict[f'{mapString}{top}'] :
          topAgents.insert(x,agentx)
    if agentx not in topAgents :
      topAgents.append(agentx)
  for x,agentx in enumerate(topAgents):
    if x < 5:
      topAgentsPrint.append(str(dict[f'{mapString}{topAgents[x]}'])+'.'+topAgents[x])
    else:
      break
  return topAgentsPrint

#CHECKS IF THERES AN UPDATE
def updateCheck():
  updateWindow.withdraw()
  locallastedit = os.path.getmtime('./comps')
  locallastedit = datetime.fromtimestamp(locallastedit).strftime('%Y-%m-%d')
  locallastedit = locallastedit.split('-')
  locallastedit = int(locallastedit[0]),int(locallastedit[1]),int(locallastedit[2])
  html_text = requests.get('https://valorantfilleragent.jimdofree.com/').text
  soup = BeautifulSoup(html_text, 'lxml')
  try:
    lastedit = soup.find('div', id = 'fecha').text
    lastedit = lastedit.split('-')
    lastedit = int(lastedit[0]),int(lastedit[1]),int(lastedit[2])

  except:
    print('Repo did not load...')
    lastedit = locallastedit

  if (lastedit[0]+lastedit[1] > locallastedit[0]+locallastedit[1]) or ((lastedit[0]+lastedit[1] == locallastedit[0]+locallastedit[1]) and (lastedit[2] > locallastedit[2])):
    x = root.winfo_rootx() - 8
    y = root.winfo_rooty() - 35
    updateWindow.resizable(False, False)
    updateWindow.transient(root)
    updateWindow.iconbitmap("icons/valorant.ico")
    updateWindow.geometry(f'400x80+{x}+{y}')
    updateWindow.deiconify()

#MAIN CODE ##################################################
if __name__ == '__main__':
  menuButtons = [fillWindow, fullWindow, symbolWindow, numberWindow] #help menu windows
  buttons = [] #agent buttons
  maps = [] #maps in Valorant
  agents = [] #agents selected
  map = [] #map selected
  map.append('noMap') #default, map not selected
  recommended = [] #results
  dict = {} #dictionary for agent pick rate per map

  helpMenuOnclicks('')
  updateCheck()

  #AGENTS
  controllerS = ['Astra','Brimstone','Omen','Viper','Harbor']
  initiatorS = ['Breach','KAY/O','Skye','Sova','Fade']
  sentinelS = ['Chamber','Cypher','Killjoy','Sage']
  duelistS = ['Jett','Neon','Phoenix','Raze','Reyna','Yoru']
  # duelistS = ['Jett','Neon','Phoenix','Raze','Reyna','Yoru','NewAgent']             ++++++++++++++++++

  #COMPS
  asc = []
  bin = []
  bre = []
  fra = []
  hav = []
  ice = []
  spl = []
  pea = []
  # newMap = []                                               ++++++++++++++++++
  comps = [asc,bin,bre,fra,hav,ice,pea,spl]
  # comps = [asc,bin,bre,fra,hav,newMap,ice,spl]              ++++++++++++++++++

  #READ COMP FILES AND FILL COMP ARRAYS
  fileArray = []
  for file in listdir('./comps/'):
    maps.append(str(file).replace('.csv','')) # add.csv for new map to dir             ++++++++++++++++++
    fileArray.append(file)
  for x, filex in enumerate(fileArray):
    try:
      file = open(f'./comps/{filex}')
      csvreader = csv.reader(file)
      next(csvreader)
      for row in csvreader:
        comps[x].append(row)
    finally:
      file.close()

  #MAKE DIC FOR AGENT WEIGHT
  for mapx in maps: #iterates every map
    stringx = mapx[0].lower() + mapx[1] + mapx[2]
    for agentx in (controllerS + initiatorS + sentinelS + duelistS): #iterates every agent
      weight = 0
      for compx in eval(stringx): #iterates every comp
        if agentx in compx:
          weight += 1
      dict[f'{stringx}{agentx}'] = weight #adds to dictionary times agent repeats per map
root.config(menu=menubar)
root.mainloop()