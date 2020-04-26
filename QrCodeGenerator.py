import pyqrcode
f = input("File Name : ")
s = input("Text to Convert : ")
qr = pyqrcode.create(s)
qr.png("qrcodes/" + f + ".png",scale=10)