import pygame

from GameAsset import GameAsset
from Bullet import Bullet

class Player(GameAsset):

    def __init__(self, playerImg, playerX, playerY, playerSpeed):
        super().__init__(playerImg, playerX, playerY)
        self.playerSpeed = playerSpeed
        self.bulletReady = False
        self.bullets = []
        self.playerdX, self.playerdY = 0, 0

    def processEvent(self, event, mixer):
        self.playerdX, self.playerdY = 0, 0
        if event.type == pygame.KEYDOWN:
            self.bulletReady = True
            if event.key == pygame.K_LEFT:
                self.playerdX = -self.playerSpeed
            if event.key == pygame.K_RIGHT:
                self.playerdX = self.playerSpeed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerdX = 0
            if event.key == pygame.K_SPACE and self.bulletReady:
                bullet = Bullet(pygame.image.load("assets/bullet.png"), self.x, self.y)
                mixer.Sound("assets/laser.wav").play()
                self.bullets.append(bullet)
                self.bulletReady = False

    def updatePosition(self):
        self.x, self.y = self.x + self.playerdX, self.y + self.playerdY
        for bullet in self.bullets:
            bullet.updatePosition()
    
    def draw(self, screen):
        super().draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)