# The Reddit User Data Collector #

This script scrapes a reddit user's overview page to collect data on recent subbreddit posts and comments, as well as karma. As it is now, it uses this functionality to either view one redditor's activity summary or to view and compare two redditor's activity

## the guts ##
v2 implements a User class, each instance of which has a username, set of recent active subreddits, a dictionary that counts their recent post+comments, and , of course, their post/comment karma.

The private method "\__soupkitchen" scrapes and parses via the fakeuser agent, requests, and BeautifulSoup modules. I use the old reddit url in this because the HTML is more intuitive, IMO.

The method "history" nicely prints out karma numbers and the recent_history dict, which, as mentioned earlier, counts the number of posts and comments in each subreddit they've recently been active in.

Finally, the script user will choose to either view one redditor or compare two. When viewing one, it will create an instance using the give username will call the history method to print the info. When comparing two users, it will ask for two usernames and call the history method on both. It will also compare their subreddit sets, give the number of common subreddits, and print them if there are any.

In terms of exception handling, if the post or comment karma variables draw up a NoneType and cause an AttributeError, which indicates the user doesn't exist, it will print an message stating as such. The active_subs set and recent_history dict are allowed to continue with a NoneType  and be empty because an existing user may simply have no comments or posts. An existing user will always have post and comment karma.

v1 is my first attempt at implementing this idea, before I realized I could use a class to make things a bit easier

## known issues ##
* For some existing reddit users, nothing will be scraped, as if the user doesn't exist, and will cause the karma AttributeError. The user most certainly does exist; you can go to their overview page in your browser and see their activity, but the script nonetheless draws up blank. I have no idea why this happens for some users and not most others. Is it something with requests and reddit?

* Sometimes, the redditor's username (u/username) will appear in the set and/or dict of subreddits. Not sure why this happens either

