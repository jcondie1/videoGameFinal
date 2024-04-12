
import pygame
from engines.platformer import GameEngine
from utils import RESOLUTION, UPSCALED
#from utils.screenManager import ScreenManager

pygame.init()
pygame.font.init()

# Load the start screen image
start_screen_image = pygame.image.load('images/background.png') 
start_screen_image = pygame.transform.scale(start_screen_image, list(map(int, RESOLUTION)))  # Scale image to fit screen

def main():
    #Initialize the module
    pygame.init()
    pygame.font.init()
    pygame.mixer.music.load('Screen Saver.mp3')
    pygame.mixer.music.play(loops=-1)
    #Get the screen
    screen = pygame.display.set_mode(list(map(int, UPSCALED)))
    drawSurface = pygame.Surface(list(map(int, RESOLUTION)))

    while True:
        if display_start_screen(screen):
            break  # Exit if the start screen function indicates to quit
        gameEngine = GameEngine()
        #gameEngine = ScreenManager()
        
        RUNNING = True
        gameEngine.gameOver = False
        paused = False

        while gameEngine.gameOver == False:
        #while RUNNING == True:
            #gameEngine.draw(drawSurface)
            
            pygame.transform.scale(drawSurface,
                                list(map(int, UPSCALED)),
                                screen)
        
            pygame.display.flip()
            gameClock = pygame.time.Clock()
            
            # event handling, gets all event from the eventqueue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    # change the value to False, to exit the main loop
                    gameEngine.gameOver = True
                    #RUNNING = False
                elif event.type == pygame.KEYDOWN and event.key is pygame.K_p:
                    paused = not paused  # Toggle pause state
                else:
                    gameEngine.handleEvent(event)
            if not paused:
                gameEngine.draw(drawSurface)
                pygame.transform.scale(drawSurface, list(map(int, UPSCALED)), screen)
                pygame.display.flip()
                gameClock.tick(60)
                seconds = gameClock.get_time() / 1000
                gameEngine.update(seconds)

            if gameEngine.gameOver:
                display_game_over_screen(screen)
                break

    pygame.quit()

# Function for displaying the start screen
def display_start_screen(screen):
    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True  # Indicates the game should quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start the game with SPACE key
                    start = True

        # Display the start screen image
        screen.blit(start_screen_image, (0, 0))
        font = pygame.font.SysFont('Arial', 100)
        font2 = pygame.font.SysFont('Arial', 50)
        text = font.render('FISH RUN', True, (255, 255, 255))
        text2 = font2.render('Press SPACE to start', True, (255, 255, 255))
        screen.blit(text, (RESOLUTION[0] / 2 - text.get_width() / 2, 200))
        screen.blit(text2, (RESOLUTION[0] / 2 - text2.get_width() / 2, 500))
        pygame.display.flip()

# Function for displaying the game over screen
def display_game_over_screen(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Arial', 48)
    text = font.render('Game Over', True, (255, 255, 255))
    text_rect = text.get_rect(center=(RESOLUTION[0] / 2, RESOLUTION[1] / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before exiting

if __name__ == '__main__':
    main()