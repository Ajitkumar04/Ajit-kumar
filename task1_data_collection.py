import requests
import time
import os
import json
from datetime import datetime

headers = {"User-Agent": "TrendPulse/1.0"}
headers = {"User-Agent": "TrendPulse/1.0"}
try:
    top_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json",
        headers=headers
    ).json()[:500 ]
  
except Exception as e:
    print("Failed to fetch top stories:", e)
    top_ids = []
categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}
def assign_category(title):
    t = title.lower()
    for cat, keywords in categories.items():
        if any(k.lower() in t for k in keywords):
            return cat
    return None
collected = []
for cat in categories.keys():
    count = 0
    for sid in top_ids:
        if count >= 25:
            break
        try:
            url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
            data = requests.get(url, headers=headers).json()
            if not data or "title" not in data:
                continue
            category = assign_category(data["title"])
            if category == cat:
                story = {
                    "post_id": data["id"],
                    "title": data["title"],
                    "category": category,
                    "score": data.get("score", 0),
                    "num_comments": data.get("descendants", 0),
                    "author": data.get("by", ""),
                    "collected_at": datetime.now().isoformat()
                }
                collected.append(story)
                count += 1
        except Exception as e:
            print(f"Failed to fetch story {sid}: {e}")
    
    time.sleep(2)
with open("data/trends_20240115.json","w")as file:
    json.dump(collected,file,indent=4)

print(len(collected))

