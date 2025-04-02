# create transcript files from other.tsv of common voice dataset
import os
from tqdm import tqdm
import csv

with open(
    os.path.join(os.getcwd(), "data", "other.tsv"),
    "r",
    encoding="utf-8"
) as file:
    reader = csv.reader(file, delimiter="\t")
    next(reader)
    for row in tqdm(reader):
        filename = row[1].split(".")[0]
        open(
            os.path.join(os.getcwd(), "data", "clips", f"{filename}.txt"),
            "w",
            encoding="utf-8"
        ).write(row[3])
