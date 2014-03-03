from twitter import Twitter, OAuth, TwitterHTTPError

# put your twitter tokens, keys, secrets, and twitter handle in the following variables
OAUTH_TOKEN = ""
OAUTH_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
TWITTER_HANDLE = ""

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))


def search_tweets(q, count=10, result_type="recent"):
    """
        Returns a list of tweets matching a certain phrase (hashtag, word, etc.)
    """

    return t.search.tweets(q=q, result_type=result_type, count=count)


def auto_fav(q, count=1, result_type="recent"):
    """
        Favorites tweets that match a certain phrase (hashtag, word, etc.)
    """

    result = search_tweets(q, count, result_type)

    for tweet in result['statuses']:
        try:
            # don't favorite your own tweets
            if tweet['user']['screen_name'] == TWITTER_HANDLE:
                continue

            result = t.favorites.create(_id=tweet['id'])
            print "favorited: %s" % (result['text']).encode('utf-8')

        # when you have already favorited a tweet this error is thrown
        except TwitterHTTPError as e:
            print "error: ", e


def auto_follow(q, count=10, result_type="recent"):
    """
        Follows anyone who tweets about a specific phrase (hashtag, word, etc.)
    """

    result = search_tweets(q, count, result_type)
    following = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])

    for tweet in result['statuses']:
        try:
            if tweet['user']['screen_name'] != TWITTER_HANDLE and tweet['user']['id'] not in following:
                if tweet['user']['followers_count'] > 2000 and tweet['user']['friends_count'] > 2000 :
                  ratio = tweet['user']['friends_count']/tweet['user']['followers_count']
                  if ratio > 0.6:
                    t.friendships.create(user_id=tweet['user']['id'], follow=True)
                    following.update(set([tweet['user']['id']]))
                    print "followed " + tweet['user']['screen_name']

        except TwitterHTTPError as e:
            print "error: ", e

            # quit on error unless it's because someone blocked me
            if "blocked" not in str(e).lower():
                quit()


def auto_follow_followers():
    """
        Follows back everyone who's followed you
    """

    following = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])
    followers = set(t.followers.ids(screen_name=TWITTER_HANDLE)["ids"])

    not_following_back = followers - following

    for user_id in not_following_back:
        try:
            t.friendships.create(user_id=user_id, follow=True)
        except Exception as e:
            print e


def auto_unfollow_nonfollowers():
    """
        Unfollows everyone who hasn't followed you back
    """

    following = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])
    followers = set(t.followers.ids(screen_name=TWITTER_HANDLE)["ids"])

    # put user IDs here that you want to keep following even if they don't
    # follow you back
    users_keep_following = set([])

    not_following_back = following - followers

    for userid in not_following_back:
        if userid not in users_keep_following:
            t.friendships.destroy(user_id=userid)



