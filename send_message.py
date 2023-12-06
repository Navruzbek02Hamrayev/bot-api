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
btn2 = {'text': 'button 2'}
btn3 = {'text': 'button 3'}

reply_markup = {
    "keyboard": [
        [btn1, btn2],
        [btn3]
    ]
}

send_message(chat_id=chat_id, text='ok', reply_markup=reply_markup)