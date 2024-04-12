
from gameObjects import Guppy, Drawable
from gameObjects.fish import Fish
from gameObjects.fish2 import Fish2
from gameObjects.fish3 import Fish3
from gameObjects.obstacle import Obstacle
from utils import vec, RESOLUTION, WORLD_SIZE, ACCEL

from random import randint, choice
import pygame

from utils.vector import rectAdd

class GameEngine(object):
    def __init__(self):

        # for sound effects
        pygame.mixer.init()
        self.collision_sound = pygame.mixer.Sound('loser.mp3') 

        self.guppy = Guppy(vec(16, WORLD_SIZE[1]-16*3))
        self.background = Drawable(vec(0, 0), "ocean2.png", parallax=0)
        self.obstacles = []
        self.offset = 0 
        self.velocity = 50
        self.gameOver = False
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 20)
        self.timer = 0
        self.fishHitBox = pygame.Rect(0,0, 10, 10)

    def draw(self, drawSurface):

        score_surface = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
        score_rect = score_surface.get_rect(topright=(RESOLUTION[0]-10, 10))
        # Draw other game elements normally
        self.background.position = vec(-self.offset % WORLD_SIZE[0], 0)
        self.background.draw(drawSurface)

        self.fishHitBox = self.guppy.getCollisionRect()
        pygame.draw.rect(drawSurface, (255, 0, 0), self.fishHitBox, 1)
        # If the background wraps around, draw the trailing part

        if self.offset % WORLD_SIZE[0] > 0:
            self.background.position = vec(-self.offset % WORLD_SIZE[0]- WORLD_SIZE[0], 0)
            self.background.draw(drawSurface)

        for r in self.obstacles:
            r.draw(drawSurface)
            hitbox = r.getCollisionRect()
            # Code for hit box debugging
            #pygame.draw.rect(drawSurface, (255, 0, 0), hitbox, 1)
        self.guppy.draw(drawSurface)
        
        drawSurface.blit(score_surface, score_rect)
        # Code for hit box debugging
        #pygame.draw.rect(drawSurface, (9,255,255), self.fishHitBox, 1)

    def handleEvent(self, event):
        self.guppy.handleEvent(event)

    def update(self, seconds):
        """Add to a global timer, update"""
        self.score += 1
        self.timer += 1
        self.guppy.update(seconds)
        #self.fishHitBox.update(seconds)
        #self.fish.update(seconds)
        self.velocity+= ACCEL*seconds
        self.offset+=self.velocity*seconds
        fishHitBox = self.guppy.getCollisionRect()
        if self.timer % 20 == 0:
            self.obstacles.append(Fish(position=vec(100, RESOLUTION[1] - 50), parallax=0))
        if self.timer % 100 == 0:
            self.obstacles.append(Fish2(position=vec(100, RESOLUTION[1] - 50), parallax=0))
        if self.timer % 200 == 0:
            self.obstacles.append(Fish3(position=vec(100, RESOLUTION[1] - 50), parallax=0))

        Drawable.updateOffset(self.guppy, WORLD_SIZE)

        for r in range(len(self.obstacles)):
            self.obstacles[r].velocity = -self.velocity 
            self.obstacles[r].update(seconds)

            obsHitBox = self.obstacles[r].getCollisionRect()
            # if the obstacle hit box and fish hitbox collide, then the game ends and sound effect plays
            if obsHitBox.colliderect(fishHitBox):
                self.collision_sound.play()
                self.gameOver = True
                break

      