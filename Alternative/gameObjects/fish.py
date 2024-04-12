import random
import pygame
from FSMs.animation import WalkingFSM
from FSMs.movement import AccelerationFSM
from . import Mobile
from utils.constants import ACCEL  # Ensure ACCEL is defined as it is in platformer.py
from utils import vec, RESOLUTION

class Fish(Mobile):
    def __init__(self, position, parallax=1):
        self.initial_y_position = random.randint(0, RESOLUTION[1])
        position = vec(RESOLUTION[0], self.initial_y_position)

        super().__init__(position, "yellowFish.png", parallax)

        # Movement attributes
        self.velocity = -50  # Initial velocity, negative for moving left. Match this with the background's velocity.
        self.acceleration = ACCEL

    def update(self, seconds):
        #self.velocity -= ACCEL * seconds
        self.velocity -= self.acceleration * seconds

        # Move Fish from right to left at the updated velocity
        self.position[0] += self.velocity * seconds
        self.position[1] = self.initial_y_position

        super().update(seconds)

    def getCollisionRect(self):
        newRect =  pygame.Rect(0,0, 45, 35)
        newRect.left = int(self.position[0]+20)
        newRect.top = int(self.position[1]+15)
        return newRect