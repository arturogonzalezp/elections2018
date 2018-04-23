import indicoio
import os

LANGUAGE = "es"

class SentimentAnalyzer:
    def __init__(self):
        self.indicoio = indicoio
        self.indicoio.config.api_key = os.environ.get("INDICO_API_KEY")

    def analyze_sentiment(self, text):
        sentiment = self.indicoio.sentiment(text, language=LANGUAGE)
        return sentiment