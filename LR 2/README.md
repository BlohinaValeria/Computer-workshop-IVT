# Лабораторная работа №2. Тема 2 - Сборка сайта с помощью Node, npm, yarn, SASS

## План работы:

1.  Изучение материалов по сборке сайта с использованием Node, npm, yarn, SASS.
2.  Создание собственного кастомного дизайна сайта (пример: сайт-портфолио) с использованием Bootstrap (или Bulma, Tailwind).
3.  Подготовка отчета в виде текстового документа с демонстрацией результатов выполнения (скриншоты, скринкаст).

## Выполнение работы:
На основе шаблона сайта «Котопес» разработан собственный сайт «Сайт-портфолио», используя подход webpack.

Пример содержимого файла `index.html`:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Демо портфолио</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUalbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <header>
            <h1 class="text-center">Портфолио Блохиной В.С</h1>
            <hr>
            <figure class="text-center">
                <small class="text-center">
                    <em>Сайт-портфолио студентки 2 курса РГПУ им. А.И. Герцена</em>
                </small>
            </figure>
        </header>

        <div class="row">
            <div class="col col-sm-12 col-xs-12 col-md-12 col-lg-6">
                <h2>Карта</h2>
                <p>191186, Санкт-Петербург, набережная реки Мойки 48</p>
                <div id="map">
                    <script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A126f3b1a77e0307ba1d45ae2c8e3381b2770ed331dd611f574bb08613a08d27d&amp;width=500&amp;height=320&amp;lang=ru_RU&amp;scroll=true"></script>
                </div>
            </div>

            <div class="col col-sm-12 col-xs-12 col-md-12 col-lg-6">
                <h2>Важная информация</h2>
                <img src="" style="width:200px" class="img-fluid" alt="котопес">
                <figure>
                    <blockquote class="blockquote">
                        <p class="lead">
                            «Компьютеры — это как велосипед. Только для нашего сознания»
                        </p>
                    </blockquote>
                    <figcaption class="blockquote-footer">
                        Стив Джобс
                    </figcaption>
                </figure>
                <ul class="list-unstyled">
                    <li><u><mark>Об образовании</mark></u></li>
                    <li><strong>Уровень образования:</strong>бакалавриат</li>
                    <li><strong>Направление:</strong>09.03.01 Информатика и вычислительная техника</li>
                    <li><strong>Hаправленность (профиль):</strong>Технологии разработки программного обеспечения и обработки больших данных</li>
                    <li>
                    <li><u><mark>Первое образование</mark></u></li>
                    <ul>
                        <li>Образовательное учереждение: Некрасовский педагогический колледж № 1</li>
                        <li>Специальность: 44.02.02 Преподавание в начальных классах</li>
                        <li>Год окончания: 2023 г</li>
                    </ul>
                    </li>
                </ul>
            </div>
        </div>

        <div class="row-mt-5">
            <div class="col text-center">
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal0order">
                    Перейти в портфолио
                </button>
            </div>
        </div>
    </div>

    <footer>
        <hr>
        <p class="" small>(C) Блохина В.С портфолио</p>
    </footer>

    <div class="modal fade" id="modal0order" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Работы представлены по ссылке</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
                </div>
                <div class="modal-body">
                    Тут должна быть ссылка
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68Sly3Te4Bkz" crossorigin="anonymous"></script>
</body>
</html>
```
## Итоговый сайт:
![]()
