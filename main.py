from enum import Enum
import pyautogui
import time
from PIL import Image
import os

class Status(Enum):
    NOTHING = 1
    MENU = 2
    NEXT = 3
    LEVEL_UP = 4
    CLICK = 5
    EXIT_SHOP = 6
    CONTINUE = 7
    PLAY_AGAIN = 8
    TO_BATTLE = 9
    FIGHT_AS_WAR = 10
    FIVE_WAVES = 11
    SKIP = 12
    QUEEN = 13

menu_path = "assets/menu.png"
next_path = "assets/next.png"
level_up_path = "assets/level_up.png"
click = "assets/click.png"
exit_shop = "assets/exit_shop.png"
continue_img = "assets/continue.png"
play_again = "assets/play_again.png"
to_battle = "assets/to_battle.png"
fight_as_war = "assets/fight_as_war.png"
five_waves = "assets/five_waves.png"
skip = "assets/skip.png"
queen = "assets/queen.png"

# map image path → (Status, confidence)
targets_war = [
    (menu_path, Status.MENU, 0.8),
    (next_path, Status.NEXT, 0.8),
    (level_up_path, Status.LEVEL_UP, 0.8),
    (click, Status.CLICK, 0.4),
    (exit_shop, Status.EXIT_SHOP, 0.8),
    (continue_img, Status.CONTINUE, 0.8),
    (play_again, Status.PLAY_AGAIN, 0.8),
    (to_battle, Status.TO_BATTLE, 0.8),
    (fight_as_war, Status.FIGHT_AS_WAR, 0.8),
    (five_waves, Status.FIVE_WAVES, 0.8),
    (skip, Status.SKIP, 0.8),
]

targets_queen = [
    (menu_path, Status.MENU, 0.8),
    (next_path, Status.NEXT, 0.8),
    (level_up_path, Status.LEVEL_UP, 0.8),
    (queen, Status.QUEEN, 0.8),
]

targets_mogg_leveling = [
    (menu_path, Status.MENU, 0.8),
    (next_path, Status.NEXT, 0.8),
    (level_up_path, Status.LEVEL_UP, 0.5),
]
def check_status(targets: list) -> Status:
    screenshot = pyautogui.screenshot()
    result = Status.NOTHING
    for path, status, conf in targets:
        try:
            if pyautogui.locate(path, screenshot, confidence=conf):
                return status
        except Exception as e:
            print(f"{status.name} not found: {e}")
    return result

def qeen_hybee():
    while True:
        time.sleep(0.3)
        result = check_status(targets_queen)
        if(result is Status.MENU):
            # First Spell
            pyautogui.moveTo(860, 465,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.NEXT):
            pyautogui.moveTo(958, 710,duration=0.2)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.leftClick()
        elif(result is Status.LEVEL_UP):
            pyautogui.moveTo(955, 527,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.QUEEN):
            # Qeen Hybee
            pyautogui.moveTo(635, 216,duration=0.2)
            pyautogui.leftClick()
def leveling_war():
    while True:
        time.sleep(0.3)
        result = check_status(targets_war)
        if(result is Status.MENU):
            # Attack
            pyautogui.moveTo(955, 324,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.NEXT):
            pyautogui.moveTo(958, 710,duration=0.2)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.leftClick()
            break
        elif(result is Status.LEVEL_UP):
            pyautogui.moveTo(955, 527,duration=0.2)
            pyautogui.leftClick()
            break
        elif(result is Status.CLICK):
            pyautogui.leftClick()
            pyautogui.leftClick()
            pyautogui.leftClick()
            pyautogui.leftClick()
            pyautogui.leftClick()
        elif(result is Status.EXIT_SHOP):
            pyautogui.moveTo(1586, 71,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.CONTINUE):
            pyautogui.moveTo(957, 254,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.PLAY_AGAIN):
            pyautogui.moveTo(967, 271,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.TO_BATTLE):
            pyautogui.moveTo(804, 638,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.FIGHT_AS_WAR):
            pyautogui.moveTo(802, 436,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.FIVE_WAVES):
            pyautogui.moveTo(816, 654,duration=0.2)
            pyautogui.leftClick()
        elif(result is Status.SKIP):
            pyautogui.moveTo(366, 59,duration=0.2)
            pyautogui.leftClick()
def leveling_shadow_roc():
    while True:
        # Visit specific neghbour click
        pyautogui.moveTo(1041, 988,duration=0.2)
        pyautogui.leftClick()
        # Items
        while True:
            time.sleep(0.5)
            result = check_status(targets_mogg_leveling)
            if(result is Status.MENU):
                # Sizzler Explosion
                pyautogui.moveTo(1004, 466,duration=0.2)
                pyautogui.leftClick()
            elif(result is Status.NEXT):
                pyautogui.moveTo(958, 710,duration=0.2)
                pyautogui.leftClick()
                time.sleep(0.5)
                pyautogui.leftClick()
                break
            elif(result is Status.LEVEL_UP):
                pyautogui.moveTo(955, 527,duration=0.2)
                pyautogui.leftClick()
                break

        # Enter house
        pyautogui.moveTo(882, 654,duration=0.2)
        pyautogui.leftClick()
        time.sleep(10)
        # Exit house
        pyautogui.moveTo(1511, 909,duration=0.2)
        pyautogui.leftClick()
        # Visit nehgour
        pyautogui.moveTo(1155, 993,duration=0.2)
        pyautogui.leftClick()
while True:
    # print(pyautogui.position())
    # time.sleep(1)

    # Give some time to open AQ
    time.sleep(3)
    # qeen_hybee()
    leveling_war()
    # leveling_shadow_roc()
