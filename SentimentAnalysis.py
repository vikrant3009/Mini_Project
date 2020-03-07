# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:04:14 2020

@author: VIKRANT
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
headline = '''Yes Bank problem bank-specific, not sectoral: SBI chief
"This is not a sectoral problem. It is a bank-specific problem," he said. "The RBI will take all steps to ensure financial stability.'''
print("Sentiment Score : " , sia.polarity_scores(headline)['compound'])