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

как это выгледит
![hippo](doc/list_test.gif)

```python 
from tpg import * #inport lib

out=settings({'point1':true,'point2':false}) # change dict
p

out=settings({},jsonf='test_json.json')# read and write json file 

print(out) # print new dict 

```
в 1 случее в функцию был передан словарь он может быть с любыми ключами и их количеством но  
значения должно быть true или false функция вернет обновлённый словарь измененый пользователем