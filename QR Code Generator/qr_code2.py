import qrcode
from PIL import Image
import qrcode.constants
qr =  qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size= 10,border =4 ,)
qr.add_data("https://www.linkedin.com/in/vivekbpi/")
qr.make(fit=True)
img  = qr.make_image(fill_color= "black",back_color = "blue")
img.save("LinkdinQR.png")


# to install qrcode module for python run this first .
# import subprocess
# import sys

# # Install the qrcode module
# subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]"])
