from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400
    
    file = request.files['file']
    if file.filename == '':
        return "Nome de arquivo vazio", 400

    image = Image.open(file.stream)
    output = remove(image)
    filename = os.path.splitext(file.filename)[0]
    output_filename = f"{filename}-remov3.png"
    output_path = os.path.join("static", output_filename)
    output.save(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
