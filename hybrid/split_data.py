# vim: tabstop=2 softtabstop=2 shiftwidth=2 expandtab
import numpy as np
from glob import glob

def split(path):
  POS_PATH = path + "/pos"
  NEG_PATH = path + "/neg"

  files = glob(path+"/[!.]*.txt")
  pos = []
  neg = []

  def from_files(lst, p):
    files = glob(p+"/[!.]*.txt")

    for file in files:
      with open(file, 'r') as f:
        lst.append(f.read())

  from_files(pos, POS_PATH)
  from_files(neg, NEG_PATH)

  # Assume evenly-distributed data (50/50 pos/neg)
  half = len(pos)/2 # len(pos) == len(neg)
  # TODO: shuffle data before-hand?
  validation = {
      "data": np.array(pos[:half] + neg[:half]),
      "target": np.array([1] * half + [0] * half),
      }
  training = {
      "data": np.array(pos[half:] + neg[half:]),
      "target": np.array([1] * half + [0] * half),
      }

  return validation, training
