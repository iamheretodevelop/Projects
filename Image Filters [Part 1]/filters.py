import image_io
import math
# Use this file to write your filter functions!

def red_stripes(image_matrix):
    a = 0
    b = 50
    for  i in range(len(image_matrix)):
        for row in range(a, b):
            for col in range(len(image_matrix[0])):
                image_matrix[row][col][0] = 255 
        a += 100
        if b + 100 > len(image_matrix):
            b = len(image_matrix)
        else:
            b += 100
    #Second method: 
    # for row in range(len(image_matrix)):
    #     val = row // 50
    #     for col in range(len(image_matrix[0])):
    #         pixels = image_matrix[row][col]
    #         if val % 2 == 0:
    #             pixels[0] = 255
        
    return image_matrix
    

def grayscale(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[0])):
            pixels = image_matrix[row][col]
            avg = math.floor(((pixels[0] + pixels[1] + pixels[2])/3))
            pixels[0] = avg 
            pixels[1] = avg
            pixels[2] = avg

    return image_matrix
    