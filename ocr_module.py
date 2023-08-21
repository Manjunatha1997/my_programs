
import cv2
from paddleocr import PaddleOCR,draw_ocr
from pyzbar import pyzbar
import cv2
import cv2
import zxingcpp


class OCR:
    def __init__(self):
        pass

    def load_model(self):
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        return ocr

    def get_predictions(self,model,image):
        result = model.ocr(image, cls=True)
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        ocr_image = draw_ocr(image, boxes, txts, scores, font_path='simfang.ttf')
        return ocr_image, txts


class BarcodeReader:
    def __init__(Self):
        pass
    def decode(self,image):
    # decodes all barcodes from an image
        decoded_objects = pyzbar.decode(image)
        for decoded in decoded_objects:
            # draw the barcode
            image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                                (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                                color=(0, 255, 0),
                                thickness=5)
            data = decoded.data.decode('utf-8')

        return image,data


class QRReader:
    def __init__(self):
        pass
    def get_qr_data(self,img):
        results = zxingcpp.read_barcodes(img)
        for result in results:
            value = format(result.text)
            return value
