import csv
import nltk
import re
tweets=[]
with open('/home/siddarth/Twitter_Research/trainingset2000.csv','rb') as f:
    reader=csv.reader(f)
    for row in reader:
        tweets.append(row)
#print tweets
tweetssenti=[]
for (a,b,c,d,e,f) in tweets:
    words_filtered=[e.lower() for e in f.split() if len(e)>=3]
    tweetssenti.append((words_filtered,a))
#print tweetssenti
print 'Analyzing Tweet Sentiments'

def get_words_in_tweets(tweetssenti):
    all_words = []
    for (words, sentiment) in tweetssenti:
      all_words.extend(words)
    return all_words
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    #print wordlist
    word_features = wordlist.keys()
    return word_features
word_features = get_word_features(get_words_in_tweets(tweetssenti))
print 'word_features done'
#print word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
        
    return features
print 'obtaining training set'   
training_set = nltk.classify.util.apply_features(extract_features, tweetssenti)
#print training_set
print 'training the classfier .....'
classifier = nltk.NaiveBayesClassifier.train(training_set)
print ' Trained!'
print classifier.show_most_informative_features(200)
test_tweet=[]
with open('/home/siddarth/Twitter_Research/jb.csv','rb') as s:
    reader=csv.reader(s)
    for row in reader:
       test_tweet.append(row)
    #print test_tweet
    #print
    #print "End of the Tweets"

testing=[]
for (d, e, f) in test_tweet:
    print f
    #print 'preprocessing'
    filtered=[e.lower() for e in f.split()]
    #print filtered
    testing.append(filtered)
    #print "appended"

for tw in testing:
    #print tw
    print classifier.classify(extract_features(tw))


