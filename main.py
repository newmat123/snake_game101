"""
libaries used to run the main file
"""
import time
from operator import attrgetter
from snake import Snake
import pygame

if __name__ == '__main__':
    WINDOW_X = 500
    WINDOW_Y = 500
    NEW_DIR = "RIGHT"

    SCORE_X = WINDOW_X // 2
    SCORE_Y = 15
    GAME_SPEED = 5

    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    bagground = pygame.Color(55, 55, 55)

    pygame.init()
    pygame.display.set_caption("wild Game!!!")
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    snakes = [
        Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
        Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
        Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
        Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
        Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
        Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
        Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
        Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500)
    ]

    RUNNING = True
    while RUNNING:

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    NEW_DIR = "UP"
                if event.key == pygame.K_DOWN:
                    NEW_DIR = "DOWN"
                if event.key == pygame.K_LEFT:
                    NEW_DIR = "LEFT"
                if event.key == pygame.K_RIGHT:
                    NEW_DIR = "RIGHT"

        for i, snake in enumerate(snakes):
            snake.move_snake(NEW_DIR)
            # below not nessecary
            if snake.hit_apple():
                #print(snake)
                print("snake" + str(i) + ": " + str(snake.score_))

        # draw frame
        screen.fill(bagground)
        # Draw snake and apple

        # gets the snake with the higest score
        theSnake = max(snakes, key=attrgetter('score_'))

        for pos in theSnake.snake_body_:
            pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, red,
        pygame.Rect(theSnake.apple_pos_[0], theSnake.apple_pos_[1], 10, 10))

        for snake in snakes:
            snake.get_apple_pos()

        #draw score
        font = pygame.font.Font('freesansbold.ttf', SCORE_Y)
        text = font.render('your score is: ' + str(theSnake.score_), True, white)
        textRect = text.get_rect()
        textRect.center = (SCORE_X, SCORE_Y)
        screen.blit(text, textRect)

        # draw Game over
        if theSnake.snake_death():
            font = pygame.font.Font('freesansbold.ttf', 32)

            text = font.render('GAME OVER', True, green, blue)
            textRect = text.get_rect()

            textRect.center = (WINDOW_X // 2, WINDOW_Y // 2)
            screen.blit(text, textRect)

            RUNNING = False

        # Refresh game screen and Frame Per Second /Refresh Rate
        pygame.display.update()
        fps.tick(GAME_SPEED)

    time.sleep(2)
    pygame.quit()
