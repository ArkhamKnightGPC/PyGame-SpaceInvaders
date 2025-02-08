import pygame

from GameAsset import GameAsset

class Enemy(GameAsset):

    speedX, speedY = 4, 10

    def __init__(self, enemyImg, enemyX, enemyY):
        super().__init__(enemyImg, enemyX, enemyY)
        self.goRight = True
        self.inAction = True
        
    def updatePosition(self):
        enemydX, enemydY = 0, 0
        if self.goRight:
            if self.x >= 580:
                self.goRight = False
                enemydY = Enemy.speedY
            else:
                enemydX = Enemy.speedX
        else:
            if self.x <= -4:
                self.goRight = True
                enemydY = Enemy.speedY
            else:
                enemydX = -Enemy.speedX
        self.x, self.y = self.x + enemydX, self.y + enemydY
        
    def draw(self, screen):
        if self.inAction:
            super().draw(screen)