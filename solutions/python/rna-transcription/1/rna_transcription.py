COMPLEMENTS = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

def to_rna(dna_strand: str) -> str:
    """Transcribes a DNA strand to RNA.

    Given a DNA strand, return its RNA complement (per RNA transcription).
        G -> C
        C -> G
        A -> U
        T -> A

    Args:
        dna_strand (str): The DNA strand to be transcribed.

    Returns:
        str: The RNA complement of the input DNA strand.
    """

    return ''.join(COMPLEMENTS[base] for base in dna_strand)
