import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import random
import csv
from os import listdir, path

root= tk.Tk()
root.title('FillerAgent v1.02 by classman')
root.geometry("400x400")
root.resizable(False, False)
root.iconbitmap("icons/valorant.ico")

canvas1 = tk.Canvas(root, width = 400, height = 400, bg='#0f1923')
bgPhoto = PhotoImage(file = "icons/Bg.png")
canvas1.create_image(10, 10, image = bgPhoto, anchor = NW)
canvas1.pack()

global label1
label1 = tk.Label(root, text='')

global label3
label3 = tk.Label(root, text='')

label6 = tk.Label(root, text='Filler Agent v1.02', bg='#0f1923')
label6.config(font=('helvetica', 14, 'bold'), fg='white')
canvas1.create_window(200, 30, window=label6)

label4 = tk.Label(root, text='(MAY2022 4.08)', bg='#0f1923')
label4.config(font=('helvetica', 10), fg='white')
canvas1.create_window(200, 52, window=label4)

label2 = tk.Label(root, text='Select 4 picked agents:', bg='#0f1923')
label2.config(font=('helvetica', 10, 'bold'), fg='white')
canvas1.create_window(200, 150, window=label2)

label5 = tk.Label(root, text='Possible filler agents:', bg='#0f1923')
label5.config(font=('helvetica', 10, 'bold'), fg='white')
canvas1.create_window(200, 350, window=label5)

#SELECT MAPS ##################################################
def selectMap (mapz, button): 
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
# #HELL                                                               ++++++++++++++++++
# buttonHell = tk.Button(height = 1, width = 8, text='Hell', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Hell", buttonHell)], bg='#292929', fg='white', activebackground="#e04252")
# canvas1.create_window(200, 110, window=buttonHell)

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
# #MAX20                                                              ++++++++++++++++++
# maxPhoto = PhotoImage(file = "icons/Max_icon.png")
# buttonMax = tk.Button(height = 21, width = 63, text='Max', command=lambda:[appendAgent("Max", buttonMax, 0)], image = maxPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
# canvas1.create_window(340, 270, window=buttonMax)

#SELECT ACTIONS ####################################################
#DELETE LABEL
def delLabel (): 
  label1.destroy()

#CLEARS
def clear ():  
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
def recommend ():
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
      topAgents = [recommended[0]]
      for agentx in recommended:
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
  #NOMAP      
  elif map[0] == 'noMap' :
    topAgentsPrint.append('Select_a_Map')
  #NO4AGENTS     
  elif len(agents) < 4 :
    topAgentsPrint.append('Select_4_Agents')
  #NOCLUE
  if not topAgentsPrint and len(agents) != 5:
    topAgentsPrint.append('Uncertain')
    topAgentsPrint = make(topAgentsPrint)

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
def suggest ():  
    delLabel()
    label3.destroy()
    clear()
    global label1
    comp = []
    #NOMAP      
    if map[0] == 'noMap' :
      label1 = tk.Label(root, width = 55, text= 'Select_a_Map', bg='#0f1923', fg='white')
    else:
      mapString = map[0]
      mapString = mapString[0].lower() + mapString[1] + mapString[2]
      comp = eval(mapString)[random.randint(0,9)]
    for agent in comp:
        appendAgent(agent, eval(f'button{agent}'.replace(r'/','')), 1)

    canvas1.create_window(200, 300, window=label1)
    buttonRecomend['state'] = 'disabled'
    buttonSuggest['state'] = 'disabled'
fullPhoto = PhotoImage(file = "icons/ill2.png")
buttonSuggest = tk.Button(height = 22, width = 63, text='FullSuggest', command=suggest, image = fullPhoto, bg='#0f1923', borderwidth=0, activebackground="#0f1923")
canvas1.create_window(270, 325, window=buttonSuggest)

def make (xprint): 
  # controller, initiator, sentinel, duelist
  roles = [0,0,0,0]
  typesR = [controllerS, initiatorS, sentinelS, duelistS]
  for agentx in agents:
    for x,typex in enumerate(typesR):
      if agentx in typex:
        roles[x] = 1
        break
  if sum(roles) != 3:
    return xprint
  xprint.clear()
  xprint.append("X:")
  match roles:
    case [0,1,1,1]:
      xprint.append("Controller")
    case [1,0,1,1]:
      xprint.append("Initiator")
    case [1,1,0,1]:
      xprint.append("Sentinel")
    case [1,1,1,0]:
      xprint.append("Duelist")
  return xprint
      
#MAIN OF THE CODE ##################################################
if __name__ == '__main__':
  buttons = [] #agent buttons
  maps = [] #maps in Valorant
  agents = [] #agents selected
  map = [] #map selected
  map.append('noMap') #default map not selected
  recommended = [] #results
  dict = {} #dictionary for agent pick rate per map

  #AGENTS
  controllerS = ['Astra','Brimstone','Omen','Viper']
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
  # newMap = []                                               ++++++++++++++++++
  comps = [asc,bin,bre,fra,hav,ice,spl]
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
root.mainloop()