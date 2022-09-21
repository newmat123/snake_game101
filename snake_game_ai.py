"""
used for placing the apple at a random location
"""
import random
import numpy as np

from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step as ts

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

        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=1, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(1,), dtype=np.int32, minimum=0, name='observation')
        self.state_ = 0
        self.episode_ended_ = False

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

        if self.snake_dir_ == "UP":
            self.snake_head_[1] -= 10
        elif self.snake_dir_ == "DOWN":
            self.snake_head_[1] += 10
        elif self.snake_dir_ == "LEFT":
            self.snake_head_[0] -= 10
        elif self.snake_dir_ == "RIGHT":
            self.snake_head_[0] += 10

        self.snake_body_.insert(0, list(self.snake_head_))

        if not self.hit_apple():
            self.snake_body_.pop()

    def hit_apple(self) -> bool:
        """checks if the snake hit an apple"""
        if self.snake_head_[0] == self.apple_pos_[0] and self.snake_head_[1] == self.apple_pos_[1]:
            # self.apple_exist_ = False
            # self.score_ += 1
            # self.get_apple_pos()
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

    def snake_death(self) -> bool:
        """returns true is the snake is dead and false if not"""
        for snake_part in self.snake_body_[1:]:
            if self.snake_head_[0] == snake_part[0] and self.snake_head_[1] == snake_part[1]:
                return True

        if self.snake_head_[0] < 0 or self.snake_head_[0] >= self.window_x_: # checks the x axsis
            return True
        if self.snake_head_[1] < 0 or self.snake_head_[1] >= self.window_y_: # checks the y axsis
            return True
        return False

    def action_spec(self):
        return self.action_spec_

    def observation_spec(self):
        return self.observation_spec_

    def reset(self) -> None:
        """ resets envioment """
        self.state_ = 0
        self.episode_ended_ = False
        return ts.restart(np.array([self._state], dtype=np.int32))

    #[1,0,0] fwd, right, left  bool only one true and tow false
    def step(self, new_snake_dir) -> any:
        """moves the snake in a given direction"""

        if self.episode_ended_:
            # The last action ended the episode. Ignore the current action and start
            # a new episode.
            return self.reset()

        # checks input
        if new_snake_dir[0] == 1:
            pass
        elif new_snake_dir[1] == 1:
            pass
        elif new_snake_dir[2] == 1:
            pass
        else:
            raise ValueError('`action` not a valid dirrection.')

        self.move_snake(new_snake_dir)

        reward = 0
        if self.hit_apple():
            self.apple_exist_ = False
            self.score_ += 1
            reward = 10
            self.get_apple_pos()

        if self.snake_death():
            self.episode_ended_ = True
            reward = -10

        if self.episode_ended_:
            reward = (self.score_*10) - self.state_
            return ts.termination(np.array([self.state_], dtype=np.int32), reward)
        return ts.transition(np.array([self.state_], dtype=np.int32), reward=0.0, discount=1.0)

        raise ValueError('somthin went wrong')
