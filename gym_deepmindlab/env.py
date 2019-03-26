import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import deepmind_lab
from . import LEVELS, MAP

class DeepmindLabEnv(gym.Env):
    metadata = {'render.modes': ['rgb_array']}

    def __init__(self, scene, colors = 'RGB_INTERLEAVED', width = 84, height = 84, **kwargs):
        super(DeepmindLabEnv, self).__init__(**kwargs)

        if not scene in LEVELS:
            raise Exception('Scene %s not supported' % (scene))

        self._colors = colors
        self._lab = deepmind_lab.Lab(scene, [self._colors], \
            dict(fps = str(60), width = str(width), height = str(height)))

        self.action_space = gym.spaces.Discrete(len(ACTION_LIST))
        self.observation_space = gym.spaces.Box(0, 255, (height, width, 3), dtype = np.uint8)

        self._last_observation = None

    def step(self, action):
        reward = self._lab.step(ACTION_LIST[action], num_steps=4)
        terminal = not self._lab.is_running()
        obs = None if terminal else self._lab.observations()[self._colors]
        self._last_observation = obs if obs is not None else np.copy(self._last_observation)
        return self._last_observation, reward, terminal, dict()


    def reset(self):
        self._lab.reset()        
        self._last_observation = self._lab.observations()[self._colors]
        return self._last_observation

    def seed(self, seed = None):
        self._lab.reset(seed=seed)

    def close(self):
        self._lab.close()

    def render(self, mode='rgb_array', close=False):
        if mode == 'rgb_array':
            return self._lab.observations()[self._colors]
        #elif mode is 'human':
        #   pop up a window and render
        else:
            super(DeepmindLabEnv, self).render(mode=mode) # just raise an exception

def _action(*entries):
  return np.array(entries, dtype=np.intc)

ACTION_LIST = [
    _action(-20,   0,  0,  0, 0, 0, 0), # look_left
    _action( 20,   0,  0,  0, 0, 0, 0), # look_right
    #_action(  0,  10,  0,  0, 0, 0, 0), # look_up
    #_action(  0, -10,  0,  0, 0, 0, 0), # look_down
    _action(  0,   0, -1,  0, 0, 0, 0), # strafe_left
    _action(  0,   0,  1,  0, 0, 0, 0), # strafe_right
    _action(  0,   0,  0,  1, 0, 0, 0), # forward
    _action(  0,   0,  0, -1, 0, 0, 0), # backward
    #_action(  0,   0,  0,  0, 1, 0, 0), # fire
    #_action(  0,   0,  0,  0, 0, 1, 0), # jump
    #_action(  0,   0,  0,  0, 0, 0, 1)  # crouch
]