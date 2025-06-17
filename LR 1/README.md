# Лабораторная работа 1. Тема 1 - Статическийсайт. GitHub Pages. Hugo. 

1. В рамках развертывания статического сайта с помощью Hugo
2. Установка Hugo
3. Установка темы Blowfish
4. Редактирование сайта:
:small_red_triangle: Добавление раздела «Обо мне»
:small_red_triangle: Дизайн сайта
:small_red_triangle: Добавление ссылки на github
5. Развертывание на GitHub Pages сайта на Hugo с помощьюYAMLскрипта в GitHub Actions.

## Ссылка на сайт:
[перейти](https://blohinavaleria.github.io/web-portfolio/)

## Задание: скрипт для развертывания Hugo с помощью GitHubActions.
```
# Sample workflow for building and deploying a Hugo site to GitHubPages
name: Deploy Hugo site to Pages
on:
# Runs on pushes targeting the default branch
push:
branches: ["main"]
# Allows you to run this workflow manually from the Actions tabworkflow_dispatch:
# Sets permissions of the GITHUB_TOKEN to allow deployment toGitHub Pages
permissions:
contents: read
pages: write
id-token: write
# Allow only one concurrent deployment, skipping runs queued betweenthe run in-progress and latest queued. # However, do NOT cancel in-progress runs as we want to allowtheseproduction deployments to complete. concurrency:
group: "pages" cancel-in-progress: false
# Default to bash
defaults:
run:
shell: bash
jobs:
# Build job
build:
runs-on: ubuntu-latest
env:
HUGO_VERSION: 0.128.0
steps: - name: Install Hugo CLI
run: |
wget -O ${{ runner.temp }}/hugo.deb
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSI
ON}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \
&& sudo dpkg -i ${{ runner.temp }}/hugo.deb
- name: Install Dart Sass
run: sudo snap install dart-sass
- name: Checkout
uses: actions/checkout@v4
with:
submodules: recursive
- name: Setup Pages
id: pages
uses: actions/configure-pages@v5
- name: Install Node.js dependencies
run: "[[ -f package-lock.json || -f npm-shrinkwrap.json ]] &&npmci
|| true"
- name: Build with Hugo
env:
HUGO_CACHEDIR: ${{ runner.temp }}/hugo_cache
HUGO_ENVIRONMENT: production
run: |
hugo \ --minify \ --baseURL "${{ steps.pages.outputs.base_url }}/"
- name: Upload artifact
uses: actions/upload-pages-artifact@v3
with:
path: ./public
# Deployment job
deploy:
environment:
name: github-pages
url: ${{ steps.deployment.outputs.page_url }}
runs-on: ubuntu-latest
needs: build
steps: - name: Deploy to GitHub Pages
id: deployment
uses: actions/deploy-pages@v4
```

## Описание скрипта:
1. Триггеры (on): Запускается при отправке изменений в основную ветку (main) или вручную через веб-интерфейс.
2. Разрешения (permissions): Дает workflow права на чтениеконтента репозитория и запись на GitHub Pages.
3. Параллельность (concurrency): Позволяет только одномуразвертыванию за раз, но не отменяет текущее развертывание.
4. Работа со сборкой (build job):
   :wavy_dash: Окружение (env): Определяет версию Hugo для использования.
   :wavy_dash: Установка Hugo: Скачивает и устанавливает HugoCLI (Command Line Interface).
   :wavy_dash: Установка Dart Sass: Устанавливает Dart Sass (используется для обработки CSS).
   :wavy_dash: Извлечение кода (Checkout): Извлекает исходныйкодсайта, включая подмодули (например, темы).
   :wavy_dash: Настройка Pages (Setup Pages): Настраивает GitHubPages.
   :wavy_dash: Установка Node.js зависимостей (Install Node.js dependencies): Устанавливает зависимости Node.js, еслиони есть.
   :wavy_dash: Сборка с Hugo (Build with Hugo): запускает Hugo для сборки сайта с оптимизацией(--minify) и указанием базового URL.
   :wavy_dash: Загрузка артефакта (Upload artifact): Загружает сгенерированный сайт (из папки public) в качестве артефакта.
   :wavy_dash: Работа с развертыванием (deploy job):
   :heavy_minus_sign: Окружение (environment): Определяет окружение GitHub Pages и URL сайта.
   :heavy_minus_sign: Зависимость (needs): Зависит от успешного завершениязадачи build.
   :heavy_minus_sign: Развертывание на GitHub Pages (Deploy to GitHubPages): Развертывает артефакт на GitHub Pages.
