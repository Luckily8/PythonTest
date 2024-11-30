import cv2
import numpy as np
import os
print(" =========  《基础功能：图像边缘检测，得到负片与边缘图像》 ")
# 读取图像
image_path = r'H:/Library/图片/崩铁/花火.jpg'

# 检查文件是否存在
if not os.path.exists(image_path):
    print(f"Error: File does not exist at {image_path}")
else:
    # 使用 os 模块读取文件并处理中文路径
    with open(image_path, 'rb') as f:
        image_data = f.read()
    image_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)

    # 检查图像是否成功读取
    if image is None:
        print(f"Error: Unable to read image at {image_path}")
    else:
        # 应用高斯模糊
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

        # 应用 Canny 边缘检测
        edges = cv2.Canny(blurred_image, 100, 200)

        # 显示结果
        # cv2.imshow('Original Image', image)
        cv2.imshow('Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # 保存结果
    # cv2.imwrite('wdf.jpg', edges)
print(" =========  《附加功能：海龟绘图，像素点输出》 ")
    # 结合海龟绘图
        # import turtle
# 使用海龟画图绘制边缘检测后的图像
        # screen = turtle.Screen()
        # screen.setup(width=800, height=600)
        # screen.title("边缘检测结果")

        # t = turtle.Turtle()
        # t.speed(0)
        # t.penup()

        # height, width = edges.shape
        # screen.setworldcoordinates(0, height, width, 0)

        # for y in range(height):
        #     for x in range(width):
        #         if edges[y, x] == 255:  # 边缘像素
        #             t.goto(x, y)
        #             t.pendown()
        #         else:
        #             t.penup()

        # turtle.done()
 # 输出 edges 矩阵中所有像素点的值
        # height, width = edges.shape
        # for y in range(height):
        #     for x in range(width):
        #         if edges[y, x] == 255:
        #             print(f"edges[{y}, {x}] = {edges[y, x]}")