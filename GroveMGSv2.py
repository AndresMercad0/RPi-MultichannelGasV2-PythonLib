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


  #################################################################################
  #                               CALIBRATE SENSOR                                #
  #################################################################################
  by Veselin Hadzhiyski 2021 (vcoder@abv.bg)

  There are two important parameters:
   * R0 - Sensor resistance on ambient air. It is a constant value written in the sketch. Obtained through calibration.
   * RS_gas - sensor resistance on gas with some concentration. This value changes when the concentration changes.
   .--------------------------------------------------------------------------------------.
   | NOTE: During calibration, for better accuracy and results, use well ventilated room. |
   '--------------------------------------------------------------------------------------'
   * The Rs/R0 ratio correspond to the gas concentration. And for that are the calibration curves. The calibration curves are given in the wiki.

   How to calibrate?
   |
   '->  Run the sketch, wait the sensor to heat up (if it is first run of the sensor, you must preheat it for more than 72 hours.
        If it is already preheated, run it for few hours, to reach stable parameters), and read the R_gas value.
        Then, write the value to the R0 value in the sketch. Because the calibration curves are not linear, I use logarithmic function to receive the correct data in PPM in different points.
        Of course, there is some error in the different points, but it's enough accurate.
        And that's it! The sensor is ready for operation.

'''

'''
 * LIBRARIES *
'''
# General Purpose
import math
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

        
        '''
        -------------------------  PPM CO  -------------------------
        CO range: 0 - 1000 PPM
        Calibrated according calibration curve by Winsen: 0 - 150 PPM
        Calibration by Veselin Hadzhiyski 2021 (vcoder@abv.bg)

        RS/R0       PPM
        1           0
        0.77        1
        0.6         3
        0.53        5
        0.4         10
        0.29        20
        0.21        50
        0.17        100
        0.15        150
        '''
        print("----- PPM CO -----")
        sensorValue = sensor.measure_co()
        sensor_volt = sensor.calc_vol(sensorValue)
        print(f"CO: {sensorValue}  eq  {sensor_volt}V")

        RS_gas = (3.3-sensor_volt)/sensor_volt
        print(f"RS_gas: {RS_gas}")

        R0 = 31 # This value is obtained from the ambient air and must be determined through sensor calibration, as referenced in the code's initial comments.
        print(f"R0: {R0}")

        ratio =  RS_gas/R0
        print(f"ratio: {ratio}")
        
        lgPPM = (math.log10(ratio) * -3.82) - 0.66  # - 3.82) - 0.66; - default      - 2.82) - 0.12; - best for range up to 150 ppm
        PPM = pow(10,lgPPM)
        print(f"PPM: {PPM}")



        '''
        -------------------------  PPM NO2  -------------------------
        NO2 range: 0 - 10 PPM
        Calibrated according calibration curve by Winsen: 0 - 10 PPM
        Calibration by Veselin Hadzhiyski 2021 (vcoder@abv.bg)

        RS/R0       PPM
        1           0
        1.4         1
        1.8         2
        2.25        3
        2.7         4
        3.1         5
        3.4         6
        3.8         7
        4.2         8
        4.4         9
        4.7         10
        '''
        print("----- PPM NO2 -----")
        sensorValue = sensor.measure_no2()
        sensor_volt = sensor.calc_vol(sensorValue)
        print(f"NO2: {sensorValue}  eq  {sensor_volt}V")

        RS_gas = (3.3-sensor_volt)/sensor_volt
        print(f"RS_gas: {RS_gas}")

        R0 = 40 # This value is obtained from the ambient air and must be determined through sensor calibration, as referenced in the code's initial comments.
        print(f"R0: {R0}")

        ratio =  RS_gas/R0
        print(f"ratio: {ratio}")

        lgPPM = (math.log10(ratio) * + 1.9) - 0.2  # + 2   -0.3
        PPM = pow(10,lgPPM)
        print(f"PPM: {PPM}")



        # Wait before the next measurement
        time.sleep(2)


if __name__ == "__main__":
    main()
