/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Alexander
 * Created on: Sep 2025
 * This program shows the temperature in Kelvin.
*/

//variable for the temperature of the microbit
let temperatureOfMicrobit: number = 0

basic.clearScreen()
basic.showIcon(IconNames.Happy)

input.onButtonPressed(Button.A, function () {
    temperatureOfMicrobit = input.temperature() + 273
    basic.showString(" The temperature is: " + temperatureOfMicrobit.toString() + " K")
})
