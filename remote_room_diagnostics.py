#a script that lets you leave your raspberry pi somewhere, and view environment data on its environment from your shell.

#defining libraries
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()


print("__________               __           __   __      __                              ")
print("\______   \ ____   ____ |  | __ _____/  |_/  \    /  \_____ _______   ____ ________")
print(" |       _//  _ \_/ ___\|  |/ // __ \   __\   \/\/   /\__  \\_  __ \_/ __ \\___   /")
print(" |    |   (  <_> )  \___|    <\  ___/|  |  \        /  / __ \|  | \/\  ___/ /    / ")
print(" |____|_  /\____/ \___  >__|_ \\___  >__|   \__/\  /  (____  /__|    \___  >_____ \")
print("        \/            \/     \/    \/            \/        \/            \/      \/")
print("                                Remote Room Diagnostics                            ")

#defining humidity measurement function to print
def humidity():
	humid = sense.get_humidity()
	strhumid = (str(int(humid)))
	print("~~~~~~~~~")
	print(strhumid + "\% H \n")
	

#defining barometric pressure measurement function to print
def barometric():
	pressure = sense.get_pressure()
	strpressure = (str(int(pressure)))
	print(strpressure + "mbar \n")
	
#defining thermometer function to print
def thermometer():
	temp = sense.get_temperature()
	prtemp = (int(float(str(temp))))
	print(str(prtemp - 10) + "degC \n")
	print("~~~~~~~~~")

#do it again
while True:	
	sleep(1)
	humidity()
	barometric()
	thermometer()
