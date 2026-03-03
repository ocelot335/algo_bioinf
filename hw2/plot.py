import matplotlib.pyplot as plt

x = list(range(1, 11))

y_experimental = [
    0.658,
    1.186,
    1.734,
    2.279,
    2.832,
    3.380,
    3.872,
    4.339,
    4.769,
    5.186,
]

y_theoretical = list(range(1, 11))

plt.figure(figsize=(8, 6))

plt.plot(
    x,
    y_experimental,
    marker="o",
    linestyle="-",
    color="b",
    linewidth=2,
    label="Эксперимент",
)

plt.plot(
    x,
    y_theoretical,
    marker="",
    linestyle="--",
    color="r",
    linewidth=2,
    label="Теория",
)

plt.title(
    "Зависимость среднего числа случайных находок от порога E-value",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Порог E-value < n", fontsize=12)
plt.ylabel("Среднее количество находок на 1 запрос", fontsize=12)

plt.xticks(x)
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(fontsize=11)

plt.savefig("evalue_graph.png", dpi=300, bbox_inches="tight")
