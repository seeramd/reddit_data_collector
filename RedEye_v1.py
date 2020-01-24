from requests import get
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# soup_kitchen scrapes user's overview page
def soup_kitchen(username):
    ua = UserAgent()
    header = {'User-Agent': ua.chrome}
    url = "https://old.reddit.com/user/" + username

    source = get(url,headers=header)
    soup = BeautifulSoup(source.text,'lxml')

    subs = soup.findAll('a',{'class':'subreddit hover'})
    subs += soup.findAll('a',{'class':'subreddit hover may-blank'})

    sub_set = set()
    sub_dict = {}

    for k in subs:
        sub_set.add(k.text.lstrip('r/'))

    for k in subs:
        sub_dict.setdefault(k.text.lstrip('r/'),0)
        sub_dict[k.text.lstrip('r/')] += 1

    return sub_set,sub_dict

def print_logo():
    print("""
______ ___________ _______   _______ 
| ___ \  ___|  _  \  ___\ \ / /  ___|
| |_/ / |__ | | | | |__  \ V /| |__  
|    /|  __|| | | |  __|  \ / |  __| 
| |\ \| |___| |/ /| |___  | | | |___ 
\_| \_\____/|___/ \____/  \_/ \____/ 
                                     
                 v1
                                               
         written by Timaeus
""")

def print_userdict(user,sub_dict):
    print(user + "'s recent activity")
    print('r/'.ljust(15) + 'Posts+Comments')
    for k,v in sub_dict.items():
        print((k).ljust(20,'.') + str(v))
    print('')

#=============================================================================

print_logo()


user1 = '<InsertUser1Here>'
user2 = '<InsertUser2Here>'

sub_set1, sub_dict1 = soup_kitchen(user1)
sub_set2, sub_dict2 = soup_kitchen(user2)

comp_score = 0

for val in sub_set1:
    if val in sub_set2:
        comp_score += 1

print_userdict(user1,sub_dict1)
print_userdict(user2,sub_dict2)

print(comp_score)




        
