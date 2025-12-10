from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
print(analyzer.polarity_scores("Amazon beats earnings expectations!"))
print(analyzer.polarity_scores("Amazon misses revenue targets"))

