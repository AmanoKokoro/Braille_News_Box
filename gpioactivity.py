#!/usr/bin/env python3

import RPi.GPIO as GPIO

"""
solenoid -> ◎

solenoids map

0 ◎    ◎ 1
2 ◎    ◎ 3
4 ◎    ◎ 5


"""
"""solenods setup util and action """


class GpioActivity:
    def __init__(self, gpio_number):
        self.solenoid_list = [	[1, 0, 0, 0, 0, 0],
                               [1, 0, 1, 0, 0, 0],
                               [1, 1, 0, 0, 0, 0],
                               [1, 1, 0, 1, 0, 0],
                               [1, 0, 0, 1, 0, 0],
                               [1, 1, 1, 0, 0, 0],
                               [1, 1, 1, 1, 0, 0],
                               [1, 0, 1, 1, 0, 0],
                               [0, 1, 0, 1, 0, 0],
                               [0, 1, 1, 1, 0, 0],
                               [1, 0, 0, 0, 1, 0],
                               [1, 0, 1, 0, 1, 0],
                               [1, 1, 0, 0, 1, 0],
                               [1, 1, 0, 1, 1, 0],
                               [1, 0, 0, 1, 1, 0],
                               [1, 1, 1, 0, 1, 0],
                               [1, 1, 1, 1, 1, 0],
                               [1, 0, 1, 1, 1, 0],
                               [0, 1, 1, 0, 1, 0],
                               [0, 1, 1, 1, 1, 0],
                               [1, 0, 0, 0, 1, 1],
                               [1, 0, 1, 0, 1, 1],
                               [0, 1, 1, 1, 0, 1],
                               [1, 1, 0, 0, 1, 1],
                               [1, 1, 0, 1, 1, 1],
                               [1, 0, 0, 1, 1, 1],
                               [0, 0, 1, 1, 0, 1],
                               [0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0]]
        self.solenoid_gpio = gpio_number
        self.switch_gpio = 6


    def gpio_setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.solenoid_gpio, GPIO.OUT)
        for i, gpio in enumerate(self.solenoid_gpio):   #gpio is pi number
            GPIO.output(gpio, 0)


    def change_character(self, cnum):
        print("Characterchr : ", chr(cnum + 65))
        for i, gpio in enumerate(self.solenoid_gpio):   #gpio is pi number
            GPIO.output(gpio, self.solenoid_list[cnum][i])


    def destroy(self):
        for i, closepin in enumrate(self.solenoid_gpio):
            GPIO.output(closepin, 0)
        GPIO.cleanup()
