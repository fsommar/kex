# vim: tabstop=2 softtabstop=2 shiftwidth=2 expandtab
"""
  Split the data into a training and validation set, each
  set containing 50/50 positive and negative reviews.
"""

import os
import numpy as np
from glob import glob


MAIN_PATH = os.path.dirname(__file__) + "/../data/aclImdb/test"

def split():
  """
    Returns: validation_set, training_set
  """
  POS_PATH = MAIN_PATH + "/pos"
  NEG_PATH = MAIN_PATH + "/neg"

  pos = []
  neg = []

  def from_files(lst, path):
    files = glob(path+"/[!.]*.txt")

    for file in files:
      with open(file, 'r') as f:
        lst.append(f.read())

  from_files(pos, POS_PATH)
  from_files(neg, NEG_PATH)

  # Assume evenly-distributed data (50/50 pos/neg)
  half = len(pos)//2 # len(pos) == len(neg)
  validation = {
      "data": np.array(pos[:half] + neg[:half]),
      "target": np.array([1] * half + [0] * half),
      }
  training = {
      "data": np.array(pos[half:] + neg[half:]),
      "target": np.array([1] * half + [0] * half),
      }

  return validation, training
