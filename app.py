# app.py
import json
from flask import Flask, request, jsonify, render_template, abort, send_from_directory
from flask_cors import CORS
import spacy
from jinja2 import TemplateNotFound

app = Flask(__name__)
cors = CORS(app, resources={
    r"/analyze": {"origins": ["http://127.0.0.1:5000", "https://infoonity.com"]}
})
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page_name>')
def render_page(page_name):
    try:
        return render_template(f'{page_name}.html')
    except TemplateNotFound:
        abort(404)

# Route for serving ad images with cache control
@app.route('/static/images/<image_name>.png')
def serve_ad_image(image_name):
    response = send_from_directory('static/images', f'{image_name}.png')
    response.headers['Cache-Control'] = 'no-cache, must-revalidate'
    return response

# Error handling
try:
    with open('allowed_domains.json') as file:
        allowed_domains = json.load(file)["allowed_domains"]
except json.JSONDecodeError as e:
    print("Error reading the JSON file:", e)
    allowed_domains = []
except FileNotFoundError:
    print("allowed_domains.json file not found")
    allowed_domains = []

@app.route('/analyze', methods=['POST'])
def analyze_text():
    origin = request.headers.get('Origin')
    if origin not in ["http://127.0.0.1:5000", "https://infoonity.com"]:
        return jsonify({"error": "Unauthorized origin"}), 403

    data = request.json
    text = data.get('text', '')

    doc = nlp(text)
    priority_keywords = ['car', 'carrot', 'parrot']
    keyword = 'default'

    for token in doc:
        if token.text.lower() in priority_keywords:
            keyword = token.text.lower()
            break

    if keyword == 'default':
        for token in doc:
            if token.pos_ == 'NOUN':
                keyword = token.text.lower()
                break

    return jsonify({"keyword": keyword})

if __name__ == '__main__':
    app.run(debug=True)
