Дано Файл operations.json - файл со списком операций, совершенных клиентом разное время. Файл в формате json. По каждой операции есть:

date - информация о дате совершения операции
state - статус перевода (EXECUTED - выполнена, CANCELED - отменена)
operationAmount - сумма операции и валюта
description - описание типа перевода
from - откуда
to - куда
Задача
- Вывести на экран список из 5 последних совершенных (выполненных) операций клиента в
формате:
Дата перевода Описание перевода
Откуда Куда
Сумма перевода Валюта

Пример для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
Условия
решение должно представлять из себя скрипт на языке python
вывести последние 5 выполенных (EXECUTED) операций на экран
операции разделены пустой строкой
дата перевода должна быть в формате ДД.ММ.ГГГГ (пример 14.10.2018)
сверху списка должны быть самые последние операции (по дате)
номер карты должен маскироваться и не отображаться целиком, в формате XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом)
номер счета должен маскироваться и не отображаться целиком, в формате **XXXX (видны только последние 4 цифры номера счета)
Комментарий - все данные и операции сгенерированы и не имеют ничего общего с реальными счетами
