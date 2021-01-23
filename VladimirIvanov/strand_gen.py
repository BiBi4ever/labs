#!/usr/bin/env python3

from typing import *
from random import shuffle


def gen_sequence_percent(length: int, percentages: Dict[AnyStr, float] = {}) -> AnyStr:
    """ Generates random sequence with specified nucleotide content
    """
    pile = ""
    for nuc, perc in percentages.items():
        pile += nuc * int(length * perc)
    pile = [n for n in pile]
    shuffle(pile)
    return ''.join(pile)

