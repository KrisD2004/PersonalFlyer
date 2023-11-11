# Tello-Drone

## Tello Drone Control with Keyboard

This project demonstrates how to control a Tello drone using Python and the Tello SDK. It provides a simple keyboard interface to perform various drone actions such as takeoff, landing, moving up, moving forward, rotating clockwise, and performing flips.

## Prerequisites

Python 3.x
Tello drone connected to your computer's Wi-Fi
Installed tello_sdk and keyboard packages (install using pip install tello_sdk keyboard)

## Usage

1. Make sure your Tello drone is powered on and connected to your computer's Wi-Fi.

2. Open a terminal and navigate to the project directory.

3. Run the main.py script:

css
python main.py

4. Use the following keys to control the drone:

* 't': Take off and land
* 'u': Move up
* 'w': Move forward
* 's': move backward
* 'a': move left
* 'd': move right
* 'r': Rotate clockwise
* 'f': perfrom a flip
* 'c': circle object
* 'e': figure 8 pattern
* 'b': to barrel roll
* 'l': Perform a land
* 'q': Quit the program
* 'v' : to record vdeio

## Camera

* Used openCv to be able to get the camera to work. P.s. camera is laggy but it works!

* When you start stream it willl have add a file so delete the output.avi file when you done with the drone program. 