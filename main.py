import pygame

#import math



# class Map():

#     def __init__(self, **kwargs):
#         super(Map, self).__init__(**kwargs)

#         self.cols = mapZise
#         for y in range(mapZise):
#             for x in range(mapZise):
#                 self.add_widget(Label(text="0"))

class Snake():
    def __init__(self):
        pass

    snake_head = [10,10]
    snake_body = [[10,10],[10,11],[10,12]]

    snake_body = [100, 50]
 
    # defining first 4 blocks of snake
    # body
    snake_body = [  [100, 50],
                    [90, 50],
                    [80, 50],
                    [70, 50]
                ]

    def drawSnake():
        #place snake
        pass

class DrawMap():
    def __init__(self, mapZise):
        mapZise_ = mapZise
        pygame.display.init

    def draw(self):
        for y in range(self.mapZise_):
            for x in range(self.mapZise_):
                pygame.draw.rect()
    


if __name__ == '__main__':

    window_x = 500
    window_y = 500

    pygame.init()
    screen = pygame.display.set_mode((window_x, window_y))
    
    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((55, 55, 55))

        # Draw map
        for y in range(20):
            for x in range(20):
                pygame.draw.rect(screen, (20, 50), (0, 0, 50, 50))

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
    
    # DrawMap(20)
    # Snake.placeSnake()