import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import deepmind_lab

def _to_pascal(text):
    return ''.join(map(lambda x: x.capitalize(), text.split('_')))

LEVELS = ['lt_chasm', 'lt_hallway_slope', 'lt_horseshoe_color', 'lt_space_bounce_hard', \
'nav_maze_random_goal_01','nav_maze_random_goal_02', 'nav_maze_random_goal_03', 'nav_maze_static_01' \
'nav_maze_static_02', 'seekavoid_arena_01', 'stairway_to_melon']


MAP = { _to_pascal(l):l for l in LEVELS }

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
        self.observation_space = gym.spaces.Box(0, 255, (height, width, 3), dtype = np.int8)

    def step(self, action):
        reward = self._lab.step(ACTION_LIST[action], num_steps=4)
        terminal = not self._lab.is_running()
        obs = None if terminal else self._lab.observations()[self._colors]
        return obs, reward, terminal, None


    def reset(self):
        self._lab.reset()        
        return self._lab.observations()[self._colors]

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