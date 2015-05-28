import requests as req
import json

apiKey = "3b94a3df-2448-4d5a-920f-14a2e0c10eef"
base_url = "https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?text={1}&language=eng&apikey={0}"

## Function normalizes it
## parameter score: a value between -1, 1 from id0l 
# color scale from http://stackoverflow.com/questions/340209/generate-colors-between-red-and-green-for-a-power-meter
def rgbConverter(score): 
  n = (score+1)/2.0*100
  R = (255 * (100 - n)) / 100.0
  G = (255 * n) / 100.0
  B = 0
  colorList = [int(R),int(G),int(B)]
  return colorList

def format_comment(comment): 
    c = (comment.split())
    d  = "+".join(c)
    formatted = base_url.format(apiKey, d)
    return formatted 

def get_data(url): 
    data = req.get(url).json()
    score_sentiment = data["aggregate"]["score"]
    return score_sentiment

def rgbMood(comment): 
   sentiment = get_data(format_comment(comment))
   colors = rgbConverter(sentiment)
   return "rgb"+ str(tuple(colors))
