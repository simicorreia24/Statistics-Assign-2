#!/usr/bin/env python
# coding: utf-8

# # Statistics Assignment 2
# 
# Question1:
# 
# Raindrops are falling at an average rate of 20 drops per square inch per minute. What would
# be a reasonable distribution to use for the number of raindrops hitting a particular region
# measuring 5 inches2 in t minutes? Why? Using your chosen distribution, compute the
# probability that the region has no rain drops in a given 3 second time interval. A reasonable
# choice of distribution is P
# 
# Solution: 
# 
# We need to use Poisson Distribution in this question
# Firstly, we need to find the amount of rainfall in t minutes
# t*no of drops*inches = t * lambda 
#                                    = t * 20* 5 
#                                    = 100t 
# Therefore, there are 100 drops for 5 square inches.
# 20 has been chosen as it is being mentioned that the region has no rain drops in a given 3second time interval. 20 in 1 minute or 60 seconds calculation.
# P(X=0) = ((100/20)^0/0!)*e^-100/20 = e-5 = 6.737947 * 10-3
# 
# Question2:
# 
# Let X be a random day of the week, coded so that Monday is 1, Tuesday is 2, etc. (so X takes
# values 1, 2,..., 7, with equal probabilities). Let Y be the next day after X (again represented as
# an integer between 1 and 7). Do X and Y have the same distribution? What is P(X)
# 
# Solution:
# 
# X    Y    P(X)     P(Y)
# 1    2    1/7     1/7
# 2    3    1/7     1/7 
# 3    4    1/7     1/7
# 4    5    1/7     1/7
# 5    6    1/7     1/7
# 6    7    1/7     1/7
# X and Y follows same distribution as they are having similar data distribution or you can say same probabilities
# Here, P(X<Y) = 1/7+1/7+1/7+1/7+1/7+1/7 = 6/7
# 

# In[ ]:




