import simpy

class Simulator:
    def __init__(self, env, network):
        self.env = env
        self.network = network

    def run(self, duration):
        print(f"Simulation started for {duration} seconds...")
        self.env.run(until=duration)
        print("Simulation finished.")
