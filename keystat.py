import curses
from pynput.keyboard import Key, Listener

def drawUi(stdscr):
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

curses.wrapper(drawUi)

def on_press(key):
    print(key)
with Listener(on_press=on_press) as listener:
    listener.join()