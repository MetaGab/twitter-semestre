from check_hours import check
from tweet import tweet
from datetime import datetime, timezone, timedelta
import numpy as np
import cv2 as cv


hours = check()
percentage = hours*100//408
file = open("C:\\Users\\Gabo Banda\\Documents\\Proyectos\\twitter_bot\\p.txt", "a+")
file.seek(0)
log = open("C:\\Users\\Gabo Banda\\Documents\\Proyectos\\twitter_bot\\log.txt", "a+")

prev = file.readline()
print(prev)
log.write("RAN AT {} WITH PERCENTAGE {}% \n".format(datetime.now(), percentage))
if prev and int(prev) >= percentage:
	pass
else:
	tz = timezone(timedelta(hours=-7))
	now = datetime.now(tz)
	file.truncate(0)
	file.write(str(percentage))
	font = cv.FONT_HERSHEY_DUPLEX
	img = np.zeros((128,512,3), np.uint8)
	cv.rectangle(img,(0,0),(511,127),(237, 199, 109),-1)
	cv.rectangle(img,(30,26),(481,101),(255, 255, 255),-1)
	cv.rectangle(img,(33,29),(478,98),(0, 0, 0),-1)
	end = (473-38)*percentage//100 + 38
	cv.rectangle(img,(33,29),(478,98),(0, 0, 0),-1)
	color = (0,255,0)
	if now.day in [11, 12, 13] and now.month == 11:
		color = (168, 70, 31)
	cv.rectangle(img,(38,34),(end,93),color,-1)
	if percentage > 10:
		org = (222, 75)
	else:
		org = (234, 75)
	cv.putText(img=img, text=str(percentage)+"%", org=org, fontFace=font, fontScale=1, color=(0,0,0), thickness=8, lineType=cv.LINE_AA)
	cv.putText(img=img, text=str(percentage)+"%", org=org, fontFace=font, fontScale=1, color=(255,255,255), thickness=2, lineType=cv.LINE_AA)
	
	if now.day in [11, 12, 13] and now.month == 11:
		color = (168, 70, 31)
		proxy = cv.imread("C:\\Users\\Gabo Banda\\Documents\\Proyectos\\twitter_bot\\proxy.png")
		proxy = cv.resize(proxy, (50, 50), interpolation=cv.INTER_AREA )
		for column in range(proxy.shape[0]):
			for row in range(proxy.shape[1]):
				if np.any(proxy[column, row] != 0):
					img[40+column,105+row] = proxy[column, row]
	cv.imwrite('C:\\Users\\Gabo Banda\\Documents\\Proyectos\\twitter_bot\\bar.png', img)
	tweet(percentage)
	