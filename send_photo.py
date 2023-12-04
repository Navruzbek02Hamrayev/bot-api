from settings import TOKEN
import requests



def send_photo(chat_id, photo):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        "chat_id": chat_id,
        "photo": photo
    }
    requests.post(url, params=payload)

photo = 'AgACAgIAAxkBAANhZW1eWzpqrbpqaijXnRyMEyOBxocAAkLSMRsw22hLDk6nUI0jdmgBAAMCAAN5AAMzBA'
send_photo('1258594598', photo)
