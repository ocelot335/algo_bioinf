import argparse
import math
import sys


def calc_parameters(gc1_perc, gc2_perc, mean_len):
    """
    Возвращает (log_start, log_trans, log_emit).
    """
    p_change = 1.0 / mean_len
    p_stay = 1.0 - p_change

    log_trans = {
        0: {0: math.log(p_stay), 1: math.log(p_change)},
        1: {0: math.log(p_change), 1: math.log(p_stay)},
    }

    gc1 = gc1_perc / 100.0
    gc2 = gc2_perc / 100.0

    p_g1 = p_c1 = gc1 / 2.0
    p_a1 = p_t1 = (1.0 - gc1) / 2.0

    p_g2 = p_c2 = gc2 / 2.0
    p_a2 = p_t2 = (1.0 - gc2) / 2.0

    log_emit = {
        0: {
            "G": math.log(p_g1),
            "C": math.log(p_c1),
            "A": math.log(p_a1),
            "T": math.log(p_t1),
        },
        1: {
            "G": math.log(p_g2),
            "C": math.log(p_c2),
            "A": math.log(p_a2),
            "T": math.log(p_t2),
        },
    }

    log_start = [math.log(0.5), math.log(0.5)]

    return log_start, log_trans, log_emit


def read_input(filename):
    seq = []
    try:
        with open(filename, "r") as f:
            first_line = f.readline()
            if not first_line.startswith(">"):
                seq.append(first_line.strip().upper())

            for line in f:
                line = line.strip().upper()
                if not line.startswith(">"):
                    seq.append(line)
    except FileNotFoundError:
        print(f"! Файл {filename} не найден.")
        sys.exit(1)

    full_seq = "".join(seq)
    full_seq = full_seq.replace(" ", "").replace("\n", "").replace("\r", "")
    return full_seq


def viterbi_calc(seq, log_start, log_trans, log_emit):
    """
    seq: строка ДНК
    log_start: {0: val, 1: val}
    log_trans: {0: {0: val, 1: val}, 1: ...}
    log_emit:  {0: {'A': val...}, 1: ...}
    """
    n = len(seq)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = log_start[0] + log_emit[0][seq[0]]
    dp[0][1] = log_start[1] + log_emit[1][seq[0]]
    backtr = [[0, 0] for _ in range(n)]
    for i in range(1, n):
        p0_from0 = dp[i - 1][0] + log_trans[0][0]
        p0_from1 = dp[i - 1][1] + log_trans[1][0]

        if p0_from0 >= p0_from1:
            dp[i][0] = p0_from0 + log_emit[0][seq[i]]
            backtr[i][0] = 0
        else:
            dp[i][0] = p0_from1 + log_emit[0][seq[i]]
            backtr[i][0] = 1

        p1_from1 = dp[i - 1][1] + log_trans[1][1]
        p1_from0 = dp[i - 1][0] + log_trans[0][1]

        if p1_from1 >= p1_from0:
            dp[i][1] = p1_from1 + log_emit[1][seq[i]]
            backtr[i][1] = 1
        else:
            dp[i][1] = p1_from0 + log_emit[1][seq[i]]
            backtr[i][1] = 0

    mark = 0
    marking = []
    if dp[n - 1][0] >= dp[n - 1][1]:
        mark = 0
    else:
        mark = 1

    for i in range(n - 1, 0, -1):
        marking.append(str(mark + 1))
        mark = backtr[i][mark]
    marking.append(str(mark + 1))
    return "".join(reversed(marking))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Входной файл последовательности")

    parser.add_argument(
        "--gc1",
        type=float,
        required=True,
        help="GC%% первой бактерии(e.g. 28.49)",
    )
    parser.add_argument(
        "--gc2",
        type=float,
        required=True,
        help="GC%% второй бактерии(e.g. 72.65)",
    )
    parser.add_argument(
        "--mean",
        type=float,
        default=300,
        help="Средняя длина фрагмента(по умолчанию 300)",
    )

    parser.add_argument(
        "--output", "-o", default="decoded.txt", help="выходной файл"
    )

    args = parser.parse_args()

    log_start, log_trans, log_emit = calc_parameters(
        args.gc1, args.gc2, args.mean
    )

    sequence = read_input(args.input_file)

    decoded_path = viterbi_calc(sequence, log_start, log_trans, log_emit)

    with open(args.output, "w") as f:
        f.write(decoded_path)


if __name__ == "__main__":
    main()
