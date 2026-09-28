# Social Media Feed Analyzer

A Python-based data analysis pipeline designed to process, analyze, and extract insights from social media feeds. This project handles the entire data lifecycle: from raw data generation and cleaning to sentiment analysis, database integration with MongoDB, and exporting datasets for visualization in Power BI.

## Key Features

* **Data Processing Pipeline:** Automated scripts to generate, inspect, and clean raw social media datasets.
* **In-Depth Analytics:** Modules dedicated to analyzing hashtags, trending topics, time-based engagement, and user sentiment.
* **MongoDB Integration:** Seamlessly import cleaned data into MongoDB for NoSQL storage and perform advanced database-level queries.
* **Business Intelligence Ready:** Export processed engagement and sentiment metrics into structured CSV formats optimized for Power BI dashboards.

## Project Structure

The repository is organized into source code and data directories:

```text
social-media-feed-analyzer/
│
├── data/                               # Generated datasets and exports
│   ├── cleaned_social_media_posts.csv
│   ├── social_media_analysis.csv       # Power BI export
│   ├── social_media_posts.csv
│   └── social_media_sentiment.csv
│
├── src/                                # Source code modules
│   ├── analysis.py
│   ├── clean_data.py
│   ├── export_for_powerbi.py
│   ├── generate_data.py
│   ├── hashtag_analysis.py
│   ├── inspect_data.py
│   ├── mongodb_analysis.py
│   ├── mongodb_import.py
│   ├── sentiment_analysis.py
│   ├── time_analysis.py
│   └── trending_analysis.py
│
├── .gitignore
└── README.md

```

## Prerequisites

* Python 3.x
* MongoDB (Local or Atlas instance running)
* Required Python libraries: `pandas`, `pymongo` (add any others like `vaderSentiment` or `matplotlib` depending on your specific setup)

## Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/chandu13-larry/social-media-feed-analyzer.git
cd social-media-feed-analyzer

```


2. Create and activate a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

```


3. Install dependencies:
*(Note: Ensure you have a `requirements.txt` file, or install packages manually via pip).*
```powershell
pip install -r requirements.txt

```



## Usage Workflow

Run the scripts in the `src/` directory to process and analyze the data. Based on the pipeline, a typical workflow looks like this:

1. **Prepare the Data:**
Generate and clean your initial social media dataset.
```powershell
python src/generate_data.py
python src/clean_data.py

```


2. **Run Analytics:**
Execute specific analysis modules to uncover trends and sentiment.
```powershell
python src/sentiment_analysis.py
python src/hashtag_analysis.py

```


3. **Database Integration:**
Import your cleaned data into MongoDB and run database-level analytics.
```powershell
python src/mongodb_import.py
python src/mongodb_analysis.py

```


4. **Export for Visualization:**
Format and save the final dataset for Power BI ingestion.
```powershell
python src/export_for_powerbi.py

```



## Author

Chandu / [chandu13-larry](https://www.google.com/search?q=https://github.com/chandu13-larry&utm_source=gemini)