import gymexamples
import gymnasium as gym
import time

env = gym.make('gymexamples/GridWorld-v0', render_mode="human")

status_action_reward=[]
env.reset()
for _ in range(10000):
    action=env.action_space.sample()
    observation, reward, terminated, truncated,info= env.step(action)
    status_action_reward.append([observation,  reward])
    env.render()
    print(observation, reward, terminated, truncated,info)
env.close()