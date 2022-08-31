from time import sleep
import keyboard
import mouse
import winsound

def press(key, message='Triggering keyboard event', hold_time=0.2, post_delay=1):
    print('{} (keyboard {})'.format(message, key))
    keyboard.press(key)
    sleep(hold_time)
    keyboard.release(key)
    sleep(post_delay)

def click(button='left', message='Triggering mouse event', hold_time=0.2, post_delay=1):
    print('{} (mouse {})'.format(message, button))
    mouse.press(button)
    sleep(0.2)
    mouse.release(button)
    sleep(post_delay)

def wheel(amount, message='Triggering wheel event', direction='up'):
    print('{} (wheel {} {} times)'.format(message, direction, amount))
    if direction == 'up':
        for i in range(amount):
            mouse.wheel(1)
            sleep(0.2)
    else:
        for i in range(amount):
            mouse.wheel(-1)
            sleep(0.2)

def item_menu(amount, message='Selecting item', direction='up'):
    keyboard.press('ctrl')
    sleep(0.2)
    wheel(amount, message=message, direction=direction)
    keyboard.release('ctrl')

# Enter quest
def enter_quest(quest_board_init):
    click()
    press('space', message='Selecting new quest', post_delay=3)
    if quest_board_init:
        press('space', message='Selecting master rank')
        press('w', message='Moving cursor to bottom')
        press('w', message='Moving cursor up')
    press('space', message='Selecting event quest')
    press('a', message='Moving to last page')
    press('w', message='Moving cursor to bottom')
    press('w', message='Moving cursor up')
    press('w', message='Moving cursor up')
    press('space', message='Selecting Fatalis quest')
    press('space', message='Confirming')
    press('space', message='Confirming', post_delay=4)
    press('space', message='Opening quest window')
    press('s', message='Moving cursor down')
    press('space', message='Starting quest')
    press('space', message='Confirming', post_delay=8)
    press('x', message='Skipping animation')

# Get material
def get_material():
    item_menu(3, message='Selecting mantel')
    press('e', message='Wearing mantel')
    press('w', message='Moving forward', hold_time=3, post_delay=2)
    press('f', message='Entering battle field', post_delay=17)
    item_menu(3, message='Selecting cat knife')
    press('space', message='Landing', post_delay=3)
    press('e', message='Stealing material', post_delay=8)

# Return from quest
def return_from_quest():
    press('esc', message='Opening main menu', post_delay=2)
    wheel(1, message='Selecting submenu', direction='down')
    press('j', message='Moving cursor down')
    press('j', message='Moving cursor down')
    press('space', message='Selecting return from quest')
    press('space', message='Confirming', post_delay=12)
    press('space', message='Confirming', post_delay=3)
    press('w', message='Moving cursor to bottom')
    press('space', message='Collecting material')
    press('a', message='Moving cursor left')
    press('space', message='Confirming', post_delay=3)
    press('space', message='Returning to village', post_delay=12)

# Move to quest board
def move_to_quest_board():
    press('d', message='Moving right', hold_time=2)
    press('w', message='Moving forward', hold_time=1)
    press('d', message='Moving right', hold_time=1)
    press('s', message='Moving backward', hold_time=1)

if __name__ == '__main__':
    frequency = 1000  # Set frequency to 1000 Hertz
    duration = 1000  # Set duration to 1000 ms == 1 second
    sleep(3)
    winsound.Beep(frequency, duration)

    quest_board_init = True
    for i in range(3):
        enter_quest(quest_board_init)
        get_material()
        return_from_quest()
        move_to_quest_board()
        quest_board_init = False
