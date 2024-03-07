from flask import Flask, request, jsonify
from selenium_script import scrape_website

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape_endpoint():
    # Get URL from request body
    url = request.json.get('url')

    # Scrape website using Selenium
    scraped_data = scrape_website(url)

    # Return scraped data as JSON response
    return jsonify(scraped_data)

if __name__ == "__main__":
    app.run(debug=True)
