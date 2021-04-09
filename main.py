import tweepy
import json
import re


def qualify_for_giveaway(api, tweet, user_to_track, comment_text):

    api.create_friendship(user_to_track)
    if not tweet.retweeted:
        api.retweet(tweet.id)
    if not tweet.favorited:
        tweet.favorite()

    # AFAIK, no easy way to check if you've already commented. Next best thing.
    try:
        api.update_status(comment_text, tweet.id)
    except tweepy.error.TweepError:
        print(f"Giveaway for {tweet.id} already entered.")
        return False

    return True


def meets_criteria(body, giveaway_criteria):
    for criteria in giveaway_criteria:
        if not re.search(criteria, body):
            return False
    return True


def main(api, user_to_track, giveaway_criteria, comment_text):
    # Fetch latest tweets.
    count = 200
    tweets = api.user_timeline(
        screen_name=user_to_track, count=count, include_rts=False, tweet_mode="extended"
    )

    # Check if a tweet meets the criteria for a giveaway. If so, qualify for the giveaway.
    entered_count = 0
    qualified_count = 0
    for tweet in tweets:
        if meets_criteria(tweet.full_text, giveaway_criteria):
            qualified_count += 1
            if qualify_for_giveaway(api, tweet, user_to_track, comment_text):
                entered_count += 1

    print(f"Pulled latest {count} tweets from {user_to_track}.")
    print(f"Qualified for {qualified_count} giveaways. Entered {entered_count}.")


if __name__ == "__main__":

    # Place all your private information in this file.
    f = open(
        "super_secret.json",
    )

    # Fetch data from super_secret.json.
    data = json.load(f)
    consumer_key = data["Consumer_Key"]
    consumer_secret = data["Consumer_Secret"]
    access_token = data["Access_Token"]
    access_token_secret = data["Access_Token_Secret"]
    user_to_track = data["User_To_Track"]
    giveaway_criteria = data["Giveaway_Criteria"]
    comment_text = data["Comment_Text"]

    # Authenticate to Twitter.
    api = None
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Create API object.
        api = tweepy.API(auth)

    except Exception as e:
        print("Failed to authenticate. Double check your tokens, keys, etc.")
        print(e)

    main(api, user_to_track, giveaway_criteria, comment_text)
