#!/usr/bin/env python3
from newsapi import NewsApiClient
y
import newsget


class GetCharacter:

    #initialize
    def __init__(self):
        self.c = 0
        self.asciilist = []

    #return news character list written in Ascii
    def getasciichar(self, stringdata):
        self.asciilist.clear()  #list clear
        for i, self.c in enumerate(stringdata):
            for uni_char in range(ord('A'), ord('Z')):
                if (uni_char == ord(self.c)): #Big_character
                    self.c = ord(self.c) - 65 #65 = ASCII(A)
                    self.asciilist.append(self.c) #list add
                    break

                elif ((uni_char + 32) == ord(self.c)): #little_character = Big + 32
                    self.c = ord(self.c) - 32 - 65 #A - a = 32
                    self.asciilist.append(self.c)
                    break

        printdata = (list(map(lambda x: x + 65, self.asciilist))) #print ascii data list 

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
