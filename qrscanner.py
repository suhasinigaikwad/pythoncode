import qrcode

qr = qrcode.QRCode(version= 15,box_size = 7,border = 3)
data = "https://www.instagram.com/suhanig_10/"
qr.add_data(data)
qr.make(fit= True)
image=qr.make_image(fill='black',back_color='white')
image.save('QR.png')
