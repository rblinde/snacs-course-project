''' Create network visualisation of karate club network'''

import random
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import community

random.seed(38838)

COLORS = {0: '#F44336', 1: '#3F51B5'}

def convert_communities(communities):
    sequence = {};

    for i, c in enumerate(communities):
        for node in list(c):
            sequence[int(node)] = i

    sequence = sorted(list(sequence.items()))
    return [i[1] for i in sequence]

def ground_truth():
    ''' Find ground truth '''
    communities = list()
    with open('datasets/karate/communities.txt') as file:
        communities = [int(i.split()[1]) for i in file.readlines()]
    return communities

def create_figure(truth):
    ''' Create image '''
    graph = nx.read_edgelist('datasets/karate/edges.txt')
    communities = list(community.asyn_lpa_communities(graph))
    communities = convert_communities(communities)

    edgecolors = [COLORS[i] for i in truth]
    nodecolors = [COLORS[i] for i in communities]
    position = nx.spring_layout(graph)
    nx.draw(graph, position, node_color=nodecolors, edgecolors=edgecolors, linewidths=2)

    # plt.axis('off')
    # plt.subplots_adjust(top=5)
    plt.suptitle(f"Zachary karate network compared to ground-truth")
    plt.savefig('plots/karate-graph.png', bbox_inches='tight')

if __name__ == '__main__':
    TRUTH = ground_truth()
    create_figure(TRUTH)
