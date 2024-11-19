import argparse

def dominant_phenotype_probability(k, m, n):
    """
    Calculate the probability of an offspring displaying the dominant phenotype
    given the population distribution of k, m, and n.
    """
    total = k + m + n  # Total number of organisms
    
    # Calculate probabilities of each mating combination
    prob_dominant = 0
    
    # Pairings with guaranteed dominant phenotype
    prob_dominant += (k / total) * ((k - 1) / (total - 1))  # AA x AA
    prob_dominant += 2 * (k / total) * (m / (total - 1))    # AA x Aa
    prob_dominant += 2 * (k / total) * (n / (total - 1))    # AA x aa

    # Pairings involving heterozygotes
    prob_dominant += (m / total) * ((m - 1) / (total - 1)) * 0.75  # Aa x Aa
    prob_dominant += 2 * (m / total) * (n / (total - 1)) * 0.5     # Aa x aa

    return prob_dominant

def main():
    parser = argparse.ArgumentParser(description="Calculate probability of dominant phenotype offspring.")
    parser.add_argument("input_file", help="Input file containing k, m, n values.")
    args = parser.parse_args()

    # Read input file
    with open(args.input_file, "r") as file:
        k, m, n = map(int, file.readline().strip().split())

    # Calculate and print result
    result = dominant_phenotype_probability(k, m, n)
    print(f"{result:.5f}")

if __name__ == "__main__":
    main()
