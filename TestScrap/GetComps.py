from queue import Empty
from bs4 import BeautifulSoup
import requests
import csv
import time

# _________________ Rib.gg CSV _________________
def readRibgg():
    file = ('ribgg.csv')
    try:
        f = open(file)
        csvreader = csv.reader(f)
        next(csvreader)
        for fileComp in csvreader:
            tempArr = [] 
            tempArr = (fileComp[1].replace(',','')).split()
            if int(fileComp[2]) >= 1: # comps con wins menor a 1 se ignoran (wins por default)
                addToFile(fileComp[0],tempArr)
            else:
                break
            tempArr.clear()
    finally:
        f.close()


# _________________ Sub-Page w/ Comps _________________
def subPage(link):
    print('======== NEW MATCH ========')
    print(link)
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    comp1 = []
    comp2 = []

    # Get maps played
    maps = soup.find_all('div', class_ = 'center-map')

    # Get all agents played per map
    quote1 = soup.find_all('div', class_ = 'stat-wrap overview-wrapper') # encuentra tablas
    for x in range(0,len(quote1)):
        quote2 = quote1[x].findChildren('div', recursive=False) # x es donde está la info de x mapa
        quote3 = quote2[1].findChildren('div', recursive=False) # 1 es donde está la info de comp 1 arriba
        quote3 = quote3[1].find_all('img')
        quote4 = quote2[2].findChildren('div', recursive=False) # 2 es donde está la info de comp 2 abajo
        quote4 = quote4[1].find_all('img')
        for z in range(0,len(quote3)):
            try:
                comp1.append(str(quote3[z].get('title')))
                comp2.append(str(quote4[z].get('title')))
            except:
                print('COMP WITH LESS THAN 4 AGENTS')
        if len(comp1) == 5 and len(comp2) == 5:
            addToFile(maps[x].text.replace('Selección',''),comp1)
            addToFile(maps[x].text.replace('Selección',''),comp2)
        comp1.clear()
        comp2.clear()

# _________________ Main page _________________
def mainPage():
    html_text = requests.get('https://www.thespike.gg/es/matches/results').text
    soup = BeautifulSoup(html_text, 'lxml')

    matches = soup.find_all("li", class_ = 'single-match main-colour-background')
    percentage = 0
    print(f'Number of matches to scan: {len(matches)}')
    for child in matches:
        link = "%s%s" % ('https://www.thespike.gg',child.a.get('href'))
        subPage(link)
        percentage += 1
        print(f'Match {percentage} of {len(matches)}')
        print(f'{round((percentage/len(matches))*100, 2)}% completed.')

# _________________ Read / Write file _________________
def addToFile(file, comp):
    file = ''.join(filter(str.isalnum, file))
    xfile = ('./comps/' + file + '.csv')

    f = open(xfile)
    f2 = open(xfile, 'a')
    flag = 0

    # Revisar si existe comp antes de agregar
    csvreader = csv.reader(f)
    for fileComp in csvreader:
        if (set(comp) == set(fileComp)) or len(comp) == 0:
            flag = 1
    if flag == 0:
        print(f'Added {comp} to {file}')
        write = csv.writer(f2)
        write.writerow(sorted(comp))        
    f2.close()
    f.close()

# _________________ Main _________________
if __name__ == '__main__':
    print('1. TheSpike Scrap')
    print('2. RibGG CSV')
    x = input()
    if x == '1':
        start = time.perf_counter()
        mainPage()
        end = time.perf_counter()
        print(f'Tiempo: {round((end-start)/60,4)} minutes')
    elif x == '2':
        readRibgg()