from machine import Pin, reset
from Blinker.Blinker import Blinker, BlinkerButton, BlinkerNumber
from Blinker.BlinkerDebug import *
import time
auth = 'Your Device Secret Key'
ssid = 'Your WiFi network SSID or name'
pswd = 'Your WiFi network WPA password or WEP key'
BLINKER_DEBUG.debugAll()
Blinker.mode('BLINKER_WIFI')
#连接wifi
try:
    Blinker.begin(auth, ssid, pswd)
    time.sleep(0.1)
except OSError as e:
    reset()   
#创建引脚对象
led = Pin(18, Pin.IN)
pw1 = Pin(13, Pin.OUT)
rst1 = Pin(19,Pin.OUT)
iled = Pin(2,Pin.OUT)
#定义引脚值，拉高重启和开机引脚的电平
pinVal = 1
pw1.value(pinVal)
rst1.value(pinVal) 
#创建组件对象
button1 = BlinkerButton('btn-power')
button2 = BlinkerButton('btn-shutdown')
button3 = BlinkerButton('btn-rest')
button4 = BlinkerButton('btn-state')
#回调函数
def button_callback_power(state):
    BLINKER_LOG('get button state: ', state)
    global pinVal
    pinVal = 0
    pw1.value(pinVal)
    time.sleep(0.4)
    pinVal = 1
    pw1.value(pinVal)
    print(str(Pin(13).value())+"pinValue: "+str(pinVal))

def button_callback_shutdown(state):
    BLINKER_LOG('get button state: ', state)
    global pinVal
    pinVal = 0
    pw1.value(pinVal)
    time.sleep(10)
    pinVal = 1
    pw1.value(pinVal)

def button_callback_rest(state):
    BLINKER_LOG('get button state: ', state)
    global pinVal
    pinVal = 0
    rst1.value(pinVal)
    time.sleep(0.4)
    pinVal = 1
    rst1.value(pinVal)

button1.attach(button_callback_power)
button2.attach(button_callback_shutdown)
button3.attach(button_callback_rest)

if __name__ == '__main__':
    while True:
        try:
            Blinker.run()
            state = led.value()
            if state == 1:
                iled.on()
                button4.print('on')
            else:
                iled.off()
                button4.print('off')
            time.sleep(0.4)
        except OSError as e:
            reset()
