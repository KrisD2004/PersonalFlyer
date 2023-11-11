from tello_sdk import Tello
import keyboard

# Initialize the Tello object
tello = Tello.Tello()

# Initialize the connection
tello.init()

# Function to go up
def move_up(x):
    response = tello.up(x)
    print(f"Go up {x} cm - Response: {response}")

# Function to go down
def move_down(x):
    response = tello.down(x)
    print(f"Go down {x} cm - Response: {response}")

# Function to go forwards
def move_forward(x):
    response = tello.forward(x)
    print(f"Go forward {x} cm - Response: {response}")

# Function to go backward
def move_backward(x):
    response = tello.back(x)
    print(f"Go backward {x} cm - Response: {response}")

# Function to go left
def move_left(x):
    response = tello.left(x)
    print(f"Go left {x} cm - Response: {response}")

# Function to go right
def move_right(x):
    response = tello.right(x)
    print(f"Go right {x} cm - Response: {response}")

# Function to rotate
def rotate(direction, degrees):
    response = tello.rotate(direction, degrees)
    print(f"Rotate {direction} {degrees} degrees - Response: {response}")

# Function to perform a flip
def flip(direction):
    response = tello.flip(direction)
    print(f"Perform a flip {direction} - Response: {response}")

# Function to turn off the lights
def set_light_off():
    response = tello.send_command("leds off")
    print("Set light off response:", response)

# Function to set the color of the LED
def set_light_color(r, g, b):
    response = tello.send_command(f"leds {r} {g} {b}")
    print(f"Set light color response:", response)

# Function to set the color of the LED and pulse
def set_light_pulse(r, g, b, p):
    response = tello.send_command(f"leds pulse {r} {g} {b} {p}")
    print(f"Set light pulse response:", response)

# Function to set the 2 colors of the LED to flash
def set_light_flash(r1, g1, b1, r2, g2, b2, f):
    response = tello.send_command(f"leds flash {r1} {g1} {b1} {r2} {g2} {b2} {f}")
    print(f"Set light flash response:", response)

# Main control loop
def main():
    print("Press the keys to control the Tello drone:")
    print("  - 'u' to go up")
    print("  - 'd' to go down")
    print("  - 'w' to go forward")
    print("  - 's' to go backward")
    print("  - 'a' to go left")
    print("  - 'f' to go right")
    print("  - 'r' to rotate (clockwise)")
    print("  - 'l' to rotate (counter-clockwise)")
    print("  - 'x' to perform a flip")
    print("  - 'o' to turn off the lights")
    print("  - 'c' to set light color to red")
    print("  - 'p' to set light to pulse in blue")
    print("  - 'k' to set light to flash between red and blue")
    print("  - 'q' to quit")

    while True:
        if keyboard.is_pressed('u'):
            move_up(50) 
        elif keyboard.is_pressed('d'):
            move_down(50) 
        elif keyboard.is_pressed('w'):
            move_forward(50) 
        elif keyboard.is_pressed('s'):
            move_backward(50)  
        elif keyboard.is_pressed('a'):
            move_left(50) 
        elif keyboard.is_pressed('f'):
            move_right(50)  
        elif keyboard.is_pressed('r'):
            rotate('cw', 90)  
        elif keyboard.is_pressed('l'):
            rotate('ccw', 90)  
        elif keyboard.is_pressed('x'):
            flip('f')  
        elif keyboard.is_pressed('o'):
            set_light_off()
        elif keyboard.is_pressed('c'):
            set_light_color(255, 0, 0)  
        elif keyboard.is_pressed('p'):
            set_light_pulse(0, 0, 255, 2)  
        elif keyboard.is_pressed('k'):
            set_light_flash(255, 0, 0, 0, 0, 255, 1)  # Red and blue colors with 1Hz flash
        elif keyboard.is_pressed('q'):
            break

if __name__ == "__main__":
    main()
