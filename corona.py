from plyer import notification
from bs4 import BeautifulSoup
import requests
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:\programming\Python projects\Corona Notification\icon_PUV_icon.ico",
        timeout=5,
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        myHtmlData = getData("https://prsindia.org/covid-19/cases")
        soup = BeautifulSoup(myHtmlData, 'html.parser')

        for tr in soup.table.tbody.find_all('tr'):
            str = ""
            for td in tr:
                str += f"{td.get_text()},"
            
            list = str.split(',')

            while ("" in list):
                list.remove("")

            states=['Haryana','Maharashtra'] # you can add states you want to get notified
            for item in states:
                if item==list[1]:
                    print(list)
                    title='Cases of Corona'  
                    message=f"{item} \nConfirmed: {list[2]}\nActive: {list[3]}, Cured: {list[4]}\nDeaths: {list[5]}"
                    notifyMe(title,message)
                    time.sleep(10)

    time.sleep(3600)   # after every one hour   
