from utils import SpriteManager, SCALE, RESOLUTION, vec
from pygame import SRCALPHA

import pygame

class Drawable(object):
    
    CAMERA_OFFSET = vec(0,0)
    
    @classmethod
    def updateOffset(cls, trackingObject, worldSize):
        
        objSize = trackingObject.getSize()
        objPos = trackingObject.position
        
        offset = objPos + (objSize // 2) - (RESOLUTION // 2)
        
        for i in range(2):
            offset[i] = int(max(0,
                                min(offset[i],
                                    worldSize[i] - RESOLUTION[i])))
        
        cls.CAMERA_OFFSET = offset
        
        

    @classmethod    
    def translateMousePosition(cls, mousePos):
        newPos = vec(*mousePos)
        newPos /= SCALE
        newPos += cls.CAMERA_OFFSET
        
        return newPos
    
    def __init__(self, position=vec(0,0), fileName="", offset=None, parallax=1):
        if fileName != "":
            self.image = SpriteManager.getInstance().getSprite(fileName, offset)
        
        self.position=vec(*position)
        self.imageName = fileName
        self.flipImage = [False, False]
        self.parallax = parallax
    
    def draw(self, drawSurface):
        blitImage = self.image
      
        if self.flipImage[0] or self.flipImage[1]:
            blitImage = pygame.transform.flip(self.image, *self.flipImage)
        
        drawSurface.blit(blitImage,
                         list(map(int,
                                  self.position - Drawable.CAMERA_OFFSET* self.parallax)))
            
    def getSize(self):
        return vec(*self.image.get_size())    
   
    def getWidth(self):
        return self.getSize()[0]
    
    def getHeight(self):
        return self.getSize()[1]

    def getPosition(self):
        return self.position
    
    def handleEvent(self, event):
        pass
    
    def update(self, seconds):
        pass
      
    def getCollisionRect(self):
        newRect =  self.image.get_rect()
        newRect.left = int(self.position[0])
        newRect.top = int(self.position[1])
        return newRect
    
      
      