import numpy
import tensorflow as tf
from snake import Snake


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
