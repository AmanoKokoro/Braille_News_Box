#!/usr/bin/env python3
from newsget import NewsGet
from gpioactivity import GpioActivity
from getcharacter import GetCharacter
import RPi.GPIO as GPIO


def main():
    #pin open
    gpio = GpioActivity((22, 25, 27, 24, 17, 23))
    #pinsetup
    gpio.gpio_setup()
    #NewsAPIを初期化
    newsget = NewsGet()
    getcharacter = GetCharacter()
    #print('ニュースの数:' + len(newsget.sources['sources']))

    while True:
        #Go to Next News
        for x in range(len(newsget.sources['sources'])):
            print(x + 1, '個目のニュース')

            if gpio.pin_input() == 1:
                #get News data
                news = newsget.headline_get(x)
                #News data convert ascii
                asciinews = getcharacter.getasciichar(news)

                #Go to NextCharacter
                for y in asciinews:
                    if gpio.pin_input() == 1: #ボタン入力待ち
                        gpio.change_character(y) #文字切り替え

        newsget.refresh()

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\n***Ctrl+Cで停止しました***\n")
        pass
