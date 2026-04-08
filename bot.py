import requests

# Твій токен зі скріншоту
TOKEN = "8604060417:AAEHgQExyUHp-feyosGhBrAHzey1XHZlmHKU"
# Твій ID
CHAT_ID = "913214131"

def check():
    try:
        # Запит до станції Clever
        r = requests.get("https://clever-app-prod.azurewebsites.net/api/v4/stations/1025698", timeout=15)
        
        if r.status_code == 200:
            data = r.json()
            # Отримуємо статус (чи є вільні павербанки)
            status = data.get("status", "Невідомо")
            text = f"Статус станції Clever: {status}"
        else:
            text = f"Помилка сайту Clever: {r.status_code}"
            
        # Відправка в Telegram
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": text})
        print("Повідомлення відправлено!")

    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    check()
