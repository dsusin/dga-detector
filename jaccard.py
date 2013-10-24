#
# jaccard.py
# Jaccard shingling algorithm project
#
# Copyright (c) 2012, Gokul Das
#
# Modified by Daniel Susin
# - Works with Python 2.7
# - Tries to detect DGA generated domains
# - usage: jaccard.py [2nd_level_domain]. Ex: "python jaccard.py gloogle"

from __future__ import division
import sys


def bigram_shingler(str):
    """Extract a set of 2 character n-grams (character bigrams) from string"""
    big_set = {str[x:x+2] for x in range(0, len(str) -1) if len(str) > 1}
    return big_set

def jacc_ind(bigrams1, bigrams2):
    """Calculate Jaccard index for 2 bigrams"""
    unin = bigrams1 | bigrams2
    intn = bigrams1 & bigrams2
    if len(unin) == 0: return 0.0
    else: return len(intn) / len(unin)

if len(sys.argv) !=2:
    print("Missing argument")
    sys.exit()

word=sys.argv[1]

from domains import top_domains
words = top_domains.split()
corpus = {i : bigram_shingler(i) for i in words}

in_big = bigram_shingler(word)
index_list = [(i, jacc_ind(in_big, corpus[i])) for i in corpus]
sorted_list = sorted(index_list, key = lambda x : x[1], reverse = True)
print("\nThe 3 best matches are:")
for i in range(3): print(sorted_list[i][0]+": "+str(sorted_list[i][1]))
if sorted_list[i][1]<0.2:
    print "\nProbable DGA generated domain\n"
