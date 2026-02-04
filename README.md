# Morse Code Learning Device ran on a RPico2W controller

## Summary
The project implements an embedded system used for learning the Morse Code in an interactive way, given the hardware components that form the UI. It uses Micropython and various libraries for the hardware's components.

## Implementation

### Hardware
- RPico2W microcontroller
- 2x16 LCD display with I2C communication
- 8x8 MAX7219 matrix with SPI communication
- active buzzer
- 2 arcade buttons

### Software
- Micropython
- Libraries: machine, pico_i2c, utime, max7219, random

## How it works
By following the instructions on the LCD, you will acces (via the buttons) the main menu where you can select different options. The first two are the learning modules, the last one closes the app.
Thereby, the system has 2 modules of learning: Auditive learning adn  Visual learning.

In the **Auditive learning** mode, the user has to guess the letter associated with the sound heard from the buzzer. After hearing a specific combination of short and long sounds, the user has to scroll (button B) on the 8x8 Matrix through the alphabet and select (button A)
the corresponding letter. After winning/losing, you can retry or close the program.

In the **Visual learning** mode, the user had to imitate the combination of beeps that matches the letter displayed on the 8x8 Matrix. after using the button B to simulate the corresponding sound, button A is used to confirm. Same as the previous module, after winning/losing, 
you can retry or close the program.

## Demo
[![VIDEO DEMO](https://img.youtube.com/vi/7ZZPD4EdzOs/hqdefault.jpg)](https://www.youtube.com/watch?v=7ZZPD4EdzOs)
