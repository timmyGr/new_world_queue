import pyscreenshot as ps
import pytesseract as pt
import cv2

from PIL import Image, ImageOps

position = 0

while True:
    # Grab screenshot and invert
    image = ps.grab()
    im_invert = ImageOps.invert(image)
    im_invert.save('new_world.png', quality=100)

    # Binarize
    image = cv2.imread('new_world.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = 180 # to be determined
    _, image_binarized = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    pil_image = Image.fromarray(image_binarized)

    # OCR for text
    pt.pytesseract.tesseract_cmd = "C:\Program Files (X86)\\Tesseract-OCR\\tesseract"
    text = pt.image_to_string(pil_image)

    # Detect Position
    text_list = text.splitlines()

    for index, value in enumerate(text_list):
        if "QUEUE" in value:
            try:
                q_pos = int(text_list[index+2])

                if position == 0:
                    position = q_pos

                if position > q_pos:
                    position = q_pos
                    print("Position: " + str(q_pos))
            except Exception:
                pass

            break
            