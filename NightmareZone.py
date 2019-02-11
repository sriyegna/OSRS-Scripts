import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random

##Have runelite XP tab open to offset the inventory left

button = Button.left
mouse = Controller()

# Coordinates of the items
coords = [[[1467, 786], [1485, 807]], [[1509, 786], [1527, 807]], [[1551, 786], [1569, 807]], [[1593, 786], [1608, 807]],
          [[1593, 820], [1608, 844]], [[1551, 820], [1569, 844]], [[1509, 820], [1527, 844]], [[1467, 820], [1485, 844]],
          [[1467, 856], [1485, 877]], [[1509, 856], [1527, 877]], [[1551, 856], [1569, 877]], [[1593, 856], [1608, 877]],
          [[1593, 893], [1608, 915]], [[1551, 893], [1569, 915]], [[1509, 893], [1527, 915]], [[1467, 893], [1485, 915]]]

##Randomize the interval for mouse movements, then increment ycoord by old-new/interval
time.sleep(200)

#loop through up to 16 items (*15*) and drink each potion 4 times
for i in range(0, 14):
    print("Pot: " + str(i+1))
    for j in range(0, 4):
        xcoord = random.randint(coords[i][0][0], coords[i][1][0])
        ycoord = random.randint(coords[i][0][1], coords[i][1][1])
        
        mouse.position = (xcoord, ycoord)
        mouse.click(button)
        print(j+1)
        
        sleeptime = random.randint(250, 330) #110 - 250
        #sleeptime = 70 + random.randint(1, 5) - random.randint(1, 10) #for prayer
        
        #Alert for upcoming click
        print("Going to sleep for: " + str(sleeptime) + " seconds.")
        for k in range(sleeptime, 0, -1):
            if (k == 30):
                print("30s left.")
            elif (k == 20):
                print("20s left.")                
            elif (k == 10):
                print("10s left.")                                
            time.sleep(1)
    
        #Random wait that isnt a whole integer
        time.sleep(random.random())        

    
