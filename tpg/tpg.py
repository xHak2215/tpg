import json
import os
import time
import sys
import threading
import traceback
from datetime import datetime
import inspect
import ctypes
from ctypes import wintypes
import re

from .ansi import  ansi, art
import console_tool

import keyboard
import subprocess
import psutil

def console_is_active():
    """определяет активно ли окно, совместимо с X11 оболочкой и Windows"""
    if os.name == 'nt':
        try:
            GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
            GetConsoleWindow = ctypes.windll.kernel32.GetConsoleWindow
            GetForegroundWindow.restype = wintypes.HWND
            GetConsoleWindow.restype = wintypes.HWND
            return GetForegroundWindow() == GetConsoleWindow()
        except Exception:
            return False
        
    elif os.name == 'posix':
        try:
            active = subprocess.check_output(["xdotool", "getactivewindow"]).strip().decode()
            # получить _NET_WM_PID окна
            out = subprocess.check_output(["xprop", "-id", active, "_NET_WM_PID"]).decode()
            m = re.search(r"=\s*(\d+)", out)
            p = psutil.Process(os.getpid())
            for anc in p.parents():
                if m and anc.pid == int(m.group(1)):
                    return True
        except Exception as e:
            return True
        return False
    else:
        return True

def listgr(unitperedvogenielist:list, kastcor='>', title=None, style='standart', ansi='\033[0m')->str|None:
    cursor=0
    event=None
    cor=''
    while True:
        if event:
            key = event.name
        else:
            key='-'

        if key and console_is_active():
            if os.name == 'nt': 
                os.system("cls")
            else:
                os.system("clear")

            if title:
                print(title)

            if keyboard.is_pressed('esc'):
                return None
            
            if keyboard.is_pressed('down'):
                cursor=cursor+1
                if os.name != 'nt':time.sleep(0.1) 

            if keyboard.is_pressed('up'):
                cursor=cursor-1
                if os.name != 'nt':time.sleep(0.1)

            if cursor<0:
                cursor=0
            if cursor>len(unitperedvogenielist)-1:
                cursor=len(unitperedvogenielist)-1
            for i in range(len(unitperedvogenielist)):
                if style =='standart':
                    if cursor==i:
                        cor=kastcor
                    else:
                        cor=' '
                    print(f"{ansi}{cor}{str(unitperedvogenielist[i])}")

                elif style=='scob':
                    if cursor==i:
                        cor='+'
                    else:
                        cor=''
                    prob=' '*(max(0,15-len(str(unitperedvogenielist[i]))))

                    print(f"{ansi}{str(unitperedvogenielist[i])}{prob}({cor})")
                else:
                    raise SyntaxError('no style'+style)
                #if type(unitperedvogenielist[i])=="dict":
                #    for a in unitperedvogenielist[i].keys():
                #        print('  '+cor+a+'ᐁ')
                #        for s in a:
                #            print(s)
            if keyboard.is_pressed('enter'):
                unitperedvogenie=unitperedvogenielist[cursor]
                while keyboard.is_pressed('enter'):
                    time.sleep(0.1)
                return unitperedvogenie
        event = keyboard.read_event()
        
def settings(data:dict,kastcor='>',title=None,style='zapoln',jsonf=None,ansi='\033[0m')->str|dict:
    cursor=0
    if jsonf and os.path.isfile(jsonf):
            with open(jsonf, 'r') as json_settings:
                data = json.load(json_settings)
    else:
        raise FileNotFoundError(f'no file ({jsonf}) in the directories')
    event=None
    while True:
        if event:
            key = event.name
        else:
            key='-'
        if key and console_is_active():
            if os.name == 'nt': 
                os.system("cls")
            else:
                os.system("clear")

            cor=''
            if title:
                print(title)
            if keyboard.is_pressed('esc'):
                with open(jsonf, "w") as json_settings:
                    json_settings.write(json.dumps(data))
                while keyboard.is_pressed('esc'):
                    time.sleep(0.1)
                return data
            if keyboard.is_pressed('down'):
                cursor=cursor+1
                if os.name!='nt':time.sleep(0.1)
                
            if keyboard.is_pressed('up'):
                cursor=cursor-1
                if os.name!='nt':time.sleep(0.1)

            if cursor<0:
                cursor=0
            if cursor>len(list(data.keys()))-1:
                cursor=len(list(data.keys()))-1
            for i in range(len(list(data.keys()))):
                punkt=list(data.keys())[i]
                if cursor==i:
                    cor=kastcor
                else:
                    cor=' '
                if style == 'zapoln':
                    if bool(data[punkt]):
                        flag='█'
                    else:
                        flag='░'
                elif style == '+':
                    if bool(data[punkt]):
                        flag='+'
                    else:       
                        flag='-'
                else:
                    raise ValueError("no the style, style: zapoln, +")
                print(f"{ansi}{cor}{punkt} {' ' * int(20 - len(punkt))} {'['+flag+']'}")
            if keyboard.is_pressed('enter'):
                if data[list(data.keys())[cursor]]:
                    data[list(data.keys())[cursor]]=False
                else:
                    data[list(data.keys())[cursor]]=True
                while keyboard.is_pressed('enter'):
                    time.sleep(0.1)
                key=True
                event=None
                continue

        event = keyboard.read_event()
        
def terminal_size() ->tuple:
    """
    terminal size
    
    Returns:
        tuple: 0 - height. 1 - lines num
    """
    # X , Y 
    return (int(os.get_terminal_size().columns) , int(os.get_terminal_size().lines))

def color(text, color, style='standart', begraund='blak', end='\33[0m')->str:#text,color,stule,beggraubd
    r"""позволяет перекрашивать цвет работает на `ansi`

    Args:
        text (_str_): текст который будет перекрашен
        color (_srt_): цвет текста
        stule (str, optional): стиль. Defaults to 'standart'.
        begraund (str, optional): задний фон. Defaults to 'blak'.
        end (str, optional): конец строки. Defaults to '\33[0'.

    Returns:
        str: текст с `ansi` кодами
    """
    
    self=ansi()
    try:
        stule=self.style[style]
    except KeyError:
        raise KeyError(f'error Not correct parameters , parameters :{self.style.keys()} ')
    try:
        color=self.color[color]
    except KeyError:
        raise KeyError(f'error Not correct parameters , parameters :{self.style.keys()} ')
    try:
        begraund=self.beggraubd[begraund]
    except KeyError:
        raise KeyError(f'error Not correct parameters , parameters :{self.beggraubd.keys()} ')
    return f"\33[{stule};{color};{begraund}m{text}{end}"
    
def yes_ro_no(text:str, kastcor='>', yestxt='yes', notxt='no', midst=False, deep=terminal_size()[1]-3):
    out=False
    yes=''
    no='>'
    otst=0
    event=None
    while True:
        if event:
            key = event.name
        else:
            key='-'
        if key and console_is_active():
            if os.name == 'nt': 
                os.system("cls")
            else:
                os.system("clear")
                
            if key == 'left':
                yes=kastcor
                no=''
                out=True
            if key == 'right':
                no=kastcor
                yes=''
                out=False
            if key == 'enter':
                while keyboard.is_pressed('enter'):
                    time.sleep(0.1)
                    pass
                return out
            if midst:
                otst=terminal_size()[0] // 2
            print(f"{'\n'*deep}{' '*otst}{text}\n{' '*otst}{yes}{yestxt} {no}{notxt}")
            
        event = keyboard.read_event()
        
def cursor(X:int, Y:int):
    """Перемещает курсор в консоли на указанные координаты."""
    console_tool.cursor(X, Y)    
    
'''
if y > 0:
    print(f"\033[{y}Am{text}")#в верх
else:
    print(f"\033[{y}Bm{text}")#в низ
if x > 0:
    print(f"\033[{x}Cm{text}")#в перед 
else:
    print(f"\033[{x}Dm{text}")# на зад
'''           
        
def clear():
    print('\033[0m') #очистка
    if os.name == 'nt': 
        os.system("cls")
    else:
        os.system("clear")

def frame(text:str, x=-1, y=-1)->str:
    
    text=str(text)
    split=text.split('\n')
    
    if x==-1 and y==-1:
        ots=' '*(int(round(terminal_size()[0]/2))-int(len(text)+2))
    else:
        ots=' '*x
    temp_string=f"{ots}╔{'═'*len(max(split, key=len))}╗"
    for t in split:
        temp_string=temp_string+f"\n{ots}║{t}{' '*(len(max(split, key=len))-len(t))}║"
    temp_string=temp_string+f"\n{ots}╚{'═'*len(max(split, key=len))}╝"
        
    return temp_string

class InputMany:
    def __init__(self):
        self.output = []
        self.inputs_list = []
        self.input_in = 0
        self.lock = threading.Lock()

    def input_at(self, x: int, y: int, prompt: str):
        """Отобразить приглашение в позиции (x,y)."""
        self.inputs_list.append((x, y, prompt))

    def _reader(self, x: int, y: int, prompt: str, index:int):
        """
        Читает ввод и сохраняет в self.output в позиции index.
        index нужен, чтобы сохранить порядок ответов соответствующим переданным координатам.
        """
        cursor(x + len(prompt), y)
        user_input = sys.stdin.readline()
        with self.lock:
            self.output.append(user_input)

    def run_inputs(self) -> list:
        """
        coordinates: последовательность кортежей (x, y, prompt)
        Возвращает список ответов в том же порядке, в котором заданы coordinates.
        """
        threads = []

        # Сначала отрисуем все промпты
        for (x, y, prompt) in self.inputs_list:
            cursor(x, y)
            sys.stdout.write(prompt)
            sys.stdout.flush()
        
        ix=0
        for i, (x, y, prompt) in enumerate(self.inputs_list):
            t = threading.Thread(target=self._reader, args=(x, y, prompt, ix))
            t.daemon = True
            threads.append(t)
            t.start()
            t.join()
            ix+=1

        #for t in threads:
        #    t.join()

        return self.output

class display:
    def __init__(self):
        templist=[]
        size=terminal_size()
        for lens in range(size[1]): 
            temp={}
            for i in range(size[0]):
                temp[i]=' '
            templist.append(temp)
        self.display=templist
        
    def box(self,px:int, py:int, x:int, y:int, symbol='█', filling=False, color=("\33[0m","\33[0m")):
        """### create box

        Args:
            px (int): length box
            py (int): height box
            x (int): X Corridate
            y (int): Y Corridate
            symbol (str, optional): symbol box. Defaults to '█'.
            filling (bool): заполнен ли квадрат.
            color (tuple): цвет синволов где 0 элемент это начало ANSI кода (перед синволом), а 1 его конец (после синвола).
        """
        
        if y>len(self.display)+py:
            raise TypeError(f"Y goes beyond (max {len(self.display)})")
        if x>len(self.display[0])+px:
            raise TypeError(f"X goes beyond (max {len(self.display[0])})")
        
        for xpos in range(x, x+px):
            self.display[y][xpos] = color[0] + symbol + color[1]
            
        if filling:
            for y in range(y,y+py):
                for xe in range(x,x+px):
                    self.display[y][xe] = color[0] + symbol + color[1]
        else:
            for y in range(y,y+py):
                self.display[y][x] = color[0] + symbol + color[1]
                self.display[y][x+px] = color[0] + symbol + color[1]
                 
        for xpos in range(x,x+px):
            self.display[y][xpos] = color[0] + symbol + color[1]
            
    def cursor(self ,x : int, y : int, symbol='█', color=("\33[0m","\33[0m")):
        try:
            self.display[y]
        except KeyError:
            raise KeyError(f'no the lines end lines {len(self.display)}')
        try:
            self.display[y][x] = color[0] + symbol + color[1]
        except KeyError:
            raise KeyError(f'There is no such symbol')
    
    def line(self, point1:tuple[int,int], point2:tuple[int,int], symbol='█', color:tuple=("\33[0m","\33[0m")):
        """
        Рисует линию между point1 и point2.
        Args:
            point1 (tuple): координаты 1 точки формат: `(X, Y)`
            point2 (tuple): координаты 2 точки формат: `(X, Y)`
            color (tuple): цвет синволов где 0 элемент это начало ANSI кода (перед синволом), а 1 его конец (после синвола).
            symbol (str): синвол из которого сотоит линия.
        """
        x0, y0 = point1
        
        x1, y1 = point2
        
        if y0 < 0 or y1 < 0 or y0 >= len(self.display) or y1 >= len(self.display):
            raise TypeError(f"Y goes beyond (max {len(self.display)-1})")

        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy

        x, y = x0, y0
        while True:
            # проверяем, что строка существует (по Y) - уже гарантировано; по X используем запись в словарь
            self.display[y][x] = color[0] + symbol + color[1]
            if x == x1 and y == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x += sx
            if e2 <= dx:
                err += dx
                y += sy

    def circle(self, cx: int, cy: int, radius: int, symbol='█', full=0, color:tuple=("\33[0m","\33[0m")):
        '''### функция рисующая круг (**работает криво!**)

        Args: 
            x (int): X координата 
            y (int): Y координата  
            radius (int): радиус круга
            symbol (str): синвол из которого сотоит круг.
            color (tuple): цвет синволов где 0 элемент это начало ANSI кода (перед синволом), а 1 его конец (после синвола).
        '''
        rows = len(self.display)
        cols = len(self.display[0]) if rows > 0 else 0
        aspect = 2.0  # char_height / char_width

        # это какой то лютый гавнокод
        def plot(px, py):
            if 0 <= py < rows and 0 <= px < cols:
                self.display[py][px] = color[0] + symbol + color[1]
                self.display[py][px + full] = color[0] + symbol + color[1]

        def plot_hline_outline(x1, x2, y):
            if y < 0 or y >= rows: return
            if x1 > x2: x1, x2 = x2, x1
            # обрезаем по границам
            if x2 < 0 or x1 > cols-1: return
            x1 = max(0, x1); x2 = min(cols-1, x2)
            plot(x1, y)
            if x2 != x1:
                plot(x2, y)
        
        x = 0
        y = radius
        d = 3 - 2 * radius

        while x <= y:

            #ax = round(x * aspect)
            #ay = y
            #ax_y = round(y * aspect)

            plot(cx, cx)
            plot(cx, cx)

            plot(cx, cx)
            plot(cx, cx)

            if d <= 0:
                d = d + 4 * x + 6
            else:
                d = d + 4 * (x - y) + 10
                y -= 1
            x += 1
    
    def clear_display(self):
        """### clear display"""
        
        self.display={}
        templist=[]
        size=terminal_size()
        for lens in range(size[1]): 
            temp={}
            for i in range(size[0]):
                temp[i]=' '
            templist.append(temp)
        self.display=templist
    
    def trigon(self, x:int, y:int, h:int, w:int, symbol='█', filling:bool=False, color=("\33[0m","\33[0m")):
        """рисует треугольник

        Args:
            x (int): X координата
            y (int): Y координата
            h (int): высота
            w (int): ширена
            symbol (str, optional): синвол из кторого будет состоять фигура. Defaults to '█'.
            color (tuple): цвет синволов где 0 элемент это начало ANSI кода (перед синволом), а 1 его конец (после синвола).
        """
        
        higft=0
        wight=0

        while h>=higft:
            if filling:
                self.line((x+wight, y+higft),(x-wight, y+higft), color=color)
            else:
                self.display[y+higft][x+wight] =color[0] + symbol + color[1]
                self.display[y+higft][x-wight] =color[0] + symbol + color[1]
            if wight<=w:
                wight+=1
            higft+=1

        for line in range(x-wight+1, x+wight-1):
            self.display[y+higft-1][line] = color[0] + symbol + color[1]
        
    def echo(self, end='\r', print_std:bool=True) -> str:
        """выводит буфер на экран

        Args:
            end (str, optional): аргумент end. Defaults to '\r'.
            print_std (bool): вудет ли вывод содержимого буфера в терминал. Defaults to `True`. 

        Returns:
            str: содержимое буфера
        """
        
        strings='' # НЕ СТРИНГИ А СТРОКИ
        for i in self.display:
            for st in list(dict(i).keys()):
                strings=strings+i[st]
            strings+='\n'
        if print_std:
            print(strings, end=end)
        
        return strings
        
        
def write_to_log_file(file, t, path_save_log):
    if path_save_log:
        path=os.path.join(path_save_log, file)
    else:
        path=file
    with open(path, 'a', buffering=1) as f:
        f.write(t+'\n')        

class logse:
    def __init__(self):
        self.file='log.log'
        self.level=2
        self.seve_log_file=True
        self.patern=f"{datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")} |{sys._getframe(1).f_locals['__file__']}| "
        self.path_save_log=None
        
        # color
        self.color_green='\33[32m'
        self.color_red='\33[31m'
        self.color_yelow='\33[33m'
    
    def info(self, text, info_patern=f"info: ", end='\033[0m'):
        if self.level>=0:
            print(self.patern+f"{self.color_green}line:{inspect.stack()[1][2]} |{info_patern}{str(text)}{end}")
        
            if self.seve_log_file:
                write_to_log_file(self.file, self.patern+f"line:{inspect.stack()[1][2]} |{info_patern}{str(text)}", self.path_save_log)    
                
    def warning(self, text, warning_patern=f"warning: ", end='\033[0m'):
        if self.level>=1:
            print(self.patern+f"{self.color_yelow}line:{inspect.stack()[1][2]} |{warning_patern}{str(text)}{end}")
            
            if self.seve_log_file:
                write_to_log_file(self.file, self.patern+f"line:{inspect.stack()[1][2]} |{warning_patern}{str(text)}", self.path_save_log)    
        
    def error(self, text, error_patern=f"ERROR: ", end='\033[0m'):
        if self.level>=2:
            print(self.patern+f"{self.color_red}line:{inspect.stack()[1][2]} |{error_patern}{str(text)}{end}")
            
            if self.seve_log_file:
                write_to_log_file(self.file, self.patern+f"line:{inspect.stack()[1][2]} |{error_patern}{str(text)}", self.path_save_log)
        
