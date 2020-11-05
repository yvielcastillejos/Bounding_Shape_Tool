import pygame
import sys
import random
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from scipy import ndimage
import os
from buttons import*
from boundbox import event, folder_img

def main():
    pygame.init()
    pygame.display.set_caption('Bound Shapes by YC')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size = (S_WIDTH+150,S_HEIGHT+50), flags = 0)
    surface = screen.convert()
    pictures = folder_img(dir)
    img_dir = None
    index, prevind = 0, 0
    if len(pictures) >  0:
        img_dir = pygame.image.load(f"/Users/yvielcastillejos/python/bounding_shape/images/{pictures[0]}")
        img_dir = pygame.transform.scale(img_dir,(500,500))

    r = pygame.Rect((20, 20),(S_WIDTH, S_HEIGHT))
    r1 = pygame.Rect((S_HEIGHT,0),(170,S_WIDTH + 150))
    r2 = pygame.Rect((0,S_WIDTH),(S_HEIGHT , 170))
    r3 = pygame.Rect((0,0),(20, S_WIDTH+170))
    r4 = pygame.Rect((0,0),(S_HEIGHT, 20))

    pygame.draw.rect(surface, clr2, r1)
    pygame.draw.rect(surface, clr2, r2)
    pygame.draw.rect(surface, clr2, r3)
    pygame.draw.rect(surface, clr2, r4)
    screen.blit(surface, (0,0))

    if img_dir != None:
         screen.blit(img_dir,(20,20))
    else:
         pygame.draw.rect(surface, clr2, r)
    draw_buttons(screen,8)
    text_render(surface, screen)
    pygame.display.update()

    pos = None
    todraw = []
    rad  = []
    redo, redorad = [], []

    myfont = pygame.font.SysFont("fontname", 50)
    while True:
         clock.tick(60)
         draw_buttons(surface,8)
         text_render(surface, surface)
         pos, todraw, rad,redo,redorad,index, prevind = event(surface, pos, todraw,rad, screen, redo,redorad, index,pictures, prevind)
         text1 = myfont.render("L1", 1, (96, 108, 118))

         if img_dir != None:
             img_dir = pygame.image.load(f"/Users/yvielcastillejos/python/bounding_shape/images/{pictures[index]}")
             img_dir = pygame.transform.scale(img_dir,(500,500))
             surface.blit(img_dir,(20,20))
             if index != prevind:
                 todraw, rad, redo, redorad = [],[],[],[]
                 draw_buttons(surface,100)
                 text_render(surface, surface)
                 screen.blit(surface, (0,0))
                 pygame.display.update()
                 prevind = index
         else:
             pygame.draw.rect(surface, clr2, r)
    return


if __name__ == "__main__":
    main()
