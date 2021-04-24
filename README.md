# sensor-detector

## Создание виртуального окружения
`python3 -m venv venv`

`source venv/bin/activate`

## Установка зависимостей
`pip install -r requirements.txt`

## Запуск приложения
`uvicorn main:app --reload --host 0.0.0.0 --port 5000`

## Тестирование
` curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@img.jpg" http://localhost:5000/prediction/`
