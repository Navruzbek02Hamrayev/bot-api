from settings import TOKEN
import requests



def send_contact(chat_id, numer, fname, lname=None):
    url = f'https://api.telegram.org/bot{TOKEN}/sendContact'
    payload = {
        "chat_id": chat_id,
        "phone_number": numer,
        "first_name": fname,
    }
    if lname:
        payload['last_name'] = lname

    requests.post(url, params=payload)
    

send_contact('1258594598', '+998883277733', 'Diyorbek', 'Jumanov')
