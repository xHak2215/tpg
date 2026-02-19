TPG - terminal pseudo graphics
a small library for creating graphical interfaces (TUI)

The library's functionality includes:

· Lists
· Simplified color handling (ANSI)
· Console cursor control
· Choice menus (yes/no)
· Settings menu with JSON support
· Drawing geometric shapes in the console

Examples and basic functionality
Control: Move cursor up/down with arrow keys, select with Enter

---

listgr:

```python
import tpg #import lib
out_point=listgr(['point1','point2','point3'])
print(out_point)
```

[image](list_test.gif)

Arguments:
kastor - parameter responsible for the cursor displayed before the selected item (default '>')

title - text above the list

style - style, default 'standard', other options 'scob'

Control: Move cursor up/down with arrow keys, change with Enter, exit with Esc

ansi - ability to use ANSI escape sequences in the menu. Just pass the ANSI sequence; it's recommended to use the color function described below.

---

settings:

```python
import tpg #import lib

out=settings({'point1':true,'point2':false}) # change dict
print(out) # print new dict from json file

out=settings({},jsonf='test_json.json')# read and write json file 

print(out) # print new dict 
```

doc/settings_ui_test.gif

In the first case, a dictionary was passed to the function. It can have any number of keys, but the values must be true or false. The function returns the updated dictionary modified by the user.

In the second case, the dictionary is extracted from a json file whose name is specified in the jsonf argument. After user changes, the json file will be modified, and the function returns a dictionary with the updated data from the json.

yes_or_no:

```python
import tpg #import lib

if yes_or_no('yes or no'): # yes - True no - False 
    print("press yes") 
else:
    print('press no')  
```

doc/yes_or_no.gif

Arguments:

· text - title above the interactive elements
· kastcor - cursor displayed before the selected element
· yestxt - text for the 1st element (yes by default)
· notxt - text for the 2nd element (no by default)

color:

```python
from tpg import * #import lib

# color color, style, background
print(color("green text, yellow background",'red','standard','yellow')) 
print('text') 
```

Supported colors:

· black
· red
· green
· yellow
· blue
· violet
· cyan
· white

These work for both background and text color.

move_cursor:

move_cursor - changes the cursor position in the console

Example:

```python
from tpg import *

move_cursor(5,5)
print("hello world")
```

Arguments:

· x - X coordinate of the cursor
· y - Y coordinate of the cursor

clear:

clear - completely clears the console

frame:

frame - creates a frame with text inside

```python
from tpg import *

print(frame('aaa\naaaa'))
```

Arguments:

· text - text inside the frame
· x - X coordinate of the frame, default is -1 and the frame is centered horizontally
· y - Y coordinate of the frame, default is -1 and the frame is centered vertically
· text_color - text color in ANSI format
· frame_color - frame color in ANSI format

---

display class:

A class for drawing with symbols in the console

Functions:

· cursor
· echo
· box
· clear_display
· line
· triangle
· circle
· multi_line
· printf

Examples:

Square/Rectangle:

```python
import tpg

display=tpg.display()

display.box(5, 5, 2, 2)

display.echo()
```

Parameters:

· px - shape width
· py - shape height
· x - X coordinate of the top-left character
· y - Y coordinate of the top-left character
· color - a tuple with 2 elements: index 0 is the starting ANSI code placed before the character, index 1 is the code placed after the character
· filling - whether the square is filled

Displaying text at coordinates:

```python
import tpg

display=tpg.display()

display.cursor(5,5)

display.echo()
```

Drawing lines:

```python
import tpg

display=tpg.display()

display.line((2,2), (32,5))

display.echo()
```

Arguments:

· point1 (tuple) - tuple with coordinates of the first point: index 0 is X, index 1 is Y
· point2 (tuple) - tuple with coordinates of the second point: index 0 is X, index 1 is Y
· color (tuple) - color of the line characters: index 0 is the start ANSI code (before character), index 1 is the end code (after character)
· symbol (str) - the character the line is made of

Circles:

```python
import tpg 

display=tpg.display()

display.circle(5, 5, 4)

display.echo()
```

Arguments:

· cx - x coordinate of the circle's center
· cy - y coordinate of the circle's center
· radius - radius of the circle
· symbol - character for the circle

Triangle:

```python
import tpg

display=tpg.display()

display.trigon(10, 6, 5, 5)

display.echo()
```

Arguments:

· x - X coordinate of the vertex
· y - Y coordinate of the vertex
· h - height of the triangle
· w - width of the triangle (its base)
· filling - whether the triangle is filled

Connecting points with a line:

```python
import tpg 

display = tpg.display()

display.multi_line([(2,2), (10,10), (2,10), (2,2)])

display.echo()
```

Arguments:

· points (list) - list of points to connect, where each element is a tuple with X coordinate (index 0) and Y coordinate (index 1)
· color (tuple) - color of the characters: index 0 is the start ANSI code (before character), index 1 is the end code (after character)
· symbol (str) - the character the line is made of

Example programs:

Displaying 2 rectangles (squares with specified properties) where one contains text and the other is filled

```python
import tpg

display=tpg.display()

display.box(15, 11, 1, 1, block='@')

display.box(15, 11, 22, 1, filling=True)

display.cursor(3,3, symbol='hi')

display.echo(end='\n')
```

Displaying text:
Displays text on the screen where each character has its own coordinates.

```python
from tpg import display

display=display()

display.printf(2, 2, "text 1")

display.echo()
```

Arguments:

· x (int) - X coordinate of the first character
· y (int) - Y coordinate
· text (str) - text to display
· color (tuple) - color of characters: index 0 is the start ANSI code (before character), index 1 is the end code (after character)

---

logse class

A mini logger class with different logging levels and flexible settings

```python
import tpg

log=tpg.logse()

log.info("test info")

log.warning("test warning")

log.error("test error")
```

info - logging level 1

warning - logging level 2

error - logging level 3

Common arguments for all levels:

· text - the logging text that appears after the common pattern (pattern - object of the log class)
· info_pattern - indicates the log type, appears after the pattern, followed by the text itself
· end - end of the log line

Objects of the log class required for configuration:

· file - stores the name of the log file
· save_log_file - whether logs should be written to a file
· level - displayed logging level. -1 - no levels displayed, 0 - only info, 1 - info and warning, 2 - all logging levels (info, warning, error)
· pattern - a common template for the log file line, by default contains date, time, and the path to the executed file
· path_save_log - path to the directory where the log file will be saved; if None, saving occurs in the current file's directory

Here's what it looks like:

doc/log_test.png