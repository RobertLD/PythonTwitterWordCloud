import numpy
from twython import Twython

# twitter variables
key = "Lj0oeKr3odJB31kvZBdtTHX3M"
secert = "we479yf87erghuerdfg"
twitter = Twython(key, secert)

timeline = twitter.get_user_timeline(screen_name = 'realDonaldTrump', count = 1)
