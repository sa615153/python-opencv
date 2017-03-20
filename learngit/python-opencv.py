cv2.4.13， python 2.7.12


通过上面的例子我们了解了如何最有效率地使用math库和numpy库中的数学函数。因为它们各有长短，因此在导入时不建议使用*号全部载入，而是应该使用import numpy as np的方式载入，这样我们可以根据需要选择合适的函数调用。

mona lisa：
渐变，，模糊处理障眼法？透视？  chapter10图像混合，addweighted
chapter17， enrode， 做出核心支架信息？

distance detection:
 轮廓在形状分析和物体的检测和识别中很有用
 find objects in an image using Template Matching：先识别，再算位置，推出角度
 霍夫变换在检测各种形状的的技术中非常流行，如果你要检测的形状可以用数学表达式写出，你就可以是使用霍夫变换检测它
 
 feature detection and description
	亚像素级精确度的角点

 


imshow和waitkey联合使用
cv2.imshow('image',img)
cv2.waitkey(2000)
#照片显示2秒后消失，若没有waitKey，只会闪一下

# //video file：
r'I:\USTC\opencv\2.4.13\opencv\sources\3rdparty\ffmpeg'
两个dll改版本号，复制到python根目录下
把3rd那个目录加入环境变量不管用，得复制

在dell里，ffmpeg里文件复制改名，且复制到python_64下，但python_64不再环境变量里，但ffmepg在环境变量里，可用(需把目录换成斜杠'C:/Users/JPang3/Desktop/beijing/opencv/opencv_projects/python-opencv/wildlife.wmv')


#  //save video
http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html#display-video
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#display-video
fourcc = cv2.VideoWriter_fourcc(*'XVID')不可用

版本：
    # cv3
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
	3.0以前3.0-beta（2014.11.11）
	在中文版python tutorials Jan 3 21:06:22 2014
	fourcc = cv2.cv.FOURCC(*'XVID')可用

	In OpenCV 2, findContours returns just two values, contours and hierarchy. 
	The error occurs when python tries to assign those two values to the three names given on left in this statement:
	drawContours cv2 无返回值，cv3有返回值

	# cv3
	#box = cv2.boxPoints(rect)
	# cv2
	box = cv2.cv.BoxPoints(rect)

	# img3 = cv2.circle(img3,center,radius,(0,255,0),2)
    # cv2
    n = cv2.circle(img3,center,radius,(0,255,0),2)
	
	#cv3
    # img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
    #cv2
    cv2.line(img3,(cols-1,righty),(0,lefty),(0,255,0),2)
	
	
blur 模糊，去噪音， filters 滤波器

最新版python-opencv-python-tutorials措辞比较准确，

高斯窗口threshold， 高斯模糊（滤波）+ ostu threshold

第一个像素卷积平均值或别的值会在卷积第二个像素时用到吗？

梯度滤波器=高通滤波器，看来以前的均值中值高斯双边都是低通滤波器
在前面的部分我们实现了一个 HPF（高通滤波），现在我们来做 LPF（低通滤波）将高频部分去除。--高低指频率

 gradients_edge
 求边界，即求离散导数，边界存在导致边界边缘两侧高度明显不同，导数较大
 在数字图像中，微分用差分计算，一般dx=1，所以dy/dx=f(x)-f(x-1)。

canny 不需要阈值处理

draw and compute area
	area = cv2.contourArea(cnt)
	hull = cv2.convexHull(cnt)
	hull_area = cv2.contourArea(hull)

	cv2.drawContours(img3,[box],0,(0,0,255),2)

	
	
drawContours
    向灰度图上画轮廓一定要制定灰度值，而不是颜色值
	
	
	
	
	
	
	
识别
    contours - more function - cv2.matchShapes   That would be a simple step towards OCR  光学字符识别（英语：Optical Character Recognition, OCR）
    hsv，依据颜色值做出mask，再bitwise原图，达到跟踪特定颜色物体的效果（同颜色其他物体也被保留）13.2.py
	直方图反向投影:
	

	

交互：
    8 通过while(1)不断更新trackbar的数值，进而不断改变颜色
	8.1 cv2.setMouseCallback('image',draw_circle)  ->   draw_circle ->  用b,g,r,修改img  -> while(1)显示、更新trackbar数值bgr
	8.2 cv2.setMouseCallback('image',draw_circle)  ->   draw_circle ->  获取trackbar数值bgr,修改img -> while(1)只负责显示
	cv2.createTrackbar('R','image',0,255,nothing)
	
	
	
	samples/python/color_histogram.py  
	def set_scale(val):
        global hist_scale
        hist_scale = val
    cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

histogram
    一副高质量的图像的像素值分布应该很广泛
	直方图均衡化经常用来使所有的图片具有相同的亮度条件的参考工具

	反向投影(Backprojection)
		http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/imgproc/histograms/back_projection/back_projection.html
			查看某像素，的颜色值(h,s),看这个值(h,s)坐标对代表的值，在"模型直方图"中出现的情况，，模型直方图该值(h,s)越亮,说明这个像素的这个颜色在目标物体中出现的次数n越多，
			这样理解？：
			由因为在目标物体中而发生的该(h,s)颜色值的概率 大于 因为在别的物体中，而发生该颜色值的概率。（因为别的物体没有这个颜色，否则别的物体也属于目标物体），n越大，越像目标颜色，
			
			而且，这是很简陋的识别，目标物体有的颜色，别的物体最好别有，，，还是在靠颜色识别，跟hsv蓝色追踪没本质区别
			
			
			
			http://blog.csdn.net/chenjiazhou12/article/details/22150421
			1、原理
            图像的反向投影图是用输入图像的某一位置上像素值（多维或灰度）对应在直方图的一个bin上的值来代替该像素值，所以得到的反向投影图是单通的。
			举个小例

			(1)例如灰度图像如下
			Image=

			  0    1    2    3
			  4    5    6    7
			  8    9   10   11
			  8    9   14   15
			(2)该灰度图的直方图为（bin指定的区间为[0,3)，[4,7)，[8,11)，[12,16)）
			Histogram=
			  4    4    6    2
			(3)反向投影图
			Back_Projection=
			  4    4    4    4
			  4    4    4    4
			  6    6    6    6
			  6    6    2    2
			例如位置(0,0)上的像素值为0，对应的bin为[0,3)，所以反向直方图在该位置上的值这个bin的值4。
			#第一点举例：这点这颜色总共出现过4次
			
			
			
			
			http://www.cnblogs.com/liu-jun/p/3482211.html
			# 如果一幅图像的区域中显示的是一种结构纹理或者一个独特的物体，那么这个区域的直方图可以看作一个概率函数，他给的是某个像素属于该纹理或物体的概率。

			# 所谓反向投影就是首先计算某一特征的直方图模型，然后使用模型去寻找测试图像中存在的该特征。 #用概率取探查

			利用Hue直方图解释反向投影原理：

			1、获取测试图像中每个像素的hue数据 hi,j，并找到 hi,j 在hue直方图中的bin的位置。

			2、查询hue直方图中对应bin的数值。

			3、将该数值存储在新的图像中（BackProjection），也可以先归一化hue直方图数值到0-255范围，这样可以直接显示BackProjection图像（单通道图像）。

			4、通过对测试图像每个像素采取以上步骤，可以得到最终的BackProjection图像。
			

卷积
    # 此处卷积可以把分散的点连在一起
	disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	cv2.filter2D(dst,-1,disc,dst)

大概是振幅越高，频率越低，幅度谱亮点周围都是振幅高的--即低频分量，除去之后剩高频分量
























































































































































































	



