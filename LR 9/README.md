# Лабораторная работа по теме №9 Объектное хранилище S3. Yandex Object Storage

## Задание 
1. Изучите материалы по ссылкам, которые размещены в теме.
2. Создайте бакет (хранилище) в Yandex Cloud.
3. Создайте сервисный аккаунт (Identity and Access Management).
:heavy_exclamation_mark: Важно: Не забудьте сохранить секретный ключ, он нужен для подключения приложения к хранилищу.
Реализуйте функции (локально) для выполнения основных операций с объектами в хранилище: получение списка загруженных файлов, загрузка файла в бакет, получение файла, удаление файла. Продемонстрируйте их работу.

:heavy_exclamation_mark: ВНИМАНИЕ: Используйте стандартное хранилище, чтобы Yandex Cloud не списывал оплату! В бесплатный уровень использования входит хранение 1 ГБ и первые 1000 или 10000 операций в зависимости от типа. Вы можете выбрать любой язык программирования и библиотеку для работы с S3 Storage. Например, можно использовать Python и boto3.

:small_red_triangle: Дополнительное задание (по желанию). Запустите MinIO Server локально. Запустите подготовленную программу, заменив аутентификационные Yandex Object Storage на данные MinIO. Покажите работу функций создания файла и получения списка файлов выбранного бакета.
Подготовьте отчёт, который включает описание действий и скриншоты с результатами выполнения.

:heavy_exclamation_mark: Важно: отчёт не должен содержать секретные ключи.
Рекомендуется хранить данные в ~/.aws/credentials (если используется boto3) или в переменных окружения. Подробнее см. в документации Yandex Cloud, в разделе Настройка > Локально.
Для использования стандартного хранилища часто необходимо менять тип из примеров кода, например: https://yandex.cloud/ru/docs/storage/tools/boto.

s3.put_object(Bucket='bucket-name', Key='object_name', Body='TEST', StorageClass='STANDARD')

# Код программы
  ```python
import boto3
import os
from botocore.exceptions import NoCredentialsError, ClientError

# Настройки Yandex Cloud S3
ENDPOINT_URL = "https://storage.yandexcloud.net"
BUCKET_NAME = "buckettt" # Ваше название бакета
TEST_FILE = "test.txt"

# Инициализация клиента (ключи берутся автоматически из ~/.aws/credentials)
s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT_URL
)


def create_test_file():
    """Создает тестовый файл, если он не существует"""
    if not os.path.exists(TEST_FILE):
        with open(TEST_FILE, 'w') as f:
            f.write("Тестовое содержимое файла")
        print(f"Создан тестовый файл {TEST_FILE}")


def list_files():
    """Получение списка файлов в бакете"""
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if "Contents" in response:
            print("\nСодержимое бакета:")
            for obj in response["Contents"]:
                print(f"- {obj['Key']} (размер: {obj['Size']} байт)")
        else:
            print("\nБакет пуст.")
    except NoCredentialsError:
        print("Ошибка аутентификации. Проверьте ключи.")
    except ClientError as e:
        print(f"Ошибка при доступе к бакету: {e}")


def upload_file(file_path, object_name):
    """Загрузка файла в бакет"""
    try:
        if not os.path.exists(file_path):
            print(f"Ошибка: файл {file_path} не найден")
            return False

        s3.upload_file(
            file_path,
            BUCKET_NAME,
            object_name,
            ExtraArgs={"StorageClass": "STANDARD"},
        )
        print(f"\nФайл {object_name} успешно загружен.")
        return True
    except NoCredentialsError:
        print("Ошибка аутентификации.")
        return False
    except ClientError as e:
        print(f"Ошибка загрузки: {e}")
        return False


def download_file(object_name, output_path):
    """Скачивание файла"""
    try:
        s3.download_file(BUCKET_NAME, object_name, output_path)
        print(f"\nФайл {object_name} скачан в {output_path}.")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            print(f"\nФайл {object_name} не найден в бакете")
        else:
            print(f"\nОшибка скачивания: {e}")
        return False


def delete_file(object_name):
    """Удаление файла"""
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=object_name)
        print(f"\nФайл {object_name} удалён.")
        return True
    except ClientError as e:
        print(f"\nОшибка удаления: {e}")
        return False


if __name__ == "__main__":
    # 1. Создаем тестовый файл
    create_test_file()

    # 2. Показываем начальное состояние бакета
    print("Начальное состояние бакета:")
    list_files()

    # 3. Загружаем файл
    object_name = "test-file.txt"
    if upload_file(TEST_FILE, object_name):
        # 4. Показываем содержимое после загрузки
        print("\nПосле загрузки:")
        list_files()

        # 5. Скачиваем файл
        downloaded_file = "downloaded.txt"
        if download_file(object_name, downloaded_file):
            print(f"Файл успешно сохранен локально как {downloaded_file}")

            # 6. Удаляем файл из бакета
            if delete_file(object_name):
                # 7. Показываем финальное состояние
                print("\nФинальное состояние бакета:")
                list_files()
  ```
# Создание ключа 
![скриншот](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%209/LAB.png)

# Создание в бакете
![пост запрос](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%209/bucket1.png)
  
# Отображение в бакете
![пост запрос](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%209/bucket2.png)

# Удаление в бакете программа 
![пост запрос](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%209/bucket3.png)

# Отображение в бакете 
![пост запрос](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%209/bucket4.png)


