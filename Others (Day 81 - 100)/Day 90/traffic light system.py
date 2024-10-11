'''
    - Write a Python program to create a class that simulates a basic traffic light system 
      with methods to change and display the current light.
'''

import time
import threading

class TrafficLight:
    def __init__(self):
        self.colors = ["Red", "Green", "Yellow"]
        self.current_color = self.colors[0]
        self.timer = {"Red": 5, "Green": 5, "Yellow": 2}

    def change_light(self):
        while True:
            for color in self.colors:
                self.current_color = color
                print(f"Traffic Light: {self.current_color}")
                time.sleep(self.timer[color])

    def display_light(self):
        while True:
            print(f"Current Traffic Light: {self.current_color}")
            time.sleep(1)

def main():
    traffic_light = TrafficLight()
    change_thread = threading.Thread(target=traffic_light.change_light)
    display_thread = threading.Thread(target=traffic_light.display_light)

    change_thread.daemon = True
    display_thread.daemon = True

    change_thread.start()
    display_thread.start()

    while True:
        pass

if __name__ == "__main__":
    main()
