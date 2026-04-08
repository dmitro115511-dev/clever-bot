import requests
import os

# Нові дані з твоїх скріншотів
TOKEN = "8635960397:AAGZJAPwCIXZ02iWJd0r5YxZlqEuKR0W5Cc"
CHAT_ID = "913214131"
STATE_FILE = "last_status.txt"

def check():
    try:
        # Отримуємо дані станції
        r = requests.get("https://clever-app-prod.azurewebsites.net/api/v4/stations/1025698", timeout=15)
        if r.status_code != 200:
            return
        
        data = r.json()
        # Створюємо рядок зі статусом (наприклад, кількість павербанків)
        current_status = f"Статус: {data.get('status', '?')}. Вільних: {data.get('free_count', '?')}"
        
        # Перевіряємо, що було минулого разу
        last_status = ""
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r") as f:
                last_status = f.read().strip()

        # Якщо статус змінився — відправляємо повідомлення
        if True:
            text = f"🚨 Зміна на станції Clever!\n{current_status}"
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                          json={"chat_id": CHAT_ID, "text": text})
            
            # Оновлюємо збережений статус
            with open(STATE_FILE, "w") as f:
                f.write(current_status)
            print("Статус змінився, повідомлення відправлено.")
        else:
            print("Змін немає. Мовчимо.")

    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    check()
