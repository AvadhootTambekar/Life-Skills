# DNA Sequence Analyzer 🧬

A beginner-friendly **Python bioengineering mini project** that analyzes DNA sequences and demonstrates basic concepts in molecular biology and bioinformatics.

## Project Overview

DNA consists of four nucleotide bases: adenine (**A**), thymine (**T**), guanine (**G**), and cytosine (**C**). This command-line program accepts a DNA sequence and produces a simple analysis report.

## Features

- Validates DNA input (accepts only A, T, G, and C).
- Counts the total number of nucleotides.
- Calculates the count and percentage of each nucleotide.
- Calculates **GC content** as a percentage.
- Produces the **complementary DNA strand** using A ↔ T and G ↔ C pairing.
- Transcribes the entered DNA sequence into RNA by replacing T with U.
- Accepts lowercase input and ignores spaces and other whitespace.

## Technologies Used

- **Language:** Python 3
- **Libraries:** None (Python standard features only)
- **Interface:** Command line / terminal

## Getting Started

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python dna_sequence_analyzer.py
   ```

   On some systems, use `python3` instead of `python`.
5. Enter a DNA sequence when prompted.

## Example

**Input:**

```text
Enter DNA Sequence: ATGCGTAC
```

**Output:**

```text
===== DNA ANALYSIS REPORT =====
DNA Sequence: ATGCGTAC
Total Nucleotides: 8
A: 2 (25.00%)
T: 2 (25.00%)
G: 2 (25.00%)
C: 2 (25.00%)
GC Content: 50.00%
Complementary DNA: TACGCATG
RNA Sequence: AUGCGUAC
================================
```

## Scientific Concepts

**GC content** describes the proportion of DNA bases that are guanine or cytosine:

```text
GC Content (%) = [(G + C) / Total nucleotides] × 100
```

**Complementary DNA** is determined by base-pairing rules: A pairs with T, and G pairs with C. The displayed complement is aligned base-for-base with the entered strand (it is not the reverse complement).

**RNA transcription (simplified):** This program replaces T with U in the entered DNA strand, treating it as a coding-strand sequence. It does not perform full biological transcription or translate RNA into protein.

## Project Structure

```text
DNA-Sequence-Analyzer/
├── dna_sequence_analyzer.py   # Main Python program
└── README.md                  # Project documentation
```

## Learning Outcomes

This project offers practice with Python functions, strings, loops, input validation, percentages, and fundamental DNA/RNA concepts.

## Future Improvements

- Add reverse-complement calculation.
- Read DNA sequences from FASTA files.
- Calculate sequence statistics for multiple samples.
- Build a graphical interface for easier use.

## Academic Purpose

Created as an educational mini project for **B.Tech Bioengineering** students learning Python and introductory bioinformatics.
