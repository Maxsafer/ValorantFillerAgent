
# Filler Agent

Software for Valorant Compositions based on Pro Matches.
#### 
![alt text](https://drive.google.com/uc?export=view&id=1XGlvZlr_SePxL6nGLPF0AS7pwFXDESJq)
## Authors

- [@Maxsafer](https://www.github.com/Maxsafer) aka classman


## Screenshots

#### Fill based on PRO matches
Compositions based on PRO matches will have a star "☆".
#### 
![alt text](https://drive.google.com/uc?export=view&id=1iJ-1goodKvAspdRqkqLKuMMoQrOkx9r-)

#### Fill based on AI
Compositions based on what the program thinks will have no star.
#### 
![alt text](https://drive.google.com/uc?export=view&id=1FqPb-s0_78REzS1f5lwWHtsX_XzCBbeJ)

#### Full composition recommended
Selects a PRO composition randomly.
#### 
![alt text](https://drive.google.com/uc?export=view&id=10C-YsN4wlFdOewfhMlEq_7AJ9h4iZQAD)
## Usage/Examples
#### [Fill] Get a recommendation on what agent should fill
* A map most first be selected.
* 4 agents most be selected. (The agents picked will appear as they are being selected below the agent grid)
* Proceed to click on "Fill" and a list with the possible filler agents will appear bellow.  (Compositions based on PRO matches **will have a star "☆"**, those filled by the AI wont)
#### [Full] Get a recommendation on what composition to play based on PRO matches
* A map most first be selected.
* Proceed to click on "Full" and a random PRO composition will appear bellow.
#### [Clear] Clear to reuse
* Clears the selected agents or outputs displayed.
## Add/Import Compositions

#### The user can ADD MORE compositions or IMPORT other users compositions file
The path for the composition file is *"<appFolder>/comps/comps.csv"* and can be edited from note pad.

#### To IMPORT
Simply replace the existing ".csv" file with the desired one.

#### To ADD MORE
Open the ".csv" file and add a row below the map name with the desired composition and dont forget to save the file. (The app needs to be restarted after a file change to reload compositions)
* ***Note*** There should NOT be an empty line.
* ***Note*** Agents most be listed with commas and should be five, no more, no less, without exception. *E.g. Agent1,Agent2,Agent3,Agent4,Agent5*
* ***Note*** KAY/O is written as "KO" (double capital letters).
* ***Note*** Every agent starts with a single capital letter followed by lower cases (with KAY/O being an exception). *E.g. Killjoy*
* ***Note*** Avoid repeating compositions in a single map. *To clarify: You can have the same composition for different maps.*
#### 
Example instructions can be seen below.
#### 
![alt text](https://drive.google.com/uc?export=view&id=1q01l_avyN9bR6N3tM601jO7vLCxItulS)
####
If you're planning on making your your own composition file, I recommend keeping it in alphabetical order so it's easier to spot repeated compositions.


## Optimizations

For future updates I am still wondering if I should do the following. I thought about making the AI purely based on the ".csv" file but that would also mean that the AI is as good as the file provided to it.

There is still a lot I would like to implement.
