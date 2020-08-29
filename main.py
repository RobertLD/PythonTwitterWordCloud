import numpy
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
    corpus = twitter.get_user_timeline(screen_name = screen_name, count = 200, max_id = lastId)
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

mask = np.array(Image.open('poopvector.png'))
out = plt.figure(figsize=(100,100))
out.add_subplot(1,2,1)
plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
out.add_subplot(1,2,2)
plt.imshow(wc, interpolation='bilinear')
plt.title(screen_name +"'s tweets")
plt.axis("off")
plt.show()