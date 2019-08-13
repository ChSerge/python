import requests
import json

# Используем Yandex tranlate api. Доки тут: https://tech.yandex.ru/translate/doc/dg/concepts/About-docpage/

"""
dict_lang = {
    "/ru_en": "ru-en",  # русский-английский (по умолчанию)
    "/en_ru": "en-ru",  # английский-русский 
    "/ru_de": "ru-de",  # русский-немецкий
    "/de_ru": "de-ru",  # немецкий-русский 
    "/ru_fr": "ru-fr",  # русский-французский
    "/fr_ru": "fr-ru",  # французский-русский 
    "/ru_es": "ru-es",  # русский-испанский
    "/es_ru": "es-ru",  # испанский-русский 
    "/ru_it": "ru-it",  # русский-итальянский
    "/it_ru": "it-ru",  # итальянский-русский 
}
"""

dict_lang = {
    "/ru_en": ["ru-en", "русский-английский"], 
    "/en_ru": ["en-ru", "английский-русский"], 
    "/ru_de": ["ru-de", "русский-немецкий"],
    "/de_ru": ["de-ru", "немецкий-русский"],
    "/ru_fr": ["ru-fr", "русский-французский"],
    "/fr_ru": ["fr-ru", "французский-русский"],
    "/ru_es": ["ru-es", "русский-испанский"],
    "/es_ru": ["es-ru", "испанский-русский"],
    "/ru_it": ["ru-it", "русский-итальянский"],
    "/it_ru": ["it-ru", "итальянский-русский"],
}



lang = 'ru-en'      # "ru-en" русский-английский (по умолчанию)
                    # "en-ru" английский-русский 
                    # 'ru-de' русский-немецкий
                    # 'de-ru" немецкий-русский 
                    # "ru-fr" русский-французский
                    # "fr-ru" французский-русский 
                    # "ru-es" русский-испанский
                    # "es-ru" испанский-русский 
                    # "ru-it" русский-итальянский
                    # "it-ru" итальянский-русский 



#api_key = 'trnsl.1.1.20180215T072655Z.85a3da116efded15.8db4596a413e61cd579dcb066a703b18769d54cb'
#api_key = 'trnsl.1.1.20190812T174613Z.ef38a2d1292be3d2.eb6c91e6e42ce22e3db0c84b540ff39bb407d431'
#lang = 'ru-en'
#text = 'Привет мир!'

def get_translation(api_key, in_text, lang='ru-en'):
#def get_translation(api_key, in_text, lang):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    responce = requests.post(url, params={'key': api_key, 'lang': lang, 'text': in_text})
    out_text = responce.json()['text'][0]
    return out_text

#print(responce.content)

# Преобразуем полученыый контент из json в dict

# response_content = json.loads(res.content.decode('utf-8'))
# print(response_content['text'][0])

# Либо проще:

#print(responce.json())










