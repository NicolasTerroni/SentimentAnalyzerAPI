import os

# Set NLTK_DATA environment variable
os.environ["NLTK_DATA"] = "/usr/share/nltk_data"

import nltk
nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer


def analyze_text(text: str):
    """Receives a text message and returns NLTK sentiment analysis results."""
    
    sid = SentimentIntensityAnalyzer()
    
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores["compound"] >= 0.05:
        sentiment_label = "positive"
    elif sentiment_scores["compound"] <= -0.05:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"

    results = {
        "text": text,
        "score": float(sentiment_scores["compound"]),
        "label": sentiment_label
    }
    
    return results
