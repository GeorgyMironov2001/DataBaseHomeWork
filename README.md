
LMDB - это библиотека, реализующая самый нижний основополагающий слой баз данных — хранилище.

a) это модификация Berkeley DB. Его разработчик Говард Чу из комапании OpenLDAP, вот.

Основные идеи

1 - На диске лежит файл, он отображается в нашу память и мы с ним работаем

2 - key value - Набор функций среди которых:

    Вставка элемента
                                                
    Поиск элемента с заданным ключом
                                             
    Удаление элемента
                                             
    Итерирование по интервалам ключей в порядке их сортировки
    
 Я буду пользоваться реализацией этой библиотеки для python, но изначально она была написана на C
 
 Как взаимодействовать с библиотекой?
 
 1) Есть объект Environment class, он отвечает за общее окружения баз данных
 2) Есть объект Transaction class, это основной метод взаимодействия с базами данных, он создается из Environment class, по умолчанию транзакция привязывается к основной базе данных. Есть методы put, get, delete, commit, abort и т.д, Примеры операций можно найти в test.py
 3) Database class - создается из транзакций, чтобы взаимодействовать с ним нужно привязать к нему транзакцию и работать с этой транзакцией.

Методы восстановления:
    В каждый момент времени поддерживается B+ дерево. Его корни это корни баз данных, с которыми взаимодействуют какие-то транзакции и в каждый момент времени есть валидная версия корня базы данных. Когда происходит транзакция на изменение данных, то происходит следующее:
1) находим корень соответсвующий нужной базе данных
2) вершины на пути от корня до элемента изменения копируются и в них происходит изменение
3) При завершении транзакции и при условии, что старые узлы никто не просматривает, старые узлы удаляются.

Таким образом если происходит ошибка во время транзакции, то мы не портим наши данные.

В файле test.py происходит следующее:
1) в базу данных загружается элемент
2) заводятся 2 новые транзакции на запись и на чтение
3) 1 из них удаляет элемент и завершается, 2 не завершается
4) открывается 3 транзакция на чтение, которая проверяет, что в базе данных нет элемента
5) Но в то же время 2 транзакция видит элемент



Документация и полезные ссылки

https://lmdb.readthedocs.io/en/release/# - документация 

https://habr.com/ru/company/vk/blog/480850/

        
