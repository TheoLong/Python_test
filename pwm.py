import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

PWM1="P9_14"
PWM2="P9_16"
PWM3="P8_13"
PWM.start(PWM3,100,3000)
PWM.start(PWM2,52,3000)
PWM.start(PWM1,52,3000)

for i in range (0,100):
	direction=raw_input("direction: ")
	if direction == "w":
		PWM.set_duty_cycle(PWM1,20)
	        PWM.set_duty_cycle(PWM2,20)
	elif direction == "s":
		PWM.set_duty_cycle(PWM1,90)
	       	PWM.set_duty_cycle(PWM2,90)
	elif direction == "a":
                PWM.set_duty_cycle(PWM1,0)
                PWM.set_duty_cycle(PWM2,100)
	elif direction == "d":
                PWM.set_duty_cycle(PWM1,100)
                PWM.set_duty_cycle(PWM2,0)
	else:
		PWM.set_duty_cycle(PWM1,52)
		PWM.set_duty_cycle(PWM2,52)
PWM.stop(PWM1)
PWM.stop(PWM2)
PWM.cleanup()
