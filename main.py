# Simple QR code generator in Python

import qrcode as qr

img = qr.make("https://www.linkedin.com/in/yash-halwai-198007203/")

img.save("YashHalwai_LinkedIn.png") 