"""DNA Sequence Analyzer — beginner-friendly bioengineering mini project."""


def analyze_dna(sequence):
    dna = "".join(sequence.upper().split())

    if not dna:
        print("Error: Please enter a DNA sequence.")
        return

    if any(base not in "ATGC" for base in dna):
        print("Invalid DNA! Use only A, T, G, C.")
        return

    print("\n===== DNA ANALYSIS REPORT =====")
    print("DNA Sequence:", dna)
    print("Total Nucleotides:", len(dna))

    for base in "ATGC":
        count = dna.count(base)
        percentage = count / len(dna) * 100
        print(f"{base}: {count} ({percentage:.2f}%)")

    gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
    print(f"GC Content: {gc:.2f}%")

    complement = dna.translate(str.maketrans("ATGC", "TACG"))
    print("Complementary DNA:", complement)

    rna = dna.replace("T", "U")
    print("RNA Sequence:", rna)
    print("================================")


if __name__ == "__main__":
    sequence = input("Enter DNA Sequence: ")
    analyze_dna(sequence)
