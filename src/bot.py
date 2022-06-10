import tweepy
from time import sleep
import credentials # User specific API credentials

class NewsBot:
    def __init__(self):
        self.headline = ""
        self.forecast = ""

        auth = tweepy.OAuthHandler(credentials.key, credentials.secret_key, credentials.bearer_token)
        self.api = tweepy.API(auth)
        print("News bot online")

    def activate(self):
        print("Bot running")

    def __scan_and_compile_news(self):
        rawHeadline = "headline"
        self.headline = self.__filter(rawHeadline)

    def __check_forecast(self):
        self.forecast = ""
    
    def __filter(self, rawText: str):
        """Modifies an input string by changing some words to make it funnier"""
        return f"new {rawText}"

    def post_news(self):
        self.__scan_and_compile_news()
        print(self.headline)

    def post_weather(self):
        print(self.forecast)