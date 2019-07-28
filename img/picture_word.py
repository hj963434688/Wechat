import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#设置所使用的字体
font = ImageFont.truetype('ArialHB.tcc', size=20)

#打开图片
imageFile = "emotion.jpg"
im1 = Image.open(imageFile)

#画图
draw = ImageDraw.Draw(im1)
draw.text((160, 0), "helloworld", (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
draw = ImageDraw.Draw(im1)                          #Just draw it!

#另存图片
im1.save("target.")