#similar to room_diagnostics.py but here you use the joystick to select what sensor data you want to display on the 8x8 LED Matrix.
# Up for barometric pressure, down for humidity, and middle for thermometer, all in different colours so you can easily tell which is which.

#defining libraries
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

#defining colours
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

print("__________               __           __   __      __                              ")
print("\______   \ ____   ____ |  | __ _____/  |_/  \    /  \_____ _______   ____ ________")
print(" |       _//  _ \_/ ___\|  |/ // __ \   __\   \/\/   /\__  \\_  __ \_/ __ \\___   /")
print(" |    |   (  <_> )  \___|    <\  ___/|  |  \        /  / __ \|  | \/\  ___/ /    / ")
print(" |____|_  /\____/ \___  >__|_ \\___  >__|   \__/\  /  (____  /__|    \___  >_____\\")
print("        \/            \/     \/    \/            \/        \/            \/      \/")
print("                              Local Room Diagnostics                               ")

sleep(3)

#defining thermometer function to display on 8x8 led display on SenseHat
def thermometer():
	temp = sense.get_temperature()
	sleep(1)
	strtemp = (str(int(temp)))
	sense.show_message(strtemp + "degC", text_colour=green, back_colour=black, scroll_speed=0.05)

#defining barometric pressure measurement function to display on 8x8 led display on SenseHat
def barometric():
	pressure = sense.get_pressure()
	sleep(1)
	strpressure = (str(int(pressure)))
	sense.show_message(strpressure + "mbar", text_colour=red, back_colour=black, scroll_speed=0.05)

#defining humidity measurement function to display on 8x8 led display on SenseHat
def humidity():
	humid = sense.get_humidity()
	sleep(1)
	strhumid = (str(int(humid)))
	sense.show_message(strhumid + "\% H", text_colour=blue, back_colour=black, scroll_speed=0.05)


sense.stick.direction_up = barometric
sense.stick.direction_down = humidity
# sense.stick.direction_left = 
# sense.stick.direction_right = 
sense.stick.direction_middle = thermometer

#do it again
while True:	
	pass

