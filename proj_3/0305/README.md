proj_03-05-a.py
---------------
Use the program developed in Project 03-03 to implement high-boost filtering, 

as given in Eq. (3.6-9). The averaging part of the process should be done using 

the mask in Fig. 3.32(a).


proj_03-05-b.py:
---------------
Download Fig. 3.40(a) from the book web site and enhance it using the program you 

developed in (a). Your objective is to approximate the result in Fig. 3.40(e).

origin_image.bmp is the original image

gaussian_blured_image.bmp is the result of blurring with a Gaussian filter

scal_gmasked_image.bmp is the result after unsharp mask, and I scal the interval from

[-255, 255] to [0, 255]

unsharp.bmp is the result after unsharp masking that k = 1

highboost_filter_image.bmp is the result after unsharp masking that k = 3 > 0 



