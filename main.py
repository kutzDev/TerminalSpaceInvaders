import curses
import random
import time
from curses import wrapper

def main(stdscr):

    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    stdscr.clear()
    stdscr.refresh()

    sh, sw = 20, 90
    win = curses.newwin(sh + 1, sw + 1, 0, 0)
    win.border()
    win.keypad(True)

    player_pos = [sh//2, sw//16]
    enemies = []
    spawn_timer = 0
    def spawn_enemies():
        y = random.randint(1, sh - 1)
        x = sw - 1
        return [y,x]


    while True:
        win.erase()
        win.border()

        spawn_timer += 1
        if spawn_timer == 10:
            new_enemie = spawn_enemies()
            enemies.append(new_enemie)
            spawn_timer = 0
        for i in enemies[:]:
            win.addch(i[0], i[1], '<')
            i[1] -= 1
            if i[1] <= 0:
                enemies.remove(i)
            elif i == player_pos:
                win.addstr(sh//2, sw//2, "GAME OVER!")
                win.refresh()
                curses.napms(3500)
                return
        win.addch(player_pos[0], player_pos[1], '>')
        win.refresh()

        key = win.getch()
        if key == ord('q') or key == ord('Q'):
            break
        elif key == ord('w') or key == ord('W'):
            if player_pos[0] > 1:
                player_pos[0] -= 1
        elif key == ord('s') or key == ord('S'):
            if player_pos[0] < sh - 1:
                player_pos[0] += 1

curses.wrapper(main)