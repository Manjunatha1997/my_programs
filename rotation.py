import cv2
import imutils


ori = cv2.imread('/home/manju/original.jpg')

ori1 = cv2.imread('/home/manju/original.jpg')
rot = cv2.imread('/home/manju/rot.jpg')

# ori = cv2.resize(ori,(640,480))
# rot = cv2.resize(rot,(640,480))

# rot = cv2.rotate(rot,cv2.cv2.ROTATE_90_CLOCKWISE)
# rotated = imutils.rotate_bound(rot, 90)

# ori = imutils.rotate(ori,angle=90)
# rotated = imutils.rotate(rot,90)

# print(rotated)

# if ori.any() == rotated.any():
#     print('equal.....')
# else:
#     print("not equal....")


rot = imutils.rotate(rot,180)

if ori.shape == rot.shape:
    # print("The images have same size and channels")
    difference = cv2.subtract(ori, rot)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("not equal...")

cv2.imshow('original',ori)
cv2.imshow('rot',rot)
# cv2.imshow('rotational',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()


