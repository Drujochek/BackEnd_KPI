# Лабораторна робота №1 Налаштування середовища. Розробка базового REST API

ФІОТ ІО-01

Тарасюк Юрій Васильович

Номер у списку групи 26

Посилання на задеплоєний застосунок:

https://devserversoft.herokuapp.com/records - записи

https://devserversoft.herokuapp.com/users - користувачі

https://devserversoft.herokuapp.com/categories - категорії

Для запуску проетка локально із використанням Python , потрібно виконати наступні команди 

set FLASK_APP=projectfiles (якщо використовувати Unix подібні системи замість "set" потрібно вказати "export")

flask run

Для запуску проетка локально із використанням Docker , потрібно виконати наступні команди 

docker build --build-arg PORT=5005 . -t <image_name>:latest

docker-compose build

docker-compose -up
