import pyautogui
import time
import random
import pygetwindow as gw

def read_messages_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        messages = file.readlines()
    # Убираем лишние пробелы и пустые строки
    messages = [message.strip() for message in messages if message.strip()]
    return messages

messages = read_messages_from_file('messages21.txt')

def switch_to_discord():
    """Переключается на окно браузера с Discord."""
    for window in gw.getWindowsWithTitle("Discord"):
        if window.isMinimized:  
            window.restore()
        window.activate()
        time.sleep(1)  # Даем время активироваться
        return True
    print("⚠️ Discord не найдено!")
    return False

time.sleep(3)  # Даем время переключиться вручную, если нужноo

while True:
    if switch_to_discord():  # Если нашли окно Discord
        message = random.choice(messages)  # Выбираем случайное сообщение
        pyautogui.write(message)  # Вводим в поле ввода
        pyautogui.press("enter")  # Отправляем
        delay = random.randint(65, 85)  # Выбираем случайную задержку
        print(f"Отправлено: {message} | Следующее через {delay} сек.")
        time.sleep(delay)  # Ждём перед следующим сообщением
    else:
        print("⏳ Ожидание, пока появится окно Discord...")
        time.sleep(15)  # Проверяем снова через 10 секунд
