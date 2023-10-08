## Dungeon-wars-editor

Редактор уровней для игры [dungeon-wars](https://github.com/Araime/dungeon-wars).


## Что реализовано:
Создание новых и редактирование существующих уровней.  
!!! Для доступа к существующим уровням необходимо папку levels из игры
положить в корень репозитория.

![img](img.png)

## Установка

### Скачать

Python3 должен быть уже установлен.
[Скачать](https://github.com/Araime/dungeon-wars-editor/archive/master.zip) этот 
репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начиная с Python версии 3.3, виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```sh
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбранном каталоге.
```sh
Python -m venv env
```
В репозитории появится папка виртуального окружения env  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```sh
env\scripts\activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/MZ72r22/2.png" alt="2" border="0"></a>

#### Установить зависимости

Используйте `pip` для установки 
зависимостей:

```sh
pip install -r requirements.txt
```

### Запуск

```sh
python main.py
```

## Credits

hero - leoz lk  
cherry, gem, background - Luis Zuno  
weapons - 0x72
dungeon tiles - Rostislav Gnatovsky, Szadi, 0x72  
water, fly decor - finalbossblues  

## Цель проекта

Данный репозиторий создан с целью изучения возможности создания игр
на Python.
