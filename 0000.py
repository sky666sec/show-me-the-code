from  PIL import  Image,ImageFont,ImageDraw
#打开一个图像文件
image = Image.open("C:\\Users\sky666\Pictures\sky666.jpg")
#获取图像尺寸
w , h = image.size
#设置图像字体
font  = ImageFont.truetype("arial.ttf",50)
#绘制新的图像
draw = ImageDraw.Draw(image)
#加入文本文字
draw.text((w*4/5 , h/5), 'sky666sec' ,  font = font)
#保存绘制好的图像
image.save("C:\\Users\sky666\Pictures\sky666sec.jpg")


