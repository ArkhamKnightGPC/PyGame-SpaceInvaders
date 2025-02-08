import pygame
import random

from Player import Player
from Enemy import Enemy
from CollisionDetection import isCollision

pygame.init()
screen = pygame.display.set_mode(size=(640, 480))

#window title, icon, background image, score text position
font = pygame.font.Font('freesansbold.ttf', 32)
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("assets/background.png")
textX, textY = 10, 10

#player
playerImg = pygame.image.load("assets/player.png")
playerX, playerY = 300, 400
playerSpeed = 12
player = Player(playerImg, playerX, playerY, playerSpeed)

#enemy
enemyImg = pygame.image.load("assets/enemy.png")
enemies = []

#background music
mixer = pygame.mixer
mixer.music.load("assets/background.wav")
mixer.music.play(-1)

#game loop
running = True
while running:
    #screen.fill(color=(0, 150, 0))
    screen.blit(source=background, dest=(0,0))

    for event in pygame.event.get():
        #update player position
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            player.updatePosition(event, mixer)
        #check if QUIT button was pressed
        if event.type == pygame.QUIT:
            running = False
    
    #update enemy positions
    enemyCount = 0
    for enemy in enemies:
        if enemy.inAction:
            for bullet in player.bullets:
                if bullet.inAction and isCollision(bullet, enemy):
                    mixer.Sound("assets/explosion.wav").play()
                    enemy.inAction = False
                    break
            if enemy.inAction:
                enemyCount += 1
                enemy.updatePosition()

    #generate new enemies
    if enemyCount < 5 and random.uniform(0, 1) > 0.9:
        enemies.append(Enemy(enemyImg, random.randint(40, 460), random.randint(60, 230)))
    
    #graw game assets
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    #show player score
    score = font.render("Score: " + str(len(enemies) - enemyCount), True, (255,255,255))
    screen.blit(source=score, dest=(textX, textY))
    
    pygame.display.update()
