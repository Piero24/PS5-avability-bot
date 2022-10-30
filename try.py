import telepot
import requests
from bs4 import BeautifulSoup
import time

TOKEN = 'YOUR-BOT-TOKEN'

chat_id_list = ['YOUR-CHAT-ID',]

bot = telepot.Bot(TOKEN)

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',}

list_link = ["https://www.unieuro.it/online/Playstation-5/PlayStation-5-Digital-Edition-pidSONPS5DIGITAL", "https://www.unieuro.it/online/Playstation-5/PlayStation-5-pidSONPS5DISC",
                "https://www.trony.it/online/console-giochi-e-tempo-libero/console/play-station-5/sony-ent-playstation-5_sku-2200010367", "https://www.euronics.it/console/sony-computer/playstation-5-digital-edition/eProd202008907/"]

is_avable = False


while is_avable != True :

    for link_ in list_link:

        page = requests.get(link_, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')



        # Qui la Playstation 5 è disponibile
        if (soup.findAll("div", {"class": "available on susy--span-4"}) or soup.find(id="disponibile") or soup.findAll("span", {"class": "button__icon--iconTxt i-prenota_ritira"}) or soup.findAll("span", {"class": "button__icon--iconTxt i-cart"})):

            is_avable = True
            for chat_id in chat_id_list:
                bot.sendMessage(chat_id, "!!! PS5 DISPONIBILE !!!")
                bot.sendMessage(chat_id, "IL LINK DI PREORDINE E':")
                bot.sendMessage(chat_id, link_)
                print("!!! PS5 DISPONIBILE !!!")
                print(link_)
                continue



        # Qui la Playstation 5 NON è disponibile
        elif (soup.findAll("div", {"class": "available off susy--span-4"}) or soup.find(id="nondisponibile") or soup.findAll("span", {"class": "button__icon--iconTxt i-notifica"})):

            #print("PS5 NON DISPONIBILE")
            #for chat_id in chat_id_list:
                #bot.sendMessage(chat_id, "PS5 NON DISPONIBILE")
                continue


        else:

            is_avable = True
            for chat_id in chat_id_list:
                bot.sendMessage(chat_id,"!!! PROBLEMA BOT PS5 !!!")
                print("!!! PROBLEMA BOT PS5 !!!")
                print(link_)
                continue


    time.sleep(90)
