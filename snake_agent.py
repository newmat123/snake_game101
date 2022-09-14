import numpy
import tensorflow as tf
from snake import Snake

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

Snake([100,100], [[100,100],[90,100],[80,100],[70,100]], "RIGHT", 500, 500)



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



class CardGameEnv(py_environment.PyEnvironment):

    def __init__(self) -> None:
        self._action_spec = array_spec.BoundedArraySpec(
        shape=(), dtype=np.int32, minimum=0, maximum=1, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
        shape=(1,), dtype=np.int32, minimum=0, name='observation')
        self._state = 0
        self._episode_ended = False

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
        self._state = 0
        self._episode_ended = False
        return ts.restart(np.array([self._state], dtype=np.int32))

    def _step(self, action):

        if self._episode_ended:
            # The last action ended the episode. Ignore the current action and start
            # a new episode.
            return self.reset()

        # Make sure episodes don't go on forever.
        if action == 1:
            self._episode_ended = True
        elif action == 0:
            new_card = np.random.randint(1, 11)
            self._state += new_card
        else:
            raise ValueError('`action` should be 0 or 1.')

        if self._episode_ended or self._state >= 21:
            reward = self._state - 21 if self._state <= 21 else -21
            return ts.termination(np.array([self._state], dtype=np.int32), reward)
        return ts.transition(np.array([self._state], dtype=np.int32), reward=0.0, discount=1.0)
