import pandas as pd
import requests

HUNTER_API_KEY = "212cede95ac48e5af7ed69b4216634d9a76f1c69"  # Replace with your real key

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
