from flask import Flask, render_template, request
import os

app = Flask(__name__)

noun_images = {
    "cat": "cat.jpg",
    "dog": "dog.jpg",
    "pizza": "pizza.jpg",
    "mountain": "mountain.jpg",
    "nyu": "nyu.jpg"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/madlib', methods=['POST'])
def madlib():
    noun = request.form.get('noun', '').lower()
    verb = request.form.get('verb', '').lower()
    adj  = request.form.get('adj', '').lower()

    # look up the image or use default
    image_file = noun_images.get(noun, "default.jpg")

    return render_template(
        "madlib.html",
        noun=noun,
        verb=verb,
        adj=adj,
        image=image_file
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

