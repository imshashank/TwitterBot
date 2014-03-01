#Twitter Follow Bot

A Python bot that can automatically follow users and favorite tweets associated with a specific search query on Twitter. Also has the ability to unfollow all users not currently following you back.

##Algorithm
It only follows user who have follower count > 2000 & following count > 2000 and the ratio of followers to following is greater than 0.6

I have found these modifications very helpful. 

##Dependencies

You will need to install Python's `twitter` library first:

    easy_install twitter
    
You will also need to create an app account on https://dev.twitter.com/apps

1. Sign in with your Twitter account
2. Create a new app account
3. Modify the settings for that app account to allow read & write
4. Generate a new OAuth token with those permissions
5. Manually edit this script and put those tokens in the script

##Usage

Currently, the bot has three functions:

####Automatically follow any users that tweet something with a specific phrase

    from twitter_follow_bot import auto_follow
  
    auto_follow("phrase")
    
You can also search based on hashtags.
  
By default, the bot looks up the 100 most recent tweets. You can change this number with the `count` parameter:

    from twitter_follow_bot import auto_follow
  
    auto_follow("phrase", count=1000)
    
####Automatically follow any users that have followed you

    from twitter_follow_bot import auto_follow_followers
    
    auto_follow_followers()

####Automatically favorite any tweets that have a specific phrase

    from twitter_follow_bot import auto_fav
  
    auto_fav("phrase", count=1000)

####Automatically unfollow any users that have not followed you back (with exceptions that you can set)

    from twitter_follow_bot import auto_unfollow_nonfollowers
  
    auto_unfollow_nonfollowers()
  
You will need to manually edit the code if you want to add special users that you will keep following even if they don't follow you back.

Inspired by https://github.com/rhiever/twitter-follow-bot
