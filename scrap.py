import requests
from bs4 import BeautifulSoup
import smtplib
import time


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',}


list_link = ["https://www.unieuro.it/online/Playstation-5/PlayStation-5-Digital-Edition-pidSONPS5DIGITAL", "https://www.unieuro.it/online/Playstation-5/PlayStation-5-pidSONPS5DISC",
                "https://www.trony.it/online/console-giochi-e-tempo-libero/console/play-station-5/sony-ent-playstation-5_sku-2200010367", "https://www.euronics.it/console/sony-computer/playstation-5-digital-edition/eProd202008907/"]


oggetto = "Subject: !!! PS5 DISPONIBILE !!!\n\n"
contenuto = "IL LINK DI PREORDINE E': \n "

is_avable = False

while is_avable != True :

    for link_ in list_link:

        page = requests.get(link_, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')



        # Qui la Playstation 5 è disponibile
        if (soup.findAll("div", {"class": "available on susy--span-4"}) or soup.find(id="disponibile") or soup.findAll("span", {"class": "button__icon--iconTxt i-prenota_ritira"}) or soup.findAll("span", {"class": "button__icon--iconTxt i-cart"})):

            is_avable = True
            contenuto = contenuto + link_
            messaggio = oggetto + contenuto
            email = smtplib.SMTP("smtp.live.com", 25)
            email.ehlo()
            email.starttls()
            email.login("FROM", "PASSWORD")
            email.sendmail("FROM","TO",messaggio)
            email.quit()


        # Qui la Playstation 5 NON è disponibile
        elif (soup.findAll("div", {"class": "available off susy--span-4"}) or soup.find(id="nondisponibile") or soup.findAll("span", {"class": "button__icon--iconTxt i-notifica"})):

            #print("PS5 NON DISPONIBILE")
            continue

        else:

            is_avable = True
            er_object = "Subject: !!! PROBLEMA BOT PS5 !!!\n\n"
            er_message = er_object + link_
            email = smtplib.SMTP("smtp.live.com", 25)
            email.ehlo()
            email.starttls()
            email.login("FROM", "PASSWORD")
            email.sendmail("FROM","TO",er_message)
            email.quit()

    time.sleep(90)
