import argparse
import gym
import time


def building_arg_parser():
    parser = argparse.ArgumentParser(description='Run an environment')
    parser.add_argument('--input-env', dest='input_env', required=True,
                        choices=['cartpole', 'mountaincar', 'pendulum', 'taxi', 'lake'],
                        help='Specify the name of the environment')

    return parser


if __name__ == '__main__':
    args = building_arg_parser().parse_args()
    input_env = args.input_env

    name_map = {'cartpole': 'CartPole-v0',
                'mountaincar': 'MountainCar-v0',
                'pendulum': 'Pendulum-v0',
                'taxi': 'Taxi-v2',
                'lake': 'FrozenLake-v0'}

    # Create the environment and reset it
    env = gym.make(name_map[input_env])
    env.reset()

    # Iterate 1000 times
    for i in range(10000):
        # Render the environment
        env.render()

        print(i)
        time.sleep(0.015)

        # Take a random action
        env.step(env.action_space.sample())
