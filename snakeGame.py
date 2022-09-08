import pygame
import random

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
bagground = pygame.Color(55, 55, 55)

snake_speed = 60

window_x = 500
window_y = 500

pygame.init()
pygame.display.set_caption("wild Game!!!")
screen = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

snake_head = [100,100]
snake_body = [[100,100],[90,100],[80,100],[70,100]]
snake_dir = "RIGHT"
change_to = snake_dir

fruit_pos = [0, 0]
fruit_exist = False

score = 0


def drawApple():
    global fruit_exist, fruit_pos
    if not fruit_exist:
        fruit_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
        
    pygame.draw.rect(screen, red, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))
    fruit_exist = True

def gameOver():
    print("game over")
    pygame.quit()

running = True
while running:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and snake_dir != "DOWN":
        snake_dir = "UP"
    elif change_to == "DOWN" and snake_dir != "UP":
        snake_dir = "DOWN"
    elif change_to == "LEFT" and snake_dir != "RIGHT":
        snake_dir = "LEFT"
    elif change_to == "RIGHT" and snake_dir != "LEFT":
        snake_dir = "RIGHT"

    if snake_dir == "UP":
        snake_head[1] -= 10
    elif snake_dir == "DOWN":
        snake_head[1] += 10
    elif snake_dir == "LEFT":
        snake_head[0] -= 10
    elif snake_dir == "RIGHT":
        snake_head[0] += 10

    snake_body.insert(0, list(snake_head))

    if snake_head[0] == fruit_pos[0] and snake_head[1] == fruit_pos[1]:
        fruit_exist = False
    else:
        snake_body.pop()

    # draw frame
    # Background color
    screen.fill(bagground) 

    # Draw snake and apple
    for pos in snake_body:
        pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, green, pygame.Rect(snake_body[0][0], snake_body[0][1], 10, 10))
    drawApple()

    for snakePart in snake_body[1:]:
        if snake_head[0] == snakePart[0] and snake_head[1] == snakePart[1]:
            gameOver()
    
    if snake_head[0] < 0 or snake_head[0] >= window_x or snake_head[1] < 0 or snake_head[1] >= window_y:
        gameOver()

    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)

# Done! Time to quit.
pygame.quit()