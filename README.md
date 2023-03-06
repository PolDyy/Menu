# Menu

______________________

## Запуск проекта

1) Клонировать репозиторий и перейти в него в командной строке:
`git init`

`git clone https://github.com/PolDyy/Menu.git`

2) Cоздать и активировать виртуальное окружение в корне проекта:

`python -m venv venv`

`source venv/Scripts/activate` или `source venv/bin/activate`

3) Переходим в директорию Uptrader:

`cd Menu/Uptrader/`

4) Установить зависимости:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

5) Создаем файл .env с секретным ключом

6) Выполнить миграции:

`python manage.py makemigrations`

`python manage.py migrate`

7) Запустить сервер:

`python manage.py runserver`

## База данных 

При необходимости изменить или просмотреть базу данных необходимо использовать 
уже созданного суперюзерa:\n
логин: admin\n
пароль: admin\n

## При добавлении 
новых пунктов меню нехобходимо соблюсти следющие требования:

1) поле path должно содержать элементы поле path родительского элемента пути и не пересекаться с уже созданными полями. Например
предок: path = 01; потомок 1: path = 0101;  потомок 2: path = 0102;
2) поле depth  должно равняться шлубине вложенности элемента.
