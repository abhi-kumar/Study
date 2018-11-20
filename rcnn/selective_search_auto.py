import cv2
import selectivesearch



img = cv2.imread("dog.jpg", 1)
img_lbl, regions = selectivesearch.selective_search(img, scale=500, sigma=0.9, min_size=10)

print "Total number of proposals = ", len(regions)

#Drawing only a few
for i in range(0, len(regions), len(regions)/100):
	x1 = regions[i]['rect'][0]
	y1 = regions[i]['rect'][1]
	x2 = regions[i]['rect'][2]
	y2 = regions[i]['rect'][3]

	img = cv2.rectangle(img, (x1, y1), (x2, y2), [0,255,0], 2)

cv2.imshow("Image with random proposals", img)
cv2.waitKey(0)
