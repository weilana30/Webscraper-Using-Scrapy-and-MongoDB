# Webscraper-Using-Scrapy-and-MongoDB

## Overview
This project demonstrates how to use **Scrapy** for web scraping and store the scraped data into a **MongoDB** database.

## Features
- Scrapes data from a specified website.
- Cleans and processes the scraped data.
- Stores the data in a MongoDB database.
- Supports customizable spiders for different data sources.

## Requirements
To run this project, ensure you have the following installed:

- Python (>= 3.8)
- Scrapy (>= 2.8)
- pymongo (>= 4.0)
- MongoDB server

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/weilana30/Webscraper-Using-Scrapy-and-MongoDB/edit/main/README.md
   cd Webscraper-Using-Scrapy-and-MongoDB
   ```

2. **Install Dependencies**
   Install the required Python libraries using pip:
   ```bash
   pip install scrapy pymongo
   ```

3. **Configure MongoDB**
   - Ensure MongoDB is installed and running on your machine.
   - Update the MongoDB connection details in the `settings.py` file of your Scrapy project:
     ```python
     MONGO_URI = "mongodb://localhost:27017"
     MONGO_DATABASE = "scrapy_data"
     ```

4. **Create a Spider**
   - Use Scrapy to generate a new spider:
     ```bash
     scrapy genspider example example.com
     ```
   - Define the scraping logic in the generated spider file (e.g., `spiders/example.py`).

5. **Run the Spider**
   Execute the following command to start the spider and scrape data:
   ```bash
   scrapy crawl example
   ```

## Project Structure
```
Webscraper-Using-Scrapy-and-MongoDB/
├── scrapy.cfg
├── project-name/
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       └── books.py
└── README.md
```
- **items.py**: Defines the structure of the scraped data.
- **pipelines.py**: Contains the logic for storing the data into MongoDB.
- **settings.py**: Configures project settings like MongoDB connection, user agents, and request throttling.
- **spiders/**: Houses the spider definitions for various websites.

## Usage

1. **Modify the Spider**
   - Update the `start_urls` and the parsing logic in your spider to target the desired website and data.

2. **Run the Project**
   Use the following command to execute the spider and save data to MongoDB:
   ```bash
   scrapy crawl books
   ```

3. **Access the Data**
   Open the MongoDB shell or use a MongoDB GUI client to view the scraped data:
   ```bash
   mongo
   use scrapy_data
   db.scrapy_items.find()
   `
