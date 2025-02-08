import pygame

from GameAsset import GameAsset
from Bullet import Bullet

class Player(GameAsset):

    def __init__(self, playerImg, playerX, playerY, playerSpeed):
        super().__init__(playerImg, playerX, playerY)
        self.playerSpeed = playerSpeed
        self.bullets = []

    def updatePosition(self, event, mixer):
        playerdX, playerdY = 0, 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerdX = -self.playerSpeed
            if event.key == pygame.K_RIGHT:
                playerdX = self.playerSpeed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerdX = 0
            if event.key == pygame.K_SPACE:
                bullet = Bullet(pygame.image.load("assets/bullet.png"), self.x, self.y)
                mixer.Sound("assets/laser.wav").play()
                self.bullets.append(bullet)
        self.x, self.y = self.x + playerdX, self.y + playerdY
        for bullet in self.bullets:
            bullet.updatePosition()
    
    def draw(self, screen):
        super().draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)