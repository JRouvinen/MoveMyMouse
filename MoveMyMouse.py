# This is a simple py script to move your mouse

# imports
import mouse
import keyboard
import time

# Mouse commands

# left click -> mouse.click('left')

# right click -> mouse.click('right')

# middle click -> mouse.click('middle')

# drag from (0, 0) to (100, 100) relatively with a duration of 0.1s -> mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)

# move 100 right & 100 down -> mouse.move(100, 100, absolute=False, duration=0.2)

# make a listener when left button is clicked -> mouse.on_click(lambda: print("Left Button clicked."))
# make a listener when right button is clicked -> mouse.on_right_click(lambda: print("Right Button clicked."))

# remove the listeners when you want -> mouse.unhook_all()

# scroll down -> mouse.wheel(-1)

# scroll up -> mouse.wheel(1)

global version
version = '0.1'


def checktime(start, target):
    now = time.time()
    diff = round(now - start, 0)
    if diff >= float(target):
        return False
    else:
        return True


def movemouse(target):
    if target == 9999999999:
        print(f'[!] Moving mouse for you until you stop me...')
    else:
        print(f'[!] Moving mouse for you for {target} seconds -->')

    print('[>] (Press any key to stop)')
    run_script = True
    time_start = time.time()
    try:
        while run_script is True and keyboard.is_pressed('space') is False:
            # move 100 down
            mouse.move(0, 100, absolute=False, duration=1)
            # mouse left click
            mouse.click('left')
            time.sleep(0.2)
            if checktime(time_start, target) is False:
                run_script = False
            # scroll down
            mouse.wheel(-2)
            time.sleep(0.2)
            # move 100 up
            mouse.move(0, -100, absolute=False, duration=1)
            # mouse left click
            mouse.click('left')
            time.sleep(0.2)
            # scroll up
            mouse.wheel(2)
            time.sleep(0.2)
            if checktime(time_start, target) is False:
                run_script = False
        print('[!] --- DONE! ---')

    except KeyboardInterrupt:
        print('[!] --- Keyboard interrupt! ---')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'### MoveMouse! [V{version}] ###')
    print('[?] How long i should move your mouse for you?')
    print(
        '[>] (s for seconds or m for minutes [example: 10s or 10m] \n or leave empty if i should move mouse until you '
        'stop me)')
    target = input('[-] Time to run:')
    if target == '':
        target = 9999999999
    elif target[-1:] == "m":
        target = int(target[:-1]) * 60
    else:
        target = int(target[:-1])
    movemouse(target)
