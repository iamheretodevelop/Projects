
# Use this file to write your filter functions!

def invert_colors(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[0])):
            pixels = image_matrix[row][col]
            pixels[0] = 255 - pixels[0] 
            pixels[1] = 255 - pixels[1]
            pixels[2] = 255 - pixels[2]

    return image_matrix


def flip(image_matrix):
    new_image_matrix = []
    for row in range(len(image_matrix)-1, -1, -1):
        # for col in range(len(image_matrix[0])):
            pixels = image_matrix[row]
            new_image_matrix.append(pixels)
    return new_image_matrix

def sepia(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[0])):
            pixels = image_matrix[row][col]
            red = pixels[0] 
            blue = pixels[1] 
            green = pixels[2]
            pixels[0] = int((red * .393) + (blue * .769) + (green * .189))
            pixels[1] = int((red * .349) + (blue *.686) + (green * .168))
            pixels[2] = int((red * .272) + (blue *.534) + (green * .131))
            if pixels[0] > 255:
                pixels[0] = 255
            if pixels[1] > 255:
                pixels[1] = 255
            if pixels[2] > 255:
                pixels[2] = 255
            
    return image_matrix
