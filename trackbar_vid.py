import cv2
import math

def BrightnessContrast(brightness=0):
    # getTrackbarPos returns the current
    # position of the specified trackbar.
    brightness = cv2.getTrackbarPos('Brightness','PUPPY')

    contrast = cv2.getTrackbarPos('Contrast','PUPPY')

    effect = controller(frame, brightness,contrast)

    # The function imshow displays an image
    # in the specified window
    cv2.imshow('Effect', effect)
    out.write(frame)

def controller(videocapture, brightness=255, contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

    if brightness != 0:

        if brightness > 0:

            shadow = brightness

            max = 255

        else:

            shadow = 0
            max = 255 + brightness

        al_pha = (max - shadow) / 255
        ga_mma = shadow

        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(videocapture, al_pha,videocapture, 0, ga_mma)

    else:
        cal = videocapture

    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)

        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(cal, Alpha,cal, 0, Gamma)

    # putText renders the specified text string in the image.
    cv2.putText(cal, 'B:{},C:{}'.format(brightness, contrast), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    return cal


if __name__ == '__main__':
    videocapture = cv2.VideoCapture(-1)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    cv2.namedWindow('PUPPY')

    cv2.createTrackbar('Brightness','PUPPY', 255, 2 * 255,BrightnessContrast)
    cv2.createTrackbar('Contrast', 'PUPPY',127, 2 * 127,BrightnessContrast)

    while True:
        ret,frame = videocapture.read()
        cv2.imshow("video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    videocapture.release()
    cv2.destroyAllWindows()
