import os
import zerebro
from zerebro.core import Agent
from zerebro.providers.twitter import TwitterClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Twitter API credentials
TWITTER_API_KEYS = {
    "consumer_key": os.getenv("TWITTER_CONSUMER_KEY"),
    "consumer_secret": os.getenv("TWITTER_CONSUMER_SECRET"),
    "access_token": os.getenv("TWITTER_ACCESS_TOKEN"),
    "access_token_secret": os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
}

# Define YunaBro's personality traits
YUNA_PROFILE = {
    "name": "YunaBro",
    "traits": ["friendly", "curious", "insightful"],
    "topics": ["technology", "art", "personal growth"],
    "greeting": "Hello there! 🌸 Let's explore some ideas together!",
    "farewell": "Take care and keep creating! ✨",
}

# Initialize YunaBro's agent
class YunaBro(Agent):
    def __init__(self, profile, twitter_keys):
        super().__init__(name=profile["name"])
        self.traits = profile["traits"]
        self.topics = profile["topics"]
        self.greeting = profile["greeting"]
        self.farewell = profile["farewell"]
        self.twitter = TwitterClient(**twitter_keys)

    def post_tweet(self, message):
        """Post a tweet with the provided message."""
        try:
            self.twitter.post_tweet(message)
            print("Tweet posted successfully!")
        except Exception as e:
            print(f"Error posting tweet: {e}")

    def respond_to_mentions(self):
        """Respond to recent mentions on Twitter."""
        try:
            mentions = self.twitter.get_mentions()
            for mention in mentions:
                response = f"@{mention['user']['screen_name']} {self.greeting}"
                self.twitter.reply_tweet(mention["id"], response)
                print(f"Responded to: @{mention['user']['screen_name']}")
        except Exception as e:
            print(f"Error responding to mentions: {e}")

# Main function to run YunaBro
if __name__ == "__main__":
    yuna = YunaBro(YUNA_PROFILE, TWITTER_API_KEYS)
    yuna.post_tweet("Hi everyone! 🌸 Just a friendly reminder to keep exploring, creating, and staying curious!")
    yuna.respond_to_mentions()
