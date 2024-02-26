from flask import Flask, render_template, request, redirect, url_for
import cv2
import pytesseract
import numpy as np

# Prerequisite: Install Flask, OpenCV, and pytesseract
# Ensure Tesseract-OCR is installed and accessible
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with your Tesseract-OCR path

def preprocess_and_read_text(image_bytes):
    """
    Preprocesses an image and extracts text using pytesseract.

    Args:
        image_bytes: The image data as bytes.

    Returns:
        The extracted text.
    """

    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    
    # Preprocess the image (optional)
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



    # Extract text with configuration options
    text = pytesseract.image_to_string(thresh, config='--psm 6 tessedit_char_whitelist=0123456789')
    return text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_and_process():
    if request.method == 'POST':
        # Get uploaded image
        image_file = request.files['image']
        if image_file:
            # Read image bytes
            image_bytes = image_file.read()

            # Preprocess and extract text
            extracted_text = preprocess_and_read_text(image_bytes)

            return render_template('result.html', text=extracted_text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
