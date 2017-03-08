
import RPi.GPIO as GPIO
import time
import os

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.OUT) #motorlayer
	GPIO.setup(12,GPIO.IN)  #sensor1
	GPIO.setup(13,GPIO.IN)	#sensor2
        GPIO.setup(15,GPIO.IN)	#sensor3
        GPIO.setup(40,GPIO.IN)	#sensor4
        GPIO.setup(18,GPIO.OUT)	#disinfectlayer

def reset():
	GPIO.output(11,GPIO.LOW)
#	GPIO.output(13,GPIO.LOW)
def run():
	GPIO.output(11,GPIO.HIGH)
#	GPIO.output(13,GPIO.LOW)

def getnum():
	a = GPIO.input(12)
        b = GPIO.input(13)
        c = GPIO.input(15)
	if a == 0 and b == 0 and c == 0:
		print(a,b,c)
		return 1
        if a == 0 and b == 0 and c == 1:
                print(a,b,c)
                return 2 
        if a == 0 and b == 1 and c == 0:
                print(a,b,c)
		return 3
        if a == 0 and b == 1 and c == 1:
		print(a,b,c)
                return 4 
        if a == 1 and b == 0 and c == 0:
		print(a,b,c)
                return 5 
        if a == 1 and b == 0 and c == 1:
                print(a,b,c)
                return 6 
        if a == 1 and b == 1 and c == 0:
                print(a,b,c)
                return 7 
        if a == 1 and b == 1 and c == 1:
                print(a,b,c)
                return 8 


def stop():
	reset()
	
def back(n):
	reset()
	run()
	i = 0 
	while i == 0: 
		exist = GPIO.input(40)
		if exist == 0 :
			n0 = getnum()
			if n0 == n:
				stop()
				i = 1	

def disinfect():
	reset()
	GPIO.output(18,GPIO.HIGH)  	
	time.sleep(5)
	GPIO.output(18,GPIO.LOW)

def snap(n):
	os.sys("raspistill -o /Shoes/pics/"+ n + ".jpg")		
	

if __name__=='__main__':
	init()
	reset()
	back(8)
	disinfect()
 	GPIO.cleanup()
