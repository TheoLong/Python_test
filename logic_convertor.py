
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

PWM1="P9_14"
PWM2="P8_13"
PWM.start(PWM1,50,3000)
PWM.start(PWM2,50,3000)
for i in range(0,100):
	DC=input("set duty cycle: ")
	PWM.set_duty_cycle(PWM1,DC)
	#f=input("set frequency: ")	
	
