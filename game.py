import pygame
import sys
import config # Import the config Module
import random
import shapes


def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen



def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

            
    return True


def draw_circle(screen,color,circle_center,radius,thickness):
    pygame.draw.circle(screen,color,circle_center,radius,thickness)



def main():
    screen = init_game()
    running = True
    clock = pygame.time.Clock() # Initialize the clock her
    
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config

        circle_color = config.RED
        position = [100, 100]
        circle_radius = 10
        
        key = pygame.key.get_pressed()
        if key [pygame.K_s]:
            position[0] -= 5
        if key [pygame.K_d]:
            position[0] += 5

        draw_circle(screen,circle_color,position,circle_radius,0)

        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()