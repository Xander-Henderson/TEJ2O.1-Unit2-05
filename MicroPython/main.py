"""
Created by: Alexander
Created on: Sep 2025
This module shows the temperature of the microbit in kelvin
"""

from microbit import *

# variable for the temperature
temperature_of_microbit_in_kelvin = 0

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        # https://pc-microbit-micropython.readthedocs.io/en/latest/sensors/thermometer.html
        temperature_of_microbit_in_kelvin = temperature() + 273
        display.show("The temperature is: " + str(temperature_of_microbit_in_kelvin) + " K")
