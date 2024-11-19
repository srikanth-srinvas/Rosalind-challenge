import argparse

# RNA codon table mapping
CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

def translate_rna_to_protein(rna_sequence):
    """
    Translate an RNA sequence into a protein sequence using the codon table.
    """
    protein = []
    for i in range(0, len(rna_sequence), 3):  # Process RNA in codons (triplets)
        codon = rna_sequence[i:i+3]
        if codon in CODON_TABLE:
            amino_acid = CODON_TABLE[codon]
            if amino_acid == '':  # Stop codon encountered
                break
            protein.append(amino_acid)
    return ''.join(protein)

def main():
    parser = argparse.ArgumentParser(description="Translate RNA into a protein string.")
    parser.add_argument("input_file", help="Input file containing the RNA sequence.")
    args = parser.parse_args()

    # Read RNA sequence from file
    with open(args.input_file, "r") as file:
        rna_sequence = file.readline().strip()

    # Translate RNA to protein
    protein = translate_rna_to_protein(rna_sequence)

    # Print the protein string
    print(protein)

if __name__ == "__main__":
    main()