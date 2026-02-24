import fitz  # PyMuPDF
import cv2
import numpy as np

doc = fitz.open("C:/Users/RomikaRani/OneDrive - Kongsberg Digital AS/Desktop/important/Time andwork3.pdf")
out = fitz.open()

for page in doc:
    pix = page.get_pixmap(dpi=300)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)

    _, thresh = cv2.threshold(inverted, 200, 255, cv2.THRESH_BINARY)

    new_page = out.new_page(width=page.rect.width, height=page.rect.height)
    new_page.insert_image(new_page.rect, stream=cv2.imencode(".png", thresh)[1].tobytes())

out.save("output.pdf")