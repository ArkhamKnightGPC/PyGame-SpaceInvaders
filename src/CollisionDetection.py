import math

from GameAsset import GameAsset

def isCollision(asset1 : GameAsset, asset2 : GameAsset):
    distance = math.sqrt(math.pow(asset1.x - asset2.x, 2) + math.pow(asset1.y - asset2.y, 2))
    return distance < 27