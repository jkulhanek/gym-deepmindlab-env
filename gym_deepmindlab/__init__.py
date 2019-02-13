from gym.envs.registration import register
from gym_deepmindlab.env import DeepmindLabEnv, MAP

for key, l in MAP.items():
    register(
        id='DeepmindLab%s-v0' % key ,
        entry_point='gym_deepmindlab:DeepmindLabEnv',
        kwargs = dict(scene = l)
    )
