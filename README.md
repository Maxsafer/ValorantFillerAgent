
# Valorant Filler Agent
## Authors
- [@Maxsafer](https://www.github.com/Maxsafer) aka classman
####
Software for Valorant Compositions based on Pro Matches.
####
![Home](https://drive.google.com/uc?export=view&id=1RFcM5UE1G91RD5yq3LszxtoetzgH2tVQ)
####
Features:
####
Fills a 4 agent composition with the 5th.
  * Based on pro composition = ☆:
  * Based on what role is missing = Role X:
  * Based on what other compositions with the same structure chose = X:
  * Gives a Full composition based on win rate.
  * Gives a Full composition that uses a specific selected agent.
  * Notifies when there is a new version.

## Screenshots

#### <u>Fill based on PRO matches</u>
Select 4 agents to get a compositions based on PRO matches.
#### 
![Fill](https://drive.google.com/uc?export=view&id=1rSWU__7_cYkMAym5M9YMoVhF2TLAQJsm)

#### <u>Full composition recommended</u>
Selects a top 10 PRO composition based on wins.
#### 
![Full](https://drive.google.com/uc?export=view&id=1RRGSX6IrvL0ZSI_g_Z7WF-tFIwPVdwxE)
#### 
Selects a top 10 PRO composition based on wins and one agent selected.
#### 
![Fullone](https://drive.google.com/uc?export=view&id=1-l_nvl9bATrKJ5ucq5_LATotimXHlBD6)
![Fullone](https://drive.google.com/uc?export=view&id=1K09Q3tT_O6lZWhkOZL69UcgXhyiVoEcM)

#### <u>Menu</u>
Help drop down menu.
#### 
![Help](https://drive.google.com/uc?export=view&id=1mRgD-o_a147JeFsL3xRrIaS918t8kzcP)

#### <u>Updates</u>
Notifies the user when ther is an update.
#### 
![Update](https://drive.google.com/uc?export=view&id=1VETc8iO3hi3jbTXXIptBJg99mRRVgjjb)

## Usage/Examples
#### [Fill] Get a recommendation on what agent should fill
* The fill button will fill a composition recommending the top 5 agents in descending order that could complete a composition.
* In order for it to work, a map and 4 agents must be selected.

#### [Full] Get a recommendation on what composition to play based on PRO matches
* The full button will select a top 10 composition played by professionals. These compositions are top 10 based on win rate.
* If only 1 agent is selected, it will pop a composition with that agent.
* Proceed to click on "Full" and a random PRO composition will be selected. (It can be modified by deselecting any agent and then clicking "Fill")

#### [Clear] Clears agents selected and output text
* Clears the selected agents or outputs displayed.

#### [Symbols] Used to represent the output type.
* ☆: Means the composition was filled based on a pro composition.
* X: Composition was filled based on an analysis. (This requires previous knowledge to understand what is a good recommendation)
* The number on the agent list represents the times an agent has been picked on the selected map.
* ***Note*** The number does not represent the times that an agent has been picked with that composition.

## Add/Import Compositions
#### The user can ADD MORE compositions or IMPORT other users compositions files
The path for the composition file is *"-appFolder-/comps/-map-.csv"* and can be edited from note pad.

#### To IMPORT
Simply replace the existing ".csv" file with the desired one.

#### To ADD MORE
Open the ".csv" file and add a row below the head with the desired composition and dont forget to save the file. (The app needs to be restarted after a file change to reload compositions)
* ***Note*** There should NOT be an empty line.
* ***Note*** Agents must be listed with commas and should be five, no more, no less, without exception. *E.g. Agent1,Agent2,Agent3,Agent4,Agent5*
* ***Note*** Every agent starts with a single capital letter followed by lower cases (with KAY/O being an exception). *E.g. Killjoy*
* ***Note*** Avoid repeating compositions in a single map, as it will repeat agents on the output. *To clarify: You can have the same composition for different maps.*

####
If you're planning on making your your own composition file, I recommend keeping it in alphabetical order so it's easier to spot repeated compositions.

## Download
####
Download as .ZIP from this GitHub.
#### 
![Download](https://drive.google.com/uc?export=view&id=1nnKBHeV-LQqsp8t1qFmaA21Vo9RaUL9H)

####
Drag and drop the folder from inside the .ZIP to anywhere on your system.
#### 
![Dragndrop](https://drive.google.com/uc?export=view&id=15pCq5iN1SBkkwHcI01WHiA9d75uy82dh)

####
Read KeepExeHere.txt
#### 
![Read](https://drive.google.com/uc?export=view&id=1X3oiUuACSAzfjMoHpachajZbebXLQdmc)

## Test it online!
https://valorantfilleragent.jimdofree.com/
(Download it for a better experience)

## Optimizations
There is still a lot I would like to implement.
