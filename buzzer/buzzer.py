from RPi import GPIO
from aiy._buzzer import PWMController
import time

def main():
	is_on = False
	print('Tone is played while button is Pressed (Ctrl-C to exit)')
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	time.sleep(.1)
	with PWMController(gpio=22) as controller:
		try:
			time.sleep(.1)
			controller.set_frequency(freq_hz=440.00)
			time.sleep(.25)
			controller.set_frequency(freq_hz=523)
			time.sleep(.25)
			controller.set_frequency(freq_hz=659)
			time.sleep(.25)
			controller.set_frequency(freq_hz=0)
			while True:
				if GPIO.input(23) == GPIO.LOW :
					if is_on == False:
						controller.set_frequency(freq_hz=440.00)
					is_on = True
				else:
					is_on = False
					controller.set_frequency(freq_hz=0)
				time.sleep(.1)
		finally:
			#controller.close()
			print('Done.')


if __name__ == '__main__':
	main()
