from queue import Empty
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
bgPhoto = PhotoImage(file = "icons\Bg.png")
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
    buttonASC['state'] = 'normal'
    buttonBND['state'] = 'normal'
    buttonBRE['state'] = 'normal'
    buttonFRA['state'] = 'normal'
    buttonHAV['state'] = 'normal'
    buttonICE['state'] = 'normal'
    buttonSPL['state'] = 'normal'
    button['state'] = 'disabled'
#ASCENT
buttonASC = tk.Button(height = 1, width = 8, text='Ascent', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Ascent", buttonASC)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(60, 80, window=buttonASC)
#BIND
buttonBND = tk.Button(height = 1, width = 8, text='Bind', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Bind", buttonBND)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(130, 80, window=buttonBND)
#BREEZE
buttonBRE = tk.Button(height = 1, width = 8, text='Breeze', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Breeze", buttonBRE)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(200, 80, window=buttonBRE)
#FRACTURE
buttonFRA = tk.Button(height = 1, width = 8, text='Fracture', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Fracture", buttonFRA)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(270, 80, window=buttonFRA)
#HAVEN
buttonHAV = tk.Button(height = 1, width = 8, text='Haven', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Haven", buttonHAV)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(340, 80, window=buttonHAV)
#ICEBOX
buttonICE = tk.Button(height = 1, width = 8, text='Icebox', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Icebox", buttonICE)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(60, 110, window=buttonICE)
#SPLIT
buttonSPL = tk.Button(height = 1, width = 8, text='Split', font=('helvetica', 9, 'bold'), command=lambda:[selectMap("Split", buttonSPL)], bg='#292929', fg='white', activebackground="#e04252")
canvas1.create_window(130, 110, window=buttonSPL)

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
astraPhoto = PhotoImage(file = "icons\Astra_icon.png")
buttonAstra = tk.Button(height = 21, width = 63, text='Astra', command=lambda:[appendAgent("Astra", buttonAstra, 0)], image = astraPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(60, 180, window=buttonAstra)
#BREACH2
breachPhoto = PhotoImage(file = "icons\Breach_icon.png")
buttonBreach = tk.Button(height = 21, width = 63, text='Breach', command=lambda:[appendAgent("Breach", buttonBreach, 0)], image = breachPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(130, 180, window=buttonBreach)
#BRIM3
brimstonePhoto = PhotoImage(file = "icons\Brimstone_icon.png")
buttonBrimstone = tk.Button(height = 21, width = 63, text='Brimstone', command=lambda:[appendAgent("Brimstone", buttonBrimstone, 0)], image = brimstonePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(200, 180, window=buttonBrimstone)
#CHAMBER4
chamberPhoto = PhotoImage(file = "icons\Chamber_icon.png")
buttonChamber = tk.Button(height = 21, width = 63, text='Chamber', command=lambda:[appendAgent("Chamber", buttonChamber, 0)], image = chamberPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(270, 180, window=buttonChamber)
#CYPHER5
cypherPhoto = PhotoImage(file = "icons\Cypher_icon.png")
buttonCypher = tk.Button(height = 21, width = 63, text='Cypher', command=lambda:[appendAgent("Cypher", buttonCypher, 0)], image = cypherPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(340, 180, window=buttonCypher)
#JETT6
jettPhoto = PhotoImage(file = "icons\Jett_icon.png")
buttonJett = tk.Button(height = 21, width = 63, text='Jett', command=lambda:[appendAgent("Jett", buttonJett, 0)], image = jettPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(60, 210, window=buttonJett)
#KO7
kAYOPhoto = PhotoImage(file = "icons\KAYO_icon.png")
buttonKAYO = tk.Button(height = 21, width = 63, text='KAY/O', command=lambda:[appendAgent("KAY/O", buttonKAYO, 0)], image = kAYOPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(130, 210, window=buttonKAYO)
#KJ8
killjoyPhoto = PhotoImage(file = "icons\Killjoy_icon.png")
buttonKilljoy = tk.Button(height = 21, width = 63, text='Killjoy', command=lambda:[appendAgent("Killjoy", buttonKilljoy, 0)], image = killjoyPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(200, 210, window=buttonKilljoy)
#NEON9
neonPhoto = PhotoImage(file = "icons\Killjoy1.png")
buttonNeon = tk.Button(height = 21, width = 63, text='Neon', command=lambda:[appendAgent("Neon", buttonNeon, 0)], image = neonPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(270, 210, window=buttonNeon)
#OMEN10
omenPhoto = PhotoImage(file = "icons\Omen_icon.png")
buttonOmen = tk.Button(height = 21, width = 63, text='Omen', command=lambda:[appendAgent("Omen", buttonOmen, 0)], image = omenPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(340, 210, window=buttonOmen)
#PHOENIX11
phoenixPhoto = PhotoImage(file = "icons\Phoenix_icon.png")
buttonPhoenix = tk.Button(height = 21, width = 63, text='Phoenix', command=lambda:[appendAgent("Phoenix", buttonPhoenix, 0)], image = phoenixPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(60, 240, window=buttonPhoenix)
#RAZE12
razePhoto = PhotoImage(file = "icons\Raze_icon.png")
buttonRaze = tk.Button(height = 21, width = 63, text='Raze', command=lambda:[appendAgent("Raze", buttonRaze, 0)], image = razePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(130, 240, window=buttonRaze)
#REYNA13
reynaPhoto = PhotoImage(file = "icons\Reyna_icon.png")
buttonReyna = tk.Button(height = 21, width = 63, text='Reyna', command=lambda:[appendAgent("Reyna", buttonReyna, 0)], image = reynaPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(200, 240, window=buttonReyna)
#SAGE14
sagePhoto = PhotoImage(file = "icons\Sage_icon.png")
buttonSage = tk.Button(height = 21, width = 63, text='Sage', command=lambda:[appendAgent("Sage", buttonSage, 0)], image = sagePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(270, 240, window=buttonSage)
#SKYE15
skyePhoto = PhotoImage(file = "icons\Skye_icon.png")
buttonSkye = tk.Button(height = 21, width = 63, text='Skye', command=lambda:[appendAgent("Skye", buttonSkye, 0)], image = skyePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(340, 240, window=buttonSkye)
#SOVA16
sovaPhoto = PhotoImage(file = "icons\Sova_icon.png")
buttonSova = tk.Button(height = 21, width = 63, text='Sova', command=lambda:[appendAgent("Sova", buttonSova, 0)], image = sovaPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(60, 270, window=buttonSova)
#VIPER17
viperPhoto = PhotoImage(file = "icons\Viper_icon.png")
buttonViper = tk.Button(height = 21, width = 63, text='Viper', command=lambda:[appendAgent("Viper", buttonViper, 0)], image = viperPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(130, 270, window=buttonViper)
#YORU18
yoruPhoto = PhotoImage(file = "icons\Yoru_icon.png")
buttonYoru = tk.Button(height = 21, width = 63, text='Yoru', command=lambda:[appendAgent("Yoru", buttonYoru, 0)], image = yoruPhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(200, 270, window=buttonYoru)
#FADE19
fadePhoto = PhotoImage(file = "icons\Fade_icon.png")
buttonFade = tk.Button(height = 21, width = 63, text='Fade', command=lambda:[appendAgent("Fade", buttonFade, 0)], image = fadePhoto, bg='white', borderwidth=0, activebackground="white",disabledforeground='black', font=('helvetica', 11, 'bold'),fg='black')
canvas1.create_window(270, 270, window=buttonFade)

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

    #for loop each agent button and reset it
    for button in buttons:
      button['state'] = 'normal'  
      string = button['text']
      string = string[0].lower() + string[1:]
      button.config(bg='white', height = 21, width = 63, image = eval(f'{string}Photo'.replace(r'/','')))
    buttons.clear() #clears agents button array

    buttonRecomend['state'] = 'normal'
    buttonSuggest['state'] = 'normal'
clearPhoto = PhotoImage(file = "icons\clear.png")
buttonClear = tk.Button(height = 22, width = 63, text='Clear', command=clear, image = clearPhoto, bg='#0f1923', borderwidth=0, activebackground="#0f1923")
canvas1.create_window(130, 325, window=buttonClear)

#RECOMMEND BASED ON PRO COMPS ######################################
def recommend ():
  recommended.clear()
  #ASCENT ASCENT ASCENT ASCENT ASCENT ASCENT ASCENT ASCENT 
  if len(agents) == 4 and map[0] == 'Ascent':
    for comps in asc :
      if all(x in comps for x in agents) == 1:
        for element in comps:
          if element not in agents:
            recommended.append(element) 
  #BIND BIND BIND BIND BIND BIND BIND BIND BIND BIND BIND 
  elif len(agents) == 4 and map[0] == 'Bind':
    for comps in bnd :
      if all(x in comps for x in agents) == 1:
        for element in comps:
          if element not in agents:
            recommended.append(element)   
  #BREEZE BREEZE BREEZE BREEZE BREEZE BREEZE BREEZE BREEZE 
  elif len(agents) == 4 and map[0] == 'Breeze':
    for comps in bre :
      if all(x in comps for x in agents) == 1:
        for element in comps:
          if element not in agents:
            recommended.append(element) 
  #FRACTURE FRACTURE FRACTURE FRACTURE FRACTURE FRACTURE FRACTURE  
  elif len(agents) == 4 and map[0] == 'Fracture':
    for comps in fra :
      if all(x in comps for x in agents) == 1:
        for element in comps:
          if element not in agents:
            recommended.append(element) 
  #HAVEN HAVEN HAVEN HAVEN HAVEN HAVEN HAVEN HAVEN HAVEN HAVEN HAVEN
  elif len(agents) == 4 and map[0] == 'Haven':
    for comps in hav :
      if all(x in comps for x in agents) == 1:
        for element in comps:
          if element not in agents:
            recommended.append(element) 
  #ICEBOX ICEBOX ICEBOX ICEBOX ICEBOX ICEBOX ICEBOX ICEBOX ICEBOX
  elif len(agents) == 4 and map[0] == 'Icebox':
    for comps in ice :
      if all(x in comps for x in agents) == 1:
        for element in comps:
          if element not in agents:
            recommended.append(element) 
  #SPLIT SPLIT SPLIT SPLIT SPLIT SPLIT SPLIT SPLIT SPLIT SPLIT
  elif len(agents) == 4 and map[0] == 'Split':
    for comps in spl :
      if all(x in comps for x in agents) == 1:
        for element in comps:
          if element not in agents:
            recommended.append(element) 
  #NOMAP      
  elif map[0] == 'noMap' :
    recommended.append('Select_a_Map')
  #NO4AGENTS     
  elif len(agents) < 4 :
    recommended.append('Select_4_Agents')
  #PRO
  if recommended and recommended[0] != 'Select_4_Agents' and recommended[0] != 'Select_a_Map' :
    recommended.insert(0,'☆:')
  #NOCLUE
  if not recommended and len(agents) != 5:
    recommended.append('Uncertain')
    #MAKE COMP
    make()

  buttonRecomend['state'] = 'disabled'
  buttonSuggest['state'] = 'disabled'
  global label3
  label3 = tk.Label(root, width = 43, text= recommended, bg='#0f1923', fg='white')
  label3.config(font=('helvetica', 12))
  canvas1.create_window(200, 370, window=label3)
fillPhoto = PhotoImage(file = "icons\ill.png")
buttonRecomend = tk.Button(height = 22, width = 63, text='Fill', command=recommend, image = fillPhoto, bg='#0f1923', borderwidth=0, activebackground="#0f1923")
canvas1.create_window(200, 325, window=buttonRecomend)

#SUGGEST FULL COMP #################################################
def suggest ():  
    delLabel()
    label3.destroy()
    clear()
    global label1
    comp = []
    if map[0] == 'Ascent' :
      comp = asc[random.randint(0,9)]
    elif map[0] == 'Bind' :
      comp = bnd[random.randint(0,9)]
    elif map[0] == 'Breeze' :
      comp = bre[random.randint(0,9)]
    elif map[0] == 'Fracture' :
      comp = fra[random.randint(0,9)]
    elif map[0] == 'Haven' :
      comp = hav[random.randint(0,9)]
    elif map[0] == 'Icebox' :
      comp = ice[random.randint(0,9)]
    elif map[0] == 'Split' :
      comp = spl[random.randint(0,9)]
    #NOMAP      
    elif map[0] == 'noMap' :
      label1 = tk.Label(root, width = 55, text= 'Select_a_Map', bg='#0f1923', fg='white')
    for agent in comp:
        appendAgent(agent, eval(f'button{agent}'.replace(r'/','')), 1)

    canvas1.create_window(200, 300, window=label1)
    buttonRecomend['state'] = 'disabled'
    buttonSuggest['state'] = 'disabled'
fullPhoto = PhotoImage(file = "icons\ill2.png")
buttonSuggest = tk.Button(height = 22, width = 63, text='FullSuggest', command=suggest, image = fullPhoto, bg='#0f1923', borderwidth=0, activebackground="#0f1923")
canvas1.create_window(270, 325, window=buttonSuggest)

#AI COMP FILLER ####################################################
def make ():
  #controllerS, initiatorS, sentinelS, duelistS
  compMake = [0,0,0,0,0]
  suma = 0
  counter = 0
  counter2 = 0
  if map[0] == 'Ascent' :
    for x in range(0,5):
      if x == 0 and any(x in controllerS for x in agents) :
        compMake[0] = 1
      elif x == 0 :
        suma += 1
      if x == 1 and ('Sova' in agents) :
        compMake[1] = 1
      elif x == 1 :
        suma += 1
      if x == 2 and ('Cypher' in agents or 'Killjoy' in agents or 'Sage' in agents) :
        compMake[2] = 1
      elif x == 2 :
        suma += 1
      if x == 3 and any(x in duelistS for x in agents) :
        for x in agents :
          if x in duelistS :
            counter += 1
        compMake[3] = 1
      elif x == 3 :
        suma += 1
      if x == 4 and (counter == 2 or 'KAY/O' in agents or 'Skye' in agents or 'Breach' in agents or 'Chamber' in agents) :
        compMake[4] = 1
      elif x == 4 :
        suma += 1
    if compMake.index(0) == 0 and suma == 1:
      recommended.clear()
      recommended.append('Brimstone')
      recommended.append('Omen')
    elif compMake.index(0) == 1 and suma == 1:
      recommended.clear()
      recommended.append('Sova')
    elif compMake.index(0) == 2 and suma == 1:
      recommended.clear()
      recommended.append('Killjoy')
      recommended.append('Cypher')
    elif compMake.index(0) == 3 and suma == 1:
      recommended.clear()
      recommended.append('Duelist')
    elif compMake.index(0) == 4 and suma == 1:
      recommended.clear()
      recommended.append('Skye')
      recommended.append('KAY/O')
      recommended.append('Chamber')
  elif map[0] == 'Bind' :
    #duelistsMake = []
    for x in range(0,5):
      if x == 0 and any(x in sentinelS for x in agents) :
        compMake[0] = 1
      elif x == 0 :
        suma += 1
      if x == 1 and ('Sova' in agents) :
        compMake[1] = 1
      elif x == 1 :
        suma += 1
      if x == 2 and any(x in controllerS for x in agents) :
        compMake[2] = 1
      elif x == 2 :
        suma += 1
      if x == 3 and any(x in duelistS for x in agents) :
        for x in agents :
          if x in duelistS :
            counter += 1
            #duelistsMake.append(x)
        compMake[3] = 1
      elif x == 3 :
        suma += 1
      if x == 4 and (counter == 2 or 'Skye' in agents or 'Breach' in agents) : #(len(duelistsMake) == 2)
        compMake[4] = 1
      elif x == 4 :
        suma += 1
    if compMake.index(0) == 0 and suma == 1:
      recommended.clear()
      recommended.append('Chamber')
      recommended.append('Killjoy')
    elif compMake.index(0) == 1 and suma == 1:
      recommended.clear()
      recommended.append('Sova')
    elif compMake.index(0) == 2 and suma == 1:
      recommended.clear()
      recommended.append('Brimstone')
      recommended.append('Omen')
    elif (compMake.index(0) == 3 or compMake.index(0) == 4) and suma == 1:
      recommended.clear()
      #for element in duelistS:
      #  if element not in duelistsMake :
      #    recommended.append(element)  
      recommended.append('Duelist')
      recommended.append('Breach')
      recommended.append('Skye')
  elif map[0] == 'Breeze' :
    for x in range(0,5):
      if x == 0 and any(x in controllerS for x in agents) :
        compMake[0] = 1
      elif x == 0 :
        suma += 1
      if x == 1 and ('Sova' in agents or 'Skye' in agents) :
        compMake[1] = 1
      elif x == 1 :
        suma += 1
      if x == 2 and ('Chamber' in agents or 'Cypher' in agents) :
        compMake[2] = 1
      elif x == 2 :
        suma += 1
      if x == 3 and any(x in duelistS for x in agents) :
        for x in agents :
          if x in duelistS :
            counter += 1
        compMake[3] = 1
      elif x == 3 :
        suma += 1
      if x == 4 and (counter == 2 or 'KAY/O' in agents or 'Skye' in agents) :
        compMake[4] = 1
      elif x == 4 :
        suma += 1
    if compMake.index(0) == 0 and suma == 1:
      recommended.clear()
      recommended.append('Viper')
    elif compMake.index(0) == 1 and suma == 1:
      recommended.clear()
      recommended.append('Sova')
    elif compMake.index(0) == 2 and suma == 1:
      recommended.clear()
      recommended.append('Chamber')
      recommended.append('Cypher')
    elif compMake.index(0) == 3 and suma == 1:
      recommended.clear()
      recommended.append('Jett')
    elif compMake.index(0) == 4 and suma == 1:
      recommended.clear()
      recommended.append('Duelist')
      recommended.append('KAY/O')
      recommended.append('Skye')
  elif map[0] == 'Fracture' :
    for x in range(0,5):
      if x == 0 and any(x in controllerS for x in agents) :
        compMake[0] = 1
      elif x == 0 :
        suma += 1
      if x == 1 and any(x in initiatorS for x in agents) :
        compMake[1] = 1
      elif x == 1 :
        suma += 1
      if x == 2 and any(x in duelistS for x in agents) :
        for x in agents :
          if x in duelistS :
            counter += 1
        compMake[2] = 1
      elif x == 2 :
        suma += 1
      if x == 3 and any(x in sentinelS for x in agents) :
        for x in agents :
          if x in sentinelS :
            counter2 += 1
        compMake[3] = 1
      elif x == 3 :
        suma += 1
      if x == 4 and (counter == 2 or counter2 == 2) :
        compMake[4] = 1
      elif x == 4 :
        suma += 1
    if compMake.index(0) == 0 and suma == 1:
      recommended.clear()
      recommended.append('Astra')
      recommended.append('Brimstone')
    elif compMake.index(0) == 1 and suma == 1:
      recommended.clear()
      recommended.append('Breach')
    elif compMake.index(0) == 2 and suma == 1:
      recommended.clear()
      recommended.append('Jett')
      recommended.append('Raze')
    elif compMake.index(0) == 3 and suma == 1:
      recommended.clear()
      recommended.append('Chamber')
    elif compMake.index(0) == 4 and suma == 1:
      for x in agents : 
        if x in sentinelS and x == 'Chamber':
          recommended.clear()
          recommended.append('Sentinel')
        elif x in sentinelS :
          recommended.clear()
          recommended.append('Chamber')
  elif map[0] == 'Haven' : 
    for x in range(0,5):
      if x == 0 and ('Astra' in agents or'Brimstone' in agents or 'Omen' in agents)  :
        compMake[0] = 1
      elif x == 0 :
        suma += 1
      if x == 1 and any(x in sentinelS for x in agents) :
        compMake[1] = 1
      elif x == 1 :
        suma += 1
      if x == 2 and any(x in duelistS for x in agents) :
        for x in agents :
          if x in duelistS :
            counter += 1
        compMake[2] = 1
      elif x == 2 :
        suma += 1
      if x == 3 and ('Skye' in agents or 'KAY/O' in agents) or (counter == 2) :
        compMake[3] = 1
      elif x == 3 :
        suma += 1
      if x == 4 and ('Breach' in agents or 'Sova' in agents) :
        compMake[4] = 1
      elif x == 4 :
        suma += 1
    if compMake.index(0) == 0 and suma == 1:
      recommended.clear()
      recommended.append('Brimstone')
      recommended.append('Omen')
    elif compMake.index(0) == 1 and suma == 1:
      recommended.clear()
      recommended.append('Chamber')
      recommended.append('Cypher')
      recommended.append('Killjoy')
    elif compMake.index(0) == 2 and suma == 1:
      recommended.clear()
      recommended.append('Jett')
    elif compMake.index(0) == 3 and suma == 1:
      recommended.clear()
      recommended.append('Skye')
      recommended.append('KAY/O')
    elif compMake.index(0) == 4 and suma == 1:
      recommended.clear()
      recommended.append('Sova')
  elif map[0] == 'Icebox' :
    for x in range(0,5):
      if x == 0 and any(x in sentinelS for x in agents) :
        compMake[0] = 1
      elif x == 0 :
        suma += 1
      if x == 1 and any(x in controllerS for x in agents) :
        compMake[1] = 1
      elif x == 1 :
        suma += 1
      if x == 2 and ('Sova' in agents) :
        compMake[2] = 1
      elif x == 2 :
        suma += 1
      if x == 3 and any(x in duelistS for x in agents) :
        for x in agents :
          if x in duelistS :
            counter += 1
        compMake[3] = 1
      elif x == 3 :
        suma += 1
      if x == 4 and ('Skye' in agents or 'KAY/O' in agents) or (counter == 2) :
        compMake[4] = 1
      elif x == 4 :
        suma += 1
    if compMake.index(0) == 0 and suma == 1:
      recommended.clear()
      recommended.append('Chamber')
    elif compMake.index(0) == 1 and suma == 1:
      recommended.clear()
      recommended.append('Viper')
    elif compMake.index(0) == 2 and suma == 1:
      recommended.clear()
      recommended.append('Sova')
    elif compMake.index(0) == 3 and suma == 1:
      recommended.clear()
      recommended.append('Jett')
    elif compMake.index(0) == 4 and suma == 1:
      recommended.clear()
      recommended.append('Skye')
      recommended.append('KAY/O')
  elif map[0] == 'Split' :
    for x in range(0,5):
      if x == 0 and any(x in controllerS for x in agents) :
        compMake[0] = 1
      elif x == 0 :
        suma += 1
      if x == 1 and any(x in duelistS for x in agents) :
        for x in agents :
          if x in duelistS :
            counter += 1
        compMake[1] = 1
      elif x == 1 :
        suma += 1
      if x == 2 and any(x in initiatorS for x in agents) :
        compMake[2] = 1
      elif x == 2 :
        suma += 1
      if x == 3 and ('Cypher' in agents or'Killjoy' in agents or counter == 2) :
        compMake[3] = 1
      elif x == 3 :
        suma += 1
      if x == 4 and ('Sage' in agents) :
        compMake[4] = 1
      elif x == 4 :
        suma += 1
    if compMake.index(0) == 0 and suma == 1:
      recommended.clear()
      recommended.append('Astra')
      recommended.append('Omen')
    elif compMake.index(0) == 1 and suma == 1:
      recommended.clear()
      recommended.append('Raze')
    elif compMake.index(0) == 2 and suma == 1:
      recommended.clear()
      recommended.append('Breach')
      recommended.append('Skye')
    elif compMake.index(0) == 3 and suma == 1:
      recommended.clear()
      recommended.append('Cypher')
      recommended.append('Killjoy')
    elif compMake.index(0) == 4 and suma == 1:
      recommended.clear()
      recommended.append('Sage')

#MAIN OF THE CODE ##################################################
if __name__ == '__main__':
  buttons = [] #agent buttons
  agents = [] #agents selected
  map = [] #map selected
  map.append('noMap') #default map not selected
  recommended = [] #results

  #AGENT ROLES
  controllerS = ['Astra','Brimstone','Omen','Viper']
  initiatorS = ['Breach','KAY/O','Skye','Sova','Fade']
  sentinelS = ['Chamber','Cypher','Killjoy','Sage']
  duelistS = ['Jett','Neon','Phoenix','Raze','Reyna','Yoru']

  #COMPS
  asc = []
  bnd = []
  bre = []
  fra = []
  hav = []
  ice = []
  spl = []
  comps = [asc,bnd,bre,fra,hav,ice,spl]

  #READ COMP FILES AND FILL COMP ARRAYS
  fileArray = []
  for file in listdir('./comps/'):
    fileArray.append(file)
  for x in range(0,len(listdir('./comps/'))):
    file = open(f'./comps/{fileArray[x]}')
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
      comps[x].append(row)
    file.close()

root.mainloop()