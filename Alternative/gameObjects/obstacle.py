import pygame

from utils.constants import ACCEL
from . import Mobile
from utils import vec, RESOLUTION
from random import randint

class Obstacle(Mobile):
    def __init__(self, sprite_sheet, n_frames):
        # Initialize position off-screen to the right
        #position = vec(RESOLUTION[0], randint(0, RESOLUTION[1]))
        position = vec(RESOLUTION[0]+50, RESOLUTION[1]/2)
        # Select a random part of the sprite sheet for this obstacle
        frame = randint(0, 2)
        frame2 = randint(0,1)

        super().__init__(position, sprite_sheet, 1, (frame, frame2))

        # Movement speed should match the background's scrolling speed
        self.velocity = -50  # Negative for leftward movement, adjust as needed
        self.offset = 0  # Initial offset

    def update(self, seconds):
        # Update the obstacle's position to move leftward with the background

        self.velocity -= ACCEL * seconds
        # Update offset with the new velocity
        self.offset += self.velocity * seconds

        # Update position using offset
        self.position[0] = RESOLUTION[0] + 50 + self.offset  # Adjust starting point as needed

        # Reset position and offset if the obstacle moves off-screen
        if self.position[0] < -self.getSize()[0]:
            self.position[0] = RESOLUTION[0]
            self.offset = 0
        super().update(seconds)
        """
        self.move_speed -= ACCEL * seconds
        self.position[0] += self.move_speed

        # If the obstacle moves off-screen to the left, you can reset or remove it
        if self.position[0] < -self.getSize()[0]:  # Assuming getSize() gives the obstacle's dimensions
            # Reset the position to the right side for continuous flow or handle removal
            self.position[0] = RESOLUTION[0]

        super().update(seconds)
        """
    def getCollisionRect(self):
        newRect =  pygame.Rect(65,55, 170, 280)
        newRect.left = int(self.position[0])
        newRect.top = int(self.position[1])
        return newRect
