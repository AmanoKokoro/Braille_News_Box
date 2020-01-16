#!/usr/bin/env python3
from newsapi import NewsApiClient
import newsget


class GetCharacter:

    def __init__(self):
        self.c = 0
        self.asciilist = []

    #return news character list written in Ascii
    def getasciichar(self, stringdata):
        self.asciilist.clear()
        for i, self.c in enumerate(stringdata):
            for uni_char in range(ord('A'), ord('Z')):
                if (uni_char == ord(self.c)): #Big_character
                    self.c = ord(self.c) - 65 #65 = ASCII(A)
                    self.asciilist.append(self.c)
                    break

                elif ((uni_char + 32) == ord(self.c)): #little_character = Big + 32
                    self.c = ord(self.c) - 32 - 65
                    self.asciilist.append(self.c)
                    break

        printdata = (list(map(lambda x: x + 65, self.asciilist)))

        print('Newsdata:[', end='')

        for i in printdata:
            print(chr(i), end=',')

        print(']')

        return self.asciilist


if __name__ == '__main__':
    n = newsget.NewsGet()
    getnews = GetCharacter()

    news = n.headline_get(1)

    print(getnews.getasciichar(news))
