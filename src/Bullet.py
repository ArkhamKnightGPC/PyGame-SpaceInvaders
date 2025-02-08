import pygame

from GameAsset import GameAsset

class Bullet(GameAsset):

    def __init__(self, bulletImg, bulletX, bulletY):
        super().__init__(bulletImg, bulletX, bulletY)
        self.bulletSpeed = 10
        self.inAction = True    
        
    def updatePosition(self):
        bulletdX, bulletdY = 0, 0
        if self.inAction:
            if self.y <= -4:
                self.inAction = False
            else:
                bulletdY -= self.bulletSpeed
        self.x, self.y = self.x + bulletdX, self.y + bulletdY
    
    def draw(self, screen):
        if self.inAction:
            super().draw(screen)
        