import requests

TOKEN = "8635960397:AAGZJAPwCIXZ02iWJd0r5YxZlqEuKR0W5Cc"
CHAT_ID = "913214131"

def check():
    print("Запуск перевірки...")
    try:
        # Робимо запит до Clever
        r_clever = requests.get("https://clever-app-prod.azurewebsites.net/api/v4/stations/1025698", timeout=10)
        status_text = "Станція доступна" if r_clever.status_code == 200 else "Помилка Clever"
        
        # Спроба відправити в Telegram
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": f"✅ Тест зв'язку!\nСтатус: {status_text}"}
        
        r_tg = requests.post(url, json=payload)
        
        print(f"Відповідь Telegram: {r_tg.status_code}")
        print(f"Текст відповіді: {r_tg.text}")
        
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    check()
