class GameAsset:

    def __init__(self, assetImg, assetX, assetY):
        self.img = assetImg
        self.x = assetX
        self.y = assetY

    def draw(self, screen):
        if self.x <= -4:
            self.x = -4
        if self.y >= 580:
            self.y = 580
        screen.blit(source=self.img, dest=(self.x, self.y))
