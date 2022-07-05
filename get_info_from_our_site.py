import requests

url = 'http://localhost:8000/api/posts/'  # Полный адрес эндпоинта
response = requests.get(url)  # Делаем GET-запрос
# Поскольку данные пришли в формате json, переведем их в python
response_on_python = response.json()
# Запишем полученные данные в файл capitals.txt
with open('posts.txt', 'w') as file:
    for messagi in response_on_python:
        file.write(
            f"What's about titling? {messagi['title']} is "
            f"What's about texting? {messagi['text']}, "
            f"What's about publishdating? {messagi['published_date']}, "
            f"What's about authoring? - {messagi['author']}\n"
        )