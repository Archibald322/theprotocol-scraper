"""
Apify Client Runner for TheProtocol.it Tech Jobs & IT Salaries Scraper
Actor URL: https://apify.com/moneygain/theprotocol-scraper
"""

import os
from apify_client import ApifyClient

# 1. Initialize the client with your Apify API token
# Get your free token at: https://console.apify.com/account/integrations
api_token = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
client = ApifyClient(api_token)

# 2. Define Actor input parameters
run_input = {
    "startUrls": [
        {
            "url": "https://theprotocol.it/filtry/backend;sp"
        }
    ],
    "specialization": "all",
    "technology": "",
    "seniority": "all",
    "onlyRemote": false,
    "maxItems": 10,
    "proxyConfiguration": {
        "useApifyProxy": true
    }
}

def main():
    print("🚀 Starting TheProtocol.it Tech Jobs & IT Salaries Scraper on Apify Cloud...")
    run = client.actor("moneygain/theprotocol-scraper").call(run_input=run_input)
    print(f"✅ Scraping completed! Run ID: {run.get('id')}")
    
    # 3. Fetch results from default dataset
    dataset_client = client.dataset(run["defaultDatasetId"])
    items = list(dataset_client.iterate_items())
    print(f"📊 Retrieved {len(items)} records.")
    for item in items[:5]:
        print(item)

if __name__ == "__main__":
    main()
