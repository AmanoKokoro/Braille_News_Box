#!/usr/bin/env python3
from getnews import GetNews
#from gpioactivity import GpioActivity
from getcharacter import GetCharacter



def main():
    """
    #pinを与える
    GPIO = GpioActivity((22, 25, 27, 24, 17, 23))
    #pinのプルアップ
    GPIO.gpio_setup()
    #print(GPIO.solenoid_list)
    """

    #NewsAPIを初期化
    newsget = GetNews()
    getcharacter = GetCharacter()
    #print(len(newsget.sources['sources']))

    while (1):
        for x in range(len(newsget.sources['sources'])):
            input('続けるには キー を入力してください。')
            news = newsget.headline_get(x)
            asciinews = getcharacter.getasciichar(news)
            #print(type(asciinews))

            for y in asciinews:
                input()
                print(y)

        newsget.refresh()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl+Cで停止しました\n")
        pass
