from PIL import Image
import os
import time

def quickSort(img,l,r,y):
	if(l < r):
		j = partition(img,l,r,y)
		quickSort(img,l,j-1,y)
		quickSort(img,j+1,r,y)

def partition(img,l,r,y):
	pivot = img[l,y]
	right = r
	left = l+1

	while(True):
		while left <= right and img[left,y] <= pivot:
			left += 1
		while img[right,y] >= pivot and right >= left:
			right -= 1
		if right < left:
			break
		else:
			temp = img[left,y]
			img[left,y] = img[right,y]
			img[right,y] = temp
	temp=img[l,y]
	img[l,y] = img[right,y]
	img[right,y] = temp
	return right
fn = input('Picture to be sorted > ')

try:
	start_t = time.time()
	ip = Image.open('images/' + fn + '.png', 'r')
	proceed = True
	if(ip.size[0] > 1023):
		print("File to large; try rotating the picture 90 degrees")
		proceed = False
	if(proceed):
		img = ip.load()
		yscale = (int)(ip.size[1] / 10)
		print("Sorting: " + ip.filename)

		for y in range(ip.size[1] - 1,0,-1):
			quickSort(img,0,ip.size[0]-1,y)
		ip.save(('sorted/' + fn + '_sorted.png'), 'png')
		end_t = time.time()
		print("Approximate time elapsed: %.2f" % (end_t-start_t) + " seconds")
		print("Sorted file written to: " + ('sorted/' + fn + '_sorted.png'))
		ip.close()
except:
	print("Unable to locate file '" + fn + "'")