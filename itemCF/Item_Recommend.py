#!/usr/bin/env python
"""
guoweilin
2017.11

This module cal recommend
"""

import sys
import math
import operator

def Recommend(train, user_id, W, K):
	rank = dict()
	ru = train[user_id]
	for i, pi in ru.items():
		for j, wj in sorted(W[i].iteritems(), key=lambda d:d[1], reverse = True)[0 : K]:
			if j in ru:
				continue
			if j not in rank:
				rank[j] = pi * wj
			else:
				rank[j] += pi * wj
	return sorted(rank.iteritems(), key=lambda d:d[1], reverse = True)
