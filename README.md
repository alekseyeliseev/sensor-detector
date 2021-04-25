# sensor-detector

## Уcтановка 
### Создание виртуального окружения
`python3 -m venv venv`

`source venv/bin/activate`

### Установка зависимостей
`pip install -r requirements.txt`

### Запуск приложения
`uvicorn main:app --reload --host 0.0.0.0 --port 5000`

### Тестирование
` curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@img.jpg" http://localhost:5000/prediction/`

## Уcтановка в контейнере
`docker pull python

docker run -it -p 5000:5000 --name sensor-detector python bash

cd ~

git clone  https://github.com/alekseyeliseev/sensor-detector.git

cd sensor-detector

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

apt-get update

apt-get install ffmpeg libsm6 libxext6  -y

uvicorn main:app --reload --host 0.0.0.0 --port 5000`


