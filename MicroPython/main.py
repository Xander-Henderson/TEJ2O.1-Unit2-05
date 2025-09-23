"""
Created by: Alexander
Created on: Sep 2025
This module shows the temperature of the microbit
"""

from microbit import *

# variable for the temperature
temperature_of_microbit = 0

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        temperature_of_microbit = input.temperature() + 273
        display.show (' The temperature is: ' + str(temperature_of_microbit) + ' K')
