# twitter-giveaway-bot

Examine the tweets of a user to see if they are running a giveaway. If so - follow, retweet, and comment to enter the giveaway.

## Tools

* Tweepy (Python Twitter API Wrapper) - [Tweepy](https://docs.tweepy.org/en/latest/)

## Installation

Easiest way to install is using Git via the command line. 

You can install git here: [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Once installed, run via your terminal:

```
$> git clone https://github.com/MaciejKrzysiak/twitter-giveaway-bot.git
$> cd twitter-giveaway-bot
```

### Update super_secret.json
Once downloaded and inside the twitter-giveaway-bot directory, update super_secret.json to use your credentials. 

A consumer_key, consumer_secret, access_token, and access_token_secret can all be created here: [Twitter Dev](https://developer.twitter.com/en/apply-for-access).

The user_to_track field designates which Twitter account you'd like to script to monitor. This is the user's Twitter handle without the @ symbol. Support for multiple accounts does not exist.

The giveaway_criteria field informs the bot which tweets to respond to. The bot will look for designated keywords. Find a pattern amongst the giveaway tweets. A list of keywords is supported.

The comment_text field is what the body with comment on the giveaway tweets. This could be a blockchain address, a paypal account, etc. This should be whatever is needed for you to enter the giveaway sweepstakes.


Once you've updated the secret fields, run via your terminal:
```
$> python3 main.py
```
If you do not have python3 installed, see here: [Python](https://realpython.com/installing-python/).
