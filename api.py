from flask import Flask, request, jsonify
from selenium_script import scrape_website

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape_endpoint():
    # Get URL from request body
    url = request.json.get('url')
    target_img_url = request.json.get('img_url')

    # Scrape website using Selenium
    scraped_data = scrape_website(url,target_img_url)

    # Return scraped data as JSON response
    return jsonify({'adurl': scraped_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001, debug=True)
