from Bio import SeqIO

def my_fasta(filename:str) -> dict:
    return {fasta.id:str(fasta.seq) for fasta in SeqIO.parse(open(filename),'fasta')}