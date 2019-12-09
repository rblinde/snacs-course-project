import time
import numpy as np
import networkx as nx
from networkx.algorithms import community
from collections import defaultdict

def run(datasets, name, algorithm, all_times):
    def iteration():
        # Timing
        start = time.time()
        result = algorithm(G)
        end = time.time()
        run_time = round((end - start) * 1000, 6)
        times.append(run_time)
        # Output
        print(f"Dataset {dataset} completed iteration {i} for algorithm {name}!")

    for dataset in datasets:
        G = nx.read_edgelist(f"datasets/{dataset}/edges.txt")
        times = []

        for i in range(10):
            iteration()

        all_times.append(f"{dataset}, {name}, {times}\n")

if __name__ == '__main__':
    times = []
    datasets = ["youtube"] #  "karate", "football", "email"
    run(datasets, "lpa", community.asyn_lpa_communities, times)
    # run(datasets, "gn", community.girvan_newman, times)
    # run(datasets, "gm", community.greedy_modularity_communities, times)

    with open("timings-only.txt", "w") as file:
        file.writelines(times)
