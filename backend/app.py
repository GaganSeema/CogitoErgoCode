import os
import requests
import uuid
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='../static', template_folder='../')

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
HF_TOKEN = os.environ.get("HF_TOKEN")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')

    image_bytes = query({
        "inputs": prompt,
    })

    # Save the image
    if not os.path.exists('static/generated'):
        os.makedirs('static/generated')

    filename = f"{uuid.uuid4()}.png"
    image_path = f"static/generated/{filename}"
    with open(image_path, "wb") as f:
        f.write(image_bytes)

    return jsonify({'image_url': f'/{image_path}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
