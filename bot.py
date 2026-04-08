import requests

TOKEN = "8635960397:AAGZJAPwCIXZ02iWJd0r5YxZlqEuKR0W5Cc"
CHAT_ID = "913214131"

def test():
    # Просто відправляємо текст без усяких перевірок станцій
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, json={"chat_id": CHAT_ID, "text": "ПЕРЕВІРКА: Бот працює!"})
    print(f"Статус відправки: {r.status_code}")
    print(f"Відповідь Telegram: {r.text}")

if __name__ == "__main__":
    test()
