
</details>
  <summary>languages</summary>
      <ul>
      <li><a href="https://github.com/xHak2215/tpg/blob/main/doc/eng_README.md">English</a></li>
      </ul>
</details>

TPG - terminal pseudo graphics
небольшая библиотека для создания графических интерфейсов (TUI)

в функционал библиотеки входят :

- списки
- упрощеная работа с цветами (ANSI)
- упровление курсором кансоли
- меню выбора (да/нет)
- меню настройки с потдержкой json
- отрсиовка геометрических фигур в консоли 

примеры и базовый функционал
упровление: перемещение курсора в верх в низ стрелки, выбор - enter

---

### listgr:

```python
import tpg #inport lib
out_point=listgr(['point1','point2','point3'])
print(out_point)
```

![hippo](doc/list_test.gif)

аргументы:
`kastor` - параметре отвечающий за курсор стоящий перед выбранным пунктом (по умолчанию '>')

`title` - текст над списком

`style` - стиль по умолчанию 'standart' другие 'scob'

управление: перемещение курсора в верх в низ стрелки,изменение - enter,заверщение - esc

`ansi` - возможность использовать ANSI escape sequences в меню достаточно лишь передать ANSI последовательность советую использовать функцию `color` описанную ниже



### settings:

```python
import tpg #inport lib

out=settings({'point1':true,'point2':false}) # change dict
print(out) # print new dict from json file

out=settings({},jsonf='test_json.json')# read and write json file 

print(out) # print new dict 

```

![hippo](doc/settings_ui_test.gif)

в 1 случае в функцию был передан словарь он может быть с любыми ключами и их количеством но  
значения должно быть true или false функция вернет обновлённый словарь измененный пользователем

во 2 случае словарь извлекается из json файла его име указывается в аргументе `jsonf` после пользовательских изменений json файл будет изменен а функция вернёт словарь с изменёнными данными из json

### yes_or_no:

```python
import tpg #inport lib

if yes_or_no('yes or no'): # yes - True no -false 
    print("press yes") 
else:
    print('press no')  
```
![hippo](doc/yes_or_no.gif)

аргументы:
- `text` - заголовок над интерактиынфми элементами 
- `kastcor` - курсор стоящий перед выброным элементом 
- `yestxt` - текст 1 элемента (yes по умолчанию)
- `notxt` - текст 2 элемента (no по умолчанию)

### color:

```python
from tpg import * #inport lib

# color color/цвет,stule/стиль,beggraubd/задний фон
print(color("green text,yelou begraund",'red','standart','yelou')) 
print('text') 
```

поддерживает цвета:

- blak
- red
- green
- yelou
- blue
- violet
- beruza
- white
  
подходят как для заднего фона так и для цвета текста


### move_cursor:

`move_cursor` - изменяет положения курсора в консоли

пример:
```python
from tpg import *

move_cursor(5,5)
print("hello world")
```
аргументы:
- `x` - X координата курсора
- `y` - Y координата курсора

### clear:
`clear` - полностью очерняет консоль

### frame:
`frame` - создает рамку с текстом в нутри

```python
from tpg import *

print(frame('aaa\naaaa'))
```

аргументы:
- `text` - текст находящийся в рамке
- `x` - X координата рамки, по умолчанию указано -1 и рамка находиться по середине консоли
- `y` - Y координата рамки, по умолчанию указано -1 и рамка находиться по середине консоли
- `text_color` - цвет текста в ansi формате
- `frame_color` - цвет рамки в ansi формате

---

## класс display:

> класс для рисования синволоми в консоли 

функции:

- cursor
- echo
- box
- clear_display
- line
- triangle 
- circle
- multi_line

примеры:

**квадрат/прямоугольник:**
```python
import tpg

disply=tpg.display()

disply.box(5, 5, 2, 2)

disply.echo()

```

параметры:
- `px` - ширина фигуры
- `py` - высота фигуры
- `x` - X координата 1-вого верхнего символа
- `y` - Y координата 1-вого верхнего символа 
- `color` - кортеж с 2 элементами где 0 это началоый ANSI код стоящий перед символом, а 1 элемент это код стоящий после символа 
- `filling` - заполнен ли квадрат


**вывод текста по кординатам:**

```python
import tpg

disply=tpg.display()

disply.cursor(5,5)

disply.echo()

```


**рисовка линий:**

```python
import tpg

disply=tpg.display()

disply.line((2,2), (32,5))

disply.echo()
```

**круги:**

```python
import tpg 

disply=tpg.display()

disply.circle(5, 5, 3)

disply.echo()
```

аргументы:

- `cx` - x координата середины круга 

- `cy` - y координата середины круга 

- `radius` - радиус круга

- `symbol` - синвол круга 

- `full` - толщина круга 

**триульник:**

```python
import tpg

despley=tpg.display()

despley.trigon(10, 6, 5, 5)

despley.echo()
```

аргументы:

- `x` - X координата вершины 

- `y` - Y координата вершины

- `h` - высота квадрата 

- `w` - ширина квадрата (его основания)

- `filling` - заполнен ли треугольник

**соединение точек линией:**

```
import tpg 

display = tpg.display()

display.multi_line([(2,2), (10,10), (2,10), (2,2)])

display.echo()
```

аргументы:
- points(list): список соеденяемых точек где каждый элемент это кортеж с координатой X (нулевой элемент) и Y (первый элемент) 
- color (tuple): цвет символов где 0 элемент это начало ANSI кода (перед символом), а 1 его конец (после символа).
- symbol (str): символ из которого состоит линия.

**примеры программ:**

**вывод 2 прямоугольников (квадратов с задаными свойствами) где в одном находиться текст а другой залит**

```python
import tpg

displu=tpg.display()

displu.box(15, 11, 1, 1,blok='@')

displu.box(15, 11, 22, 1, filling=True)

displu.cursor(3,3 ,symbol='hi')

displu.echo(end='\n')

```

---

## класс logse 

> класс мини логер с разными уровнями логирования и гибкими настройками

```python
import tpg

log=tpg.logse()

log.info("test info")

log.warning("test warning")

log.error("test error")
```

info -1 уровень логирования 

warning -2 уровень логирования 

error -3 уровень логирования

общие для уровнрй аргументы:

- `text` - текст логирования указывющийся после общего патерна(`patern`- обЪект класса log)
- `info_patern` - обозначает тип лога идет после патерна после него идет сам текст 
- `end` - конец строки лога

обекты класса log неободимые для настройки:

- file - хронит названия файла логов
- seve_log_file - будут ли записываться логи в файл
- level - отображаемый уровень логирования. **-1** - не отображаються никаие уровни, **0** - только `info`, **1** - `info` и `warning`, **2** - все уровни логирования( `info`, `warning`, `error`)
- patern - это единая заготовка строки лог файла по умаолчанию содержит дату и время и путь к запущеному файлу
- path_save_log - путь к дериктории в которой будет сохроняться лог файл, если равен None то сохронение происходит в тикущий деректорий файла

**вот как он выглядит:**

![hippo](doc/log_test.png)








