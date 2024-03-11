import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news_data.db'
db = SQLAlchemy(app)

class NewsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

def scrape_news():
    url = 'https://examplenews-website.com'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2', class_='news-headline')

        news_data = []
        for headline in headlines:
            news_data.append(headline.text.strip())

        return news_data

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def save_to_database(news_data):
    for headline in news_data:
        entry = NewsData(headline=headline)
        db.session.add(entry)

    db.session.commit()

if __name__ == "__main__":
    news = scrape_news()
    if news:
        save_to_database(news)
        print("Data saved to the database.")

        # Optional: Print the headlines
        for idx, headline in enumerate(news, start=1):
            print(f"{idx}. {headline}")
