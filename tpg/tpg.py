import json
import os
import time
import sys
import threading
import traceback
from datetime import datetime
import inspect

from .ansi import  ansi, art

import keyboard
import subprocess

def listgr(unitperedvogenielist:list, kastcor='>', title='', style='standart', ansi='\033[0m')->str:
    cursor=0
    while True:
        cor=''
        print(title)
        if keyboard.is_pressed('esc'):
            return None
        if keyboard.is_pressed('down'):
            cursor=cursor+1
        if keyboard.is_pressed('up'):
            cursor=cursor-1
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
                print(ansi+cor+str(unitperedvogenielist[i]))
            elif style=='scob':
                if cursor==i:
                    cor='+'
                else:
                    cor=''
                prob=' '*(max(0,15-len(str(unitperedvogenielist[i]))))
                print(ansi+f'{str(unitperedvogenielist[i])}{prob}({cor})')
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
        if os.name == 'nt': 
            os.system("cls")
        else:
            os.system("clear")
        
def settings(data:dict,kastcor='>',title='',style='zapoln',jsonf=None,ansi='\033[0m')->str:
    cursor=0
    if os.path.isfile(jsonf):
            with open(jsonf, "r") as json_settings:
                data = json.load(json_settings)
    else:
        raise FileNotFoundError(f'no faile ({jsonf})')
    while True:
        cor=''
        print(title)
        if keyboard.is_pressed('esc'):
            with open(jsonf, "w") as json_settings:
                json_settings.write(json.dumps(data))
            while keyboard.is_pressed('esc'):
                time.sleep(0.1)
            return data
        if keyboard.is_pressed('down'):
            cursor=cursor+1
        if keyboard.is_pressed('up'):
            cursor=cursor-1
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
            print(ansi+cor+punkt+ ' ' * int(20 - len(punkt)) +'['+flag+']')
        if keyboard.is_pressed('enter'):
            if data[list(data.keys())[cursor]]:
                data[list(data.keys())[cursor]]=False
            else:
                data[list(data.keys())[cursor]]=True
            while keyboard.is_pressed('enter'):
                time.sleep(0.1)
        if os.name == 'nt': 
            os.system("cls")
        else:
            os.system("clear")
        
def terminal_size() ->tuple:
    """
    terminal size
    
    Returns:
        tuple: 0 - height. 1 - lines num
    """
    # X , Y 
    return (int(os.get_terminal_size().columns) , int(os.get_terminal_size().lines))

def is_terminal_focused():
    if os.name == 'nt': 
        return True
    else:
        try:
            active = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowpid"])
            return int(active.strip()) == os.getpid()
        except Exception as e:
            return True


def color(text,color,stule='standart',begraund='blak',end='\33[0m')->str:#text,color,stule,beggraubd
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
        stule=self.stule[stule]
    except KeyError:
        raise KeyError(f'error Not correct parameters , parameters :{self.stule.keys()} ')
    try:
        color=self.color[color]
    except KeyError:
        raise KeyError(f'error Not correct parameters , parameters :{self.color.keys()} ')
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
        if key:
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

def cursor(x:int,y:int,display='█',fone=' ')->str:
    print(('\n'*y)+(fone*x+display))
    
    
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
        self.lock = threading.Lock()  # Для безопасного доступа к output
    
    def input_at(self, x: int, y: int, prompt: str): 
        """Создает поле ввода в указанных координатах"""
        # Перемещаем курсор и выводим приглашение
        with self.lock:
            sys.stdout.write(f"\033[{y};{x}H{prompt}")
            input_pos = x + len(prompt)
            sys.stdout.write(f"\033[{y};{input_pos}H")
            sys.stdout.flush()
        
        # Читаем ввод
        user_input = sys.stdin.readline()
        
        # Сохраняем результат
        with self.lock:
            self.output.append(user_input.strip())
    
    def gather_inputs(self, *coordinates):
        """### Запускает несколько полей ввода одновременно"""
        threads = []
        
        for x, y, prompt in coordinates:
            # Создаем поток для каждого поля ввода
            t = threading.Thread(target=self.input_at, args=(x, y, prompt))
            t.daemon = True
            threads.append(t)
            t.start()
        
        # Ждем завершения всех потоков
        for t in threads:
            t.join()
        
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
        
    def box(self,px:int, py:int, x:int, y:int, symbol='█', filling=False):
        """### create box

        Args:
            px (int): length box
            py (int): height box
            x (int): X Corridate
            y (int): Y Corridate
            symbol (str, optional): symbol box. Defaults to '█'.
            filling (bool): заполнен ли квадрат
        """
        
        if y>len(self.display)+py:
            raise TypeError(f"Y goes beyond (max {len(self.display)})")
        if x>len(self.display[0])+px:
            raise TypeError(f"X goes beyond (max {len(self.display[0])})")
        
        for xpos in range(x, x+px):
            self.display[y][xpos] = symbol
            
        if filling:
            for y in range(y,y+py):
                for xe in range(x,x+px):
                    self.display[y][xe] = symbol
        else:
            for y in range(y,y+py):
                self.display[y][x] = symbol
                self.display[y][x+px] = symbol   
                 
        for xpos in range(x,x+px):
            self.display[y][xpos] = symbol
            
    def cursor(self ,x : int, y : int, symbol='█'):
        try:
            self.display[y]
        except KeyError:
            raise KeyError(f'no the lines end lines {len(self.display)}')
        try:
            self.display[y][x] = symbol
        except KeyError:
            raise KeyError(f'There is no such symbol')
    
    def line(self, point1:tuple, point2:tuple, symbol='█'):
        """
        Рисует линию между point1 и point2.
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
            self.display[y][x] = symbol
            if x == x1 and y == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x += sx
            if e2 <= dx:
                err += dx
                y += sy
    
    def circle(self, cx: int, cy: int, radius: int, symbol='█', full=0):
        """### функция рисующая круг

        Args: 
            x (int): X координата 
            y (int): Y координата  
            radius (int): радиус круга
        """ 
        rows = len(self.display)
        cols = len(self.display[0]) if rows > 0 else 0
        aspect = 2.0  # char_height / char_width

        def plot(px, py):
            if 0 <= py < rows and 0 <= px < cols:
                self.display[py][px] = symbol
                self.display[py][px + full] = symbol

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
            ax = round(x * aspect)
            ay = y
            ay_inv = -y
            ax_y = round(y * aspect)

            plot_hline_outline(cx - ax, cx + ax, cy + ay)
            plot_hline_outline(cx - ax, cx + ax, cy - ay)

            plot_hline_outline(cx - ax_y, cx + ax_y, cy + x)
            plot_hline_outline(cx - ax_y, cx + ax_y, cy - x)

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
    
    def trigon(self, x:int, y:int, h:int, w:int, symbol='█'):
        """рисует треугольник

        Args:
            x (int): X координата
            y (int): Y координата
            h (int): высота
            w (int): ширена
            symbol (str, optional): синвол треугольника. Defaults to '█'.
        """
        
        higft=0
        wight=0
        
        while h>=higft:
            self.display[y+higft][x+wight] = symbol
            self.display[y+higft][x-wight] = symbol
            if wight<=w:
                wight+=1
            higft+=1

        for line in range(x-wight+1, x+wight-1):
            self.display[y+higft-1][line] = symbol
        
    def echo(self, end='\r') -> str:
        """выводит буфер на экран

        Args:
            end (str, optional): аргумент end. Defaults to '\r'.

        Returns:
            str: содержимое буфера
        """
        
        strings='' # НЕ СТРИНГИ А СТРОКИ
        for i in self.display:
            for st in list(dict(i).keys()):
                strings=strings+i[st]
            strings+='\n'
        print(strings, end=end)
        
        
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
        
