import os
from PIL import Image

def resize_image(image, size):
    img_resized = image.resize(size, Image.ANTIALIAS)
    return img_resized
#输入要转换图片地址
input_folder = r""
#输入输出图片地址
output_folder = r""
size = (286, 500)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历文件夹中的所有文件
for file in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file)

    # 检查文件是否为图片
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        img = Image.open(file_path)
        resized_image = resize_image(img, size)
        resized_image_path = os.path.join(output_folder, file)
        resized_image.save(resized_image_path)

print("图片调整大小完成！")
