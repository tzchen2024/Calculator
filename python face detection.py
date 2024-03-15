import cv2
#Imports the OpenCV library, allowing you to use its functions and classes for image processing.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Loads a pre-trained cascade classifier for detecting frontal faces. The XML file 'haarcascade_frontalface_default.xml' contains the trained model for detecting frontal faces.
img = cv2.imread('test.png') 
#Reads an image file named 'test.png' and stores it in the variable img. This function reads the image as a NumPy array, allowing further processing.
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#Converts the loaded image (img) from color (RGB) to grayscale. Grayscale images are often used for simplicity and efficiency in image processing tasks.
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
  #Iterates through each detected face, where (x, y) are the coordinates of the top-left corner of the rectangle, and (w, h) are the width and height of the rectangle respectively.
  cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
  #Draws a rectangle around each detected face on the original image (img). The parameters are: the image to draw on (img), coordinates of the top-left and bottom-right corners of the rectangle, color in BGR format (blue in this case represented by (225, 0, 0)), and thickness of the rectangle (2 pixels).
cv2.imshow('img', img)
#Displays the modified image (img) with rectangles drawn around the detected faces. The window title is set to 'img'.
cv2.waitkey()
#Waits indefinitely for a key press. This keeps the window open until any key is pressed.
cv2.imwrite("face_detected.jpg")
#Saves the modified image with detected faces as a JPEG file named "face_detected.jpg".
