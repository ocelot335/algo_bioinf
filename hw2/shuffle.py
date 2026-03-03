import random

with open("protein.fasta", "r") as f:
    lines = f.readlines()

protein = "".join([line.strip() for line in lines[1:]])

acids = list(protein)

with open("shuffled_1000.fasta", "w") as out_f:
    for i in range(1, 1001):
        random.shuffle(acids)
        shuffled_protein = "".join(acids)

        out_f.write(f">shuffled_{i}\n")
        out_f.write(f"{shuffled_protein}\n")
