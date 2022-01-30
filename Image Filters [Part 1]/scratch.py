import image_io

image = []
for row in range(500):
    r = []
    for col in range(400):
        r.append([0, 0, 0])
    image.append(r)
    
for row in range(len(image)):
    for col in range(len(image[0])):
        pixel = image[row][col]
        pixel[0] = (row + col) % 256
        pixel[1] = (col) % 256
        pixel[2] = (row) % 256

image_io.write_to_file("class.png", image)