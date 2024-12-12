# Web Scraper with Flask API

This project is a web scraper built using Python, Flask, Selenium and Beautifulsoup. It allows users to scrape product data from a walmart URL or category and returns the data in JSON format.

## Table of Contents

- Installation
- Usage
- API Endpoints
- Project Structure
- License

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/michaelgetachew-abebe/scraper-test-assignment.git
   cd src
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t web-scraper-flask .
   ```

3. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 web-scraper-flask
   ```

## Usage

Once the Docker container is running, you can access the API at `http://localhost:5000`.

### Example Requests

- **Scrape a product URL:**
  ```bash
  curl "http://localhost:5000/scrape_url?url=https://example.com/product"
  ```

- **Scrape a category URL:**
  ```bash
  curl "http://localhost:5000/scrape_category?category_url=https://example.com/category"
  ```

## API Endpoints

- **GET /scrape_url**
  - **Description:** Scrapes product data from the provided URL.
  - **Parameters:** `url` (required) - The URL of the product to scrape.
  - **Response:** JSON object containing product data.

- **GET /scrape_category**
  - **Description:** Scrapes product data from the provided category URL.
  - **Parameters:** `category_url` (required) - The URL of the category to scrape.
  - **Response:** JSON array containing product data.

## Project Structure

```
web-scraper-flask/
├── Dockerfile
├── main.py
├── requirements.txt
└── scraper.py
```

- **Dockerfile:** Contains the instructions to build the Docker image.
- **main.py:** The main Flask application file.
- **requirements.txt:** Lists the Python dependencies.
- **scraper.py:** Contains the `Scraper` class for scraping logic.