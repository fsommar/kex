# vim: tabstop=2 softtabstop=2 shiftwidth=2 expandtab
import numpy as np

def prune(validation, data, target, ratio=1):
  """
    Removes entries with polarity value = 0 and converts target values
    in range -5 .. 5 to 0 and 1 for negative and positive entries respectively.
    Optionally, if the ratio < 1 only the most informative ratio of the data
    will be returned.

    Parameters:
        validation - a list of ints in the range -5 .. 0 representing
                     the polarity of each snippet
        data       - list with snippets
        target     - same as validation
        ratio      - most informative data ratio (0 < r <= 1)

    Returns:
        validation - a binary list representing the polarity of each snippet
                     (0 - neg, 1 - pos)
        data       - list with snippets (exclusive neutral snippets)
        target     - same as validation
  """
  # sort data based on `target` values between 5 .. -5
  target_data = sorted(zip(target, data, validation), key=lambda t: t[0])

  if (ratio < 1):
    # decide cut off point
    cutoff = int(ratio * len(target_data) // 2)
    # grab bottom and top cutoffs
    target_data = target_data[:cutoff] + target_data[-cutoff:]

  # remove zeroes and change values to 0, 1
  target_data = [(1 if t > 0 else 0, d, v) for (t, d, v)\
                 in target_data if not t == 0]

  # unzip updated data and target
  n_target, n_data, n_validation = zip(*target_data)

  return n_validation, n_data, n_target
