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
- [Getting Started](#getting-started)
    - [Dependencies](#dependencies)
    - [Installing](#installing)
    - [Executing Program](#executing-program)

## Code description

An in-depth paragraph about your project and overview of use.

### Main program code.py

### Statemachine
![alt text](https://github.com/fontysrobotics/AGV_control_ROS_MCU/blob/master/StateMachineMCU.png?raw=true)

### Objects

#### Motordriver

#### IR sensor


## Getting Started
Install the circuitpython extension in visual studio code 

### Dependencies

* python 3 and pip3 
* visual studio code with cirquitpython library
* Adafruit Grand Central M4 Express MCU for deploying

### Installing
Install all the circuitpython adafruit bundles below for pip below 
```
pip3 install adafruit-circuitpython-lis3dh
```
pip3 install --user circup && circup install adafruit-circuitpython-register
```
pip3 install adafruit-circuitpython-mcp9808
```
```
pip3 install adafruit-circuitpython-hcsr04
```
```
pip3 install adafruit-circuitpython-ina260
```
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Author
Dirk Remie 

student nr: 3597571

Organisation: Fontys University, minor AR 

Eindhoven, Juli 2021

