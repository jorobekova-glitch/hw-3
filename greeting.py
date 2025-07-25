from datetime import datetime

def get_greeting(name):
    current_hour = datetime.now().hour

    if 6 <= current_hour < 12:
        greeting = "Доброе утро"
    elif 12 <= current_hour < 18:
        greeting = "Добрый день"
    elif 18 <= current_hour < 24:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    return f"{greeting}, {name}!"

user_name = input("Введите ваше имя: ")
print(get_greeting(user_name))

