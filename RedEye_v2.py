#! python3

from requests import get
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from logging import exception
from sys import exit

class User:
    #stores username, recent subreddits:post+comment counts, and karma of a reddit user
    def __init__(self,username):
        self.username = username
        self.recent_history = {}
        self.postkarma = 0
        self.commentkarma = 0

        self.__soupkitchen()
    #soup kitchen: scrape overview page
    def __soupkitchen(self):
        ua = UserAgent()
        header = {'User-Agent': ua.chrome}
        url = "https://old.reddit.com/user/" + self.username

        source = get(url,headers=header)
        soup = BeautifulSoup(source.text,'lxml')
        
        #post and comment karma
        #If no karma, user does not exist (probably)
        try:
            pk = (soup.find('span', class_= 'karma').text)
            ck = (soup.find('span', class_ = 'karma comment-karma').text)
            self.postkarma = int(pk.replace(',',''))
            self.commentkarma = int(ck.replace(',',''))
        except AttributeError: #AttributeError if NoneType (no karma found)
            exception("/u/"+self.username+" may not exist.")
            input("Press enter to quit. ")
            exit()
            
        subs = soup.findAll('a',{'class':'subreddit hover'})
        #<a></a> element in posts have a different class
        subs += soup.findAll('a',{'class':'subreddit hover may-blank'})

        #strips leading r/ (only present in submissions)
        #recent_history dict counts posts and comments {"subreddit": # of posts+comments}
        for k in subs:
            self.recent_history.setdefault(k.text.lstrip('r/'),0)
            self.recent_history[k.text.lstrip('r/')] += 1

    #prints summary of redditor's karma, active subreddits, and posts+comment count
    def history(self):
        print('*'+self.username + "'s summary*")
        print("Post Karma: " + str(self.postkarma))
        print("Comment Karma: " + str(self.commentkarma))
        #justify relative to the max length subreddit string
        n = len(max(self.recent_history, key=len))
        print('r/'.ljust(n) + 'Posts+Comments')
        for k,v in self.recent_history.items():
            print((k).ljust(n+3,'.') + str(v).rjust(3,'.'))
        print('')
#===============================================================================

print("""
______ ___________ _______   _______ 
| ___ \  ___|  _  \  ___\ \ / /  ___|
| |_/ / |__ | | | | |__  \ V /| |__  
|    /|  __|| | | |  __|  \ / |  __| 
| |\ \| |___| |/ /| |___  | | | |___ 
\_| \_\____/|___/ \____/  \_/ \____/ 
                                     
                 v2
                                               
         written by Timaeus

""")

while True:
    print('Make a selection (1 or 2): ')
    print("""
(1) See a user's history
(2) Compare two users
""")
#input: choose between checking 1 user or comparing 2
    while True:
        selection = input()

        if selection not in ['1','2','(1)','(2)']:
            print('Invalid input. Choose between 1 or 2')
        else:
            break
    #checking one user's histroy
    if selection in ['1','(1)']:
        u = input('Type the name of the user: ')
        r = User(u)

        print('')
        r.history()
    #comparing two user's history
    elif selection in ['2','(2)']:
        u1 = input('Type the name of the first user: ')
        u2 = input('Type the name of the second user: ')

        r1 = User(u1)
        r2 = User(u2)

        #counts number of common active subreddits between users
        #shared subreddits gets put in a list
        count = 0
        shared_subs = []
        for k in r1.recent_history.keys():
            if k in r2.recent_history.keys():
                count += 1
                shared_subs += [k]
        print('')
        r1.history()
        r2.history()

        print('Shared subreddits count: '+ str(count))
        if len(shared_subs) == 0:
            print('No shared subreddits')
        else:
            print('Shared subreddits: ' + ','.join(shared_subs))
        

    repeat = input('Anything else (y/n)? ')
    if repeat.lower() not in ['y','yes']:
        break
        
