###############################################################################
#                                                                             #
#                      ──── LICENSE INFORMATION ────                          #
#                                                                             #
# This code is licensed under the MIT License.                                #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.                       #
#                                                                             #
# In addition, while it is not a requirement of the license, I would greatly  #
# appreciate it if you give credit to the author,                             #
# Andres A. Mercado-Velazquez, when using or distributing this code.          #
#                                                                             #
###############################################################################

# Note: Use Python 3 to run the code and enjoy!
# Note 2: Feel free to contact the author of this code by email at andres@mevel.com.mx

'''
Code for Raspberry Pi Zero W 2 that runs the following sensor:

    Grove - Gas Sensor V2 (Multichannel) - I2C

'''


'''
  DATE:             2024-May-31 5:18 PM London Time
  AUTHOR:           Andres A. Mercado-Velazquez
  LOCATION:         IoT Lab at Queen Mary University of London
  BOARD:            Raspberry Pi Zero W 2
  BOARD DOC:        https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/
                    https://pinout.xyz
  REPO/CODE:        https://github.com/AndresMercad0/RPi-MultichannelGasV2-PythonLib


  #################################################################################
  #                    CONNECTING DEVICES/SENSORS TO THE BOARD                    #
  #################################################################################

  ------------------------------------------------------------------------------------------------
                                            I2C
  ------------------------------------------------------------------------------------------------

  ------------- Grove - Gas Sensor V2 (Multichannel) - I2C -----------------------------------------------------------------------------------------------------------------
  * Pinout     =>      https://wiki.seeedstudio.com/Grove-Multichannel-Gas-Sensor-V2/
  * Source     =>      https://github.com/Seeed-Studio/Seeed_Arduino_MultiGas
  * Library    =>      python3-pip (sudo apt-get install python3-pip)
                                       |->  adafruit-circuitpython-busdevice (sudo pip3 adafruit-circuitpython-busdevice)
                                       |->  adafruit-circuitpython-board (sudo pip3 adafruit-circuitpython-board)
                                       |->  adafruit-blinka (sudo pip3 adafruit-blinka)

    Grove Multichannel gas V2         Raspberry Pi Zero W 2
        1 GND -------------------------- GND - Pin 6
        2 VCC -------------------------- 5V - Pin 4
        3 SDA -------------------------- SDA - Pin 3
        4 SCL -------------------------- SCL - Pin 5

'''

''' 
 * LIBRARIES *
'''
# General Purpose
import time
import board # I2C
import busio # I2C
# Grove - Gas Sensor V2 (Multichannel)
from MGSv2Lib.multichannel_gas_gmxxx import MultichannelGasGMXXX

'''
 *  INIT COMMUNICATIONS  *
'''
# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA) # Uses board.SCL and board.SDA
# Init Grove - Gas Sensor V2 (Multichannel)
sensor = MultichannelGasGMXXX(i2c)

def main():
    while True:
        
        print("-----------------------------------")

        ###########################################
        #  READ GROVE MULTICHANNEL GAS SENSOR V2  #
        ###########################################
        val = sensor.measure_no2()
        print(f"NO2: {val}  =  {sensor.calc_vol(val)}V")
        val = sensor.measure_c2h5oh()
        print(f"C2H5OH: {val}  =  {sensor.calc_vol(val)}V")
        val = sensor.measure_voc()
        print(f"VOC: {val}  =  {sensor.calc_vol(val)}V")
        val = sensor.measure_co()
        print(f"CO: {val}  =  {sensor.calc_vol(val)}V")


        # Wait before the next measurement
        time.sleep(2)


if __name__ == "__main__":
    main()
