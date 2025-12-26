@echo off
echo ========================================
echo Password Complexity Checker - Docker
echo ========================================

:menu
echo.
echo Выберите действие:
echo 1. Собрать Docker-образ
echo 2. Запустить контейнер
echo 3. Остановить контейнер
echo 4. Показать логи
echo 5. Тестировать API
echo 6. Выход
echo.

set /p choice="Ваш выбор (1-6): "

if "%choice%"=="1" goto build
if "%choice%"=="2" goto up
if "%choice%"=="3" goto down
if "%choice%"=="4" goto logs
if "%choice%"=="5" goto test
if "%choice%"=="6" goto exit

echo Неверный выбор!
goto menu

:build
echo Собираем Docker-образ...
docker build -t password-checker .
goto menu

:up
echo Запускаем контейнер...
docker-compose up -d
echo Контейнер запущен: http://localhost:8000
goto menu

:down
echo Останавливаем контейнер...
docker-compose down
goto menu

:logs
echo Показываем логи...
docker-compose logs -f
goto menu

:test
echo Тестируем API...
python test_docker.py
goto menu

:exit
echo Выход...
pause