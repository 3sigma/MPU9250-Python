# coding: utf-8
# Code original: https://github.com/FaBoPlatform/FaBo9AXIS-MPU9250-Python
#

import time
import sys

from mpu9250 import MPU9250
imu = MPU9250(i2cbus=1, address=0x69)

while True:
    time.sleep(0.5)
    try:
            accel = imu.readAccel()
            print " ax = " , ( accel['x'] )
            print " ay = " , ( accel['y'] )
            print " az = " , ( accel['z'] )

            gyro = imu.readGyro()
            print " gx = " , ( gyro['x'] )
            print " gy = " , ( gyro['y'] )
            print " gz = " , ( gyro['z'] )

            mag = imu.readMagnet()
            print " mx = " , ( mag['x'] )
            print " my = " , ( mag['y'] )
            print " mz = " , ( mag['z'] )
            print


    except KeyboardInterrupt:
        sys.exit(0)

    except:
        print "Probleme lecture IMU"
    