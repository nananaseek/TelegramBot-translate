import requests
from config import URL_AUTH, URL_TRANS, KEY

hauth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=hauth)


def go_trans(word, lang):
    if auth.status_code == 200:
        token = auth.text
        htrans = {
            'Authorization': 'Bearer ' + token
        }
        if lang == 'English':
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1058
            }
            r = requests.get(URL_TRANS, headers=htrans, params=params)
            res = r.json()
            try:
                return res['Translation']['Translation']
            except:
                return 'нема такого слова'
        elif lang == 'Ukrainian':
            params = {
                'text': word,
                'srcLang': 1058,
                'dstLang': 1033
            }
            r = requests.get(URL_TRANS, headers=htrans, params=params)
            res = r.json()
            try:
                return res['Translation']['Translation']
            except:
                return 'нема такого слова'
    else:
        print('щось голова кружиться')
