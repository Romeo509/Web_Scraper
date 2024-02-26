# Web Scraper and Data Visualization

## Overview

This project is a Python-based web scraper and data visualization tool that collects news headlines from a specified website, stores them in a SQLite database, and presents them in a Flask web application. Additionally, it utilizes Plotly Express to create a dynamic bar chart visualizing the collected data.

## Features

- Web scraping of news headlines from a user-defined website.
- Storage of scraped data in a SQLite database using SQLAlchemy.
- A Flask web application for displaying news headlines and an interactive Plotly bar chart.
- Simple and clean HTML templates using Jinja2.

## Requirements

- Python 3.x
- Flask
- SQLAlchemy
- Plotly
- Beautiful Soup 4
- Requests

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/web-scraper.git
   cd web-scraper

<h3>1. Install the required packages:</h3>
    pip install -r requirements.txt

<h3>2. Run the Flask application:</h3>
    python app.py

<h3>3. Open your web browser and navigate to http://127.0.0.1:5000/ to view the application. </h3>

<h1>Usage</h1>
The web scraper automatically retrieves news headlines from the specified website and saves them to the SQLite database.
The Flask web application serves as a simple interface to view the collected headlines and an interactive Plotly bar chart.
The main page displays a list of news headlines, and the chart provides a visual representation of the headlines.

<h2>Project Structure</h2>
app.py: Main Flask application script.
scraper.py: Web scraper script for fetching news headlines.
templates/: Folder containing HTML templates for rendering web pages.

<h1>Contributing</h1>
If you'd like to contribute to this project, please follow these steps:
Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature-name.
Commit your changes: git commit -m "Add feature".
Push to your fork: git push origin feature-name.
Create a pull request.


