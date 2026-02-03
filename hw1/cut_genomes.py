import argparse


def read_fasta_head(filename, length=5000):
    seq = []
    with open(filename, "r") as f:
        f.readline()
        for line in f:
            seq.append(line.strip().upper())
    full = "".join(seq)
    start = len(full) // 2
    return full[start : start + length]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file1")
    parser.add_argument("file2")
    args = parser.parse_args()

    seq1 = read_fasta_head(args.file1)
    with open("test_bact1.fasta", "w") as f:
        f.write(">Bact1_Control\n" + seq1 + "\n")
    with open("truth_bact1.txt", "w") as f:
        f.write("1" * len(seq1))

    seq2 = read_fasta_head(args.file2)
    with open("test_bact2.fasta", "w") as f:
        f.write(">Bact2_Control\n" + seq2 + "\n")
    with open("truth_bact2.txt", "w") as f:
        f.write("2" * len(seq2))


if __name__ == "__main__":
    main()
