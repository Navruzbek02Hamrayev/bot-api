from settings import TOKEN
import requests
from time import sleep
from send_message import send_message



def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result']
    else:
        return False


def get_last_update(updates: list[dict]) -> dict:
    return updates[-1]


last_update_id = -1
while True:
    updates = get_updates()
    last_update = get_last_update(updates)


    if last_update['update_id'] != last_update_id:
        text = last_update['message']['text']
        user = last_update['message']['from']

        send_message(user['id'], text)
        last_update_id = last_update['update_id']

    sleep(0.5)
