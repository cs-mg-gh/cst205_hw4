from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
import random

app = Flask(__name__)
Bootstrap(app)


IMAGE_FOLDER = 'static/images'

all_images = os.listdir(IMAGE_FOLDER)

@app.route('/')
def home():
    random.shuffle(all_images)
    selected_images = all_images[:3]

    return render_template('index.html', images=selected_images)

if __name__ == '__main__':
    app.run(debug=True)
