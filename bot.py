import requests

# Твої дані з останніх скріншотів
TOKEN = "8635960397:AAGZJAPwCIXZ02iWJd0r5YxZlqEuKR0W5Cc"
CHAT_ID = "913214131"

def check():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # 1. Спробуємо спочатку просто привітатися
    print(f"Намагаюся написати на ID: {CHAT_ID}")
    
    payload = {
        "chat_id": CHAT_ID,
        "text": "Привіт! Якщо ти це бачиш — зв'язок налаштовано! 🎉"
    }
    
    try:
        r = requests.post(url, json=payload, timeout=10)
        print(f"Статус відповіді Telegram: {r.status_code}")
        print(f"Що каже Telegram: {r.text}")
        
        if r.status_code != 200:
            print("❌ Telegram відхилив повідомлення!")
    except Exception as e:
        print(f"❌ Помилка мережі: {e}")

if __name__ == "__main__":
    check()
