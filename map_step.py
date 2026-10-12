# map step
# goes through each partition file one at a time and makes (category, 1) pairs

import csv
import os

partitions = ["partition1.csv", "partition2.csv", "partition3.csv"]

os.makedirs("map_outputs", exist_ok=True)

for file_name in partitions:
    pairs = []

    with open("data/" + file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            pairs.append((row["item_category"], 1))

    # save the pairs for this partition
    out_name = "map_outputs/" + file_name.replace(".csv", "_map.csv")
    with open(out_name, "w") as out:
        out.write("key,value\n")
        for key, value in pairs:
            out.write(key + "," + str(value) + "\n")

    print(file_name, "->", len(pairs), "pairs")