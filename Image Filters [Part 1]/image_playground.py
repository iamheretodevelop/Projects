import filters
import image_io

# Use this playground to try out different functions!
# image_matrix = image_io.read_file("images/obama.png")
# invert = filters.grayscale(image_matrix)
# image_io.write_to_file("outputs/obama.png", invert)

image_matrix = image_io.read_file("images/pumpkins.jpeg")
red = filters.red_stripes(image_matrix)
image_io.write_to_file("outputs/pumpkins.jpeg", red)

