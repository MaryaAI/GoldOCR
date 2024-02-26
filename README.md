# Gold OCR

Text detection inside Gold Bar using PyTesseract and OpenCV

## PyTesseract
Purpose: PyTesseract is a Python wrapper for Google's Tesseract-OCR Engine. It is primarily used to perform Optical Character Recognition (OCR) to read text from images.
Use Cases: It's specifically designed for extracting text from images. This makes it highly useful for reading text from scanned documents, images of text, screenshots, and areas within images where text is present.

The provided code demonstrates how to use pytesseract to extract numbers from an image, incorporating preprocessing steps and configuration options to enhance accuracy. Here's a breakdown:

1. Import Libraries:

import pytesseract
import cv2
pytesseract: Provides functions for Optical Character Recognition (OCR) using Tesseract.
cv2: OpenCV library for image processing tasks like grayscale conversion, thresholding, and more.
2. Load the Image:

img = cv2.imread('your_image.jpg')
This line reads the image file named 'your_image.jpg' using OpenCV and stores it in the img variable.
3. Preprocess the Image (Optional):

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
Grayscale conversion: cv2.cvtColor converts the image from its original color format (BGR) to grayscale using cv2.COLOR_BGR2GRAY. This simplifies the image and improves character recognition.
Binarization: cv2.threshold converts the grayscale image to a binary image (black and white) using Otsu's thresholding method. This enhances the contrast between text and background, making it easier for Tesseract to recognize characters.
4. Extract Text with Configuration Options:

text = pytesseract.image_to_string(thresh, config='--psm 6 tessedit_char_whitelist=0123456789')
pytesseract.image_to_string: This function extracts text from the image and returns it as a string.
thresh: The preprocessed image (binary) is passed as the first argument.
config='--psm 6': This configuration option sets the page segmentation mode to 6, which instructs Tesseract to treat the entire image as a single block of text. This can be helpful for images containing just numbers.
tessedit_char_whitelist='0123456789': This option restricts Tesseract to only recognize digits (0-9) from the provided whitelist. This improves accuracy by focusing on the specific characters of interest.
5. Print the Extracted Numbers:

print(text)
This line prints the extracted text (containing only numbers) to the console.
6. Optional: Validate Extracted Numbers:

While not explicitly shown in the code, you can add a step to validate the extracted text using regular expressions. This ensures the extracted numbers conform to expected formats and helps identify potential errors.
Overall, the code effectively combines image preprocessing, configuration options, and text extraction to improve the accuracy of reading numbers from images using pytesseract.



## Installation

1- Installation of pytesseract and Pillow

```
pip install pytesseract Pillow
```

2- Install OpenCV 

3- Install Flask

4- Insatll numpy


## Run

Just add the path of the image and run the cell!


## Run Web App


## Future work
Do more tests and preprocessing for images to optimize the detection of text




