import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H,box_size=45,
                   border=5)

qr.add_data('https://en.wikipedia.org/wiki/Anna_(2019_feature_film)')

qr.make(fit=True)
img = qr.make_image(fill_color='yellow', back_color='orange')
img.save('wikiannacustoms.jpeg')

