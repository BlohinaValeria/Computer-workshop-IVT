# Тема 4 Основы работы с SoapUI - REST сервисы

## Задание 
Создайте проект с применением открытых публичных REST сервисов. Придумайте любой бизнес-процесс на их основе (последовательность действий) и реализуйте его тестирование в SoapUI - создайте TestCase.

# Проект: Проверка факта о кошках (Cat Facts Service)

:heavy_exclamation_mark: _Последовательность действий_

1. Отправка запроса: Отправляем GET запрос к Cat Facts Service.
2. Получение ответа: Получаем JSON-ответ, содержащий случайный факт о кошках.
3. Проверка структуры ответа: проверяем, содержит ли ответ поле «факт».
4. Проверка факта (содержит слово “cat”): проверяем, что поле “fact” содержит слово “cat” (или любую другую подстроку).

:heavy_exclamation_mark: Используемые сервисы:
- [ ] _Cat Facts Service:_ бесплатный публичный REST-сервис, возвращающий случайный факт о кошках.
- [ ] URL -адрес: https://catfact.ninja/fact


+ Создание проекта в SoapUI: 
![создание](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/название%20и%20создание.png)

+ Создайте Resource:
![resource](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/url.png)

+ TestSuit:
![suit](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/test%20suite.png)

+ TestCase
![case](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/test%20case.png)

+ Rest Request 
![restrequest](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/rest%20request.png)

+ Проверка Rest Request step 1
![проверка](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/проверка_json_ответ.png)

+ Проверка Rest Request step 2
![проверка2](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/проверка_2_шаг.png)

# Результат: 
![итог](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/итог.png)
