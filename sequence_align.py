#This script aligns nucleotude sequences wuth G4 parts detected by the eltetrado software

import glob
import re
import os
from Bio import pairwise2
from Bio import Align

target_seq= # input the target sequence here with "" quotes, e.g. "UGUGGGAUGGGCGGGUCUGGGA"

pdb_f=glob.glob("/home/user/*.g4seq") #this selects the input folder
alignments = [] # Store alignments with scores

for p_f in pdb_f:
    with open(p_f) as f_h:
        lines=[s.strip() for s in f_h.readlines()]
        for l in lines:
            tmp_p_seq=l
            print(tmp_p_seq)
            alignment=pairwise2.align.localms(target_seq, tmp_p_seq, 5, -4,-2,-0.5)
            aligner=Align.PairwiseAligner()
            aligner.mode="global"
            alignment2=aligner.align(tmp_p_seq, target_seq)
            print(p_f)
            for a in alignment:
                print(pairwise2.format_alignment(*a, full_sequences=True))
            for a in alignment2:
                print(a.score)
                print(a)
                #break statement to exit the loop after alignment printing output
                break
