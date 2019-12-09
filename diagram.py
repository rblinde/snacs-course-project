import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
sns.set_palette("husl")

datasets = ["Zachary karate", "US football", "email-Eu-core", "com-Amazon", "com-Youtube"]
data = {
    0: ["LPA", 0, 1.7914],
    1: ["LPA", 1, 9.6789],
    2: ["LPA", 2, 356.3242],
    3: ["LPA", 3, 92392.8496],
    4: ["BC", 0, 0.0002],
    5: ["BC", 1, 0.0003],
    6: ["BC", 2, 0.0003],
    7: ["BC", 3, 0.0002],
    8: ["BC", 4, 0.0004],
    9: ["M", 0, 3.1276],
    10: ["M", 1, 26.2841],
    11: ["M", 2, 2518.0923],
}

df = pd.DataFrame.from_dict(data, orient="index", columns=["Algorithm", "Dataset", "Time"])
fig = sns.lineplot(x="Dataset", y="Time", data=df, hue="Algorithm")

plt.xlabel("Dataset")
plt.xticks([0, 1, 2, 3, 4], datasets)
plt.ylabel("Runtime (ms)")
plt.yscale("log")
plt.subplots_adjust(top=0.9)
plt.suptitle(f"Runtime of algorithms for each dataset")
plt.savefig(f"plots/timings.png", bbox_inches='tight')
