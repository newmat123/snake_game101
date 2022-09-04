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

    snakeHead = [10,10]
    snakeBoddy = [[10,11],[10,12]]

    def placeSnake():
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

    pygame.init()
    screen = pygame.display.set_mode([500, 500])

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