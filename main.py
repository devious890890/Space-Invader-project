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

bulletImg = pygame.imgae.load("bulent.jpg")
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED
bullet_state = 'ready'

scoreValue = 0
font = pygame.font.Font('freesanbold.ttf', 64)
textX = 10
textY = 10

overFont = pygame.font.Font('freesanbold.ttf', 64)

def showScore(x, y):
    score = font.render("Score:" + str (scoreValue), True, (255,255,255))
    screen.blit(score, (x, y))

def OverText():
    Overtext = overFont.render("GAME OVER", True, (255, 2555, 255))
    screen.blit(Overtext, (200, 500))

def player(x, y):
    screen.blit(playerImg, (x,y))

def enemy(x, y, i):
        screen.blit(enemyImg[i], (x,y))

def fire_bulet(x, y):
     global bulet_state
     bullet_state = 'fire'
     screen.blit(bulletImg, (x + 16, y +10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance  = math.sqrt((enemyX - bulletX)** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE