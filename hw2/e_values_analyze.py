counts = {n: 0 for n in range(1, 11)}

with open("blast_results.tsv", "r") as f:
    for line in f:
        columns = line.strip().split("\t")

        e_value = float(columns[10])

        for n in range(1, 11):
            if e_value < n:
                counts[n] += 1

print("Порог | Всего находок | Среднее на 1 запрос")
print("-------------------------------------------")

for n in range(1, 11):
    total = counts[n]
    average = total / 1000.0
    print("E <", n, "  |  ", total, "        |  ", average)
