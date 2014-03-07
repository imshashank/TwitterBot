from auto import auto_follow
from auto import auto_fav

#this is a sample program to use the auto.py script
auto_fav("ubuntu", count=1)
auto_fav("teamfollow", count=1)
auto_fav("teamfollowback", count=0)

#auto follow 10 users who come when we search for keyword "followback"
auto_follow("followback", count=10)
auto_follow("teamfollow", count=5)

