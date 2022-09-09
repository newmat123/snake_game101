import pygame
import time
from operator import attrgetter
from snake import Snake

def checkDir(new_dir, old_dir):
    if new_dir == "UP" and old_dir != "DOWN":
        return "UP"
    elif new_dir == "DOWN" and old_dir != "UP":
        return "DOWN"
    elif new_dir == "LEFT" and old_dir != "RIGHT":
        return "LEFT"
    elif new_dir == "RIGHT" and old_dir != "LEFT":
        return "RIGHT"
    else:
        return old_dir

if __name__ == '__main__':
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    bagground = pygame.Color(55, 55, 55)

    window_x = 500
    window_y = 500
    new_dir = "RIGHT"
    
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

    score_x = window_x // 2
    score_y = 15

    pygame.init()
    pygame.display.set_caption("wild Game!!!")
    screen = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()
    game_speed = 5
    
    running = True
    while running:

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    new_dir = "UP"
                if event.key == pygame.K_DOWN:
                    new_dir = "DOWN"
                if event.key == pygame.K_LEFT:
                    new_dir = "LEFT"
                if event.key == pygame.K_RIGHT:
                    new_dir = "RIGHT"

        for i, snake in enumerate(snakes):
            snake.moveSnake(checkDir(new_dir, snake.getSnakeDir()))
            # below not nessecary
            if snake.hitApple():
                #print("snake" + str(i) + ": "+ str(snake.test()[0]) +", "+ str(snake.test()[1]))
                print("snake" + str(i) + ": " + str(snake.getScore()))
        
        # draw frame
        screen.fill(bagground) 
        # Draw snake and apple

        # gets the snake with the higest score
        theSnake = max(snakes, key=attrgetter('score_'))

        for pos in theSnake.getSnakeBody():
            pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, red, pygame.Rect(theSnake.getApplePos()[0], theSnake.getApplePos()[1], 10, 10))
        
        for snake in snakes:
            snake.getApplePos()

        #draw score
        font = pygame.font.Font('freesansbold.ttf', score_y)
        text = font.render('your score is: ' + str(theSnake.getScore()), True, white)
        textRect = text.get_rect()
        textRect.center = (score_x, score_y)
        screen.blit(text, textRect)
        
        # draw Game over
        if theSnake.snakeDeath():
            font = pygame.font.Font('freesansbold.ttf', 32)

            text = font.render('GAME OVER', True, green, blue)
            textRect = text.get_rect()
            
            textRect.center = (window_x // 2, window_y // 2)
            screen.blit(text, textRect)

            running = False
       
        # Refresh game screen and Frame Per Second /Refresh Rate
        pygame.display.update()
        fps.tick(game_speed)

    time.sleep(2)
    pygame.quit()
