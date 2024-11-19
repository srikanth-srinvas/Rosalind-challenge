import argparse

def hamming_distance(s, t):
    """
    Calculate the Hamming distance between two strings s and t.
    """
    return sum(1 for a, b in zip(s, t) if a != b)

def main():
    parser = argparse.ArgumentParser(description="Calculate the Hamming distance between two DNA strings.")
    parser.add_argument("input_file", help="Input file containing two DNA strings on separate lines.")
    args = parser.parse_args()

    # Read the input file
    with open(args.input_file, "r") as file:
        lines = file.readlines()
        s = lines[0].strip()  # First DNA string
        t = lines[1].strip()  # Second DNA string

    # Calculate the Hamming distance
    distance = hamming_distance(s, t)

    # Print the result
    print(distance)

if __name__ == "__main__":
    main()