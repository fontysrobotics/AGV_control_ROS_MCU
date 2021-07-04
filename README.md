# DACS AGV software for circuit python 

This code is used for the DACS project. 

## Preface
The DACS project is a Fontys university project, this project is related to the Adaptive robotics minor. DACS focusses on robotic cleaning solutions for offices and hotels. This code is used for the control unit of the DACS AGV, the AGV is a inhouse developed robot platform. On this platform cleaning solutions like plinth cleaning can be implemented. The navigation and user interface of the interface is prossesed in a industrial computer in the AGV. The control and processing of all the sensors and actuators in the AGV are controlled with a MCU, this code is used to program the MCU. 
 
## Table of Contents
- [Code description](#code-description)
    - [Main program](#main-program-code.py)
    - [Statemachine](#statemachine)
    - [Objects](#objects)
        - [Motordriver](#motordriver)
        - [IR sensor](#ir-sensor)
        - [Communication](#communication)
        - [LED](#led)
- [Getting Started](#getting-started)
    - [Dependencies](#dependencies)
    - [Installing](#installing)
    - [Executing Program](#executing-program)

## Code description

An in-depth paragraph about your project and overview of use.

### Main program code.py
The code.py is the main file that runs in the circuitpython MCU, in the file all the objects are instatiated and runs the statemachine.

### Statemachine
The state machine has 5 states, in the entry of each state the LED of the AGV change of color and the the MCU sends a status message to the master. This stateflow is recreated in the code.py file.
![alt text](https://github.com/fontysrobotics/AGV_control_ROS_MCU/blob/master/StateMachineMCU.png?raw=true)

### Objects
The program uses a few self made object files to keep the code clean and reusable. 

#### Motordriver
The motordriver can be used for controlling motors, it controls the speed of the motors and gives the speed feedback by using the encoders of the motor.

#### IR sensor
The IR sensors are analog sensors for measuring distance, here the signal is converted to a distance.

#### communication
We use two different communication protocols in the code, serial and UART. The serial is used to communicate with the main processing unit in the form of a industrial computer. We send important data to the master and recieve commands as the speed and direction and start and stop command. 

#### LED
The LED is used for safety and visual feedback of the AGV, for each state the LED has a different color, the control of these LED dependent on the state is controlled in this object.

## Getting Started
Install the circuitpython extension in visual studio code by typing circuit python in the vs code extensions tab and clicking on install. Make sure to install python with pip3.

### Dependencies

* python 3 and pip3 
* visual studio code with cirquitpython library
* circuitpython compatible MCU for deploying

### Installing
Install all the circuitpython adafruit bundles below for pip below 
```
pip3 install adafruit-circuitpython-lis3dh
```
```
pip3 install --user circup && circup install adafruit-circuitpython-register
```
```
pip3 install adafruit-circuitpython-mcp9808
```
```
pip3 install adafruit-circuitpython-hcsr04
```
```
pip3 install adafruit-circuitpython-ina260
```
```
pip3 install adafruit-circuitpython-neopixel
```
* Any modifications needed to be made to files/folders

### Executing program

To start the program connect the circuit python device to your computer. Make sure to download the .UF2 for the right device on the cicuit python downloads website. Drop the .UF2 file in the external drive that appears in your folder when the device is connected to your computer. Now the folder changes in "CIRCUITPY". Drop all the files in the repository in this folder. Open VS code and open this folder as workspace. Run the program with the serial monitor.

## Author
Dirk Remie 

student nr: 3597571

Organisation: Fontys University, minor AR 

Eindhoven, Juli 2021

