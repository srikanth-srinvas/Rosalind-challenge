import argparse

def find_pattern_occurrences(pattern, genome):
    """
    Finds all starting positions of the pattern in the genome string.

    Args:
    pattern (str): The pattern to search for.
    genome (str): The genome string where the search is conducted.

    Returns:
    list: A list of starting positions (0-based indexing).
    """
    positions = []
    pattern_length = len(pattern)

    for i in range(len(genome) - pattern_length + 1):
        if genome[i:i + pattern_length] == pattern:
            positions.append(i)

    return positions

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Find all occurrences of a pattern in a genome string.")
    parser.add_argument("input_file", help="Path to the input .txt file containing the pattern and genome.")

    # Parse arguments
    args = parser.parse_args()

    # Read input file
    with open(args.input_file, "r") as file:
        lines = file.readlines()

    # Extract pattern and genome, and handle extra spaces or newline characters
    pattern = lines[0].strip()
    genome = lines[1].strip()

    # Find pattern occurrences
    positions = find_pattern_occurrences(pattern, genome)

    # Print results as a space-separated string
    print(" ".join(map(str, positions)))

if __name__ == "__main__":
    main()
    