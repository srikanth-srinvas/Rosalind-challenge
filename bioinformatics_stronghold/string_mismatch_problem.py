import argparse

def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two strings."""
    return sum(1 for a, b in zip(s1, s2) if a != b)

def generate_neighbors(pattern, d):
    """Generate all k-mers within d mismatches of the given pattern."""
    nucleotides = ['A', 'C', 'G', 'T']
    neighbors = set([pattern])

    def mutate(sequence, mismatches_remaining, current_index):
        if mismatches_remaining == 0:
            neighbors.add("".join(sequence))
            return
        if current_index == len(sequence):
            return

        # Keep current character
        mutate(sequence, mismatches_remaining, current_index + 1)

        # Replace current character with each nucleotide
        original_char = sequence[current_index]
        for nt in nucleotides:
            if nt != original_char:
                sequence[current_index] = nt
                mutate(sequence, mismatches_remaining - 1, current_index + 1)
                sequence[current_index] = original_char  # Restore original

    mutate(list(pattern), d, 0)
    return neighbors

def frequent_kmers_with_mismatches(text, k, d):
    """Find the most frequent k-mers with up to d mismatches in the text."""
    counts = {}

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        # Generate all neighbors within d mismatches
        neighbors = generate_neighbors(kmer, d)
        for neighbor in neighbors:
            counts[neighbor] = counts.get(neighbor, 0) + 1

    # Find the maximum count
    max_count = max(counts.values())

    # Find all k-mers with the maximum count
    frequent_kmers = [kmer for kmer, count in counts.items() if count == max_count]
    
    return frequent_kmers

def main():
    parser = argparse.ArgumentParser(description="Find the most frequent k-mers with mismatches in a string.")
    parser.add_argument("input_file", help="Input file containing the text and parameters.")
    args = parser.parse_args()

    # Read the input file
    with open(args.input_file, "r") as file:
        lines = file.readlines()
        text = lines[0].strip()
        k, d = map(int, lines[1].strip().split())

    # Find the frequent k-mers
    result = frequent_kmers_with_mismatches(text, k, d)

    # Print the result to the terminal
    print(" ".join(result))

if __name__ == "__main__":
    main()
