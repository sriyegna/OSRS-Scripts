import time
from threading import Thread
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random
import queue
import sys
from PIL import ImageGrab

q = queue.Queue()


def prayClicker():
    time.sleep(6)
    button = Button.left
    mouse = Controller()
    while (True):
        # Laptop Coords
        xcoord = random.randint(1705, 1720)
        ycoord = random.randint(110, 126)

        mouse.position = (xcoord, ycoord)
        mouse.click(button)
        time.sleep(0.4)
        mouse.click(button)

        sleeptime = random.randint(31, 54)  # 110 - 250

        # Alert for upcoming click
        print("P: Going to sleep for: " + str(sleeptime) + " seconds.")
        for k in range(sleeptime, 0, -1):
            if (k == 30):
                print("P: 30s left.")
            elif (k == 20):
                print("P: 20s left.")
            elif (k == 10):
                print("P: 10s left.")
            time.sleep(1)

        # Random wait that isnt a whole integer
        time.sleep(random.random())

def absorptionClicker():
    time.sleep(8)
    button = Button.left
    mouse = Controller()

    # Laptop coords
    # coords = [[[1301, 685], [1327, 706]], [[1342, 685], [1372, 706]], [[1385, 685], [1413, 706]],
    # [[1430, 685], [1449, 706]],
    # [[1301, 716], [1327, 743]], [[1342, 716], [1372, 743]], [[1385, 716], [1413, 743]],
    # [[1430, 716], [1449, 743]],
    # [[1301, 754], [1327, 776]], [[1342, 754], [1372, 776]], [[1385, 754], [1413, 776]],
    # [[1430, 754], [1449, 776]]]

    # Digital Ocean RDP Coords
    #coords = [[[1688, 934], [1711, 957]], [[1730, 934], [1752, 957]], [[1773, 934], [1796, 957]],
              #[[1813, 934], [1835, 957]],
              #[[1688, 970], [1711, 994]], [[1730, 970], [1752, 994]], [[1773, 970], [1796, 994]],
              #[[1813, 970], [1835, 994]]]

    for i in range(0, 7):
        print("Overload: " + str(i + 1))
        for j in range(0, 4):
            xcoord = random.randint(coords[i][0][0], coords[i][1][0])
            ycoord = random.randint(coords[i][0][1], coords[i][1][1])

            mouse.position = (xcoord, ycoord)
            mouse.click(button)
            print(j + 1)

            sleeptime = random.randint(311, 410)  # after 5 mins
            print("O: Going to sleep for: " + str(sleeptime) + " seconds.")
            for k in range(sleeptime, 0, -1):
                if (k == 30):
                    print("O: 30s left.")
                elif (k == 20):
                    print("O: 20s left.")
                elif (k == 10):
                    print("O: 10s left.")
                time.sleep(1)

            # Random wait that isnt a whole integer
            time.sleep(random.random())
    q.put("finished")
    
    
def overloadClicker(10):
    time.sleep(5)
    button = Button.left
    mouse = Controller()

    # Laptop coords
    # coords = [[[1301, 685], [1327, 706]], [[1342, 685], [1372, 706]], [[1385, 685], [1413, 706]],
    # [[1430, 685], [1449, 706]],
    # [[1301, 716], [1327, 743]], [[1342, 716], [1372, 743]], [[1385, 716], [1413, 743]],
    # [[1430, 716], [1449, 743]],
    # [[1301, 754], [1327, 776]], [[1342, 754], [1372, 776]], [[1385, 754], [1413, 776]],
    # [[1430, 754], [1449, 776]]]

    # Digital Ocean RDP Coords
    #coords = [[[1688, 934], [1711, 957]], [[1730, 934], [1752, 957]], [[1773, 934], [1796, 957]],
              #[[1813, 934], [1835, 957]],
              #[[1688, 970], [1711, 994]], [[1730, 970], [1752, 994]], [[1773, 970], [1796, 994]],
              #[[1813, 970], [1835, 994]]]

    for i in range(0, 7):
        print("Overload: " + str(i + 1))
        for j in range(0, 4):
            xcoord = random.randint(coords[i][0][0], coords[i][1][0])
            ycoord = random.randint(coords[i][0][1], coords[i][1][1])

            mouse.position = (xcoord, ycoord)
            mouse.click(button)
            print(j + 1)

            sleeptime = random.randint(311, 410)  # after 5 mins
            print("O: Going to sleep for: " + str(sleeptime) + " seconds.")
            for k in range(sleeptime, 0, -1):
                if (k == 30):
                    print("O: 30s left.")
                elif (k == 20):
                    print("O: 20s left.")
                elif (k == 10):
                    print("O: 10s left.")
                time.sleep(1)

            # Random wait that isnt a whole integer
            time.sleep(random.random())
    q.put("finished")


def aggroClicker():
    time.sleep(3)
    button = Button.left
    mouse = Controller()

    roald = [[155, 132, 25], [156, 124, 39], [25, 7, 3], [44, 12, 7], [155, 155, 141], [61, 17, 9]]
    kendal = [[34, 30, 20], [47, 42, 27], [39, 39, 19], [37, 33, 22], [33, 27, 14]]
    snake = [[180, 94, 46], [237, 125, 60], [149, 79, 38], [128, 67, 33], [239, 111, 54]]
    corsair = [[47, 5, 3], [101, 85, 5], [39, 7, 5], [160, 160, 147], [146, 146, 132]]
    vampire = [[9, 7, 7], [182, 158, 146], [89, 10, 5], [159, 132, 117], [25, 23, 23]]
    colours = roald + kendal + snake + corsair + vampire

    while (True):
        print("starting")
        image = ImageGrab.grab().convert('RGB')
        width, height = image.size
        
        #get middle 20%
        start_width = int((width/10) * 4)
        end_width = int((width/10) * 6)
        start_height = int((height/10) * 4)
        end_height = int((height/10) * 6)
        
        validPositions = []
        
        for y in range(start_height, end_height):
            for x in range(start_width, end_width):
                r, g, b = image.getpixel((x, y))
                for i in range(len(colours)):
                    if ((colours[i][0] == r) and (colours[i][1] == g) and (colours[i][2] == b)):
                        validPositions.append([x,y])
        print(validPositions)
        
        #overallSleeptime = random.randint(682, 794)
        overallSleeptime = random.randint(5, 15)
        print("Aggro: Going to sleep for: " + str(overallSleeptime) + " seconds.")
        time.sleep(overallSleeptime)
        time.sleep(random.random())



def main():
    aggroClicker()
    #prayThread = Thread(target=prayClicker, daemon = True)
    #prayThread.start()
    #overloadThread = Thread(target=overloadClicker, daemon = True)
    #overloadThread.start()
    aggroThread = Thread(target=aggroClicker, daemon = True)
    aggroThread.start()
    #while (True):
        #time.sleep(10)
        #isFinished = q.get()
        #if (isFinished == "finished"):
            #print("Finished")
            #sys.exit()


main()