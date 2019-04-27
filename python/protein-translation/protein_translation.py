def proteins(strand):
    list_of_proteins = []
    prot_dict = {
        'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
        'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine',
        'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
        'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine',
        'UGC': 'Cysteine', 'UGG': 'Tryptophan'
    }

    list_of_codon = [strand[i: i+3] for i in range(0, len(strand), 3)]
    for cod in list_of_codon:

        if cod in ('UAA', 'UAG', 'UGA'):
            return list_of_proteins

        list_of_proteins.append(prot_dict[cod])
    return list_of_proteins
