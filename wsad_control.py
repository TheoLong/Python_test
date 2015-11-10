
import Adafruit_BBIO.PWM as PWM
#PWM.start(channel, duty, freq=2000, polarity=0)
#duty values are valid 0 (off) to 100 (on)
import Adafruit_BBIO.GPIO as GPIO

PWM.start("P9_14", 0,1000)
GPIO.setup("P9_12", GPIO.OUT); 
GPIO.output("P9_12", GPIO.LOW);
GPIO.setup("P9_11", GPIO.OUT);
GPIO.output("P9_11", GPIO.HIGH);

PWM.start("P9_16", 0,1000)
GPIO.setup("P9_13", GPIO.OUT);
GPIO.output("P9_13", GPIO.HIGH);
GPIO.setup("P9_15", GPIO.OUT);
GPIO.output("P9_15", GPIO.LOW);


PWM.set_duty_cycle("P9_14", 0)
PWM.set_duty_cycle("P9_16", 0)

#for i in range(0,100):
drt=raw_input("direction: ")
while drt != "q" or "Q":
	drt=raw_input("direction: ")
	print(drt)
	if drt == "w":
		print "echo w"
                GPIO.output("P9_12", GPIO.LOW);
                GPIO.output("P9_11", GPIO.HIGH);

                GPIO.output("P9_13", GPIO.HIGH);
                GPIO.output("P9_15", GPIO.LOW);

                PWM.set_duty_cycle("P9_14",100)
                PWM.set_duty_cycle("P9_16",100)
	elif drt == "s":
		print "echo s"
		GPIO.output("P9_12", GPIO.HIGH);
                GPIO.output("P9_11", GPIO.LOW);

                GPIO.output("P9_13", GPIO.LOW);
                GPIO.output("P9_15", GPIO.HIGH);

                PWM.set_duty_cycle("P9_14",100)
                PWM.set_duty_cycle("P9_16",100)
	elif drt == "a":
		print "echo a"
                GPIO.output("P9_12", GPIO.LOW);
                GPIO.output("P9_11", GPIO.HIGH);

                GPIO.output("P9_13", GPIO.LOW);
                GPIO.output("P9_15", GPIO.HIGH);

                PWM.set_duty_cycle("P9_14",100)
                PWM.set_duty_cycle("P9_16",100)
	elif drt == "d":
		print "echo d"
                GPIO.output("P9_12", GPIO.HIGH);
                GPIO.output("P9_11", GPIO.LOW);

                GPIO.output("P9_13", GPIO.HIGH);
                GPIO.output("P9_15", GPIO.LOW);

                PWM.set_duty_cycle("P9_14",100)
                PWM.set_duty_cycle("P9_16",100)
	else:
		print "echo stop"
                GPIO.output("P9_12", GPIO.LOW);
                GPIO.output("P9_11", GPIO.HIGH);

                GPIO.output("P9_13", GPIO.HIGH);
                GPIO.output("P9_15", GPIO.LOW);

                PWM.set_duty_cycle("P9_14",0)
                PWM.set_duty_cycle("P9_16",0)


PWM.stop("P9_14")
PWM.stop("P9_16")


PWM.cleanup()

#set polarity to 1 on start:
PWM.start("P8_13", .1, 2000, 1)
