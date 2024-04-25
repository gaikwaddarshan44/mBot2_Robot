import time
from mbot2 import mBot2  # Import the mBot2 library
from cyberpi import display  # Import the CyberPi display module

# Initialize the mBot2 instance
bot = mBot2()

# Define the threshold distance for ultrasonic sensor (in centimeters)
ULTRASONIC_THRESHOLD_DISTANCE = 50  # Adjust as needed

# Define the button pin
BUTTON_PIN = 7  # Example pin number, adjust as needed

# Define the main function
def main():
    # Flag to track if button is pressed
    button_pressed = False
    
    # Flag to track if human is detected
    human_detected = False
    
    # Timestamp when button is pressed
    button_press_time = None
    
    # Continuously patrol around the desk
    while True:
        # Check if button is pressed
        if bot.read_digital_sensor(BUTTON_PIN) == 1:
            if not button_pressed:
                button_press_time = time.time()
                button_pressed = True
            else:
                # Check if button has been pressed for 3 seconds
                if time.time() - button_press_time >= 3:
                    # Stop beeping and exit the loop
                    break
        else:
            button_pressed = False
        
        # Detect human presence using camera (simulated)
        human_detected = detect_human_with_camera()  # Simulated function
        
        # Check if human is detected
        if human_detected:
            # Stop moving and play beep sound until button is pressed for 3 seconds
            bot.stop()
            while not button_pressed:
                bot.play_tone(frequency=1000, duration=200)  # Adjust frequency and duration as needed
                time.sleep(0.2)  # Pause between beeps
                
                # Display message on CyberPi LED matrix
                display.show("Human detected!", delay=0.5)  # Display message for 0.5 seconds
                display.clear()  # Clear the display
                
                if bot.read_digital_sensor(BUTTON_PIN) == 1:
                    if not button_pressed:
                        button_press_time = time.time()
                        button_pressed = True
                    else:
                        # Check if button has been pressed for 3 seconds
                        if time.time() - button_press_time >= 3:
                            # Stop beeping and exit the loop
                            break
        else:
            # Move forward
            bot.forward(speed=50)  # Adjust speed as needed
        
        # Wait before checking again
        time.sleep(0.5)  # Adjust as needed

# Simulated function to detect human presence using camera
def detect_human_with_camera():
    # Simulate camera detection
    # Replace this with actual code to detect human using camera
    # Return True if human is detected, False otherwise
    return False  # Placeholder for simulation

# Entry point of the program
if __name__ == "__main__":
    main()
