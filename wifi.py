from wifi_qrcode_generator import wifi_qrcode

qr_code = wifi_qrcode ("ConnectionName", hidden=False,
                       authentication_type="WPA", password="YourPassword")

qr_code_img = qr_code.make_image()

qr_code_img.save("wifi_qr.jpg")