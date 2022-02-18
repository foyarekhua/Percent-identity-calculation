"""
Finding the percent identity between two sequences
"""

sequence = 'SNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQ'
match = '+ N+D+   GNYNY  R  R   L+PFERDIS   +     PC      NCY+PL+ YGF  T+G+GYQ'

seq_len = len(sequence)
num_of_valid = seq_len

for letter in match:
    if letter == '+' or letter == ' ':
        num_of_valid = num_of_valid - 1

percent_identity = (num_of_valid / seq_len) * 100
print(percent_identity)
