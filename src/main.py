from flask import Flask, request, jsonify
from scraper import Scraper

app = Flask(__name__)
scraper = Scraper()

@app.route('/scrape_url', methods=['GET'])
def scrape_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    product_data = scraper.scrape_by_url(url)
    if product_data:
        return jsonify(product_data)
    else:
        return jsonify({"error": "Failed to scrape the URL"}), 500

@app.route('/scrape_category', methods=['GET'])
def scrape_category():
    category_url = request.args.get('category_url')
    if not category_url:
        return jsonify({"error": "Category URL parameter is required"}), 400

    products = scraper.scrape_by_category(category_url)
    if products:
        return jsonify(products)
    else:
        return jsonify({"error": "Failed to scrape the category"}), 500

if __name__ == '__main__':
    app.run(debug=True)