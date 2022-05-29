# Портал для VR/AR трека Hack iN Home 2022

Команда Ave VR

## Запуск

### Создание окружения

```
// Если нет модуля venv
sudo apt-get install python3-venv

python3 -m venv env
source env/bin/activate
```

### Установка модулей в окружение

```
pip3 install -r requirements.txt
```

### Запуск портала

> Не забыть пробросить порты наружу

```
// через screen, чтобы отвязаться от сессии
screen -S AVEVR-Portal python3 main.py
```

либо если просто открыть

```
python3 main.py
```
