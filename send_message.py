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

btn1 = {'text': 'button 1'}
btn2 = {
    'text': 'share location',
    'request_location': True
}
btn3 = {
    'text': 'share contact',
    'request_contact': True
}

reply_markup = {
    "keyboard": [
        [btn1, btn2],
        [btn3]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

send_message(chat_id=chat_id, text='ok', reply_markup=reply_markup)