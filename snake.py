import random

class Snake():
    def __init__(self, snake_head, snake_body, snake_dir, window_x, window_y):
        self.window_x_ = window_x
        self.window_y_ = window_y
        self.snake_head_ = snake_head
        self.snake_body_ = snake_body
        self.snake_dir_ = snake_dir

        self.fruit_pos_ = [window_x // 2, window_y // 2]
        self.fruit_exist_ = False
        self.score_ = 0

    def getSnakeDir(self):
        return self.snake_dir_
    
    def getSnakeBody(self):
        return self.snake_body_
    
    def getScore(self):
        return self.score_

    def moveSnake(self, new_snake_dir):
        if new_snake_dir == "UP":
            self.snake_head_[1] -= 10
        elif new_snake_dir == "DOWN":
            self.snake_head_[1] += 10
        elif new_snake_dir == "LEFT":
            self.snake_head_[0] -= 10
        elif new_snake_dir == "RIGHT":
            self.snake_head_[0] += 10
        
        self.snake_dir_ = new_snake_dir
        self.snake_body_.insert(0, list(self.snake_head_))

        if self.hitApple():
            self.score_ += 1
            self.fruit_exist_ = False
        else:
            self.snake_body_.pop()

    def hitApple(self):
        if self.snake_head_[0] == self.fruit_pos_[0] and self.snake_head_[1] == self.fruit_pos_[1]:
            return True
        else:
            return False
    
    def snakeDeath(self):
        for snakePart in self.snake_body_[1:]:
            if self.snake_head_[0] == snakePart[0] and self.snake_head_[1] == snakePart[1]:
                return True
        
        if self.snake_head_[0] < 0 or self.snake_head_[0] >= self.window_x_ or self.snake_head_[1] < 0 or self.snake_head_[1] >= self.window_y_:
            return True
        return False

    def getApplePos(self):
        if not self.fruit_exist_:
            while self.fruit_pos_ in self.snake_body_:
                self.fruit_pos_ = [random.randrange(1, (self.window_x_//10)) * 10, random.randrange(1, (self.window_y_//10)) * 10]
        
        self.fruit_exist_ = True
        return self.fruit_pos_