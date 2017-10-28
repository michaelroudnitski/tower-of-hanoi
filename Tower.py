# ----------------------------------------#
# Michael Roudnitski
# Tower of Hanoi
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

complete = False
numDisks = disks
#---------------------------------------------------------------------------------------------------#
for i in range(disks):  # appends values into source list depending on how many disks the user chose
    source.append(numDisks)
    numDisks -= 1
#---------------------------------------------------------------------------------------------------#
def AB():
    """ Makes a legal move between source and temp
        if source is not empty and then temp is empty or last value of source < last value of temp
            Pops last item in source and appends it to temp
        or
        if temp is not empty and then source is empty or last value of temp < last value of source
            Pops last item in temp and appends it to source
    """
    if len(source) > 0 and (len(temp) == 0 or source[-1] < temp[-1]):
        temp.append(source.pop())
    elif len(temp) > 0 and (len(source) == 0 or temp[-1] < source[-1]):
        source.append(temp.pop())
#---------------------------------------------------------------------------------------------------#
def AC():
    """ Makes a legal move between source and destination
        if source is not empty and then dest is empty or last value of source < last value of dest
            Pops last item in source and appends it to dest
        or
        if dest is not empty and then source is empty or last value of dest < last value of source
            Pops last item in dest and appends it to source
    """
    if len(source) > 0 and (len(dest) == 0 or source[-1] < dest[-1]):
        dest.append(source.pop())
    elif len(dest) > 0 and (len(source) == 0 or dest[-1] < source[-1]):
        source.append(dest.pop())
#---------------------------------------------------------------------------------------------------#
def BC():
    """ Makes a legal move between temp and destination
        if source is not empty and then dest is empty or last value of temp < last value of dest
            Pops last item in source and appends it to dest
        or
        if dest is not empty and then temp is empty or last value of dest < last value of temp
            Pops last item in dest and appends it to temp
    """
    if len(temp) > 0 and (len(dest) == 0 or temp[-1] < dest[-1]):
        dest.append(temp.pop())
    elif len(dest) > 0 and (len(temp) == 0 or dest[-1] < temp[-1]):
        temp.append(dest.pop())
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
#---------------------------------------------------------------------------------------------------#
def is_done():
    """ Checks if the destination list is full (all values are stored in dest list)
        if it returns true, it breaks the loop

        source = []
        temp = []
        dest = [5,4,3,2,1]
        
        >>> is_done()
        All done!
        dest [5,4,3,2,1]

    """
    if len(dest) != disks:
        pass
    else:
        print "All done! "
        print "That only took ", steps, " steps"
        print "dest ", dest
        return True
#---------------------------------------------------------------------------------------------------#
def redraw_screen():
    pygame.event.clear()
    screen.fill(WHITE)
    #pegs
    pygame.draw.rect(screen, BLACK, ((WIDTH / 4) - 5, 200, 10, 380))
    pygame.draw.rect(screen, BLACK, ((WIDTH / 2) - 5, 200, 10, 380))
    pygame.draw.rect(screen, BLACK, (WIDTH - (WIDTH / 4) - 5, 200, 10, 380))
    # disks
    for i, val in enumerate(source):
        pygame.draw.rect(screen, RED, ((WIDTH / 4) - (val * 10), ground - (20 * i) - 40, (val * 10) * 2, 20))
    for i, val in enumerate(temp):
        pygame.draw.rect(screen, RED, ((WIDTH / 2) - (val * 10), ground - (20 * i) - 40, (val * 10) * 2, 20))
    for i, val in enumerate(dest):
        pygame.draw.rect(screen, RED, (WIDTH - (WIDTH / 4) - (val * 10), ground - (20 * i) - 40, (val * 10) * 2, 20))
    pygame.display.update()
    #time.sleep(0.1)
#---------------------------------------------------------------------------------------------------#
redraw_screen()
if disks % 2 == 0:  #check if number of disks are even or odd
    while complete is False:
        AB()  # make the legal move
        steps += 1 #increase step counter
        write()  # write current state of lists to console
        redraw_screen()  # draw everything
        if is_done():  # break the loop if we're done
            break

        AC()
        steps += 1
        write()
        redraw_screen()
        if is_done():
            break

        BC()
        steps += 1
        write()
        redraw_screen()
        if is_done():
            break

else:
    while complete is False:
        AC()
        steps += 1
        write()
        redraw_screen()
        if is_done():
            break
        
        AB()
        steps += 1
        write()
        redraw_screen()
        if is_done():
            break
        
        BC()
        steps += 1
        write()
        redraw_screen()
        if is_done():
            break

