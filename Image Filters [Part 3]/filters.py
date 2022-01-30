# Use this file to write your filter functions!
import copy

def is_valid_coordinate(image_matrix, r_index, c_index):
    if r_index > len(image_matrix) - 1 or c_index > len(image_matrix[0]) - 1 or r_index<0 or c_index<0:
        return False
    return True

def blur(image_matrix):
    output_image = copy.deepcopy(image_matrix)
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[0])):
            neighbors = []
            if is_valid_coordinate(image_matrix, row - 1, col-1) == True:
                neighbors.append(image_matrix[row -1][col-1])
            if is_valid_coordinate(image_matrix, row - 1, col)== True:
                neighbors.append(image_matrix[row -1][col])
            if is_valid_coordinate(image_matrix, row - 1, col+1)== True:
                neighbors.append(image_matrix[row -1][col+1])
            if is_valid_coordinate(image_matrix, row, col - 1)== True:
                neighbors.append(image_matrix[row][col - 1])
            neighbors.append(image_matrix[row][col])
            if is_valid_coordinate(image_matrix, row, col + 1)== True:
                neighbors.append(image_matrix[row][col + 1])
            if is_valid_coordinate(image_matrix, row + 1, col-1)== True:
                neighbors.append(image_matrix[row +1][col-1])
            if is_valid_coordinate(image_matrix, row + 1, col)== True:
                neighbors.append(image_matrix[row + 1][col])
            if is_valid_coordinate(image_matrix, row + 1, col+1)== True:
                neighbors.append(image_matrix[row +1][col+1])
            
            pixel = output_image[row][col]
            num_pixels = len(neighbors)
            r_tot = 0
            g_tot = 0
            b_tot = 0
            for pixels in neighbors:
                r_tot += pixels[0]
                g_tot += pixels[1]
                b_tot += pixels[2]
            new_r = r_tot//num_pixels 
            new_g = g_tot//num_pixels
            new_b = b_tot//num_pixels
            pixel[0] = new_r
            pixel[1] = new_g
            pixel[2] = new_b
            
    return output_image

def threshold(image_matrix,
              red_threshold=(0, 255),
              green_threshold=(0, 255),
              blue_threshold=(0, 255)):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[0])):
            pixel = image_matrix[row][col]
            if pixel[0] < red_threshold[0] or pixel[0]>red_threshold[1] or pixel[1] < green_threshold[0] or pixel[1]> green_threshold[1] or pixel[2]<blue_threshold[0] or pixel[2]>blue_threshold[1]:
                pixel[0] = 0
                pixel[1] = 0
                pixel[2] = 0
                
    return image_matrix