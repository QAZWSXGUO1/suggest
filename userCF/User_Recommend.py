#!/usr/bin/env python
"""
guoweilin
2017.10

This module cal recommend
"""

import sys
import math
import operator

def Recommend(user, train, W, K):
	"""
	user:recom to who
	train:test
	W:output of UserSimilarity
	"""
	rank = dict()
	interacted_items = train[user]
	for v, wuv in sorted(W[user].iteritems(), key=lambda d:d[1], reverse = True)[0 : K]:
		for i, rvi, in train[v].items():
			if i in interacted_items:
				# user has buied, not need suggest
				continue
			if i not in rank:
				rank[i] =  wuv * rvi
			else:
				rank[i] += wuv * rvi
	return sorted(rank.iteritems(), key=lambda d:d[1], reverse = True)
