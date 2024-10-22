# Запуск приложения
## Создание venv
1. py -m venv venv
2. 1. source ./venv/Scripts/activate - для windows
2. 2. source ./venv/bin/activate - для linux
3. pip install poetry
4. poetry install
5. Создание в директории проекта файл .env
6. Содержимое файла .env: APP_CONF__DB__URL = postgresql+asyncpg://Arseniy:12345@127.0.0.1:5434/my_chat
7. docker-compose up
8. alembic upgrade head
9. py main.py
10. Перейти по сслыке в браузере: http://localhost:8000/login

# Пользователи для логина в системе
Nick: ars, pass: 123
Nick: pit, pass: 1234
Nick: ivan, pass: 321