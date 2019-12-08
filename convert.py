from collections import defaultdict

def write_to_file(name, communities):
    communities = sorted(list(communities.items()))
    communities = [f"{i[0]} {','.join(str(x) for x in i[1])}\n" for i in communities]

    with open(name, "w") as file:
        file.writelines(communities)

def get_communities(file):
    communities = defaultdict(list)

    for idx, line in enumerate(file.readlines()):
        nodes = [int(x) for x in line.strip().split('\t')]
        for node in nodes:
            communities[node].append(idx)

    return communities

def main(datasets):
    for dataset in datasets:
        file_name = f"datasets/{dataset}/communities-source.txt"
        with open(file_name) as file:
            communities = get_communities(file)
            write_to_file(f"datasets/{dataset}/communities.txt", communities)

if __name__ == '__main__':
    datasets = ["amazon", "youtube"]
    main(datasets)