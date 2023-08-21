import cv2


img = cv2.imread('C:\\Users\\Manju\\Pictures\\Camera Roll\\WIN_20220304_18_04_56_Pro (2).jpg')
print(img.shape)
img = cv2.resize(img,(410,410))
print(img.shape)



grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh5 = cv2.threshold(grayscale,155,255,cv2.THRESH_TOZERO_INV)


contours, hierarchy = cv2.findContours(thresh5,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


cnt = contours


dias = []


for i in range (len(cnt)):
    (x,y),radius = cv2.minEnclosingCircle(cnt[i])
    center = (int(x),int(y))
    radius = int(radius)
    # cv2.circle(img,center,radius,(0,255,0),20)
    print('Diametro: '+str((radius*2)/100)+'mm','radius',str(radius),center)

    dias.append((radius*2)/100)

print('max dia is::::::', max(dias)*3)
# cv2.circle(img,(201,208),289,(0,255,0),-1)




cv2.imshow('thresh5',thresh5)
cv2.imshow('img',img)


cv2.waitKey(0)

