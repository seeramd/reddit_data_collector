# The Reddit User Data Collector #

This script scrapes a reddit user's overview page to collect data on recent subbreddit posts and comments, as well as karma. As it is now, it uses this functionality to compare two users given by text input to calculate a "Shared activity score", which is just the number of subreddits they have shared activity on.

## the guts ##
v2 implements a User class, each instance of which has a username, set of recent active subreddits, a dictionary that counts their recent post+comments, and , of course, their post/comment karma.

The private method "\__soupkitchen" scrapes and parses via the fakeuser agent, requests, and BeautifulSoup modules. I use the old reddit url in this because the HTML is more intuitive, IMO.

The method "history" nicely prints out the recent_history dict, which, as mentioned earlier, counts the number of posts and comments in each subreddit they've recently been active in.

Finally, this class is utilised in a somewhat underwhelming way. The script will ask for two usernames, and will use the inputs to create two user instances. It will then compare each of their sets of recent subreddits, and count what is shared. The number of shared subreddits is printed as the "Shared activity score"

In terms of exception handling, if the post or comment karma variables draw up a NoneType and cause an AttributeError, which indicates the user doesn't exist, it will print an message stating as such. The active_subs set and recent_history dict are allowed to continue with a NoneType  and be empty because an existing user may simply have no comments or posts. A user will always have at least 1 post karma and 0 comment karma.

## known issues ##
* For some existing reddit users, nothing will be scraped, as if the user doesn't exist, and will cause an AttributeError. The user most certainly does exist; you can go to their overview page in your browser and see their activity. I have no idea why this happens for some users and not most others. Is it something with requests and reddit?

* Sometimes, the redditor's username (u/username) will appear in the set and/or dict of subreddits. Not sure why this happens either

