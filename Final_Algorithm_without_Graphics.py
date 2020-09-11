'''
Graphics removed -> to port to c++ code

Some limitations with the sensor
1.if(offset > single_bulb_Lux)   ---------> gives negative value
2.Sensor must be placed at equidistant from all the lamps.
    exceptional case:- if we are getting more then number of light for a site,we can ignore
    if sensor is pointed perpendicular towards a light sourse,it will give highest value.(as per fig4,fig5 of datasheet)
3.All car walls must be of equal type(colour and texture).
4.reading should be taken during standby.(no load, door closed state)
5.Sensor and high reflective surface need to cleaned time to time.
6.If sensor placed on the top, after calibration make sure no object like chair or black surface present on the floor. 

'''
from typing import Any
from csv import reader

import time

import os, sys
sys.path.append(os.path.join("C:\\Users\\k64067997\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\yoctopuce"))
from yocto_api import *
from yocto_lightsensor import *

no_of_lights = 0
single_bulb_Lux = 0
offset = 0

#################### YOCTO SENSOR
errmsg = YRefParam()
if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
    sys.exit("init error" + errmsg.value)

def fetch_sensor_data():
    global offset
    SValue = 0

    # retreive any Light sensor
    sensor = YLightSensor.FirstLightSensor()
    if sensor is None:
        print('No module connected')
    if sensor.isOnline():
        i = 0
        while (i < 1000):
            SValue = SValue + int(sensor.get_currentValue())
            i += 1
    SValue /= 1000  # average of 1000 sample
    SValue = SValue - offset
    return SValue

###################################################################
def read_calibration(i):
    with open('Calibration.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if (row[0] == i):
                return row;
                time.sleep(1)

print("AUTO CALIBRATING")
row = read_calibration(input("Enter the site type:-"))
Total_Lux = float(row[1])
no_of_lights1 = float(row[2])
offset = float(row[3])
single_bulb_Lux = Total_Lux / no_of_lights1
print("Total Lux value is:-", Total_Lux)
print("Number of Lamps Present:-", no_of_lights1)
print("Offset value of the site:-", offset)
print("Single lamp lux is:", single_bulb_Lux)
#######################################################################
while(1):
    SValue = fetch_sensor_data()

    # Dynamically calculate offset value
    Dynamic_offset = SValue - Total_Lux
    if(Dynamic_offset > single_bulb_Lux):
        SValue = SValue - Dynamic_offset
    ##################################################################

    no_of_lights = SValue / single_bulb_Lux
    Deviation = no_of_lights - int(no_of_lights)

    if(Deviation > (.6)):                       #60% MORE LIGHT lux w.r.t calculated number of light present
        no_of_lights = int(no_of_lights) + 1
        print("no of light is:-",no_of_lights)
    elif(Deviation >= 0):                       #lux is bit higher for actual number of light present
        no_of_lights = int(no_of_lights)
        if(no_of_lights > 0):
            print("no of light is:-",no_of_lights)

    if (SValue < offset):                       #this will only work if we calibrate with ambient lights
        no_of_lights = 0
        print("                     All lights OFF")
        if(SValue == -offset):
            print("                                   Ambient light Absent")


print("This printed only during exit")
YAPI.FreeAPI()
