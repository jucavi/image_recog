from PIL import Image, ImageOps
import torch
import torchvision.transforms.functional as fn
import pytesseract
import glob

# image = Image.open('images/image2.png')
# # print(pytesseract.get_languages(config=''))
# # print(pytesseract.image_to_string(image, lang='eng'))
# # print(pytesseract.image_to_data(image))
# greyscale_image = image.convert('L')
# greyscale_image.save('greyscale_image.jpg')

# # contrast = ImageEnhance.Contrast(image)
# contrast = ImageEnhance.Contrast(greyscale_image)
# contrast.enhance(3.5).save('contrast.jpg')

# color = ImageEnhance.Color(Image.open('contrast.jpg'))
# color.enhance(1.5).save('color.jpg')

# # image.show()
# image = Image.open('color.jpg')
# inverted_image = ImageOps.invert(image)
# # image.show()
# # inverted_image.show()
# # greyscale_image.show()
# print(pytesseract.image_to_string(image, lang='eng'))
# print('-----------------------------------------------------')
# print(pytesseract.image_to_string(inverted_image, lang='eng'))

def parse_image(image, contrast=1, color=1):
    if isinstance(image, str):
        image = Image.open(image)

    thresh = 34
    f = lambda x : 255 if x > thresh else 0

    # # convert to grey scale
    image = image.convert('L').point(f, mode='1')
    # image = image.convert('L')

    # invert colors
    # image = ImageOps.invert(image)

    tensor_image = fn.to_tensor(image)
    normalize = fn.normalize(tensor_image, mean=tensor_image.mean(), std=tensor_image.std())
    image = fn.to_pil_image(normalize)
    # # change contrast
    # image = ImageEnhance.Contrast(image)
    # image = image.enhance(contrast)

    # # change color
    # image = ImageEnhance.Color(image)
    # image = image.enhance(color)

    image.show()

    return pytesseract.image_to_string(image, lang='eng')

# parsed_str = parse_image(Image.open('images/image2.png'), contrast=3, color=1.5)
# print(parsed_str)

for infile in glob.glob('images/*.png'):
    print(parse_image(Image.open(infile)))
    print('--------------------------------------')