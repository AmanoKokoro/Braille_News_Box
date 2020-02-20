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
        self.switch_gpio = 13
        self.status = 1
        self.old_status = 0
        self.gpio_setup()
        

    def gpio_setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.solenoid_gpio, GPIO.OUT)
        GPIO.setup(self.switch_gpio, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        for i, gpio in enumerate(self.solenoid_gpio):   #gpio is pi number
            GPIO.output(gpio, 0)


    def change_character(self, cnum):
        print("Characterchr : ", chr(cnum + 65))
        for i, gpio in enumerate(self.solenoid_gpio):   #gpio is pi number
            GPIO.output(gpio, self.solenoid_list[cnum][i])

    def pin_input(self):
        GPIO.wait_for_edge(self.switch_gpio, GPIO.FALLING)
        return 1


    def destroy(self):
        for i, closepin in enumrate(self.solenoid_gpio):
            GPIO.output(closepin, 0)
        GPIO.cleanup()
