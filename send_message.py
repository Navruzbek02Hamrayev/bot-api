from settings import TOKEN, chat_id
import requests



def send_message(chat_id, text, reply_markup):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        "chat_id": chat_id,
        "text": text,
        'reply_markup': reply_markup
    }
    requests.post(url, json=payload)

btn1 = {
    'text': 'go google',
    'url': 'http://google.com'
}
btn2 = {
    'text': 'go channel',
    'url': 'https://t.me/naxalov'
}

reply_markup = {
    "inline_keyboard": [
        [btn1, btn2]
    ],
}

send_message(chat_id=chat_id, text='inline keyboard', reply_markup=reply_markup)
