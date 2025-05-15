TPG - terminal python graphics (UI)<br>
небольшая библиотека для создания графических интерфейсов 
в функционал библиотеки входят :
- списки
- упрощеная работа с цветами (ANSI)
- упровление курсором кансоли
- меню выбора (да/нет)
- настройки с потдержкой json
примеры и базовый функционал

```python
from tpg import *
out_point=listgr(['point1','point2','point3'])
print(out_point)
```

аргументы:<br>
kastor - парамитер отвечающий за курсор стоящий перед выброным пунктом (по умолчанию '>')<br>
title - текст над списком <br>
style - стиль по умолчанию 'standart' другие 'scob'<br>
как это выгледит
![hippo](doc/list_test.gif)

```python 
from tpg import * #inport lib

out=settings({'point1':true,'point2':false}) # change dict
print(out) # print new dict from json file

out=settings({},jsonf='test_json.json')# read and write json file 

print(out) # print new dict 

```
в 1 случае в функцию был передан словарь он может быть с любыми ключами и их количеством но  
значения должно быть true или false функция вернет обновлённый словарь измененый пользователем<br><br>
во 2 случае словарь извлекается из json файла его име указывается в аргументе `jsonf` после пользовательских изменений json файл будет изменен а функция вернёт словарь с изменёнными данными из json 