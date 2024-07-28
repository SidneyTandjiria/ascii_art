# %%
from PIL import Image
import numpy as np

# %%
# image = Image.open("images/ascii-pineapple.jpg")
# image = Image.open("images/sheep.png")
# image = Image.open("images/hairycow.png")
image = Image.open("Batman-Logo.png")
print(f'Image loaded.\nImage size: {image.size}')

#%% resize image

base_width = 225

wpercent = (base_width / float(image.size[0]))
hsize = int((float(image.size[1]) * float(wpercent)))
resized_image = image.resize((base_width, hsize), Image.Resampling.LANCZOS)

image_array = np.array(resized_image)
print(f'Image resized: {resized_image.size}')

image.show()

## Get image brightness
# %%
brightness_array = np.zeros((image_array.shape[0], image_array.shape[1]))

print('Converting RGB values into brightness numbers...')
for x in range(len(image_array)):
    for y in range(len(image_array[x])):
        pixel = image_array[x][y]
        brightness_array[x][y] = np.mean(pixel)
        # brightness_array[x][y] = 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]
        # brightness_array[x][y] = (np.max(pixel) + np.min(pixel))/2

print(f'Finished converting to brightness array: {brightness_array.shape}')


# %%
# Sense check brightness values
print(f'Min brightness value: {round(np.min(brightness_array), 2)}')
print(f'Max brightness value: {round(np.max(brightness_array), 2)}')

# %%
# The following is a list of ascii characters from lightest to darkest
ascii_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# print(len(ascii_characters))

# %%
# Come up with a way to map brightness to ascii characters
# Brightness values range from 0 to 255
# There are 65 ascii characters



def map_to_ascii(brightness, maxBrightness=255, asciiAlpha='`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'):
    asciiLen = len(asciiAlpha)-1
    index = round((brightness / maxBrightness) * asciiLen)
    # print(index)
    return asciiAlpha[index]


# %%
# ascii_array = np.empty((brightness_array.shape[0], brightness_array.shape[1]), dtype = 'S')

print(f'Printing ascii art...\n')

for x in range(len(brightness_array)):
    print('\n', end = '')
    for y in range(len(brightness_array[x])):
        ascii_char = map_to_ascii(brightness_array[x][y])
        print(ascii_char*3, end='')

# print('\n')
# %%
