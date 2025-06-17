# Лабораторная работа №3. Тема №3 Протокол HTTP. Клиент-серверное взаимодействие

### 1. Отправка GET и POST запросов с помощью Telnet или netcat

Были отправлены GET и POST запросы к веб-ресурсу [meowfacts API](https://meowfacts.herokuapp.com/).

Пример GET запроса:
![get](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%203/GET_number%201.png)

Пример POST запроса:
![post](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%203/POST_number%201.png)

### 2. Отправка запросов с помощью CURL

Были отправлены GET и POST запросы к веб-ресурсу [meowfacts API](https://meowfacts.herokuapp.com/) с использованием утилиты CURL.

Пример GET запроса:
![get](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%203/GET_number%202.png)

Пример POST запроса:
![post](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%203/POST_number%202.png)

### 3. Использование Insomnia, Postman или HTTPie Desktop
Была использована программа Insomnia для отправки GET запроса к API Банка России для получения курса валют.

Пример GET запроса к API Банка России:
![](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%203/INSOMNIA.png)

### 4. Создание простого чата с использованием netcat
Запущены два процесса netcat: сервер и клиент. Сервер принимает входящие соединения на порту 12345, а клиент подключается к localhost на этот же порт.

Команда для запуска сервера:
```
ncat -l -p 12345
```

Команда для запуска клиента:
```
ncat localhost 12345
````

Реализация: 
![](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%203/netcat.png)
