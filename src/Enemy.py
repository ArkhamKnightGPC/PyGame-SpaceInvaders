import pygame

from GameAsset import GameAsset

class Enemy(GameAsset):

    def __init__(self, enemyImg, enemyX, enemyY):
        super().__init__(enemyImg, enemyX, enemyY)
        self.goRight = True
        self.inAction = True
        
    def updatePosition(self):
        enemydX, enemydY = 0, 0
        if self.goRight:
            if self.x >= 580:
                self.goRight = False
                enemydY = 2
            else:
                enemydX = 2
        else:
            if self.x <= -4:
                self.goRight = True
                enemydY = 2
            else:
                enemydX = -2
        self.x, self.y = self.x + enemydX, self.y + enemydY
        
    def draw(self, screen):
        if self.inAction:
            super().draw(screen)