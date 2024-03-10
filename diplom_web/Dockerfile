FROM tiangolo/uwsgi-nginx-flask:python3.11
ENV NAME="Metalin37" 
# Копируем содержимое папки ./app в рабочую директорию контейнера
COPY ./app ./
# Копируем файл requirements.txt в рабочую директорию контейнера
COPY ./requirements.txt ./
# Копируем файл uwsgi.ini в рабочую директорию контейнера
COPY ./uwsgi.ini ./
# Запускаем установку необходимых зависимостей
RUN pip install -r requirements.txt
