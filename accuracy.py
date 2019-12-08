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

def run(datasets, name, all_accuracies):
    def iteration():
        with open(ground_truth_file, 'r') as a, open(result_file, 'r') as b:
            lines_a = a.readlines()
            lines_b = b.readlines()

        assert(len(lines_a) == len(lines_b))

        score = 0

        for j in range(len(lines_a)):
            n_a, c_a = [int(x) for x in lines_a[j].split(' ')]
            n_b, c_b = [int(x) for x in lines_b[j].split(' ')]

            if (n_a == n_b and c_a == c_b):
                score += 1

        accuracies.append(round(score/len(lines_a), 3))

        print(f"Accuaracy {dataset} completed iteration {i} for algorithm {name}!")

    for dataset in datasets:
        accuracies = []
        i = 0
        ground_truth_file = f"datasets/{dataset}/communities.txt"
        result_file = f"results/{dataset}-{name}-{i}.txt"

        iteration()

        if (name not in ["gn", "gm"]):
            for i in range(1, 10):
                result_file = f"results/{dataset}-{name}-{i}.txt"
                iteration()

        all_accuracies.append(f"{dataset}, {name}, {accuracies}\n")

if __name__ == '__main__':
    accuracies = []
    datasets = ["karate", "football", "email", "amazon", "youtube"]
    run(datasets, "lpa", accuracies)
    run(datasets, "gn", accuracies)
    run(datasets, "gm", accuracies)

    with open("accuaracy.txt", "w") as file:
        file.writelines(accuracies)
