import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random

##Auto alch with slightly random delay

delay = 0.1
button = Button.left

counter = 0
counterlimit = random.randint(25, 75)
xcoord = random.randint(1845, 1858)
ycoord = random.randint(753, 771)
mouse.position = (xcoord, ycoord)
while ((counter < counterlimit) and (ncounter < 1824)):
    counter = counter + 1
    counter = ncounter + 1
    print("Click #:", ncounter, ". Location Counter: ", counter, ". X: ", xcoord, ". Y: ", ycoord)
    mouse.click(button)
    time.sleep(2 + (random.random() / 10) - (random.random() / 10))