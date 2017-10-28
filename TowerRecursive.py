# ----------------------------------------#
# Michael Roudnitski
# Tower of Hanoi Recursive
# March 3, 2017
# ----------------------------------------#

import time
import pygame

pygame.init()

HEIGHT = 600
WIDTH = 1400
ground = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
#---------------------------------------------------------------------------------------------------#
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

disks = input("Enter the number of disks you would like in your tower... ")

steps = 0
source = []
temp = []
dest = []

numDisks = disks
#---------------------------------------------------------------------------------------------------#
for i in range(disks):  # appends values into source list depending on how many disks the user chose
    source.append(numDisks)
    numDisks -= 1
#---------------------------------------------------------------------------------------------------#
def write():
    """ Prints the value of the three lists (source, temp, dest)
        >>> write()
        source [5,4,3,2]
        temp [1]
        dest []
    """
    print "source ", source
    print "temp ", temp
    print "dest ", dest
    print " "
    redraw_screen()
#---------------------------------------------------------------------------------------------------#
def redraw_screen():
    pygame.event.clear()
    screen.fill(WHITE)
    #pegs-
    pygame.draw.rect(screen, BLACK, ((WIDTH/4) - 5, 200, 10, 380))
    pygame.draw.rect(screen, BLACK, ((WIDTH/2) - 5, 200, 10, 380))
    pygame.draw.rect(screen, BLACK, (WIDTH - (WIDTH/4) - 5, 200, 10, 380))
    #disks
    for i, val in enumerate(source):
        pygame.draw.rect(screen, RED, ((WIDTH / 4) - (val * 10), ground - (20 * i) - 40, (val * 10) * 2, 20))
    for i, val in enumerate(temp):
        pygame.draw.rect(screen, RED, ((WIDTH / 2) - (val * 10), ground - (20 * i) - 40, (val * 10) * 2, 20))
    for i, val in enumerate(dest):
        pygame.draw.rect(screen, RED, (WIDTH - (WIDTH / 4) - (val * 10), ground - (20 * i) - 40, (val * 10) * 2, 20))
    pygame.display.update()
    #time.sleep(0.1)
#---------------------------------------------------------------------------------------------------#
def movestack(disk, source, dest, temp):
    if disk == 1:
        dest.append(source.pop())
        write()
    else:
        movestack(disk - 1, source, temp, dest)
        write()
        dest.append(source.pop())
        write()
        movestack(disk - 1, temp, dest, source)
        write()
        
#---------------------------------------------------------------------------------------------------#
while len(dest) != disks:
    movestack(disks, source, dest, temp)

pygame.quit()
print "All done! "
print "dest ", dest