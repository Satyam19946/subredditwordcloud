import os
os.chdir(r"C:\Users\Satyam\Desktop\Programs\reddit")

import pandas as pd
import praw
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

myReddit = praw.Reddit( client_id = 'bWDF5RWVHmQvBA', client_secret  = 'bVCGihdjs0FPD1DBqKqQU9uwt8E', user_agent = 'Wordcloud', username = 'Satyam19946', password = 'Equinox@123' )

titles = ""
ucsd = myReddit.subreddit('UCSD')
for submission in ucsd.top(limit = 2000):
  titles += submission.title
  titles += " "

sun_god = np.array(Image.open("sun_god.jpg"))
titles = titles.lower()
wordcloud = WordCloud(mask = sun_god).generate(titles)
plt.imshow(wordcloud,interpolation = 'bilinear')
plt.axis('off')
plt.margins(x=0, y=0)
plt.show()