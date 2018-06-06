#!/usr/bin/env python
"""
guoweilin
2017.11

This module train itemsimilar
"""

import sys
import math

def itemSimilarity(train):
	"""
	cal co-rated users between items
	"""	
	C = dict()
	N = dict()
	for u, items in train.items():
		for i in items:
			if i not in N:
				N[i] = 1
			else:
				N[i] += 1
			for j in items:
				if i == j:
					continue
				if i not in C:
					C[i] = dict()
				if j not in C[i]:
					C[i][j] = 1 / math.log(1 + len(items) * 1.0)
				else:
					C[i][j] += 1 / math.log(1 + len(items) * 1.0)

	#cal final similarity matrix W
	W = dict()
	for i, related_users in C.items():
		for j, cij in related_users.items():
			if i not in W:
				W[i] = dict()
			W[i][j] = cij / math.sqrt(N[i] * N[j])	
	return W
