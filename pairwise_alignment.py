import numpy as np


class direction: 
    diagonal = 0
    left = 1
    up = 2
    none = 3

class cell:
    score = 0
    direction = direction.none

def make_matrix(seq_v, seq_w):
    matrix = np.empty((len(seq_v) + 1, len(seq_w) + 1), dtype=cell)
    for i in range(len(seq_v) + 1):
        matrix[i][0] = cell()

    for j in range(len(seq_w) + 1):
        matrix[0][j] = cell()

    return matrix


def pairwise_alignment(seq_v, seq_w, blosum, penalty):
    matrix = make_matrix(seq_v, seq_w)

    for i in range(1, len(seq_v) + 1):
        for j in range(1, len(seq_w) + 1):
            matrix[i][j] = cell()

            score_left = matrix[i][j - 1].score + penalty
            score_up = matrix[i - 1][j].score + penalty
            score_diagonal = (matrix[i - 1][j - 1].score + blosum[seq_v[i - 1]][seq_w[j - 1]])

            if score_diagonal >= score_left and score_diagonal >= score_up:
                matrix[i][j].score = score_diagonal
                matrix[i][j].direction = direction.diagonal
            elif score_left >= score_up:
                matrix[i][j].score = score_left
                matrix[i][j].direction = direction.left
            else:
                matrix[i][j].score = score_up
                matrix[i][j].direction = direction.up

    new_seq_v = ""
    new_seq_w = ""
    i = len(seq_v)
    j = len(seq_w)

    while i > 0 and j > 0:
        if matrix[i][j].direction == direction.diagonal:
            new_seq_v = seq_v[i - 1] + new_seq_v
            new_seq_w = seq_w[j - 1] + new_seq_w
            i -= 1
            j -= 1
        elif matrix[i][j].direction == direction.up:
            new_seq_v = seq_v[i - 1] + new_seq_v
            new_seq_w = "-" + new_seq_w
            i -= 1
        else:
            new_seq_v = "-" + new_seq_v
            new_seq_w = seq_w[j - 1] + new_seq_w
            j -= 1

    while i > 0:
        new_seq_v = seq_v[i - 1] + new_seq_v
        new_seq_w = "-" + new_seq_w
        i -= 1

    while j > 0:
        new_seq_v = "-" + new_seq_v
        new_seq_w = seq_w[j - 1] + new_seq_w
        j -= 1
    
    return (new_seq_v, new_seq_w)
