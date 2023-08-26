import sys
import tweepy
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

consumer_key = config["twitter_keys"]["consumer_key"]
consumer_secret = config["twitter_keys"]["consumer_secret"]
access_token = config["twitter_keys"]["access_token"]
access_token_secret = config["twitter_keys"]["access_token_secret"]


def request(target_user_name):
    source_user_name = "FTovarys"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    can_dm = False
    try:
        response = api.get_friendship(source_screen_name=source_user_name, target_screen_name=target_user_name)
        can_dm = response[0].can_dm
        return can_dm
    except tweepy.errors.NotFound:
        # User does not exist.
        return can_dm
    except tweepy.errors.Unauthorized:
        # Wrong authentication vqlues.
        print("Unauthorized")
        sys.exit()
    except tweepy.errors.TweepyException:
        print("Bad internet connection")
        # Maded for bad internet connection, but works for auth error too.
        sys.exit()
