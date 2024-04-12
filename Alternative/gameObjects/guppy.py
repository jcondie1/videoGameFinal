from . import Mobile
from FSMs import WalkingFSM, AccelerationFSM
from utils import vec, RESOLUTION

from pygame.locals import *

import pygame
import numpy as np


class Guppy(Mobile):
   def __init__(self, position, parallax=1):
      super().__init__(position, "fish.png", parallax)
        
      # Animation variables specific to Guppy
      self.position = vec(RESOLUTION[0]/2-50, RESOLUTION[1]/2)
      self.framesPerSecond = 10 
      self.nFrames = 6
      #self.gravity = 100
      
      self.nFramesList = {
         "moving"   : 6,
         "standing" : 6
      }
      
      self.rowList = {
         "moving"   : 0,
         "standing" : 0
      }
      
      self.framesPerSecondList = {
         "moving"   : 8,
         "standing" : 2
      }
            
      self.FSManimated = WalkingFSM(self)
      self.LR = AccelerationFSM(self, axis=0)
      self.UD = AccelerationFSM(self, axis=1)
      
      
   def handleEvent(self, event):
      if event.type == KEYDOWN:
            
         #if event.key == K_LEFT:
            #self.LR.decrease()
            
         #elif event.key == K_RIGHT:
            #self.LR.increase()

         if event.key == K_UP:
            self.UD.decrease()
         #elif event.key == K_DOWN:
            #self.UD.increase()
            
      elif event.type == KEYUP:
             
         #if event.key == K_LEFT:
            #self.LR.stop_decrease()
            
         #elif event.key == K_RIGHT:
            #self.LR.stop_increase()

         if event.key == K_UP:
            self.UD.stop_decrease()

         #elif event.key == K_DOWN:
            #self.UD.stop_increase()
   
   def update(self, seconds): 
      self.LR.updateState()
      self.UD.updateState()
      
      self.LR.update(seconds)
      #self.UD.accel += self.gravity
      self.UD.update(seconds*100)

      #if self.position[1] > RESOLUTION[1]:
         #self.position[1] = RESOLUTION[1]
         #self.UD.accel = 0
      
      super().update(seconds)

   def getCollisionRect(self):
        newRect =  pygame.Rect(0,0, 70, 40)
        newRect.left = int(self.position[0]+20)
        newRect.top = int(self.position[1]+20)
        return newRect
   
   
  