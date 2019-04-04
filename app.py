from flask import Flask, request, render_template
from io import BytesIO
from fastai.vision import *
from PIL import Image
from commons import inf
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        print(request.files)
        if 'image_up' not in request.files:
            print("File not uploaded!!")
            return
        file = request.files['image_up']
        
        image = file.read()
        image = open_image(BytesIO(image))
        print(type(image))
        return render_template('result.html', typ=inf(image))

if __name__ == "__main__":
    app.run(debug=False)