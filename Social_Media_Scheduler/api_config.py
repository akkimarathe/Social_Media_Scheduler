import tweepy
import requests

# Twitter API
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_SECRET = "YOUR_ACCESS_SECRET"

def post_to_twitter(content):
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        api.update_status(content)
        return True
    except Exception as e:
        print(f"Twitter Error: {e}")
        return False

# Facebook API
PAGE_ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN"
PAGE_ID = "YOUR_PAGE_ID"

def post_to_facebook(content):
    try:
        url = f"https://graph.facebook.com/{PAGE_ID}/feed"
        payload = {"message": content, "access_token": PAGE_ACCESS_TOKEN}
        response = requests.post(url, data=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Facebook Error: {e}")
        return False

# Instagram API
IG_ACCESS_TOKEN = "YOUR_INSTAGRAM_ACCESS_TOKEN"
IG_USER_ID = "YOUR_INSTAGRAM_USER_ID"

def post_to_instagram(content):
    try:
        url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/media"
        payload = {"caption": content, "access_token": IG_ACCESS_TOKEN}
        response = requests.post(url, data=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Instagram Error: {e}")
        return False
