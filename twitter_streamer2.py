
#!/usr/bin/python'

import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('AsO65BpkedG8wnvmPXOm9PJmY', '16vqfhAa4ys3gp9KcjqI4Jx1FLGDHhDYXf8Mp3hlRKf9L6ApGu')
auth.set_access_token('35171862-1H5wpBejWbrtSLbW6KInfioRBjx76IsCaLuOPzvmE', 'tmOxgOLcCLsxMT7CTwUe3fxRw4gvzYeu4B4dm3dvLCrl1')

api = tweepy.API(auth)
# Open/Create a file to append data
csvFile = open('result.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, 
                    q="Batman", 
                    since="2016-02-14", 
                    until="2016-03-30", 
                    lang="en").items():
    #Write a row to the csv file/ I use encode utf-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text
csvFile.close()