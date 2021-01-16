#!/usr/bin/env python3

from typing import *
from itertools import product


aatocodons = {'F': ['UUU', 'UUC'],
              'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'],
              'I': ['AUU', 'AUC', 'AUA'],
              'V': ['GUU', 'GUC', 'GUA', 'GUG'],
              'M': ['AUG'],
              'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'P': ['CCU', 'CCC', 'CCA', 'CCG'],
              'T': ['ACU', 'ACC', 'ACA', 'ACG'],
              'A': ['GCU', 'GCC', 'GCA', 'GCG'],
              'Y': ['UAU', 'UAC'],
              'H': ['CAU', 'CAC'],
              'N': ['AAU', 'AAC'],
              'D': ['GAU', 'GAC'],
              '*': ['UAA', 'UAG', 'UGA'],
              'Q': ['CAA', 'CAG'],
              'K': ['AAA', 'AAG'],
              'E': ['GAA', 'GAG'],
              'C': ['UGU', 'UGC'],
              'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
              'G': ['GGU', 'GGC', 'GGA', 'GGG'],
              'W': ['UGG']}


def reverse_transctibe(peptide: AnyStr) -> Sequence[AnyStr]:
    """ Returns all possible nucleotide strings, which transcribes to specified peptide sequence
    """
    return [''.join(strand) for strand in product(*[aatocodons[aa] for aa in peptide])]

