from machine import Pin, SoftI2C,PWM,SPI
from pico_i2c_lcd import I2cLcd
from utime import sleep
import utime
import max7219
import morsecode

# Setup

start_state=1
main_menu_state=0


# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Define buttons
buttonA =  Pin(2,Pin.IN,Pin.PULL_UP)
buttonB =  Pin(0,Pin.IN,Pin.PULL_UP)

# Define I2C comm on LCD
i2c = SoftI2C(sda=Pin(4),scl=Pin(5),freq=400000)
lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

# Define SPI comm on MAX7219
m_clk = Pin(18, Pin.OUT)   # SCK
m_din = Pin(19, Pin.OUT)   # MOSI
m_cs  = Pin(17, Pin.OUT)   # CS
spi = SPI(
    0,
    baudrate=10_000_000,
    polarity=0,
    phase=0,
    sck=m_clk,
    mosi=m_din,
    miso=Pin(16)
)
matrix = max7219.Matrix8x8(spi, m_cs, 1)
matrix.brightness(0)

# Define passive buzzer
buzzer = PWM(Pin(28))
buzzer.duty_u16(0)

def main():
    
    print("Running...")

    global start_state
    global main_menu_state
    
    matrix.fill(0)
    matrix.show()
    
    lcd.clear()
    if start_state==1:
        print("start state on")
        lcd.putstr("     START")
        lcd.move_to(0,1)
        lcd.putstr(" Apasati but. A")
        while start_state==1:
            if buttonA.value()==0:
                start_state=0;
                main_menu_state=1;
                print("exiting start state...")
        print("main menu state on")
        
    # main menu
    while True:
        if buttonB.value()==1:
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Alege o optiune:")
            lcd.move_to(0,1)
            lcd.putstr("de invatare:")
        
            sleep(3)
        
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("But. B - scroll")
            lcd.move_to(0,1)
            lcd.putstr("But. A - select")
        
            sleep(3)
        else:
            break
    
    while True: 
        if buttonB.value()==0:
            break
    page = 1
    while True:
        if buttonA.value()==1:
            if buttonB.value()==1:
                if page == 1:
                    lcd.clear()
                    lcd.move_to(0,0)
                    lcd.putstr("Invata auditiv!")
                    lcd.move_to(0,1)
                    lcd.putstr("       1/2")
                    sleep(1)
                    
                    page=2
                    while True:
                        if buttonA.value()==0:
                            break
                        if buttonB.value()==0:
                            break
                       
                elif page == 2:
                    lcd.clear()
                    lcd.move_to(0,0)
                    lcd.putstr("Invata vizual!")
                    lcd.move_to(0,1)
                    lcd.putstr("       2/2")
                    page=3
                    sleep(1)
                    while True:
                        if buttonA.value()==0:
                            break
                        if buttonB.value()==0:
                            break
                else:
                    lcd.clear()
                    lcd.move_to(0,0)
                    lcd.putstr("   Iesi din")
                    lcd.move_to(0,1)
                    lcd.putstr("   aplicatie")
                    sleep(1)
                    page=1
                    while True:
                        if buttonA.value()==0:
                            break
                        if buttonB.value()==0:
                            break
        else:
            break
    print(page)
    if page == 2: # page 1
        morsecode.learn_by_hearing(buttonA,buttonB,buzzer,lcd,matrix)
        lcd.clear()
        matrix.fill(0)
        matrix.show()
    elif page == 3: # page 2
        morsecode.learn_by_seeing(buttonA,buttonB,buzzer,lcd,matrix)
        lcd.clear()
        matrix.fill(0)
        matrix.show()
    elif page == 1: # page 3
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(" La revedere...")
        sleep(2)
        lcd.clear()
        
        return
    
    
    
    
main()