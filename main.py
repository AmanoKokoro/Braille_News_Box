#!/usr/bin/env python3
from newsget import NewsGet
from gpioactivity import GpioActivity
from getcharacter import GetCharacter
import RPi.GPIO as GPIO


def main():
    #pinを与える
    gpio = GpioActivity((22, 25, 27, 24, 17, 23))
    #pinのプルアップ
    gpio.gpio_setup()
    #NewsAPIを初期化
    newsget = NewsGet()
    getcharacter = GetCharacter()
    #print('ニュースの数:' + len(newsget.sources['sources']))

    while True:
        for x in range(len(newsget.sources['sources'])):
            print(x + 1, '個目のニュース')

            if gpio.pin_input() == 1:
            #input('続けるには キー を入力してください。')
                news = newsget.headline_get(x)
                #print('from main news:', news)
                asciinews = getcharacter.getasciichar(news)
                #print('from main asciinews:', asciinews)

                for y in asciinews:
                    if gpio.pin_input() == 1:
                    #input()
                        gpio.change_character(y)

        newsget.refresh()

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\n***Ctrl+Cで停止しました***\n")
        pass
