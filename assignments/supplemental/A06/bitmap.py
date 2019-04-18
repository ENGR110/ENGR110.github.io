from PIL import Image

# example
def make_rgb():
    img = Image.new('RGB', (255,255), "black") # Create a new black image
    pixels = img.load() # Create the pixel map
    for i in range(img.size[0]):    # For every pixel:
        for j in range(img.size[1]):
            pixels[i,j] = (i, 100, i*j) # Set the colour accordingly
    # img.show()
    img.save('test.bmp')


BLACK = 0
WHITE = 1

image_data = []
for i in range(255):
    image_data.append([])
    for j in range(255):
        image_data[i].append(WHITE)
image_data[20][5] = BLACK

def make_bw(width, height):
    img = Image.new('1', (width, height))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = WHITE # i & j
    return img # img.save('test.bmp')

def draw_rectangle(img, x, y, width, height):
    pix = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if x < i < x+width:
                if y < j < y+height:
                    pix[i,j] = not pix[i,j]

def chessboard(img, by):
    for i in range(by):
        offset = (img.size[0]/by)
        draw_rectangle(img, int(2*i*offset), 0, offset, img.size[1])
    for i in range(by):
        offset = (img.size[1]/by)
        draw_rectangle(img, 0, int(2*i*offset), img.size[0], offset)

if __name__ == "__main__":
    # make_rgb()
    img = make_bw(138,200)
    chessboard(img, 5)
    # draw_rectangle(img, 20, 20, 20, 20)
    # draw_rectangle(img, 15, 10, 20, 20)
    img.save('test.bmp')
