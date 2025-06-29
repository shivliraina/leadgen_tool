import pandas as pd
import requests
import os
from dotenv import load_dotenv
load_dotenv()
HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")

def get_email_from_hunter(domain):
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        emails = data.get("data", {}).get("emails", [])
        return emails[0]["value"] if emails else ""
    return ""

def scrape_data(query):
    # Mocked data — replace with real scraping later
    return pd.DataFrame([
        {"Company": "AI Co", "Website": "aico.com", "Industry": "AI", "Location": "India"},
        {"Company": "TechBase", "Website": "techbase.io", "Industry": "SaaS", "Location": "India"},
    ])

def enrich_data(df):
    enriched = []
    for _, row in df.iterrows():
        domain = row['Website']
        email = get_email_from_hunter(domain)
        row['Email'] = email
        enriched.append(row)
    return pd.DataFrame(enriched)
