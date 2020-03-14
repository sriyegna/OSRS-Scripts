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
    time.sleep(12)
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
    time.sleep(9)
    button = Button.left
    mouse = Controller()

    # Laptop coords
    row1 = [[[1342, 540], [1372, 562]], [[1385, 540], [1413, 562]],
    [[1430, 540], [1449, 562]]]
    row2 = [[[1301, 577], [1327, 598]], [[1342, 577], [1372, 598]], [[1385, 577], [1413, 598]],
    [[1430, 577], [1449, 598]]]
    row3 = [[[1301, 612], [1327, 634]], [[1342, 612], [1372, 634]], [[1385, 612], [1413, 634]],
    [[1430, 612], [1449, 634]]]
    row4 = [[[1301, 650], [1327, 669]], [[1342, 650], [1372, 669]], [[1385, 650], [1413, 669]],
            [[1430, 650], [1449, 669]]]
    coords = row2 + row3 + row4

    # Digital Ocean RDP Coords
    #coords = [[[1688, 934], [1711, 957]], [[1730, 934], [1752, 957]], [[1773, 934], [1796, 957]],
              #[[1813, 934], [1835, 957]],
              #[[1688, 970], [1711, 994]], [[1730, 970], [1752, 994]], [[1773, 970], [1796, 994]],
              #[[1813, 970], [1835, 994]]]

    for i in range(0, len(coords)):
        print("Absorption: " + str(i + 1))
        for j in range(0, 4):
            xcoord = random.randint(coords[i][0][0], coords[i][1][0])
            ycoord = random.randint(coords[i][0][1], coords[i][1][1])

            mouse.position = (xcoord, ycoord)
            mouse.click(button)
            print(j + 1)

            sleeptime = random.randint(135, 182)  # after 2-3 mins
            print("A: Going to sleep for: " + str(sleeptime) + " seconds.")
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
    
    
def overloadClicker():
    time.sleep(15)
    button = Button.left
    mouse = Controller()

    # Laptop coords
    row5 = [[[1301, 685], [1327, 706]], [[1342, 685], [1372, 706]], [[1385, 685], [1413, 706]],
            [[1430, 685], [1449, 706]]]
    row6 = [[[1301, 716], [1327, 743]], [[1342, 716], [1372, 743]], [[1385, 716], [1413, 743]],
            [[1430, 716], [1449, 743]]]
    row7 = [[[1301, 754], [1327, 776]], [[1342, 754], [1372, 776]], [[1385, 754], [1413, 776]],
            [[1430, 754], [1449, 776]]]
    coords = row5 + row6

    # Digital Ocean RDP Coords
    #coords = [[[1688, 934], [1711, 957]], [[1730, 934], [1752, 957]], [[1773, 934], [1796, 957]],
              #[[1813, 934], [1835, 957]],
              #[[1688, 970], [1711, 994]], [[1730, 970], [1752, 994]], [[1773, 970], [1796, 994]],
              #[[1813, 970], [1835, 994]]]

    for i in range(0, len(coords)):
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
    time.sleep(6)
    button = Button.left
    mouse = Controller()

    roald = [[155, 132, 25], [156, 124, 39], [25, 7, 3], [44, 12, 7], [155, 155, 141], [61, 17, 9]]
    kendal = [[34, 30, 20], [47, 42, 27], [39, 39, 19], [37, 33, 22], [33, 27, 14]]
    snake = [[180, 94, 46], [237, 125, 60], [149, 79, 38], [128, 67, 33], [239, 111, 54]]
    corsair = [[47, 5, 3], [101, 85, 5], [39, 7, 5], [160, 160, 147], [146, 146, 132]]
    vampire = [[9, 7, 7], [182, 158, 146], [89, 10, 5], [159, 132, 117], [25, 23, 23]]
    #colours = roald + kendal + snake + corsair + vampire
    colours = vampire

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
        
        foundone = False
        
        for y in range(start_height, end_height):
            for x in range(start_width, end_width):
                r, g, b = image.getpixel((x, y))
                for i in range(len(colours)):
                    if ((colours[i][0] == r) and (colours[i][1] == g) and (colours[i][2] == b)):
                        validPositions.append([x,y])
                        foundone = True
                        break;
                if (foundone == True):
                    break;
            if (foundone == True):
                break;
        print(validPositions)
        monsterToClick = random.randrange(0, len(validPositions))
        print(validPositions[monsterToClick])
        mouse.position = (validPositions[monsterToClick][0], validPositions[monsterToClick][1])
        mouse.click(button)        
        
        
        overallSleeptime = random.randint(682, 794)
        #overallSleeptime = random.randint(5, 15)
        print("Aggro: Going to sleep for: " + str(overallSleeptime) + " seconds.")
        time.sleep(overallSleeptime)
        time.sleep(random.random())



def main():
    #prayThread = Thread(target=prayClicker, daemon = True)
    #prayThread.start()
    #overloadThread = Thread(target=overloadClicker, daemon = True)
    #overloadThread.start()
    #absorptionThread = Thread(target=absorptionClicker, daemon = True)
    #absorptionThread.start()    
    aggroThread = Thread(target=aggroClicker, daemon = True)
    aggroThread.start()
    while (True):
        time.sleep(10)
        isFinished = q.get()
        if (isFinished == "finished"):
            print("Finished")
            sys.exit()


main()