#NOT FINISHED YET

import curses
import random
import time
from curses import wrapper

def main(stdscr):

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()

    sh, sw = 20, 90
    win = curses.newwin(sh + 1, sw + 1, 0, 0)
    win.nodelay(True)
    win.timeout(70)
    win.border()
    win.keypad(True)

    player_pos = [sh//2, sw//16]
    enemies = []
    asteroids = []
    bullets = []
    enemy_bullets = []
    spawn_timer, points = 0, 0
    def spawn_enemies():
        return [random.randint(1, sh - 1), sw - 1]
    def spawn_asteroids():
        return [random.randint(1, sh - 1), sw - 1]
    def spawn_bullets():
        win.addch(player_pos[0], player_pos[1], '-')

    while True:
        win.erase()
        win.border()

        spawn_timer += 1
        if spawn_timer >= 10:
            enemies.append(spawn_enemies())
            asteroids.append(spawn_asteroids())
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
        for i in asteroids[:]:
            win.addch(i[0], i[1], '@')
            i[1] -= 1
            if i[1] <= 0:
                asteroids.remove(i)
            elif i == player_pos:
                win.addstr(sh//2, sw//2, "GAME OVER!")
                win.addstr(sh//1, sw//2, "Points: " + str(points))
                win.refresh()
                curses.napms(3500)
                return
        for i in bullets[:]:
            if i[1] < sw - 1:
                win.addch(i[0], i[1], '-')
                i[1] += 1
            else:
                bullets.remove(i)
        for i in bullets[:]:
            if i in asteroids:
                asteroids.remove(i)
                bullets.remove(i)
                points += 1
            elif i in enemies:
                enemies.remove(i)
                bullets.remove(i)
                points += 2
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
        elif key == ord(' '):
            bullets.append([player_pos[0], player_pos[1] + 1])


curses.wrapper(main)

