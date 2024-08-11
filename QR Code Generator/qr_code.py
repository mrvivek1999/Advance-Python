import qrcode as qr
img =  qr.make("hello QR")
img.save("welcome_qr.png")


# to install qrcode module for python run this first .
# import subprocess
# import sys

# # Install the qrcode module
# subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]"])