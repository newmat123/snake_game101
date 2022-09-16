import numpy
import tensorflow as tf
from snake_game_ai import SnakeAi

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import tensorflow as tf
import numpy as np

from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

#https://www.tensorflow.org/agents/tutorials/2_environments_tutorial

# score                 int
# snake head            [int, int]
# snakeBody             [[int, int],[int, int],...]
# dis from apple        float
# apple pos             [int, int]
# snake dirrection      str or int
# apple exist           bool

# wall dis top          int
# wall dis bottum       int
# wall dis left         int
# wall dis right        int
#snakedeath             bool




# def createSnakes():
#     snakes = [
#         Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
#         Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
#         Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
#         Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
#         Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
#         Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
#         Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500),
#         Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500)
#     ]

class Agent():
    """ ai agent """

def train_ai(snake):
    """ Trains ai """
    #plot_scores = []
    #plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeAi(snake[0], snake[1], snake[2], snake[3], snake[4],)


if __name__ == '__main__':
    SNAKE_PARAMETERS = [[100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500]
    train_ai(SNAKE_PARAMETERS)
