from machine import Pin, SoftI2C,PWM,SPI
from pico_i2c_lcd import I2cLcd
from utime import sleep
import utime
import max7219
import random

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def generate_letter():
    return random.choice(alphabet)

morsecode_dict = {
        "A":[500,900],
        "B":[900,500,500,500],
        "C":[900,500,900,500],
        "D":[900,500,500],
        "E":[500],
        "F":[500,500,900,500],
        "G":[900,900,500],
        "H":[500,500,500,500],
        "I":[500,500],
        "J":[500,900,900,900],
        "K":[900,500,900],
        "L":[500,900,500,500],
        "M":[900,900],
        "N":[900,500],
        "O":[900,900,900],
        "P":[500,900,900,500],
        "Q":[900,900,500,900],
        "R":[500,900,500],
        "S":[500,500,500],
        "T":[900],
        "U":[500,500,900],
        "V":[500,500,500,900],
        "W":[500,900,900],
        "X":[900,500,900,900],
        "Y":[900,500,900,900],
        "Z":[900,900,500,500]
    }

def play_tone(buzzer : Pin, duration):
    # Set the frequency of the PWM signal
    buzzer.freq(500)
    # Set duty cycle to 50%
    buzzer.duty_u16(32768)
    # Play the tone for the specified duration
    utime.sleep_ms(duration)
    # Turn off the buzzer
    buzzer.duty_u16(0)
'''
# Play some tones
play_tone(440, 500)  # A4 note for 500ms
utime.sleep_ms(200)
play_tone(494, 500)  # B4 note for 500ms
utime.sleep_ms(200)
play_tone(523, 500)  # C5 note for 500ms    
'''



def learn_by_hearing(buttonA : Pin,buttonB : Pin,buzzer : Pin,lcd : I2cLcd,matrix : max7219):
    print("learn by hearing")
    matrix.fill(0)
    matrix.text("1",0,0,1)
    matrix.show()
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Invata auditiv!")
    lcd.move_to(0,1)
    lcd.putstr("but. A -> START")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Asculta sunetul")
    lcd.move_to(0,1)
    lcd.putstr("Select. litera")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("A -> selecteaza")
    lcd.move_to(0,1)
    lcd.putstr("B -> scroll matr")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("but. A -> START")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    playing=True
    while playing == True:
        letter=generate_letter()
        
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("  Asculta...")
        
        for note in morsecode_dict[letter]:
            play_tone(buzzer,note)
            sleep(1)
        print("LITERA ASCULTATA ESTE: " + letter)
            
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("A -> selecteaza")
        lcd.move_to(0,1)
        lcd.putstr("B -> scroll matr")
        index=0
        matrix.fill(0)
        matrix.text("A",0,0,1)
        matrix.show()
        while True:
            utime.sleep_ms(200)
            chosen_letter = alphabet[index]
            if buttonA.value()==0:
                chosen_letter = alphabet[index-1]
                if chosen_letter == letter:
                    lcd.clear()
                    lcd.move_to(0,0)
                    lcd.putstr("Litera aleasa e")
                    lcd.move_to(0,1)
                    lcd.putstr( chosen_letter + " - CORECT!")
                else:
                    lcd.clear()
                    lcd.move_to(0,0)
                    lcd.putstr("Litera aleasa e")
                    lcd.move_to(0,1)
                    lcd.putstr( chosen_letter + " - GRESIT!")
                    sleep(1)
                    lcd.clear()
                    lcd.move_to(0,0)
                    lcd.putstr("Litera corecta e")
                    lcd.move_to(0,1)
                    lcd.putstr("      "+ letter)
                sleep(1)
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr("Mai jucam?")
                lcd.move_to(0,1)
                lcd.putstr("(A)-Da / (B)-Nu")
                while True:
                    if buttonA.value()==0:
                        lcd.clear()
                        lcd.move_to(0,0)
                        lcd.putstr("Revenim..")
                        break
                    if buttonB.value()==0:
                        lcd.clear()
                        lcd.move_to(0,0)
                        lcd.putstr("La revedere...")
                        sleep(1)
                        playing = False
                        break
                break
            
            if buttonB.value()==0:
                print("LITERA ALEASA ESTE : " + chosen_letter)
                matrix.fill(0)
                matrix.text(alphabet[index],0,0,1)
                matrix.show()
                if index < len(alphabet):
                    index = index + 1
                else:
                    index = 0
                
  
    return

''''''

def learn_by_seeing(buttonA : Pin,buttonB : Pin,buzzer : Pin,lcd : I2cLcd,matrix : max7219):
    print("learn by seeing")
    matrix.fill(0)
    matrix.text("2",0,0,1)
    matrix.show()

    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Invata vizual!")
    lcd.move_to(0,1)
    lcd.putstr("but. A -> START")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Vezi matricea")
    lcd.move_to(0,1)
    lcd.putstr("Tasteaza pe")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("butonul B")
    lcd.move_to(0,1)
    lcd.putstr("bataia coresp.")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("sunetului.")
    lcd.move_to(0,1)
    lcd.putstr("Confirma cu (A)")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Bataie scurta->.")
    lcd.move_to(0,1)
    lcd.putstr("Bataie lunga-> _")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("but. A -> START")
    sleep(1)
    
    while True:
        if buttonA.value() == 0:
            break
    
    playing=True
    while playing == True:
        
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("(A) -> CONFIRM")
        lcd.move_to(0,1)
        lcd.putstr("(B) -> BATAIE")
        
        letter = generate_letter()
        matrix.fill(0)
        matrix.text(letter,0,0,1)
        matrix.show()
        sleep(1)
        
        tones = []
        correct = False
        while True:
            if buttonB.value() == 0:
                utime.sleep_ms(200)
                start = utime.ticks_ms()
                buzzer.freq(500)
                buzzer.duty_u16(32768)
                while True:
                    if buttonB.value() == 1:
                        end = utime.ticks_ms()
                        buzzer.duty_u16(0)
                        break
                print(utime.ticks_diff(end, start))
                if utime.ticks_diff(end, start) > 500:
                    value = "lung"
                else:
                    value = "scurt"
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr(value)
                tones.append(int(utime.ticks_diff(end, start)))
                sleep(1)
            if buttonA.value() == 0:
                print(tones)
                
                if len(tones) > len(morsecode_dict[letter]):
                    correct = False
                ind = 0
                for tone in tones:
                    
                    print("tone:",tone)
                    print("morsecode_dict[letter][tone]:",morsecode_dict[letter][ind])
                    if tone <= 500:
                        if morsecode_dict[letter][ind] <=501:  #bataie scurta
                            correct = True
                        else:
                            correct = False
                            break
                    else:
                        if morsecode_dict[letter][ind] > 500:
                            correct = True
                        else:
                            correct = False
                            break
                    ind = ind + 1
                lcd.clear()
                lcd.move_to(0,0)
                if correct == True:
                    lcd.putstr("CORECT")
                else:
                    lcd.putstr("GRESIT")
                del tones
                sleep(2)
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr("Mai jucam?")
                lcd.move_to(0,1)
                lcd.putstr("(A)-Da / (B)-Nu")
                while True:
                    if buttonA.value()==0:
                        lcd.clear()
                        lcd.move_to(0,0)
                        lcd.putstr("Revenim..")
                        break
                    if buttonB.value()==0:
                        lcd.clear()
                        lcd.move_to(0,0)
                        lcd.putstr("La revedere...")
                        sleep(1)
                        playing = False
                        break
                break
                
    
    return