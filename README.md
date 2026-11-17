# TheProtocol.it Tech Jobs & IT Salaries Scraper

[![Apify Actor](https://img.shields.io/badge/Apify-Actor%20Store-orange?logo=apify)](https://apify.com/moneygain/theprotocol-scraper)
[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://github.com/Archibald322/theprotocol-scraper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Live Apify Store Actor:** [https://apify.com/moneygain/theprotocol-scraper](https://apify.com/moneygain/theprotocol-scraper)

This repository provides an open-source Python runner and documentation for **[TheProtocol.it Tech Jobs & IT Salaries Scraper](https://apify.com/moneygain/theprotocol-scraper)**.

---

## ⚡ Quickstart

### Option 1: Run in Cloud (No Code)
Launch directly from your browser via the Apify Store console:
👉 **[Open TheProtocol.it Tech Jobs & IT Salaries Scraper on Apify Store](https://apify.com/moneygain/theprotocol-scraper)**

### Option 2: Run via Python SDK
```bash
git clone https://github.com/Archibald322/theprotocol-scraper.git
cd theprotocol-scraper
pip install -r requirements.txt
export APIFY_TOKEN="your_apify_token_here"
python run.py
```

---

# 🇵🇱 TheProtocol.it IT Careers & Verified Salaries Scraper

**Scrape TheProtocol.it IT careers data to JSON, CSV, or Excel in seconds without browser overhead.** Extract tech vacancies, B2B contract rates, permanent employment salary brackets, required programming languages, seniority levels, remote work options, and direct employer application links from **TheProtocol.it** — Poland and Central Europe's leading high-transparency tech job board by Grupa Pracuj.

Designed for IT recruiting agencies, tech headhunters, HR analytics startups, salary benchmarking researchers, and autonomous AI agents. Built with high-speed HTTP requests with Chrome TLS fingerprinting, **zero browser overhead**, and **100% Pay-Per-Event (PPE) pricing** — you only pay for verified job postings delivered.

---

## ⚡ Speed & Value Comparison

| Feature | Our Lightweight TheProtocol Scraper | Heavy Browser Scrapers (Playwright / Puppeteer) |
|---|---|---|
| **Memory Usage** | **128 MB – 256 MB** | 2 GB – 4 GB |
| **Startup Fee** | **$0.00 (Zero Start Fee)** | $0.05 – $0.10 per run |
| **Speed per Page** | **0.3s – 0.6s per page** | 10s – 20s per page |
| **Pricing Model** | **Pay-Per-Event ($0.005 / job)** | Expensive Monthly Flat Rate |
| **Salary Parsing** | **Structured B2B & Employment brackets** | Unstructured raw text |
| **Anti-Bot Reliability** | **Chrome TLS session emulation** | Frequent Cloudflare challenge blocks |

---

## 📦 Sample JSON Output

```json
{
  "id": "10034821",
  "title": "Senior Python / AI Engineer",
  "company": "TechInnovations Sp. z o.o.",
  "companyLogo": "https://theprotocol.it/logos/techinnovations.png",
  "location": "Warszawa, Mazowieckie",
  "workplaceType": "remote",
  "isRemote": true,
  "seniority": "Senior",
  "salaryB2B": "26 000 - 32 000 PLN net (+ vat) / mth.",
  "salaryPerm": "20 000 - 25 000 PLN gross / mth.",
  "technologies": ["Python", "FastAPI", "Docker", "AWS", "PostgreSQL"],
  "offerUrl": "https://theprotocol.it/szczegoly/praca/senior-python-ai-engineer-warszawa,10034821",
  "publishedAt": "2026-11-17T08:00:00.000Z",
  "scrapedAt": "2026-11-17T10:00:00.000000+00:00"
}
```

---

## 🎯 Use Cases & Business Value

- **Central European IT Headhunting**: Source top developers, DevOps engineers, and AI architects across Poland and the EU remote tech corridor.
- **European IT Salary Indexing**: Track real-time B2B contract rates vs. permanent contract gross pay across 10+ tech specializations.
- **Tech Stack Trend Tracking**: Analyze rising demand for Python, Golang, React, Rust, and AI/ML frameworks.
- **Autonomous AI Career Agents**: Feed real-time European tech openings directly into talent screening and matching agents via **Apify MCP Server**.

---

## ⚙️ Input Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `startUrls` | Array | `["https://theprotocol.it/filtry/backend;sp"]` | Direct filter URLs from TheProtocol.it. |
| `specialization` | String | `"all"` | IT domain filter (`backend`, `frontend`, `fullstack`, `devops`, `qa-testing`, `big-data-science`, `security`, `mobile`). |
| `technology` | String | `""` | Technology keyword (e.g. `python`, `react`, `golang`, `aws`). |
| `seniority` | String | `"all"` | Seniority filter (`junior`, `mid`, `senior`, `lead`). |
| `onlyRemote` | Boolean | `false` | When `true`, filters strictly for 100% remote positions (`zdalna`). |
| `maxItems` | Integer | `10` | Maximum number of verified job records to scrape (Prefilled for instant 5-second test runs). |
| `proxyConfiguration` | Object | `{"useApifyProxy": true}` | Apify Proxy configuration for zero-block execution. |

---

## 🤖 Integrate with AI Agents & No-Code Platforms

### 1. Claude Desktop & Cursor via Apify MCP Server
Connect this actor directly to Cursor, Claude Desktop, Windsurf, or LangChain agents using the official Apify MCP Server:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_API_TOKEN"
      }
    }
  }
}
```
*Prompt example:*
> *"Find 15 remote Senior Python jobs in Poland paying over 25,000 PLN B2B using theprotocol-scraper."*

### 2. n8n Automation Workflows
1. Add an **Apify Node** or **HTTP Request Node** in your n8n workflow.
2. Select `Run an Actor` with Actor ID: `moneygain/theprotocol-scraper`.
3. Send daily notifications to Telegram tech job channels or Discord servers.

### 3. Make.com (Integromat)
1. Add the **Apify Module** ➔ `Run Actor and get dataset items`.
2. Sync European IT job openings into Google Sheets or Airtable.

### 4. Clay.com Enrichment
1. Use the **Apify Integration** inside Clay.
2. Map developer talent compensation benchmarks to your account scoring model.

### 5. Python SDK Integration
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_API_TOKEN")
run_input = {
    "specialization": "backend",
    "technology": "python",
    "onlyRemote": True,
    "maxItems": 20
}
run = client.actor("moneygain/theprotocol-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"[{item['company']}] {item['title']} | {item['salaryB2B']} -> {item['offerUrl']}")
```

---

## ❓ Frequently Asked Questions (SEO FAQ)

### Q1: Is it legal to scrape data from TheProtocol.it?
**Yes.** All job postings extracted are publicly accessible recruitment advertisements placed by employers seeking candidates. The scraper accesses only public listing pages without bypassing authentication or applicant portals.

### Q2: How much does it cost to scrape 1,000 job postings?
Under our **Pay-Per-Event (PPE)** pricing model, you only pay **$0.005 per verified job posting**, so 1,000 jobs cost **$5.00**. There are zero startup costs and subscribers on Apify Bronze/Silver/Gold tiers receive automatic volume discounts up to 20% ($4.00 per 1,000).

### Q3: Can I export TheProtocol data to Excel, CSV, or Google Sheets?
**Yes.** Apify provides 1-click export options in JSON, CSV, XML, Excel (.xlsx), and HTML table formats. You can also automate data delivery via Webhooks.

### Q4: Do I need proxies to scrape TheProtocol.it?
Using standard Apify datacenter proxies (`useApifyProxy: true`) is preconfigured by default to ensure 100% reliable execution without IP rate limiting.

### Q5: Does this scraper separate B2B contract rates from employment contracts?
**Yes.** The actor parses and separates `salaryB2B` (net PLN/month + VAT for contractors) and `salaryPerm` (gross PLN/month for standard employment contracts) whenever disclosed by the employer.

---

## 🔗 Explore More High-Speed B2B Scrapers & Enrichers by Our Team

Supercharge your data pipelines, sales outreach, and AI agents with our suite of lightweight, Pay-Per-Event scrapers:

| Scraper | Segment / Target | Key Value | Store Link |
|---|---|---|---|
| **TrustMRR SaaS Startups Scraper** | SaaS Revenue & M&A Data | Stripe-verified MRR, 30d revenue, active subscriptions & founder contacts | [Open on Apify Store](https://apify.com/moneygain/trustmrr-startups-scraper) |
| **Ashby ATS Tech Jobs Scraper** | Next-Gen ATS Career Feeds | Direct ATS API extraction, salaries, departments & remote flags | [Open on Apify Store](https://apify.com/moneygain/ashby-jobs-scraper) |
| **Clutch B2B Agencies Scraper** | B2B Agencies & IT Services | Decoded direct websites, review ratings, hourly rates & service focus | [Open on Apify Store](https://apify.com/moneygain/clutch-agencies-scraper) |
| **Wellfound Startup Talent Scraper** | AI & Tech Startup Jobs | Startup jobs, compensation ranges, equity & tech stack tags | [Open on Apify Store](https://apify.com/moneygain/wellfound-jobs-scraper) |
| **TheProtocol.it IT Careers Scraper** | IT Salaries & Vacancies | Verified salary brackets, tech requirements & seniority levels | [Open on Apify Store](https://apify.com/moneygain/theprotocol-scraper) |
| **Bulldogjob Tech Recruitment Scraper** | Tech Recruitment Feeds | B2B/Employment rates, tech tags & recruiter contacts | [Open on Apify Store](https://apify.com/moneygain/bulldogjob-scraper) |
