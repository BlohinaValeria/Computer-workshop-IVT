# Лабораторная работа по теме №20 

## Задание: 
Необходимо придумать и написать код с собственной реализацией паттерна Singleton, где присутствует многопоточность. В комментарии к коду требуется обосновать актуальность использования данного паттерна для этой задачи.

# Код программы
```python
import concurrent.futures
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()  # Блокировка для синхронизации потоков

    def __new__(cls, *args, **kwargs):
        with cls._lock:  
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

def calculate_square(number):
    print(f"Вычисляю квадрат {number} в потоке {threading.current_thread().name}")
    return number * number

numbers = [1, 2, 3, 4, 5]

# Создаём ThreadPoolExecutor с 3 потоками
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(calculate_square, numbers))

print("Результаты:", results)
```
# Результат программы
![](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%2020/result%20LR%2020.png)
