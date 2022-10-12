from random  import randint
from time    import sleep
from tweepy  import OAuthHandler, API

infile = open('Tweets.txt', 'r')
Facts = []
for line in infile:
    Facts.append(line.strip('\n'))
infile.close()

Hashtags = ['#Security', '#Frens']

# Credentials to access Twitter API 
# DO NOT STORE PUBLICALY!
ACCESS_TOKEN    = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET   = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY    = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Initiate the connection to Twitter API
Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)

outfile = open('Log.txt', 'a')
i = 0
while i < len(Facts):
    TwitterBot.update_status(Facts[i]+' '+Hashtags[randint(0,len(Hashtags)-1)]) # Tweet a fact as well as a random hashtag
    outfile.write(str(i)+': '+Facts[i]+'\n') # Keep a log of tweeted facts in case server shuts off
    outfile.flush()
    sleep(randint(86400) # Tweet every 24 hours
    i += 1
