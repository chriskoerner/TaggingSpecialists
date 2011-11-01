# -*- coding: utf-8 -*-

__author__ = 'kschoef'

import copy

#normalize data to be in the range of [0,1].
#NB: some values are -1, which basically means that the trust of this user is 1.0 - which in turn means that the specifity of the user could not be calculated
def normalize_data(list_):
  max_ = max(list_)
  list_c = copy.deepcopy(list_)
  for i in range(list_c.count(-1.0)):
    list_c.remove(-1.0)
  min_ = min(list_c)
  for i in range(len(list_)):
    if not(list_[i] == -1):
      list_[i] = float(list_[i])/(max_-min_)  
    else:
      list_[i] = -1.0
  return list_