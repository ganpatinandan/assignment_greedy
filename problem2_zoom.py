#-------importing libraries just to load and save images
import cv2
import numpy as np

#-------taking any image as input
print "enter complete image path like /home/images/xyz.jpg"
img=cv2.imread(raw_input())
#print img.shape

rows=img.shape[0]
cols=img.shape[1]

#------taking pivot and scale
print "enter the pivot :"

'''pivot=(100,100)
r1=pivot[0]
c1=pivot[1]'''

c1=int(raw_input("enter x"))
r1=int(raw_input("enter y"))

scale=int(raw_input("enter scale (only positive):"))


#------finding Region of interest
P=c1+cols/(2*scale)

Q=c1-cols/(2*scale)
R=r1+rows/(2*scale)
S=r1-rows/(2*scale)

if P>cols:
	ex=cols
	sx=Q-(P-ex)
elif Q<0:
	sx=0
	ex=P+(sx-Q)
else:
	ex=P
	sx=Q
if R>rows:
	ey=rows
	sy=S-(R-ey)
	
elif S<0:
	sy=0
	ey=R+(sy-S)
else:
	ey=R
	sy=S	

#print sx,sy,ex,ey
roi = img[sy:ey, sx:ex]
#-------------------------
rc=roi.shape[0]
cc=roi.shape[1]
#print rc,cc
#---------Creating zero pixel matrix for wrting zoomed image pixels

blank= np.zeros((rows,cols,3), np.uint8)



#-----------mapping Region of interest pixels on to blank matrix
b=0
d=0
for i in range(rc):
	for j in range(cc):
		blank[b:b+scale,d:d+scale]=roi[i,j]
		d=d+scale
		#print d
	b=b+scale
	d=0
	#print b
	
#save zoomed pixel matrix as jpg file
cv2.imwrite('zoom.jpg',blank)
print "Zoomed image is saved..."
