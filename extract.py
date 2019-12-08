import time
import numpy as np
import networkx as nx
from networkx.algorithms import community
from collections import defaultdict

def write_to_file(name, communities):
    sequence = {};

    for i, c in enumerate(communities):
        for node in list(c):
            sequence[int(node)] = i

    sequence = sorted(list(sequence.items()))
    sequence = [f"{i[0]} {i[1]}\n" for i in sequence]

    with open(name, "w") as file:
        file.writelines(sequence)

def coms_normal(result):
    return [set(x) for x in result]

def coms_gen(result):
    return [set(x) for x in next(result)]

def run(datasets, name, algorithm, fn, all_times):
    def iteration():
        # Timing
        start = time.time()
        result = algorithm(G)
        end = time.time()
        # Writing
        communities = fn(result)
        file_name = f"results/{dataset}-{name}-{i}.txt"
        write_to_file(file_name, communities)
        # Timing 2
        run_time = round((end - start) * 1000, 6)
        times.append(run_time)
        # Output
        print(f"Dataset {dataset} completed iteration {i} for algorithm {name}!")

    for dataset in datasets:
        G = nx.read_edgelist(f"datasets/{dataset}/edges.txt")
        times = []
        i = 0

        iteration()

        if (name not in ["gn", "gm"]):
            for i in range(1, 10):
                iteration()

        all_times.append(f"{dataset}, {name}, {times}\n")


if __name__ == '__main__':
    times = []
    datasets = ["karate", "football", "email", "amazon", "youtube"]
    run(datasets, "lpa", community.asyn_lpa_communities, coms_normal, times)
    run(datasets, "gn", community.girvan_newman, coms_gen, times)
    run(datasets, "gm", community.greedy_modularity_communities, coms_normal, times)

    with open("timings.txt", "w") as file:
        file.writelines(times)
