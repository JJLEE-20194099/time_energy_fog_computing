import os
import random
import gym
import pylab
import numpy as np
from collections import deque
from keras.layers import Input, Dense, Lambda, Add
from tensorflow.keras.optimizers import Adam, RMSprop
from keras import backend as K
