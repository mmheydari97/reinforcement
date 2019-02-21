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
                }

    # Create the environment and reset it
    env = gym.make(name_map[input_env])

    # Iterate 20 times
    for _ in range(20):
        # Reset the environment
        observation = env.reset()

        for i in range(100):
            # Render the environment
            env.render()

            # Print the current observation
            print(observation)

            # Take action
            action = env.action_space.sample()

            # Extract the observation, reward, status and
            # other info based on the action taken
            observation, reward, done, info = env.step(action)

            # Check if it's done
            if done:
                print('Episode finished after {} time steps.'.format(i+1))
                break
            time.sleep(0.015)
