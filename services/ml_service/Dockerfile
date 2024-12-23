FROM python:3.12-slim

# Скопировать содержимое текущей директории в директорию /ml_service в контейнере
COPY . /ml_service

# Доступ к директории /models снаружи контейнера
VOLUME /models

# Сделать /ml_service рабочей директорией
WORKDIR /ml_service

# Установка всех зависимостей из файла requirements.txt
RUN pip install -r requirements.txt

# Порт 8000 - доступ снаружи контейнера
EXPOSE 8000

# Rоманда запускf сервера, следует явно указать адрес хоста "0.0.0.0" и порта "8000", где будет запускаться сервер.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]

# docker build . --tag score_model:1
# docker run -p 8001:8000 -v $(pwd)/../models:/models score_model:1