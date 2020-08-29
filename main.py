import numpy as np
import re
from twython import Twython
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from IPython.display import Image as im
import matplotlib.pyplot as plt

# twitter variables
key = "Lj0oeKr3odJB31kvZBdtTHX3M"
secert = open(".secert", "r").read()
twitter = Twython(key, secert)
screen_name = "realDonaldTrump"

# get timeline
timeline = twitter.get_user_timeline(screen_name = screen_name, count = 1)
lastId = timeline[0]['id']-1
for i in range(16):
    corpus = twitter.get_user_timeline(screen_name = screen_name, count = 5, max_id = lastId)
    timeline.extend(corpus)
    lastId = timeline[-1]['id'] - 1

# break down JSON object to reveal tweet text
tweet_text = []
for tweet in timeline:
    tweet_text.append(tweet['text'])


# Beautify our tweet text to disinclude links, emojis and special characters
stringTweets = ''.join(tweet_text)
links = re.sub(r'http\S+', '', stringTweets)
emojis = re.sub(r"\\[a-z][a-z]?[0-9]+", '', links)
specialCharacters = re.sub('[^A-Za-z ]+', '', emojis)
word = specialCharacters.split(" ")

word = [w for w in word if len(w) > 2]
words = [w.lower() for w in word]
word = [w for w in word if w not in STOPWORDS]
word = [w for w in word if w != screen_name]

mask = np.array(Image.open('poop.jpg'))
# generate wordcloud

cloud = WordCloud(background_color = "white", max_words = 2500, mask = mask, contour_width = 3, stopwords=STOPWORDS)
outString = ','.join(word)
cloud.generate(outString)


out = plt.figure(figsize=(50,50))

#plt.imshow(cloud, interpolation='bilinear')
#plt.title(screen_name +"'s tweets")
#plt.axis("off")
#plt.show()

# show
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.figure()
#plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()