import cv2
img = cv2.imread("test3.jpeg")
resized=cv2.resize(img, (400,400))
cv2.imshow("hello",resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()
