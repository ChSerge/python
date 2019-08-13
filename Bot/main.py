import json
import requests
from time import sleep
from yobit import get_btc
from ya_translate import get_translation, dict_lang
from dict import dict_mess

#UU = "https://api.telegram.org/bot912179245:AAGmmtSfQM1xQnHBDupsVFFn9rtcPUrtpRE/getMe"

global URL
BOT_TOKEN = "912179245:AAGmmtSfQM1xQnHBDupsVFFn9rtcPUrtpRE"
URL = "https://api.telegram.org/bot%s/" % BOT_TOKEN

#PROXIES = {"https":"23.237.173.102:3128","http":"178.128.40.114:3128","https":"81.93.78.162:33636","https":"80.94.229.172:3128"}


TR_API_KEY = "trnsl.1.1.20190812T174613Z.ef38a2d1292be3d2.eb6c91e6e42ce22e3db0c84b540ff39bb407d431"
NOT_SUPPORTED = "Команда не поддерживется"
UNKNOWN = "Извините, не понимаю"

global last_update_id
last_update_id = 0

global mode_trans   #режим перевода: True - активен, False - не активен
mode_trans = False

global lang         #текущая пара языков перевода
lang = "ru-en"      # "ru-en" русский-английский (по умолчанию)
                    # "en-ru" английский-русский 
                    # 'ru-de' русский-немецкий
                    # 'de-ru" немецкий-русский 
                    # "ru-fr" русский-французский
                    # "fr-ru" французский-русский 
                    # "ru-es" русский-испанский
                    # "es-ru" испанский-русский 
                    # "ru-it" русский-итальянский
                    # "it-ru" итальянский-русский 

#команды:
HELP = "/help"

USD_BTC = "/btc"    # курс биткоина к доллару

ON_TR_MODE = "/ontransmode"     # включить режим перевода
OFF_TR_MODE = "/offtransmode"   # отключить режим перевода
MODE_TRANS = "/mode_trans"      # показать статус режима перевода

MODE_TR_ON  = "Режим перевода включен"
MODE_TR_OFF = "Режим перевода отключен"

RU_EN = "/ru_en"    # русский-английский (по умолчанию)
EN_RU = "/en_ru"    # английский-русский 
RU_DE = "/ru_de"    # русский-немецкий
DE_RU = "/de_ru"    # немецкий-русский 
RU_FR = "/ru_fr"    # русский-французский
FR_RU = "/fr_ru"    # французский-русский 
RU_FR = "/ru_es"    # русский-испанский
ES_RU = "/es_ru"    # испанский-русский 
RU_IT = "/ru_it"    # русский-итальянский
IT_RU = "/it_ru"    # итальянский-русский 

HELP_TEXT = ("Telegram-бот умеет отвечать на некоторые приветсвия и прощание." 
"Бот сообщает курс биткоина по отношению к доллару США.\n"
"Соответствующая команда:\n"
"/btc - курс биткоина к доллару\n"
"\n"
"Бот позволяет произвести перевод фраз с английского, немецкого, французского,\n" 
"испанского и италянского языков на русский и наоборот.\n"
"\n"
"Команды включения/выключения режима перевода и отображения его состояния:\n"
"/ontransmode - включить режим перевода\n"
"/offtransmode - отключить режим перевода\n"
"/mode_trans - показать статус режима перевода\n"
"\n"
"Команды позволяющие сменить языки перевода:\n"
"/ru_en - русский-английский\n"
"/en_ru - английский-русский\n"
"/ru_de - русский-немецкий\n"
"/de_ru - немецкий-русский \n"
"/ru_fr - русский-французский\n"
"/fr_ru - французский-русский\n" 
"/ru_es - русский-испанский\n"
"/es_ru - испанский-русский \n"
"/ru_it - русский-итальянский\n"
"/it_ru - итальянский-русский\n"
"\n"
"----------------------------------------------------------------------------\n"
"\n"
"/help - показ этой информации")

#/help - описание функционала и список поддерживаемых команд

"""
#Для загрузки команд 

help - описание функционала и список поддерживаемых команд
btc - курс биткоина к доллару
ontransmode - включить режим перевода
offtransmode - отключить режим перевода
mode_trans - показать статус режима перевода
ru_en - русский-английский
en_ru - английский-русский 
ru_de - русский-немецкий
de_ru - немецкий-русский 
ru_fr - русский-французский
fr_ru - французский-русский 
ru_es - русский-испанский
es_ru - испанский-русский 
ru_it - русский-итальянский
it_ru - итальянский-русский

"""


#---------------------------------------------------------
def get_updates():
    global URL
    url = URL + "getupdates"
    responce = requests.get(url)
    print(responce.status_code)  # 200 : good
    return responce.json()


#---------------------------------------------------------
def get_message():
    global last_update_id
    data = get_updates()
    
    last_object = data["result"][-1]
    current_update_id = last_object["update_id"]
    
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object["message"]["chat"]["id"]
        message_text = last_object["message"]["text"]
        message = { "chat_id": chat_id,
                    "text": message_text }
        return message
    return None

#---------------------------------------------------------
def send_message(chat_id, text="Подождите, пожалуйста..."):
    url = URL + "sendmessage?chat_id={}&text={}".format(chat_id, text)
    #requests.get(url, proxies=PROXIES)
    requests.get(url)


#---------------------------------------------------------
def main():
    while True:
        global mode_trans, lang
        global NOT_SUPPORTED, UNKNOWN, ON_TR_MODE, OFF_TR_MODE, MODE_TR_ON, MODE_TR_OFF
        answer = get_message()
        if answer != None:
            chat_id = answer["chat_id"]
            text = answer["text"]
            if text == "/btc":
                send_message(chat_id, get_btc())
            elif text == HELP:
                print(HELP)
                send_message(chat_id, HELP_TEXT)
            elif text == MODE_TRANS:
                if mode_trans:
                    print(MODE_TR_ON)
                    send_message(chat_id, MODE_TR_ON)
                else:
                    print(MODE_TR_OFF)
                    send_message(chat_id, MODE_TR_OFF)
            elif text == ON_TR_MODE:
                mode_trans = True
                print(MODE_TR_ON)
                send_message(chat_id, MODE_TR_ON)
            elif text == OFF_TR_MODE:
                mode_trans = False
                print(MODE_TR_OFF)
                send_message(chat_id, MODE_TR_OFF)
            elif text in dict_lang: 
                lang = dict_lang[text][0]
                lang_info = dict_lang[text][1]
                print(lang)
                send_message(chat_id, lang_info)
            elif mode_trans: 
                tr_text = get_translation(TR_API_KEY, text, lang)
                print(tr_text)
                send_message(chat_id, tr_text)
            elif text in dict_mess: 
                mess = dict_mess[text]
                print(mess)
                send_message(chat_id, mess)
            elif text[0] == "/":
                print(NOT_SUPPORTED)
                send_message(chat_id, NOT_SUPPORTED)
            else:
                print(UNKNOWN)
                send_message(chat_id, UNKNOWN)
        else:
            sleep(2)
            continue
        sleep(2)


#=================================================================
if __name__ == "__main__":
    main()

