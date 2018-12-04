"""A program that encodes and decodes hidden messages in images through LSB steganography"""
from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="images/encoded_sample.png"):
    """Decodes the hidden message in an image
    file_location: the location of the image file to decode. By default is the provided encoded image in the images folder
    """
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
    green_channel = encoded_image.split()[1]
    blue_channel = encoded_image.split()[2]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            r_pixel = red_channel.getpixel((i,j))
            g_pixel = green_channel.getpixel((i,j))
            b_pixel = blue_channel.getpixel((i,j))
            # if pixels[i, j] = r_pixel, g_pixel, b_pixel ? bin(red_pixel)[-1] == '0':
            if bin(r_pixel)[-1] == '0' or bin(g_pixel)[-1] == '0' or bin(b_pixel)[-1] == '0':
                pixels[i, j] = (r_pixel, g_pixel, b_pixel)
            else:
                pixels[i, j] = (255,255,255)
    decoded_image.save("images/decoded_image.png")

def write_text(text_to_write, image_size):
    """Writes text to an RGB image. Automatically line wraps
    text_to_write: the text to write to the image
    """
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    #Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def encode_image(text_to_encode, template_image="images/samoyed.jpg"):
    """Encodes a text message into an image
    text_to_encode: the text to encode into the template image
    template_image: the image to use for encoding. An image is provided by default.
    """
    template_image = Image.open(template_image)
    red_template = template_image.split()[0]
    green_template = template_image.split()[1]
    blue_template = template_image.split()[2]

    x_size = template_image.size[0]
    y_size = template_image.size[1]

    #text draw
    image_text = write_text(text_to_encode, template_image.size)
    bw_encode = image_text.convert('1')

    #encode text into image
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            red_template_pix = bin(red_template.getpixel((i,j)))
            green_template_pix = bin(green_template.getpixel((i,j)))
            blue_template_pix = bin(blue_template.getpixel((i,j)))
            tencode_pix = bin(bw_encode.getpixel((i,j)))

            if tencode_pix[-1] == '1':
                red_template_pix = red_template_pix[:-1] + '1'
                green_template_pix = green_template_pix[:-1] + '1'
                blue_template_pix = blue_template_pix[:-1] + '1'
            else:
                red_template_pix = red_template_pix[:-1] + '0'
                green_template_pix = green_template_pix[:-1] + '0'
                blue_template_pix = blue_template_pix[:-1] + '0'
            pixels[i, j] = (int(red_template_pix, 1), int(green_template_pix, 1), int(blue_template_pix, 1))

    encoded_image.save("images/encoded_image.png")

if __name__ == '__main__':
    decode_image()
    # encode_image("hello world")