# IRP Assignment 2

Name: yash rathi
Roll Number: 2481057

## Problems

1. Reverse Word Order
2. Binary Search
3. Digit Sum Using Recursion
4. Pair Count

## Requirements

- Python 3
- Standard input and output

## How to Run

Open a terminal in the project directory and run **one program at a time**:

```bash
python3 problems/p1_reverse_words.py
python3 problems/p2_binary_search.py
python3 problems/p3_digit_sum.py
python3 problems/p4_pair_count.py
```

Enter the input requested by the selected problem. Each program reads from standard input and prints its answer to standard output.

## Tests

Each problem has an input file and its expected output in the `tests/` directory. For example:

```bash
python3 problems/p1_reverse_words.py < tests/p1_input.txt
```

Compare the result with `tests/p1_expected.txt`.

## Problem 4 interpretation

Count index pairs `(i, j)` with `i < j` such that `arr[i] + arr[j] == k`.
