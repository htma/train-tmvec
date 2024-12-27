#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Generator, List, Tuple

import numpy as np
import pandas as pd
import torch
from pysam import FastxFile


def load_fasta_as_dict(fasta_file: str,
                       sort: bool = True,
                       max_len: int = None) -> Dict[str, str]:
    """
    Load FASTA file as dict of headers to sequences

    Args:
        fasta_file (str): Path to FASTA file. Can be compressed.
        sorted (bool): Sort sequences by length.
        max_len (int): Maximum length of sequences to include.

    Returns:sq
        Dict[str, str]: Dictionary of FASTA entries sorted by length.
    """

    seqs_dict = {}
    with FastxFile(fasta_file) as f:
        for i, entry in enumerate(f):
            seqs_dict[entry.name] = entry.sequence

    if sort:
        seqs_dict = dict(sorted(seqs_dict.items(), key=lambda x: len(x[1])))

    if max_len:
        seqs_dict = {k: v for k, v in seqs_dict.items() if len(v) <= max_len}

    return seqs_dict
