
from slistener import SListener
import time, tweepy, sys

## auth. 
## TK: Edit the username and password fields to authenticate from Twitter.
username = ''
password = ''
auth     = tweepy.auth.BasicAuthHandler(username, password)
api      = tweepy.API(auth)

## eventually you'll need to use OAuth. Here's the code for it
#consumer_key        = ""
#consumer_secret     = ""
#access_token        = ""
#access_token_secret = ""

# OAuth process, using the keys and tokens
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

def main( mode = 1 ):
    track  = ['obama']
    follow = []
            
    listen = SListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started on %s users and %s keywords..." % (len(track), len(follow))

    try: 
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
