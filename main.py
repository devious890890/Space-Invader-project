import pygame
import random
import math

SCREENWIDTH = 800
SCREENHEIGHT = 600
PLAYER_START_X = 370
PLAYER_START_Y = 300
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED = 10
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
background = pygame.image.load("background.jpg")
Caption = pygame.display.set_caption("Space Invaders")

playerImg  = pygame.image.load("rocket.jpg")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0 

enemyImg  = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for i in range (number_of_enemies):
    enemyImg.append(pygame.image.load("enemy.jpg"))
    enemyX.append(random.randint(0, SCREENWIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)