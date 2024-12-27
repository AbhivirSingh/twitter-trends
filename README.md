# Twitter Trends Web Scraper

This project is a web application that scrapes Twitter trends using Selenium and ProxyMesh, stores the data in MongoDB, and displays it on a webpage. The application is built using Flask and includes automated proxy handling for secure and efficient scraping.

## Features

- Scrapes Twitter trends dynamically.
- Utilizes ProxyMesh for secure proxy handling.
- Stores scraped data in a MongoDB database.
- Displays the top trends on a webpage with additional metadata.
- Allows users to view MongoDB JSON records directly on the webpage.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.8+
- Google Chrome
- ChromeDriver
- MongoDB
- ProxyMesh credentials
- A Twitter account

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repository/twitter-trends-web-scraper.git
   cd twitter-trends-web-scraper
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the application:** Update config.py with your credentials and file paths:
- ProxyMesh credentials
- Twitter login credentials
- MongoDB connection URI
- Path to ChromeDriver

## How to Use

1. **Start MongoDB:** Ensure MongoDB is running locally or use a cloud MongoDB instance.
2. **Run the Flask application:**
   ```bash
   python app.py
   ```
3. **Access the application:** Open your browser and navigate to http://127.0.0.1:5000.
4. **Scrape Twitter Trends:**
- Click the "Fetch Trends" button to initiate the scraping process.
- View the scraped trends, IP address used, and JSON records on the webpage.

## File Structure

```bash
twitter-trends-web-scraper/
├── app.py           # Flask application
├── script.py        # Selenium-based scraping logic
├── config.py        # Configuration file with credentials
├── templates/
│   └── index.html   # Frontend of the web application
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Dependencies

- Flask
- Selenium
- pymongo
- bson
