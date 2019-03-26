# Gym wrapper for DeepMind Lab environments
Gym implementation of connector to Deepmind lab

## Getting Started
Install the newest package by running:
```
pip install gym_deepmindlab
```

In your project:
```
import gym
import gym_deepmindlab

env = gym.make('DeepmindLabSeekavoidArena01-v0')

# Use the environment
observation = env.reset()
```

## Suppoted Environments
This is the list of supported environments:
- DeepmindLabLtChasm-v0
- DeepmindLabLtHallwaySlope-v0
- DeepmindLabLtHorseshoeColor-v0
- DeepmindLabLtSpaceBounceHard-v0
- DeepmindLabNavMazeRandomGoal01-v0
- DeepmindLabNavMazeRandomGoal02-v0
- DeepmindLabNavMazeRandomGoal03-v0
- DeepmindLabNavMazeStatic01-v0
- DeepmindLabNavMazeStatic02-v0
- DeepmindLabSeekavoidArena01-v0
- DeepmindLabStairwayToMelon-v0

## Arguments
You can specify the screen size when creating a new environment:
```
import gym
import gym_deepmindlab

env = gym.make('DeepmindLabSeekavoidArena01-v0', width = 224, height = 224)

# Use the environment
observation = env.reset()
```

## Thanks
Thanks to https://github.com/deepmind/lab for such a great work.
