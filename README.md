# sensor-detector

## Создание виртуального оукружения
`python3 -m venv venv`

## Установка зависимостей
`pip install -r requirements.txt`

## Запуск приложения
`uvicorn main:app --reload --host 0.0.0.0 --port 5000`

## Тестирование
` curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@img.jpg" http://localhost:8000/prediction/`
