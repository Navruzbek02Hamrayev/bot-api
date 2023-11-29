from settings import TOKEN
import requests



def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    requests.get(url, params=payload)

# send_message('1258594598', 'hi')
