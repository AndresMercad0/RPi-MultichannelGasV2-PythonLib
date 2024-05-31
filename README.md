# Grove - Multichannel Gas Sensor V2 on Raspberry Pi using Python

## Overview

This repository contains the code for using the Grove - Multichannel Gas V2 sensor with a Raspberry Pi Zero W 2. This applies to all Raspberry Pi models and uses the I2C protocol. The code is based on the C++ library for Arduino, published by Seeed Studio, available at https://github.com/Seeed-Studio/Seeed_Arduino_MultiGas.

The included instructions detail how to set up the sensor, connect it to the Raspberry Pi Zero W 2 (or any other Raspberry Pi model), and run the provided Python code to collect and display data from the gas sensor.

## Author Contact

Feel free to contact the author by email at andres@mevel.com.mx.

## Date and Location

- **Date:** 2024-May-31 5:42 PM London Time
- **Author:** Andres A. Mercado-Velazquez
- **Location:** IoT Lab at Queen Mary University of London

## Hardware Requirements

- **Raspberry Pi Zero W 2**
  - [Raspberry Pi Zero W 2 Documentation](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
  - [Raspberry Pi Pinout](https://pinout.xyz)

- **Grove - Multichannel Gas Sensor V2**
  - [Info](https://wiki.seeedstudio.com/Grove-Multichannel-Gas-Sensor-V2/)

## Software Requirements
- Python 3
- Required Python libraries (I2C):
  - `adafruit-circuitpython-busdevice`
  - `adafruit-circuitpython-board`
  - `adafruit-blinka`

## Setup and Wiring
```
    Grove Multichannel Gas V2         Raspberry Pi Zero W 2
        1 GND -------------------------- GND - Pin 6
        2 VCC -------------------------- 5V - Pin 4
        3 SDA -------------------------- SDA - Pin 3
        4 SCL -------------------------- SCL - Pin 5
```

## Execution
To run the code, ensure you have Python 3 installed along with the necessary libraries. You can install the required libraries using the following commands:

```bash
sudo apt-get install python3-pip
sudo pip3 install adafruit-circuitpython-busdevice
sudo pip3 install adafruit-circuitpython-board
sudo pip3 install adafruit-blinka
```
Execute the script with:
```bash
1. Clone this repo to your directory using the command “git clone https://github.com/AndresMercad0/RPi-MultichannelGasV2-PythonLib.git”.
2. Run the code with the command "python3 GroveMGSv2.py".
```

## To-do
- [x] Code in Python for Multichannel Gas Sensor V2 (I2C)
- [ ] Calibrate the sensor by code according to the calibration curve.
    - [ ] [Calibration_Curve_NO2](https://cnwinsen.com/wp-content/uploads/2021/08/MEMS-GM-102B-Manual-V2.1.pdf)
    - [ ] [Calibration_Curve_CO](https://www.winsen-sensor.com/d/files/gm-702b（ver2_2）manual.pdf)

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements
- **Veselin Hadzhiyski** (vcoder@abv.bg) for sharing his experience and help with the calibration curve.
- [paulvha](https://github.com/paulvha/multichannel-gasV2-on-raspberry) for inspiring this work with their contributions to the same task, but for C and C++ languages.


> [!NOTE]
> Although it is not a requirement of the license, the author, Andres A. Mercado-Velazquez, would appreciate it if you give credit when using or distributing this code.