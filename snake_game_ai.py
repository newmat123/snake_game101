"""
used for placing the apple at a random location
"""
import random

class SnakeAi():
    """
    docstring
    """
    def __init__(self, snake_head, snake_body, snake_dir, window_x, window_y):
        self.window_x_ = window_x
        self.window_y_ = window_y
        self.snake_head_ = snake_head
        self.snake_body_ = snake_body
        self.snake_dir_ = snake_dir

        self.apple_pos_ = [window_x // 2, window_y // 2]
        self.apple_exist_ = False
        self.score_ = 0

    #[1,0,0] fwd, right, left  bool only one true and tow false
    def move_snake(self, new_snake_dir) -> None:
        """moves the snake in a given direction"""
        if new_snake_dir[0] == 0:
            if new_snake_dir[1] == 1: # turn right
                match self.snake_dir_:
                    case "UP":
                        self.snake_dir_ = 'RIGHT'
                    case "DOWN":
                        self.snake_dir_ = 'LEFT'
                    case 'LEFT':
                        self.snake_dir_ = 'UP'
                    case 'RIGHT':
                        self.snake_dir_ = 'DOWN'
            else: # turn left
                match self.snake_dir_:
                    case "UP":
                        self.snake_dir_ = 'LEFT'
                    case "DOWN":
                        self.snake_dir_ = 'RIGHT'
                    case 'LEFT':
                        self.snake_dir_ = 'DOWN'
                    case 'RIGHT':
                        self.snake_dir_ = 'UP'

        # if new_snake_dir == "UP" and self.snake_dir_ != "DOWN":
        #     self.snake_dir_ = "UP"
        # elif new_snake_dir == "DOWN" and self.snake_dir_ != "UP":
        #     self.snake_dir_ = "DOWN"
        # elif new_snake_dir == "LEFT" and self.snake_dir_ != "RIGHT":
        #     self.snake_dir_ = "LEFT"
        # elif new_snake_dir == "RIGHT" and self.snake_dir_ != "LEFT":
        #     self.snake_dir_ = "RIGHT"

        if self.snake_dir_ == "UP":
            self.snake_head_[1] -= 10
        elif self.snake_dir_ == "DOWN":
            self.snake_head_[1] += 10
        elif self.snake_dir_ == "LEFT":
            self.snake_head_[0] -= 10
        elif self.snake_dir_ == "RIGHT":
            self.snake_head_[0] += 10

        self.snake_body_.insert(0, list(self.snake_head_))

        if self.hit_apple():
            self.score_ += 1
            self.apple_exist_ = False
        else:
            self.snake_body_.pop()

    def hit_apple(self) -> bool:
        """checks if the snake hit an apple"""
        if self.snake_head_[0] == self.apple_pos_[0] and self.snake_head_[1] == self.apple_pos_[1]:
            return True
        return False

    def snake_death(self):
        """returns true is the snake is dead and false if not"""
        for snake_part in self.snake_body_[1:]:
            if self.snake_head_[0] == snake_part[0] and self.snake_head_[1] == snake_part[1]:
                return True

        if self.snake_head_[0] < 0 or self.snake_head_[0] >= self.window_x_: # checks the x axsis
            return True
        if self.snake_head_[1] < 0 or self.snake_head_[1] >= self.window_y_: # checks the y axsis
            return True
        return False

    def get_apple_pos(self) -> list:
        """replaces the apple if needed and returns the pos of the apple."""
        if not self.apple_exist_:
            while self.apple_pos_ in self.snake_body_:
                self.apple_pos_ = [
                    random.randrange(1, (self.window_x_//10)) * 10,
                    random.randrange(1, (self.window_y_//10)) * 10
                    ]

        self.apple_exist_ = True
        return self.apple_pos_
