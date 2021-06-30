## Rock paper and Scissors Game by Aditya Mirpagar

**This project uses Python3**

*This is a a Game of Rock Paper and Scissors, written in python and using tkinter for GUI.*
*In order to run this game please check prerequisites*


*To run the program simply use "$ pyhon3 rock.py"*


**prerequisites**

1. **tkinter**
* *tkinter is a python library which is used to make basic GUI applocations. It can be installed by typing "$ sudo apt install python3-tk" (for linux users)*

2. **PIL**
* *PIL is python imaging library, is used for importing images, or just in a way interact with images in the program. it can be installed by typing "$ pip install Pillow" (for linux user, "p is capital in Pillow")*

3. **PIP**
* *PIP is a package installer for python. It is used to install different python indexes or programs (like Pillow)*

**Description**
*This game uses 3 functions in which two of them are for "score updating" and "image updating" and other one is for checking the winner. check_winner() function uses an if-else loop, which checks the conditions of player's move and computer move, And take actions according to that.*

*This program uses 6 images of rock paper and scissors (including mirrored images) left hand side we have computer and right hand side we'll be palying. Both player and computer have a function written as update_choice(), which changes the images according to the text, in update_choice() computer_choice uses a randint() function, which selects the random number (range 0,2) from the array provided on 'Line 104' as choices. Player choices are chages whenever player selects any text*

*Scores for both computer and player are updated by player_update() and computer_update 'Line 62', it increments the text each time a move or button is clicked*

*finally this all is in the tkinter 's window.tk() {root.tk}, It provides the console window wich can be used to display everything. This window.tk() can be configured e.g., background colour, fonts, grids etc.*

## This project is created by Aditya Mirpagar (Roll No. 0510CS171004) on june 30 2021. 