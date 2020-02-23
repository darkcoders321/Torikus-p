import urllib, json
from selenium import webdriver 
def look_for_video():
    api_key = "whatever your api key is get it here: https://console.developers.google.com"
    channel_id = "watch?v=qbW6FRbaSl0"

    base_video_url = 'https://www.youtube.com/watch?v=qbW6FRbaSl0'
    base_search_url = 'https://www.googleapics.com/youtube/v3/search?'

    url = base_search_url + 'key={}&part=snippet'
    