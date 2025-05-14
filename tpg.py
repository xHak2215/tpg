import json
import os
import time

import keyboard

def listgr(unitperedvogenielist:list,kastcor='>',title='',style='standart')->str:
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
                print(cor+str(unitperedvogenielist[i]))
            elif style=='scob':
                if cursor==i:
                    cor='+'
                else:
                    cor=''
                print('['+cor+']'+str(unitperedvogenielist[i]))
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
        os.system('clear') 
        
def settings(data:dict,kastcor='>',title='',style='zapoln',jsonf=None)->str:
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
            print(cor+punkt+ ' ' * int(20 - len(punkt)) +'['+flag+']')
        if keyboard.is_pressed('enter'):
            if data[list(data.keys())[cursor]]:
                data[list(data.keys())[cursor]]=False
            else:
                data[list(data.keys())[cursor]]=True
            while keyboard.is_pressed('enter'):
                time.sleep(0.1)
        os.system('clear') 
        
class ansi:
    def __init__(self):
        self.stule={
            'standart':0,
            'big':1,
            'tone':2,
            'kursive':3,
            'line':4,
            'mercanie':5
        }
        self.color={
            'blak':30,
            'red':31,
            'green':32,
            'yelou':33,
            'blue':34,
            'violet':35,
            'beruza':36,
            'white':37,
            'clear':0
        }
        self.beggraubd={
            'blak':40,
            'red':41,
            'green':42,
            'yelou':43,
            'blue':44,
            'violet':45,
            'beruza':46,
            'white':47,
            'clear':0
            
        }
def color(color,stule='standart',begraund='blak')->str:#color,stule,beggraubd
    #if len(ansis)>3:
    #    
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
    return f'\33[{stule};{color};{begraund}m'

def cursor(x:int,y:int,text:str)->str:
    if y>0:
        print(f"\033[{y}A{text}")#в верх
    else:
        print(f"\033[{y}B{text}")#в низ
    if x>0:
        print(f"\033[{x}C{text}")#в перед 
    else:
        print(f"\033[{x}D{text}")# на зад
        
    
def yes_ro_no(text:str,kastcor='>',yestxt='yes',notxt='no'):
    out=False
    yes=''
    no='>'
    while True:
        print('\n'*13)
        if keyboard.is_pressed('left'):
            yes=kastcor
            no=''
            out=True
        if keyboard.is_pressed('right'):
            no=kastcor
            yes=''
            out=False
        if keyboard.is_pressed('enter'):
            while keyboard.is_pressed('enter'):
                time.sleep(0.1)
                pass
            return out
        print(' '*(10-len(text))+text)
        print(f'{' '*15}{yes}{yestxt} {no}{notxt}')
        os.system('clear')
        
        
def cursor(x:int,y:int,text:str)->str:
    if y >0:
        print(f"\033[{y}A{text}")#в верх
    else:
        print(f"\033[{y}B{text}")#в низ
    if x>0:
        print(f"\033[{x}C{text}")#в перед 
    else:
        print(f"\033[{x}D{text}")# на зад
        
def clear():
    print("\033[2J"+'\033[0',end='') #очистка 
    os.system("clear")

    
    
    


        
