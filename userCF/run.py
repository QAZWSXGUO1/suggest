#!/usr/bin/env python
"""
guoweilin
2017.10

This is main prosess
"""

import sys
import UserSimilarity_Train
import User_Recommend

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
	W = UserSimilarity_Train.UserSimilarity(train)		
	
	user_needed = sys.argv[1]
	rank = User_Recommend.Recommend(user_needed, train, W, 3)
	print rank
