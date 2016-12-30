import re 
import csv

def processTweet(tweet):

	#Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
    #Removing quotes
    tweet = re.sub(r'^"|"$', '', tweet)
#end

#Read the tweets one by one and process it
processedTweets = []
with open('/home/siddarth/Twitter_Research/daredevil.csv','rb') as csvfile: #, open('/home/siddarth/Twitter_Research/dd.csv','wb') as out:

	jbreader = csv.DictReader(csvfile)
	for row in jbreader:
		if row['lang']=="en":
			line=row['text']
    		processedTweet = processTweet(line)
    		processedTweets.append(processedTweet)
    		#line = fp.readline()
#end loop
