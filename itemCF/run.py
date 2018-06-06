#!/usr/bin/env python
"""
guoweilin
2017.11

This is main prosess
"""

import sys
import ItemSimilarity_Train
import Item_Recommend

if __name__ == '__main__':
	"""
	main
	"""
	train = dict()
	for line in sys.stdin:
		lines = line.strip().split('\t')
		train[lines[0]] = dict()
		for i in lines[1:]:
			if i not in train[lines[0]]:
				train[lines[0]][i] = 1
			else:
				train[lines[0]][i] += 1
	W = ItemSimilarity_Train.itemSimilarity(train)
	user = sys.argv[1]
	rank = Item_Recommend.Recommend(train, user, W, 3)
	print rank
