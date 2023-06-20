from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    api_key = '9f6a579c3103f0b7a70c118c912ec642728cc9fe'  # Replace with your actual API key

    api_url = f'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'long_url': long_url
    }

    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        short_url = response.json().get('id')
        return render_template('index.html', short_url=short_url)
    else:
        return 'Error: Failed to shorten the URL.'

if __name__ == '__main__':
    app.run(debug=True)
