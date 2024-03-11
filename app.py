from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from scraper import scrape_news, save_to_database
from datetime import datetime
import plotly.express as px

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news_data.db'
db = SQLAlchemy(app)

class NewsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    headlines = NewsData.query.all()

    # Create a bar chart using Plotly
    fig = px.bar(headlines, x='headline', title='News Headlines')

    # Save the chart as HTML and pass it to the template
    chart_html = fig.to_html(full_html=False)
    return render_template('index.html', headlines=headlines, chart_html=chart_html)

if __name__ == "__main__":
    app.run(debug=True)
