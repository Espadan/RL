import gym.spaces
import matplotlib.pyplot as plt
import numpy as np


def play_and_train(env, agent, t_max=10 ** 4):
    """ This function should
    - run a full game (for t_max steps), actions given by agent
    - train agent whenever possible
    - return total reward
    """
    total_reward = 0.0

    return total_reward


if __name__ == '__main__':
    max_iterations = 1000
    visualize = False
    # Create Taxi-v2 env
    env = None
    env.reset()
    env.render()

    n_states = None
    n_actions = None

    print('States number = %i, Actions number = %i' % (n_states, n_actions))

    # create q learning agent with
    # alpha=0.5
    # get_legal_actions = lambda s: range(n_actions)
    # epsilon=0.1
    # discount=0.99

    agent = None

    plt.figure(figsize=[10, 4])
    rewards = []

    # Training loop
    for i in range(max_iterations):
        # Play & train game
        # Update rewards
        # rewards

        # Decay agent epsilon
        # agent.epsilon = ?

        if i % 100 == 0:
            print('Iteration {}, Average reward {:.2f}, Epsilon {:.3f}'.format(i, np.mean(rewards), agent.epsilon))

        if visualize:
            plt.subplot(1, 2, 1)
            plt.plot(rewards, color='r')
            plt.xlabel('Iterations')
            plt.ylabel('Total Reward')

            plt.subplot(1, 2, 2)
            plt.hist(rewards, bins=20, range=[-700, +20], color='blue', label='Rewards distribution')
            plt.xlabel('Reward')
            plt.ylabel('p(Reward)')
            plt.draw()
            plt.pause(0.05)
            plt.cla()
