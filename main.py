from gpio import *
from time import *


def main():
	
	temp_sensor_pin = 0

	pinMode(0, IN)
	pinMode(2, OUT)#air_colder
	pinMode(3, OUT)#healting_element
	
	while True:
		t_celsius = float(analogRead(temp_sensor_pin))/1023*200-100
		
		if t_celsius > 25:
			digitalWrite(2, HIGH)
			digitalWrite(3, LOW)
		elif t_celsius < 20:
			digitalWrite(2, LOW)
			digitalWrite(3, HIGH)

if __name__ == "__main__":
	main()