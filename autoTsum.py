import pyautogui
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')


pyautogui.FAILSAFE = True

GAME_REGION = ()               #(left, top, width, height)
TOP_PLAYER = ()
ALL_HEARTS = ()
PIC_FOLDER = 'screenshots\\'


def main():
    findGame()
    #scrollTop()
    sendHearts()

# Finding game region
def findGame():
    global GAME_REGION
    GAME_REGION = pyautogui.locateOnScreen(PIC_FOLDER + 'topLeft.png')

    logging.info('Locating tsum tsums game...')

    if GAME_REGION:
        
        logging.info('Game region found at '+ str(GAME_REGION))
        pyautogui.moveTo(GAME_REGION[0],GAME_REGION[1])
    else:
        logging.warning('No game found :(')

# Scroll to top
def scrollTop():
    global TOP_PLAYER
    TOP_PLAYER = pyautogui.locateOnScreen(PIC_FOLDER + 'Top.png')
    
    logging.info('Checking if at start of list...')
    pyautogui.PAUSE = 0.75
    
    if TOP_PLAYER:
        logging.info('Verified at top of list.')
    else:    
        logging.info('Scrolling up...')
        pyautogui.moveTo(GAME_REGION[0] + 300,GAME_REGION[1] + 300)
        pyautogui.dragRel(0,400,duration = 0.5)
        scrollTop()
        
def sendHearts():
    global ALL_HEARTS
    logging.info('Locating all hearts on screen...')
    pyautogui.PAUSE = 0.5

    #for heart in ALL_HEARTS:
    

main()
