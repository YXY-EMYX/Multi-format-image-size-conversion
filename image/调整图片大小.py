from PIL import Image

def resize_image(image, size):
    img_resized = image.resize(size, Image.ANTIALIAS)
    return img_resized

# 加载图像
img = Image.open("path/to/your/image.jpg")

# 调整图像大小
size = (200, 350)
resized_image = resize_image(img, size)

# 保存调整大小后的图像
resized_image.save("path/to/resized_image.jpg")
