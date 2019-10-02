import os
os.chdir(r"C:\Users\Satyam\Desktop\Programs\reddit")

import pandas as pd
import praw
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# u have to enter your own details for the next line.
myReddit = praw.Reddit( client_id = '', client_secret  = '', user_agent = '', username = '', password = '' )

titles = ""

#u can change the name of the subreddit below.
ucsd = myReddit.subreddit('UCSD')
for submission in ucsd.top(limit = 2000):
  titles += submission.title
  titles += " "

#change the name of the file if you want a different mask, or remove the mask option at line 25 of you do not want a mask. 
sun_god = np.array(Image.open("sun_god.jpg"))
titles = titles.lower()
wordcloud = WordCloud(mask = sun_god).generate(titles)
plt.imshow(wordcloud,interpolation = 'bilinear')
plt.axis('off')
plt.margins(x=0, y=0)
plt.show()
