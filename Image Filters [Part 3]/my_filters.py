"""
EXTRA CREDIT!!

Please implement your filters in this module. You can write different functions for your filter(s) here
which can be imported in the image_playground.py module to run.

There will be no tests for your filtes(s), therefore, you should test them yourselves to check the correctness of the filter(s).
Please provide a docstring to each function implemented here so that the users can read about the functions and apply them accordingly.

"""
def mirror_image(image_matrix):
    """Filter which mirrors the original image by flipping the image left to right
    
    For this, you will have to change the column orientation of the matrix, i.e., col[0] becomes col[len(no_of_columns - 1] and so on.    
    """
    new_image_matrix = []
    for row in range(len(image_matrix)):
        new_image_row = []
        for col in range(len(image_matrix[0]) - 1, -1, -1):
        # for col in range(len(image_matrix[0])):
            pixels = image_matrix[row][col]
            new_image_row.append(pixels)
        new_image_matrix.append(new_image_row)
    return new_image_matrix