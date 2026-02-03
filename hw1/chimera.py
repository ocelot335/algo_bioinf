import argparse
import random
import sys


def read_genome(filename):
    seq = []
    try:
        with open(filename, "r") as f:
            f.readline()  # пропускаем первую строку
            for line in f:
                seq.append(line.strip())
    except FileNotFoundError:
        print(f"! Файл {filename} не найден.")
        sys.exit(1)

    return "".join(seq)


def get_fragment(genome, mean_length):
    genome_len = len(genome)

    # пока не нашли подходящий кусок
    while True:
        chunk_len = int(random.expovariate(1.0 / mean_length))

        start_pos = random.randint(0, genome_len - chunk_len)

        chunk = genome[start_pos : start_pos + chunk_len]

        if set(chunk).issubset({"A", "C", "G", "T"}):
            return chunk


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("genome1", help="Файл первого генома(FASTA)")
    parser.add_argument("genome2", help="Файл второго генома(FASTA)")

    parser.add_argument(
        "--length",
        "-l",
        type=int,
        default=10000,
        help="Длина генерируемой последовательности",
    )
    parser.add_argument(
        "--mean", "-m", type=int, default=300, help="Средняя длина фрагмента"
    )

    parser.add_argument(
        "--output",
        "-o",
        default="chimera.fasta",
        help="Имя выходного файла(FASTA)",
    )
    parser.add_argument(
        "--truth",
        "-t",
        default="marks.txt",
        help="Имя файла с правильными ответами",
    )

    args = parser.parse_args()

    genome1 = read_genome(args.genome1)
    genome2 = read_genome(args.genome2)

    current_length = 0
    chimera = []
    true_marks = []

    current_genome_to_select = random.choice(
        [0, 1]
    )  # чтобы не всегда начинали химеру с чего-то одного

    while current_length < args.length:
        if current_genome_to_select == 0:
            fragment = get_fragment(genome1, args.mean)
        else:
            fragment = get_fragment(genome2, args.mean)

        chimera.append(fragment)
        true_marks.extend([str(current_genome_to_select + 1)] * len(fragment))

        current_length += len(fragment)
        current_genome_to_select = 1 - current_genome_to_select

    final_seq = "".join(chimera)[: args.length]
    final_truth = "".join(true_marks)[: args.length]

    with open(args.output, "w") as f:
        f.write(">Chimera\n")
        f.write(final_seq + "\n")

    with open(args.truth, "w") as f:
        f.write(final_truth)


if __name__ == "__main__":
    main()
