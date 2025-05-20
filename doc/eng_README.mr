**TPG - Terminal Python Graphics (UI)**  
A small library for creating graphical interfaces.  

The library includes the following features:  
- Lists  
- Simplified color handling (ANSI)  
- Console cursor control  
- Selection menus (yes/no)  
- Settings with JSON support  
Examples and basic functionality  

**Controls:** Move the cursor up/down with arrow keys, select with Enter.  

### **listgr:**  
```python
from tpg import *
out_point = listgr(['point1', 'point2', 'point3'])
print(out_point)
```  

**Arguments:**  
- `kastor` – Parameter for the cursor symbol in front of the selected item (default: `'>'`)  
- `title` – Text displayed above the list  
- `style` – Default style is `'standart'`; another option is `'scob'`  
- `ansi` – Allows the use of ANSI escape sequences in the menu. Just pass an ANSI sequence (recommended to use the `color` function described below).  

**Controls:** Move the cursor up/down with arrow keys, change selection with Enter, exit with Esc.  

**How it looks:**  
![hippo](doc/list_test.gif)  

---

### **settings:**  
```python
from tpg import *  # Import library  

# Case 1: Modify a dictionary  
out = settings({'point1': True, 'point2': False})  # Pass a dict  
print(out)  # Returns the updated dictionary  

# Case 2: Read and write to a JSON file  
out = settings({}, jsonf='test_json.json')  
print(out)  # Returns the modified dict from the JSON file  
```  

![hippo](doc/settings_ui_test.gif)  

- In the **first case**, a dictionary is passed (can have any keys, but values must be `True` or `False`). The function returns the updated dictionary after user modifications.  
- In the **second case**, the dictionary is loaded from a JSON file (specified in `jsonf`). After user changes, the JSON file is updated, and the function returns the modified dictionary.  

---

### **yes_or_no:**  
```python
from tpg import *  # Import library  

if yes_or_no('yes or no'):  # Returns True for "yes," False for "no"  
    print("Pressed yes")  
else:  
    print('Pressed no')  
```  

Takes one argument (the prompt text at the top).  
Returns `True` if "yes" is selected, `False` if "no" is selected.  

---

### **color:**  
```python
from tpg import *  # Import library  

# color(text_color, style, background_color)  
print(color('red', 'standart', 'yelou') + 'green text, yellow background')  
print(color('clear'))  # Reset colors  
print('text')  
```  

**Available colors:**  
- `blak` (black)  
- `red`  
- `green`  
- `yelou` (yellow)  
- `blue`  
- `violet`  
- `beruza` (cyan)  
- `white`  

Works for both text and background colors.  
