import tweepy
import time
from config import *

def send_reply(command, mention):
    with open(command, 'r', encoding='utf8') as file:
        try:
            api.update_status(status=file.read(), in_reply_to_status_id=mention.id, auto_populate_reply_metadata=True)
        except:
            print("Failed to tweet")

def get_command(text):
    trim_text = text.replace("@" + screen_name, "").lower()
    if prompt1 in trim_text:
        return "facts/bigot.txt"
    elif prompt2 in trim_text:
        return "facts/biology.txt"
    elif prompt3 in trim_text:
        return "facts/biology.txt"
    elif prompt4 in trim_text:
        return "facts/definewoman.txt"
    elif prompt5 in trim_text:
        return "facts/definewoman.txt"
    elif prompt6 in trim_text:
        return "facts/groomer.txt"
    elif prompt7 in trim_text:
        return "facts/history.txt"
    elif prompt8 in trim_text:
        return "facts/sexualassault.txt"
    elif prompt9 in trim_text:
        return "facts/sexualassault.txt"
    elif prompt10 in trim_text:
        return "facts/suicide.txt"
    elif prompt11 in trim_text:
        return "facts/suicide.txt"
    elif prompt12 in trim_text:
        return "facts/brainwashed.txt"
    else:
        return 0

def refresh(api, last_mentions):
    mentions = api.mentions_timeline()

    if len(last_mentions) < len(mentions):
        print("New mention (Total: " + str(len(mentions)) + ")")
        for i in range(len(last_mentions), len(mentions)):
            mention = mentions[i - len(last_mentions)]
            print(mention.text)
            command = get_command(mention.text)
            if command != 0:
                print(send_reply(command, mention))
    else:
        print("Nothing new (Total: " + str(len(mentions)) + ")")
    time.sleep(refresh_rate)
    refresh(api, mentions)

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

user = api.get_user(screen_name=screen_name)
api.wait_on_rate_limit = True

ID = user.id_str
print(ID)

mentions = api.mentions_timeline()
refresh(api, mentions)
