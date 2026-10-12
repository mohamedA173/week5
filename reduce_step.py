# reduce step
# adds up the 1s for each category to get the final counts

import json
import os

with open("shuffle_outputs/grouped.json") as f:
    grouped = json.load(f)

os.makedirs("results", exist_ok=True)
with open("results/final_counts.csv", "w") as out:
    out.write("item_category,count\n")
    for key in grouped:
        total = sum(grouped[key])
        out.write(key + "," + str(total) + "\n")
        print(key, "->", total)