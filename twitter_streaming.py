# -*- coding: utf-8 -*-

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "35171862-1H5wpBejWbrtSLbW6KInfioRBjx76IsCaLuOPzvmE"
access_token_secret = "tmOxgOLcCLsxMT7CTwUe3fxRw4gvzYeu4B4dm3dvLCrl1"
consumer_key = "AsO65BpkedG8wnvmPXOm9PJmY"
consumer_secret = "16vqfhAa4ys3gp9KcjqI4Jx1FLGDHhDYXf8Mp3hlRKf9L6ApGu"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return (True)

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Daredevil'])