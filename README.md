# League of Legends Wincon Calculator
[![Python 3.7.9](https://img.shields.io/badge/python-3.7.9-blue.svg)](https://www.python.org/downloads/release/python-374/) ![Version](https://img.shields.io/github/v/release/austinyen56/League-of-Legends-Wincon-Calculator?color=green&label=Release%20Version)


Wanna predict if you will win or not in your current game of league? This program will show ur wr and enable you to climb faster (hopefully)

## How to run this program
* You can  run the program using the .exe file presented in the releases, just simply download and double click
* You can also run the python file by ```python3 RitoWinconCalculator.py```
* The given input statements are pretty self explanatory. Please enter champion names all connected and without spaces. Eg: type "Kha' Zix" as "khazix", "Dr. Mundo" as "drmundo"
* (Starting version 2.x) If selected to generate the output to clipboard, `outfile.txt` will be generated containing the output copied to clipboard

## What is not considered in this program
Due to the wide variation of possibilities in the game,the following stats are not considered in this program:
* User stats such as current rank, overall WR, champion frequency
* General stats such as winrates from na.op.gg and Asia servers (unable to fetch data due to riot API no longer supports their servers)
* Elo related (smurf queue/ wintrading)
* Off- role/ Off- meta champions or troll matchups
* Summoner spells especially when not used in specific role (ex: JG without smite)
* Other gamemodes such as ARAM or URF
* Inting teamates/ enemies and mentality related occurances
* (Starting version 2.x) Auto mode only applies to draft and rank solo/duo. Other gamemodes are not fully supported due to no information on roles

If there are any errors or bugs, please post an issue and I will respond asap. Also, feel free to request any new features and I'll try my best to make it happen 😊