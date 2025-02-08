import pygame
import random

from Player import Player
from Enemy import Enemy
from CollisionDetection import isCollision

pygame.init()
screen = pygame.display.set_mode(size=(640, 480))

#window title, icon, background image, score text, game over text
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("assets/background.png")
score = 0
scoreFont = pygame.font.Font("freesansbold.ttf", 32)
scoreX, scoreY = 10, 10
gameOverFont = pygame.font.Font("freesansbold.ttf", 72)
gameOverStr = "GAME OVER!"
gameOverX, gameOverY = 220, 200
gameOver = False

#player
playerImg = pygame.image.load("assets/player.png")
playerX, playerY = 300, 400
playerSpeed = 6
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

    if gameOver:

        gameOverText = scoreFont.render(gameOverStr, True, (255,255,255))
        screen.blit(source=gameOverText, dest=(gameOverX, gameOverY))

        scoreText = scoreFont.render("Score: " + str(score), True, (255,255,255))
        screen.blit(source=scoreText, dest=(gameOverX + 35, gameOverY + 72))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                enemies.clear()
                player.bullets.clear()
                gameOver = False
            #check if QUIT button was pressed
            if event.type == pygame.QUIT:
                running = False

    else:
        for event in pygame.event.get():
            player.processEvent(event, mixer)
            #check if QUIT button was pressed
            if event.type == pygame.QUIT:
                running = False

        #update player position        
        player.updatePosition()

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
                if isCollision(player, enemy):
                    gameOver = True
                    gameOverStr = "GAME OVER!"

        #generate new enemies
        if enemyCount < 8 and random.uniform(0, 1) > 0.93:
            enemies.append(Enemy(enemyImg, random.randint(40, 460), random.randint(40, 250)))
        
        #graw game assets
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        #show player score
        score = len(enemies) - enemyCount
        if score > 200:
            gameOver = True
            gameOverStr = "MAX SCORE!!!"
        scoreText = scoreFont.render("Score: " + str(score), True, (255,255,255))
        screen.blit(source=scoreText, dest=(scoreX, scoreY))
        
    pygame.display.update()
