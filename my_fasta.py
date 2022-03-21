from Bio import SeqIO

def my_parser(filename:str) -> dict:
    """
    Renvoie un dictionnaire contenant toutes les séquences
    key : desc de la séquence
    value : séquence
    """
    return {fasta.id:str(fasta.seq) for fasta in SeqIO.parse(open(filename),'fasta')}