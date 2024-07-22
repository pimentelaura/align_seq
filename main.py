from blosum62 import blosum
from pairwise_alignment import pairwise_alignment

seq_v = input(str("Insert sequence v: "))
seq_w = input(str("Insert sequence w: "))
penalty = int(input("Insert the penalty: "))
seq_v = seq_v.upper()
seq_w = seq_w.upper()

(seq_v_aligned, seq_w_aligned) = pairwise_alignment(seq_v, seq_w, blosum, penalty)

print(f'Aligned sequences:\n{seq_v_aligned}\n{seq_w_aligned}')
