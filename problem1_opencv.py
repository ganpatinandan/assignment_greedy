import cv2
import numpy as np


# Read in the image.
print "enter complete image path like /home/images/xyz.jpg"
img_src=cv2.imread(raw_input())
#img_src = cv2.imread("dd1.jpg")
rows = img_src.shape[0] 
cols = img_src.shape[1]
    

    
print '''INSTRUCTIONS:-
    1. Enter the four coordinates -- top left first
       and bottom left last --
       
    2. All coordinates serially like x1 then press enter
       y1 then press enter and so on..
       

    '''
l=np.array([[0,0]]*4)
max=0    
for i in range(0,4):
    for j in range(0,2):
            
        l[i][j]=int(raw_input())
        if max<l[i][j]:
                   max=l[i][j]
            
pts_dst=l
size=(max,max)
pts_src = np.array([[0,0],[cols-1,0],[cols-1,rows-1],[0,rows-1]])
    
# Calculate the homography
h, status = cv2.findHomography(pts_src, pts_dst)
    

# Warp source image to destination
img_dst = cv2.warpPerspective(img_src, h, size[0:2])

# Show output
cv2.imshow("Image", img_dst)
cv2.waitKey(0)


