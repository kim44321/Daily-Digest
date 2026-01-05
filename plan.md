# Daily Digest

## Current Plan:

Jinja 2 Template - Template on what the mail could look like
Smtp - Sends the Templated Email
Open Meteo - Weather API
WorldNewsAPI- Sends Current News
Hugging Face - Summary Model
Wikipedia API - Allows to fetch Wikipedia Data


### Nice to haves: 
Digest is based on person's location? 
Template improvement - Frontend Skills as its written in html 
n8n - Automation
Website to add email to queue - Deploy with smth like github pages/vercel

## Recommended Modular Format:

daily-digest/
│
├── main.py # The entry point — ties everything together and runs the script
├── config.py # All your secrets, API keys, email settings, cities, etc.
├── utils/ # Reusable helper functions (good place to keep things tidy)
│ ├── **init**.py
│ ├── api.py # Functions to fetch data from weather, news, Wikipedia APIs
│ └── email_utils.py # Functions to build the email body and send it
├── summarization.py # All Wikipedia article summarization logic lives here
├── templates/ # Folder for email/HTML templates (optional but recommended)
│ └── digest.html # Jinja2 template file (or plain text if you prefer)
├── .env # Store secrets (never commit this to Git!)
├── requirements.txt # List of packages (pip install -r requirements.txt)
└── README.md # Explain what the project does + how to run it

## Weather

What is required usually on simple weather overview?
Maximum Temperature
Minimum Temperature
Humidity
Weather Code/Interpretation
Precipitation
Winds

## News
Top Headlines per country  - Latest =/= Top News
Latitude Longitude -> Country? 
NewsAPI is severely limited outside of US/UK 
2-letter ISO 3166-1 is the format used for country codes e.g. us, ph, fr

## Wikipedia
Wikipedia Featured Article of the Day 