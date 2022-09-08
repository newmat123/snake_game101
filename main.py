import pygame
import time
import random

class Snake():
    def __init__(self, snake_head, snake_body, snake_dir, snake_speed, window_x, window_y):
        pygame.init()
        pygame.display.set_caption("SNAKE!!!")

        self.screen_ = pygame.display.set_mode((window_x, window_y))
        # FPS (frames per second) controller
        self.fps_ = pygame.time.Clock()
        
        self.snake_speed_ = snake_speed #idk
        self.window_x_ = window_x
        self.window_y_ = window_y
        self.snake_head_ = snake_head
        self.snake_body_ = snake_body
        self.snake_dir_ = snake_dir
        self.new_dir_ = self.snake_dir_

        self.white_ = pygame.Color(255, 255, 255)
        self.red_ = pygame.Color(255, 0, 0)
        self.green_ = pygame.Color(0, 255, 0)
        self.blue_ = pygame.Color(0, 0, 255)
        self.bagground_ = pygame.Color(55, 55, 55)
        self.fruit_pos_ = [0, 0]
        self.fruit_exist_ = False
        self.score_ = 0
    
    def run(self):
        self.moveSnake()
        self.hitApple()

        # Draw snake and apple
        self.drawSnake()
        self.drawApple()

        self.drawScore(self.window_x_ // 2, 15)

        self.snakeDeath()

        # Refresh game screen
        pygame.display.update()
        self.fps_.tick(self.snake_speed_)


    def gameOver(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('GAME OVER', True, self.green_, self.blue_)
        textRect = text.get_rect()

        textRect.center = (self.window_x_ // 2, self.window_y_ // 2)
        self.screen_.blit(text, textRect)

        return True

    def moveSnake(self):
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.new_dir_ = "UP"
                if event.key == pygame.K_DOWN:
                    self.new_dir_ = "DOWN"
                if event.key == pygame.K_LEFT:
                    self.new_dir_ = "LEFT"
                if event.key == pygame.K_RIGHT:
                    self.new_dir_ = "RIGHT"

        if self.new_dir_ == "UP" and self.snake_dir_ != "DOWN":
            self.snake_dir_ = "UP"
        elif self.new_dir_ == "DOWN" and self.snake_dir_ != "UP":
            self.snake_dir_ = "DOWN"
        elif self.new_dir_ == "LEFT" and self.snake_dir_ != "RIGHT":
            self.snake_dir_ = "LEFT"
        elif self.new_dir_ == "RIGHT" and self.snake_dir_ != "LEFT":
            self.snake_dir_ = "RIGHT"

        if self.snake_dir_ == "UP":
            self.snake_head_[1] -= 10
        elif self.snake_dir_ == "DOWN":
            self.snake_head_[1] += 10
        elif self.snake_dir_ == "LEFT":
            self.snake_head_[0] -= 10
        elif self.snake_dir_ == "RIGHT":
            self.snake_head_[0] += 10

        self.snake_body_.insert(0, list(self.snake_head_))

    def hitApple(self):
        if self.snake_head_[0] == self.fruit_pos_[0] and self.snake_head_[1] == self.fruit_pos_[1]:
            self.score_ += 1
            self.fruit_exist_ = False
        else:
            self.snake_body_.pop()

    def drawSnake(self):
        self.screen_.fill(self.bagground_)
        for pos in self.snake_body_:
            pygame.draw.rect(self.screen_, self.blue_, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.screen_, self.green_, pygame.Rect(self.snake_body_[0][0], self.snake_body_[0][1], 10, 10))
    
    def snakeDeath(self):
        for snakePart in self.snake_body_[1:]:
            if self.snake_head_[0] == snakePart[0] and self.snake_head_[1] == snakePart[1]:
                self.gameOver()
                # return somthing
        
        if self.snake_head_[0] < 0 or self.snake_head_[0] >= self.window_x_ or self.snake_head_[1] < 0 or self.snake_head_[1] >= self.window_y_:
            self.gameOver()
            # return somthing

    def drawApple(self):
        if not self.fruit_exist_:
            self.fruit_pos_ = [random.randrange(1, (self.window_x_//10)) * 10, random.randrange(1, (self.window_y_//10)) * 10]
            
        pygame.draw.rect(self.screen_, self.red_, pygame.Rect(self.fruit_pos_[0], self.fruit_pos_[1], 10, 10))
        self.fruit_exist_ = True

    def drawScore(self, x, y):
        font = pygame.font.Font('freesansbold.ttf', y)

        text = font.render('your score is: ' + str(self.score_), True, self.white_)
        textRect = text.get_rect()
        
        textRect.center = (x, y)
        self.screen_.blit(text, textRect)


if __name__ == '__main__':
    snake_speed = 5
    window_x = 500
    window_y = 500
    snake_head = [100,100]
    snake_body = [[100,100],[90,100],[80,100],[70,100]]
    snake_dir = "RIGHT"
    
    snake1 = Snake(snake_head, snake_body, snake_dir, snake_speed, window_x, window_y)
    snake2 = Snake(snake_head, snake_body, snake_dir, snake_speed, window_x, window_y)

    running = True
    while running:

        # snake1.moveSnake()
        # snake1.hitApple()

        # # Draw snake and apple
        # snake1.drawSnake()
        # snake1.drawApple()

        # snake1.drawScore(window_x // 2, 15)

        
        # snake1.snakeDeath(window_x, window_y)
        snake1.run()
        snake2.run()

    time.sleep(2)
    # Done! Time to quit.
    pygame.quit()
