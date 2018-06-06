#!/usr/bin/env python
"""
guoweilin
2017.10

This module train usersimilar
"""

import sys
import math

def UserSimilarity(train):
	"""
	build inverse table
	"""
	item_users = dict()
	for u, items in train.items():
		for i in items:
			if i not in item_users: 
				item_users[i] = set()
			item_users[i].add(u)

	#cal co-rated items between users
	C = dict()
	N = dict()
	for i, users in item_users.items():
		for u in users:
			if u not in N:
				N[u]  = 1
			else:
				N[u] += 1
			for v in users:
				if u == v:
					continue
				if u not in C:
					C[u] = dict()
				if v not in C[u]:
					C[u][v] = 1 / math.log(1 + len(users))
				else:
					C[u][v] += 1 / math.log(1 + len(users))

	#cal final similarity matrix W
	W = dict()
	for u, related_users in C.items():
		for v, cuv in related_users.items():
			if u not in W:
				W[u] = dict()
			W[u][v] = cuv /  math.sqrt(N[u] * N[v])
	return W
