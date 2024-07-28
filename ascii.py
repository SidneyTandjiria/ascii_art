from PIL import Image
import numpy as np

class asciiArt:

    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def show(self):
        self.image.show()

    def resizeImage(self, baseWidth = 225):
        wpercent = (baseWidth / float(self.image.size[0]))
        hsize = int((float(self.image.size[1]) * float(wpercent)))
        self.resizedImage = self.image.resize((baseWidth, hsize), Image.Resampling.LANCZOS)

    def convertToBrightness(self, method):
        self.imageArray = np.array(self.resizedImage) # turn image into a numpy array
        self.brightnessArray = np.zeros((self.imageArray.shape[0], self.imageArray.shape[1]))
        # Convert RGB values to brightness values
        for x in range(len(self.imageArray)):
            for y in range(len(self.imageArray[x])):
                pixel = self.imageArray[x][y]
                # conversion depends on method
                if method == "luminosity":
                    self.brightnessArray[x][y] = 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]
                elif method == "lightness":
                    self.brightnessArray[x][y] = (np.max(pixel) + np.min(pixel))/2
                else: # default is average
                    self.brightnessArray[x][y] = np.mean(pixel)

    def convertToAscii(self, brightness, maxBrightness=255, asciiAlpha='`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'):
        asciiLen = len(asciiAlpha)-1
        index = round((brightness / maxBrightness) * asciiLen)
        return asciiAlpha[index]

    def asciify(self, baseWidth, method = "average"):
        self.resizeImage(baseWidth) # resize image to the basewidth specified
        self.convertToBrightness(method) # convert RGB array to a brightness array
        # print the ascii art
        for x in range(len(self.brightnessArray)):
            print('\n', end = '')
            for y in range(len(self.brightnessArray[x])):
                ascii_char = self.convertToAscii(self.brightnessArray[x][y])
                print(ascii_char*3, end='') # multiply by 3 otherwise the image is squished

if __name__ == "__main__":
    image = "images/starwars.jpg"
    artwork = asciiArt(image)
    # artwork.show()
    artwork.asciify(baseWidth = 130, method = "average")
