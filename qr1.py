import qrcode as qr
img = qr.make("https://www.instagram.com/nextgen.geek/?hl=en")
img.save("qrcode_generator.png")

