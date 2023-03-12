import pygame
import sys
import random
from  config_3 import *
from  grass import Grass
from  road import Road
from car import Car
from bar import Bar
def bar_spawn(bars,y):
    coord=[200,325,450,575]
    random.shuffle(coord)
    for i in range(3):
        b=Bar(screen,coord[i],y)
        bars.append(b)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
grass=Grass("grass.jpg",screen,0,0)
grass_2=Grass("grass.jpg",screen,0,-1000)
road=Road("road_3.png",screen,150,0)
road_2=Road("road_3.png",screen,150,-1000)
car=Car("car.png",screen,(SCREEN_WIDTH)//2,(SCREEN_HEIGHT)//2)
bars1=[]
bars2=[]
bar_spawn(bars1,0)
bar_spawn(bars2,-SCREEN_HEIGHT//2)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for i in range(len(bars1)):
            bars1[i].update()
            if bars1[i].rect.y>SCREEN_HEIGHT:
                bars1.clear()
                bar_spawn(bars1,0)
        for i in range(len(bars2)):
            bars2[i].update()
            if bars2[i].rect.y>SCREEN_HEIGHT:
                bars2.clear()
                bar_spawn(bars2,0)
        #for i in range(len(bars1)):
            #if car.rect.colliderect(bars1[i]):
                
        grass.update()
        grass_2.update()
        road.update()
        road_2.update()
        car.update()
        screen.fill(BLACK)
        grass.draw()
        grass_2.draw()
        

        road.draw()
        road_2.draw()
        car.draw()
        for i in range(len(bars1)):
            bars1[i].draw()
            bars2[i].draw()
        pygame.display.update()
        clock.tick(FPS)
