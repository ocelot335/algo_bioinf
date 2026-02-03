import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("truth", help="Файл с истинной разметкой")
    parser.add_argument("prediction", help="Файл с предсказанием")
    args = parser.parse_args()

    with open(args.truth, "r") as f:
        truth_str = f.read().strip()

    with open(args.prediction, "r") as f:
        pred_str = f.read().strip()

    errors = 0
    total = len(truth_str)

    for t, p in zip(truth_str, pred_str):
        t_val = int(t)
        p_val = int(p)

        if t_val != p_val:
            errors += 1

    error_rate = (errors / total) * 100.0
    accuracy = 100.0 - error_rate

    print(f"Total length: {total}")
    print(f"Errors:       {errors}")
    print(f"Error Rate:   {error_rate:.2f}%")
    print(f"Accuracy:     {accuracy:.2f}%")


if __name__ == "__main__":
    main()
