import praw
from datetime import date
import csv
import mutagen
from mutagen.mp3 import MP3
from pandas import *
import os
from speach import make_mp3


#cleaning up the info 
with open('info.txt') as file:
  secrets_list = file.readlines()
  for (i,secret) in enumerate(secrets_list):
    secrets_list[i] = secret.replace('\'','').rstrip('\n')

#info to access reddit via praw
reddit = praw.Reddit(
    client_id = secrets_list[1],
    client_secret = secrets_list[0],
    user_agent = f"videobot u/m_{secrets_list[2]}"
)

#specify subreddit
subreddit = reddit.subreddit("scarystories")

#append headers
'''with open ('used_denied.csv', 'w') as f:
          writer = csv.writer(f)
          writer.writerow(['post_id','post_date'])'''

#empty list
script_info = []
#for every submission in the the specified category and rankings
for submission in subreddit.hot(limit=4):
    #making sure its a text post and not an image or video
    if len(submission.selftext) > 40 and len(submission.selftext) < 3000:
      make_mp3(submission.selftext, 'Brian', submission.id)
      #create file object through mutagen
      audio = MP3(f"{submission.id}.mp3")
      audio_info = audio.info
      #find length of audio file
      length = int(audio_info.length)
      #use pandas to read csv
      data = read_csv("used.csv")
      column_id = data['post_id'].tolist()
      #use data to pull an entire coulumn for if statement
      if length > 60 and length < 180 and submission.id not in column_id:
          data_csv = [submission.id,'N/A',False]
          with open ('used.csv', 'a', newline = '') as f:
            writer = csv.writer(f)
            #append data
            writer.writerow(data_csv)
      else:
         #else remove audio file
         os.remove(f'{submission.id}.mp3')