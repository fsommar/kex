# vim: tabstop=2 softtabstop=2 shiftwidth=2 expandtab
import numpy as np

# 0 < ratio <= 1
# target: list of numbers in range from -5 to 5
def prune(validation, data, target, ratio=1):
  # sort data based on `target` values between 5 .. -5
  target_data = sorted(zip(target, data, validation), key=lambda tup: tup[0])

  if (ratio < 1):
    # decide cut off point
    cutoff = int(ratio * len(target_data) // 2)
    # grab bottom and top cutoffs
    target_data = target_data[:cutoff] + target_data[cutoff:]

  # remove zeroes and change values to 0, 1
  target_data = [(1 if t > 0 else 0, d, v) for (t, d, v) in target_data if not t == 0]

  # unzip updated data and target
  n_target, n_data, n_validation = zip(*target_data)

  return n_validation, n_data, n_target
