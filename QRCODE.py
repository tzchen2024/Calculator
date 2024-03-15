import qrcode
from qrcode import QRCode, constants

def generate_qrcode(text):
  #We create a function called generate_qrcode that will take some text as input and generate a QR code from it.
  qr = QRCode(
    version = 1,
    error_correction=constants.ERROR_CORRECT_L,    box_size = 10,
    border = 4,
  )
  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  #We make the QR code image with a black pattern on a white background.
  img.save('qrimg001.png') 
  #We save the image with the name "qrimg001.png".
url = input("Enter a URL")
generate_qrcode(url)
  