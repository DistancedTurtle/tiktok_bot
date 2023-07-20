import boto3
from pandas import *
import csv


def get_text():
    with open('used.csv', 'r') as file:
        data = list(csv.reader(file, delimiter=","))
    for (i,entry) in enumerate(data):
        if entry[2] == "False":
            data[i][2] = "True"
            with open('used.csv','w') as f:
                writer = csv.writer(f,delimiter=',')
                writer.writerows(data)
            return(entry[0])

def make_mp3(text, voice_id, post_id):
    polly = boto3.client('polly')
    spoken_text = polly.synthesize_speech(Text=text,
                                      OutputFormat='mp3',
                                      VoiceId=voice_id) 

    with open(f'{post_id}.mp3', 'wb') as f:
        f.write(spoken_text['AudioStream'].read())
  
