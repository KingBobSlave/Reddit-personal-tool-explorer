import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")
USERNAME = os.getenv("REDDIT_USERNAME")
PASSWORD = os.getenv("REDDIT_PASSWORD")

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET)

data = {
    "grant_type": "password",
    "username": USERNAME,
    "password": PASSWORD
}

headers = {"User-Agent": "PersonalRedditTool/0.1 by {}".format(USERNAME)}

# Get OAuth token
res = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=auth,
    data=data,
    headers=headers
)

TOKEN = res.json().get("access_token")
headers["Authorization"] = f"bearer {TOKEN}"

# Example: fetch your own saved posts
response = requests.get(
    "https://oauth.reddit.com/user/{}/saved".format(USERNAME),
    headers=headers
)

print("Status:", response.status_code)
print("Sample data:", response.json())
